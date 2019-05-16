import logging
from subprocrunner import SubprocessRunner, Which


class Execute(object):
    def _check_cmd(self, executable):
        which = Which(executable)

        if which.is_exist():
            return True
        return

    def cmd(self, command):
        status = None
        executable = command.split()
        exec_exists = self._check_cmd(executable[0])

        if exec_exists:
            runner = SubprocessRunner(command)
            runit = runner.run()

            if runit == 0:
                status = runner.stdout
        else:
            logging.error(f'{executable[0]} command not found')

        return status
