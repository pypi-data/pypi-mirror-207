import atexit
import os
import platform
import socket
import subprocess
import urllib.request
from typing import Optional

import oexp.access as access
import oexp.gen as gen

system = platform.system()


def _cpu():
    if system == 'Linux':
        return subprocess.check_output(['uname', '-m']).decode().strip()
    else:
        return subprocess.check_output(['/usr/sbin/sysctl', 'machdep.cpu.brand_string']).decode().strip()


def _user_data_dir():
    d = {
        'Darwin': lambda: os.path.join(os.path.expanduser('~'), 'Library', 'Application Support', 'oexp'),
        'Linux': lambda: os.path.join(os.path.expanduser('~'), '.oexp')
    }
    if system not in d:
        raise Exception(f"TODO: implement user_data_dir for {system}")
    else:
        return d[system]()


_initialized_java = False
_jar_process = None
_java_sock: Optional[socket.socket] = None
_java_exit_sock: Optional[socket.socket] = None
_java_conn: Optional[socket.socket] = None
_java_exit_conn: Optional[socket.socket] = None


# https://stackoverflow.com/questions/1395593/managing-resources-in-a-python-project
# https://docs.python.org/3/library/subprocess.html
# https://docs.python.org/3/library/importlib.resources.html#module-importlib.resources
def _init_java():
    global _java_sock, _jar_process, _java_exit_sock, _java_conn, _java_exit_conn
    if _java_sock is not None:
        return

    data_dir = _user_data_dir()

    cpu = _cpu()
    if cpu == "machdep.cpu.brand_string: Apple M1 Max":
        platform_label = "macos-aarch64"
    elif cpu == "x86_64":
        platform_label = "linux-x64"
    else:
        raise Exception(f"need to figure out java for {cpu}")

    j_version = f"jdk-{gen.JAVA_VERSION}"
    if system == 'Linux':
        j_folder = os.path.join(data_dir, j_version)
    else:
        j_folder = os.path.join(data_dir, j_version + ".jdk")
    tar_gz_folder = os.path.join(data_dir, "jdk.tar.gz")
    if not os.path.exists(tar_gz_folder):
        print("downloading java...")
        os.makedirs(data_dir, exist_ok=True)
        if os.path.exists(tar_gz_folder):
            os.remove(tar_gz_folder)
        #     https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html

        urllib.request.urlretrieve(
            f"https://download.oracle.com/java/17/archive/jdk-{gen.JAVA_VERSION}_{platform_label}_bin.tar.gz",
            tar_gz_folder
        )
        subprocess.run(
            [
                "/usr/bin/tar", "-xf",
                tar_gz_folder
            ],
            cwd=data_dir
        )
        print("finished downloading java!")

    last_downloaded_jar_path = os.path.join(data_dir, f"last_downloaded_jar.txt")
    jar_path = os.path.join(data_dir, f"oexp-front-0-all.jar")

    need_to_download = True
    if os.path.exists(last_downloaded_jar_path):
        with open(last_downloaded_jar_path, 'r') as f:
            need_to_download = f.read() == gen.JAR_VERSION
    if need_to_download:
        if os.path.exists(jar_path):
            os.remove(jar_path)
        print("downloading jar...")
        urllib.request.urlretrieve(
            access.JAR_URL,
            jar_path
        )
        print("finished downloading jar!")

    HOST = "127.0.0.1"
    next_port_to_try = 50_000
    last_port_to_try = 51_000

    _java_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    did_bind = False
    while next_port_to_try <= last_port_to_try:
        try:
            _java_sock.bind((HOST, next_port_to_try))
            did_bind = True
            break
        except:
            print(f"port {next_port_to_try} is being used, trying for _java_sock {next_port_to_try + 1} ")
            next_port_to_try += 1
    if not did_bind:
        raise Exception("could not bind socket 1")
    _java_sock.listen()

    if system == 'Linux':
        java = os.path.join(j_folder, "bin/java")
    else:
        java = os.path.join(j_folder, "Contents/Home/bin/java")

    _jar_process = subprocess.Popen(
        [
            java,
            "-jar",
            jar_path,
            str(next_port_to_try)
        ],
    )

    _java_conn, addr = _java_sock.accept()

    # _java_sock.connect(("localhost", int(access.PORT)))
    _java_exit_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    next_port_to_try += 1
    did_bind = False
    while next_port_to_try <= last_port_to_try:
        try:
            _java_exit_sock.bind((HOST, next_port_to_try))
            did_bind = True
            break
        except:
            print(f"port {next_port_to_try} is being used, trying for _java_exit_sock {next_port_to_try + 1} ")
            next_port_to_try += 1
    if not did_bind:
        raise Exception("could not bind socket 1")

    _java_exit_sock.listen()

    _java_conn.sendall(access.SET_EXIT_PORT)
    _java_conn.sendall(next_port_to_try.to_bytes(4, 'big'))

    _java_exit_conn, addr = _java_exit_sock.accept()
    # _java_exit_sock.connect(("localhost", int(access.PORT_EXIT)))

    atexit.register(kill_java)


def kill_java():
    _java_exit_conn.send(access.OexpExitSocketHeaders.EXIT.value)
    # https://stackoverflow.com/questions/409783/socket-shutdown-vs-socket-close
    # _java_sock.shutdown(socket.SHUT_RDWR)
    # https://stackoverflow.com/a/4084365/6596010
    _java_exit_conn.close()
    _java_conn.close()
    _java_exit_sock.close()
    _java_sock.close()
    _jar_process.kill()
