from __future__ import print_function
from __future__ import unicode_literals

import click
import traceback
from urllib.parse import urlparse
from .prompt.socketio_prompt import SocketIOPrompt
from .commands.command import argparse
from .logger import get_logger


logger = get_logger()

@click.argument('path', default='', nargs=1)
@click.command()
def cli(path):
    url = urlparse(path)
    if url.scheme == 'http':
        prompt = SocketIOPrompt(path)
    while True:
        try:
            prompt.run_cli()

        except argparse.ArgumentError as ex:
            self.logger.debug('Error: %r.', ex)
            self.logger.error("traceback: %r", traceback.format_exc())
            click.secho(ex.msg, fg='red')

        except EOFError:
            # exit out of the CLI
            break

        # TODO: uncomment for release
        except Exception as ex:
            logger.debug('Exception: %r.', ex)
            logger.error("traceback: %r", traceback.format_exc())
            click.secho(str(ex), fg='red')

if __name__ == "__main__":
    cli()
