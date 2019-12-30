import subprocess


class CmdUtils:

    @staticmethod
    def run_cmd(command):
        return subprocess.check_output(command)
