__doc__ = """Parse and extract data from Apple Numbers spreadsheets

numbers_parser is a Python module for parsing Apple Numbers .numbers files.
It supports Numbers files generated by Numbers version 10.3 and 11.0
(current as of May 2021).

It supports and is tested against Python versions from 3.5 onwards. It is
not compatible with earlier versions of Python.

Currently supported features of Numbers files are:

- Multiple sheets per document
- Multiple tables per sheet
- Text, numeric, date, currency, duration, percentage cell types

Formulas have very limited support and rely wholly on Numbers saving values
in cells as part of the saved document, which is not always guaranteed. When
a formula value is not present, the value *FORMULA* is returned. Any formula
that results in a Numbers error returns a value *ERROR*.
"""

import os
import plistlib
import warnings

from numbers_parser.document import Document  # NOQA
from numbers_parser.cell import *  # NOQA
from numbers_parser._version import __version__  # NOQA

_DEFAULT_NUMBERS_INSTALL_PATH = "/Applications/Numbers.app"
_VERSION_PLIST_PATH = "Contents/version.plist"
_SUPPORTED_NUMBERS_VERSIONS = [
    "10.3",
    "11.0",
    "11.1",
    "11.2",
]

# Don't print the source line
formatwarning_old = warnings.formatwarning
warnings.formatwarning = lambda message, category, filename, lineno, line=None: formatwarning_old(  # pragma: no cover
    message, category, filename, lineno, line=""
)


def _get_version():
    return __version__


def _check_installed_numbers_version():
    try:
        fp = open(
            os.path.join(_DEFAULT_NUMBERS_INSTALL_PATH, _VERSION_PLIST_PATH), "rb"
        )
    except IOError:  # pragma: no cover
        return None
    version_dict = plistlib.load(fp)
    installed_version = version_dict["CFBundleShortVersionString"]
    if installed_version not in _SUPPORTED_NUMBERS_VERSIONS:
        warnings.warn(
            f"Numbers version {installed_version} not tested with this version"
        )
    fp.close()


_check_installed_numbers_version()
