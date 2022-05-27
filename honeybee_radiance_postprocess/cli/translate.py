"""Commands to translate objects."""
import click
import sys
import logging
import numpy as np

_logger = logging.getLogger(__name__)


@click.group(help='Commands to translate objects.')
def translate():
    pass


@translate.command('npy-to-txt')
@click.argument(
    'npy-file', type=click.Path(exists=True, dir_okay=False, resolve_path=True)
)
@click.option(
    '--name', '-n', help='Output file name.', default='output', show_default=True
)
@click.option(
    '--extension', '-ext', help='Output file extension', default='.txt', show_default=True
)
@click.option(
    '--format', '-fmt', help='Output format for each element in the array',
    default='%.7e', show_default=True
)
def npy_to_txt(
    npy_file, name, extension, format
        ):
    """Convert a npy file to text file.

    This function reads a NumPy array from a npy file and saves it as readable file. The
    converted file is tab separated.

    \b
    Args:
        npy-file: Path to npy file.
    """
    try:
        array = np.load(npy_file)
        np.savetxt(name + extension, array, fmt=format, delimiter='\t')

    except Exception:
        _logger.exception('Converting npy file to text file failed.')
        sys.exit(1)
    else:
        sys.exit(0)


@translate.command('txt-to-npy')
@click.argument(
    'txt-file', type=click.Path(exists=True, dir_okay=False, resolve_path=True)
)
@click.option(
    '--name', '-n', help='Output file name.', default='output', show_default=True
)
def txt_to_npy(
    txt_file, name
        ):
    """Convert a text file to npy file.

    This function reads a space or tab separated text file saves it as a NumPy file. As
    an example the input file could be the annual illuminance values.

    \b
    Args:
        txt-file: Path to text file.
    """
    try:
        array = np.loadtxt(txt_file, dtype=np.float32)
        np.save(name, array)

    except Exception:
        _logger.exception('Converting text file to npy file failed.')
        sys.exit(1)
    else:
        sys.exit(0)
