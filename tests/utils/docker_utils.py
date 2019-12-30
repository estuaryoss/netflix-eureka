import errno
import os
from pathlib import Path

from tests.utils.cmd_utils import CmdUtils


class DockerUtils():

    @staticmethod
    def up(file):
        file_path = Path(file)
        if not file_path.is_file():
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file_path)
        return CmdUtils.run_cmd(["docker-compose", "pull", "&&", "docker-compose", "-f", file, "up", "-d"])

    @staticmethod
    def down(file):
        file_path = Path(file)
        if not file_path.is_file():
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file_path)
        return CmdUtils.run_cmd(["docker-compose", "-f", f"{file}", "down", "-v"])

    @staticmethod
    def start(file):
        file_path = Path(file)
        if not file_path.is_file():
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file_path)
        return CmdUtils.run_cmd(["docker-compose", "-f", f"{file}", "start"])

    @staticmethod
    def stop(file):
        file_path = Path(file)
        if not file_path.is_file():
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file_path)
        return CmdUtils.run_cmd(["docker-compose", "-f", f"{file}", "stop"])

    @staticmethod
    def up_service(file, service):
        file_path = Path(file)
        if not file_path.is_file():
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file_path)
        return CmdUtils.run_cmd(["docker-compose", "-f", f"{file}", "up", "-d", f"{service}"])

    @staticmethod
    def stop_service(file, service):
        file_path = Path(file)
        if not file_path.is_file():
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file_path)
        return CmdUtils.run_cmd(["docker-compose", "-f", f"{file}", "stop", f"{service}"])

    @staticmethod
    def start_service(file, service):
        file_path = Path(file)
        if not file_path.is_file():
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file_path)
        return CmdUtils.run_cmd(["docker-compose", "-f", f"{file}", "start", f"{service}"])

    @staticmethod
    def logs(file):
        file_path = Path(f"{file}")
        if not file_path.is_file():
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file_path)
        return CmdUtils.run_cmd(
            ["docker-compose", "-f", file, "logs", "-t", f"--tail=100"])

    @staticmethod
    def ps(id):
        return CmdUtils.run_cmd(["docker", "ps", "--filter", "name={}".format(id)])

    @staticmethod
    def exec(container_id, command):
        container_exec_cmd = ["docker", "exec", f"{container_id}"]
        container_exec_cmd.extend(command)
        return CmdUtils.run_cmd(container_exec_cmd)

    @staticmethod
    def network_prune():
        container_exec_cmd = ["docker", "network", "prune", "-f"]
        return CmdUtils.run_cmd(container_exec_cmd)

    @staticmethod
    def network_connect(deployer_net, container):
        container_exec_cmd = ["docker", "network", "connect", f"{deployer_net}", f"{container}"]
        return CmdUtils.run_cmd(container_exec_cmd)

    @staticmethod
    def network_disconnect(deployer_net, container):
        container_exec_cmd = ["docker", "network", "disconnect", f"{deployer_net}", f"{container}"]
        return CmdUtils.run_cmd(container_exec_cmd)

    @staticmethod
    def volume_prune():
        container_exec_cmd = ["docker", "volume", "prune", "-f"]
        return CmdUtils.run_cmd(container_exec_cmd)

    @staticmethod
    def exec_detached(container_id, command):
        container_exec_cmd = ["docker", "exec", "-d", f"{container_id}"]
        container_exec_cmd.extend(command)
        return CmdUtils.run_cmd(container_exec_cmd)

    @staticmethod
    def clean_up():
        DockerUtils.network_prune()
        DockerUtils.volume_prune()
