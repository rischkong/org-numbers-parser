from enum import IntEnum

from pendulum import datetime

try:
    from importlib.resources import files
# Can't cover exception using modern python
except ImportError:  # pragma: nocover
    from importlib_resources import files

DEFAULT_DOCUMENT = files("numbers_parser") / "data" / "empty.numbers"

# New document defaults
DEFAULT_COLUMN_COUNT = 8
DEFAULT_COLUMN_WIDTH = 98.0
DEFAULT_PRE_BNC_BYTES = "🤠".encode()  # Yes, really!
DEFAULT_ROW_COUNT = 12
DEFAULT_ROW_HEIGHT = 20.0
DEFAULT_NUM_HEADERS = 1
DEFAULT_TABLE_OFFSET = 80.0
DEFAULT_TILE_SIZE = 256

# Style defaults
DEFAULT_ALIGNMENT = ("auto", "top")
DEFAULT_BORDER_WIDTH = 0.35
DEFAULT_BORDER_COLOR = (0, 0, 0)
DEFAULT_BORDER_STYLE = "solid"
DEFAULT_FONT = "Helvetica Neue"
DEFAULT_FONT_SIZE = 11.0
DEFAULT_TEXT_INSET = 4.0
DEFAULT_TEXT_WRAP = True
EMPTY_STORAGE_BUFFER = b"\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"

# Numbers limits
MAX_TILE_SIZE = 256
MAX_ROW_COUNT = 1000000
MAX_COL_COUNT = 1000
MAX_HEADER_COUNT = 5
MAX_SIGNIFICANT_DIGITS = 15

# Root object IDs
DOCUMENT_ID = 1
PACKAGE_ID = 2

# System constants
EPOCH = datetime(2001, 1, 1)
SECONDS_IN_HOUR = 60 * 60
SECONDS_IN_DAY = SECONDS_IN_HOUR * 24
SECONDS_IN_WEEK = SECONDS_IN_DAY * 7

# File format enumerations
DECIMAL_PLACES_AUTO = 253


class CellType(IntEnum):
    EMPTY = 1
    NUMBER = 2
    TEXT = 3
    DATE = 4
    BOOL = 5
    DURATION = 6
    ERROR = 7
    RICH_TEXT = 8


class CellPadding(IntEnum):
    SPACE = 1
    ZERO = 2


class DurationStyle(IntEnum):
    COMPACT = 0
    SHORT = 1
    LONG = 2


class DurationUnits(IntEnum):
    NONE = 0
    WEEK = 1
    DAY = 2
    HOUR = 4
    MINUTE = 8
    SECOND = 16
    MILLISECOND = 32


class FormatType(IntEnum):
    BOOLEAN = 1
    DECIMAL = 256
    CURRENCY = 257
    PERCENT = 258
    TEXT = 260
    DATE = 261
    FRACTION = 262
    CHECKBOX = 263
    RATING = 267
    DURATION = 268
    BASE = 269
    CUSTOM_NUMBER = 270
    CUSTOM_TEXT = 271
    CUSTOM_DATE = 272
    CUSTOM_CURRENCY = 274


class NegativeNumberStyle(IntEnum):
    MINUS = 0
    RED = 1
    PARENTHESES = 2
    RED_AND_PARENTHESES = 3
