import typer
from hakai_api import Client
from typing_extensions import Annotated

from ix_aims.lib import auto_ix


def log_into_aims():
    if not Client.file_credentials_are_valid():
        typer.launch(Client.DEFAULT_LOGIN_PAGE)
        Client()


@typer.run
def main(
        work_order: Annotated[
            str,
            typer.Argument(help="The work order number in format ##_####_##")
        ]):
    """For ACO WORK_ORDER, setup iX Capture with the correct configuration and
    calibration parameters."""
    log_into_aims()
    auto_ix(work_order)


if __name__ == '__main__':
    main()
