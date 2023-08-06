import sys
from subprocess import CalledProcessError

from manageprojects.utilities.subprocess_utils import verbose_check_call
from rich import print  # noqa
from rich.console import Console
from rich.highlighter import ReprHighlighter

from ha_services.cli_tools.richt_utils import PanelPrinter, print_human_error
from ha_services.systemd.data_classes import SystemdServiceInfo


def print_systemd_file(
    *,
    info: SystemdServiceInfo,
    HighlighterClass=ReprHighlighter,
    padding=(1, 5),
):
    """
    Print Systemd service template + context + rendered file content.
    """
    pp = PanelPrinter(
        HighlighterClass=HighlighterClass,
        border_style='white',
        padding=padding,
    )
    pp.print_panel(
        content=info.get_template_content(),
        title=f'[magenta]Template[/magenta]: {info.template_path}',
    )
    pp.print_panel(
        content=info.get_template_context(),
        title='[cyan]Context:',
    )
    pp.print_panel(
        content=info.get_compiled_service(),
        title=f'[bright][green]Compiled[/green]: {info.service_file_path.name}',
        border_style='bright_yellow',
    )


class SystemdServiceError(RuntimeError):
    pass


class ServiceControl:
    """
    Manage Systemd service
    """

    def __init__(self, info: SystemdServiceInfo):
        self.info = info
        self.service_name = info.service_file_path.name

    ##################################################################################################
    # Helper

    def sudo_hint_exception_exit(self, err, exit_code=1):
        console = Console(stderr=True)
        console.print_exception(
            width=console.size.width,  # full terminal width
            show_locals=True,
            max_frames=2,
        )
        console.print('\n')
        print_human_error(
            error_message=f'{err}\n\nHint: Maybe **sudo** is needed for this command!\nTry again with sudo.',
            title='[red]Permission error',
        )
        sys.exit(exit_code)

    def write_service_file(self):
        print(f'Write "{self.info.service_file_path}"...')
        content = self.info.get_compiled_service()
        try:
            self.info.service_file_path.write_text(content, encoding='UTF-8')
        except PermissionError as err:
            self.sudo_hint_exception_exit(err)

        self.call_systemctl('daemon-reload', with_service_name=False)

    def remove_service_file(self):
        print(f'Remove "{self.info.service_file_path}"...')
        try:
            self.info.service_file_path.unlink(missing_ok=True)
        except PermissionError as err:
            self.sudo_hint_exception_exit(err)

        self.call_systemctl('daemon-reload', with_service_name=False)

    ##################################################################################################
    # systemctl

    def call_systemctl(self, command, with_service_name=True):
        args = ['systemctl', command]
        if with_service_name:
            args.append(self.service_name)
            if not self.info.service_file_path.is_file():
                print_human_error(
                    f'Systemd service file not found here: {self.info.service_file_path}'
                    '\n\nHint: Setup systemd service first!'
                )
                sys.exit(1)

        try:
            verbose_check_call(*args)
        except CalledProcessError as err:
            self.sudo_hint_exception_exit(err)

    def enable(self):
        self.call_systemctl('enable')

    def restart(self):
        self.call_systemctl('restart')

    def stop(self):
        self.call_systemctl('stop')

    def status(self):
        self.call_systemctl('status')

    ##################################################################################################
    # High level commands:
    def setup_and_restart_systemd_service(self):
        """
        Write Systemd service file, enable it and (re-)start the service.
        """
        self.write_service_file()
        self.enable()
        self.restart()
        self.status()

    def remove_systemd_service(self):
        self.stop()
        self.remove_service_file()
