# numbers-parser

[![build:](https://github.com/masaccio/numbers-parser/actions/workflows/run-all-tests.yml/badge.svg)](https://github.com/masaccio/numbers-parser/actions/workflows/run-all-tests.yml)
[![build:](https://github.com/masaccio/numbers-parser/actions/workflows/codeql.yml/badge.svg)](https://github.com/masaccio/numbers-parser/actions/workflows/codeql.yml)
[![codecov](https://codecov.io/gh/masaccio/numbers-parser/branch/main/graph/badge.svg?token=EKIUFGT05E)](https://codecov.io/gh/masaccio/numbers-parser)
[![PyPI version](https://badge.fury.io/py/numbers-parser.svg)](https://badge.fury.io/py/numbers-parser)

`numbers-parser` is a Python module for parsing [Apple Numbers](https://www.apple.com/numbers/)
`.numbers` files. It supports Numbers files generated by Numbers version 10.3, and up with the latest tested version being 13.0
(current as of April 2023).

It supports and is tested against Python versions from 3.8 onwards. It is not compatible with earlier versions of Python.

Formula evaluation relies on Numbers storing current values which should usually be the case. Formulas themselves rather than the computed values can optionally be extracted. [Style support](#styles) is somewhat limited, but has grown significantly as of version 4.0.

## Installation

``` bash
python3 -m pip install numbers-parser
```

A pre-requisite for this package is [python-snappy](https://pypi.org/project/python-snappy/) which will be installed by Python automatically, but python-snappy also requires that the binary libraries for snappy compression are present.

The most straightforward way to install the binary dependencies is to use [Homebrew](https://brew.sh) and source Python from Homebrew rather than from macOS as described in the [python-snappy github](https://github.com/andrix/python-snappy):

For Intel Macs:

``` bash
brew install snappy python3
CPPFLAGS="-I/usr/local/include -L/usr/local/lib" python3 -m pip install python-snappy
```

For Apple Silicon Macs:

``` bash
brew install snappy python3
CPPFLAGS="-I/opt/homebrew/include -L/opt/homebrew/lib" python3 -m pip install python-snappy
```

For Linux (your package manager may be different):

``` bash
sudo apt-get -y install libsnappy-dev
```

On Windows, you will need to either arrange for snappy to be found for VSC++ or you can install python binary libraries compiled by [Christoph Gohlke](https://www.lfd.uci.edu/~gohlke/pythonlibs/#python-snappy). You must select the correct python version for your installation. For example for python 3.11:

``` text
C:\Users\Jon>pip install C:\Users\Jon\Downloads\python_snappy-0.6.1-cp311-cp311-win_amd64.whl
```

## API changes in version 4.0

To better partition cell styles, background image data which was supported in earlier versions through the methods `image_data` and `image_filename` is now part of the new `cell_style` property. Using the deprecated methods `image_data` and `image_filename` will issue a `DeprecationWarning` if used.The legacy methods will be removed in a future version of numbers-parser.

`NumberCell` cell values are now limited to 15 significant figues to match the implementation of floating point numbers in Apple Numbers. For example, the value `1234567890123456` is rounded to `1234567890123460` in the same was as in Numbers. Previously, using native `float` with no checking resulted in rounding errors in unpacking internal numbers. Attempting to write a number with too many significant digits results in a `RuntimeWarning`.

## Usage

Reading documents:

``` python
from numbers_parser import Document
doc = Document("my-spreadsheet.numbers")
sheets = doc.sheets
tables = sheets[0].tables
rows = tables[0].rows()
```

### Referring to sheets and tables

Both sheets and names can be accessed from lists of these objects using an integer index (`list` syntax) and using the name
of the sheet/table (`dict` syntax):

``` python
# list access method
sheet_1 = doc.sheets[0]
print("Opened sheet", sheet_1.name)

# dict access method
table_1 = sheets["Table 1"]
print("Opened table", table_1.name)
```

### Accessing data

`Table` objects have a `rows` method which contains a nested list with an entry for each row of the table. Each row is
itself a list of the column values. Empty cells in Numbers are returned as `None` values.

``` python
data = sheets["Table 1"].rows()
print("Cell A1 contains", data[0][0])
print("Cell C2 contains", data[2][1])
```

Cells are objects with a common base class of `Cell`. All cell types have a property `value` which returns the contents of the cell in as a native Python datatype. `DurationCell` object values are `datetime.timedelta` objects which are additionally available as a formatted value matching that stored in the Numbers spreadsheet. The formatted value is returned using the `formatted_value` property.

### Cell references

In addition to extracting all data at once, individual cells can be referred to as methods

``` python
doc = Document("my-spreadsheet.numbers")
sheets = doc.sheets
tables = sheets["Sheet 1"].tables
table = tables["Table 1"]

# row, column syntax
print("Cell A1 contains", table.cell(0, 0))
# Excel/Numbers-style cell references
print("Cell C2 contains", table.cell("C2"))
```

### Merged cells

When extracting data using `rows()` merged cells are ignored since only text values are returned. The `cell()` method of `Table` objects returns a `Cell` type object which is typed by the type of cell in the Numbers table. `MergeCell` objects indicates cells removed in a merge. The remaining `Cell` has a `bool` property `is_merged` which is `True` if the cell is the result of a merge. Such cells return a `tuple` for their `size` property indicating the number of rows and columns in the merged cell. Unmerged cells return a `size` of `None`.

``` python
doc = Document("my-spreadsheet.numbers")
sheets = doc.sheets
tables = sheets["Sheet 1"].tables
table = tables["Table 1"]

cell = table.cell("A1")
print(cell.merge_range)
print(f"Cell A1 merge size is {cell.size[0]},{cell.size[1]})
```

### Row and column iterators

Tables have iterators for row-wise and column-wise iteration with each iterator
returning a list of the cells in that row or column

``` python
for row in table.iter_rows(min_row=2, max_row=7, values_only=True):
    sum += row
for col in table.iter_cols(min_row=2, max_row=7):
    sum += col.value
```

### Pandas

Since the return value of `data()` is a list of lists, you can pass this directly to pandas. Assuming you have a Numbers table with a single header which contains the names of the pandas series you want to create you can construct a pandas dataframe using:

``` python
import pandas as pd

doc = Document("simple.numbers")
sheets = doc.sheets
tables = sheets[0].tables
data = tables[0].rows(values_only=True)
df = pd.DataFrame(data[1:], columns=data[0])
```

### Bullets and lists

Cells that contain bulleted or numbered lists can be identified by the `is_bulleted` property. Data from such cells is returned using the `value` property as with other cells, but can additionally extracted using the `bullets` property. `bullets` returns a list of the paragraphs in the cell without the bullet or numbering character. Newlines are not included when bullet lists are extracted using `bullets`.

``` python
doc = Document("bullets.numbers")
sheets = doc.sheets
tables = sheets[0].tables
table = tables[0]
if not table.cell(0, 1).is_bulleted:
    print(table.cell(0, 1).value)
else:
    bullets = ["* " + s for s in table.cell(0, 1).bullets]
    print("\n".join(bullets))
```

Bulleted and numbered data can also be extracted with the bullet or number characters present in the text for each line in the cell in the same way as above but using the `formatted_bullets` property. A single space is inserted between the bullet character and the text string and in the case of bullets, this will be the Unicode character seen in Numbers, for example `"• some text"`.

### Hyperlinks

Numbers does not support hyperlinks to cells within a spreadsheet, but does allow embedding links in cells. When cells contain hyperlinks, `numbers_parser` returns the text version of the cell. The `hyperlinks` property of cells where `is_bulleted` is `True` is a list of text and URL tuples:

``` python
cell = table.cell(0, 0)
(text, url) = cell.hyperlinks[0]
```

### Styles

`numbers_parser` currently only supports paragraph styles and cell styles. The following paragraph styles are suppoprted:

* font attributes: bold, italic, underline, strikethrough
* font selection and size
* text foreground color
* horizontal and vertical alignment
* cell background color
* cell indents (first line, left, right, and text inset)

Table styles that allow new tables to adopt a style across the whole table are not planned.

Numbers conflates style attributes that can be stored in paragraph styles (the style menu in the text panel) with the settings that are available on the Style tab of the Text panel. Some attributes in Numbers are not applied to new cells when a style is applied. To keep the API simple, `numbers-parser` packs all styling into a single `Style` object. When a document is saved, the attributes not stored in a paragraph style are applied to each cell that includes it. Attributes behaving in this way are currently `Cell.alignment.vertical` and `Cell.style.text_inset`. The cell background colour `Cell.style.bg_color` also behaves this way, though this is in line with the separation in Numbers.

#### Reading styles

The cell method `style` returns a `Style` object containing all the style information for that cell. Cells with identical style settings contain references to a single style object.

Cell style attributes can be returned using a number of methods:

* `Cell.style.alignment`: the horizontal and vertical alignment of the cell as an `Alignment` names tuple
* `Cell.style.bg_color`: cell background color as an `RGB` named tuple, or a list of `RGB` values for gradients
* `Cell.style.bold`: `True` if the cell font is bold
* `Cell.style.font_color`: font color as an `RGB` named tuple
* `Cell.style.font_size`: font size in points (`float`)
* `Cell.style.font_name`: font name (`str`)
* `Cell.style.italic`: `True` if the cell font is italic
* `Cell.style.name`: cell style (`str`)
* `Cell.style.underline`: `True` if the cell font is underline
* `Cell.style.strikethrough`: `True` if the cell font is strikethrough
* `Cell.style.first_indent`: first line indent in points (`float`)
* `Cell.style.left_indent`: left indent in points (`float`)
* `Cell.style.right_indent`: right indent in points (`float`)
* `Cell.style.text_inset`: text inset in points (`float`)
* `Cell.style.text_wrap`: `True` if text wrapping is enabled (default for new cells)

#### Cell images

The methods `style.bg_image.filename` and `style.bg_image.data` return data about the image used for a cell's background, where set. If a cell has no background image, `style.bg_image`  is `None`.

``` python
cell = table.cell("B1")
with open (cell.style.bg_image.filename, "wb") as f:
    f.write(cell.style.bg_image.data)
```

### Borders

`numbers-parser` supports reading and writing cell borders, though the interface for each differs. Individual cells can have each of their four borders tested, but when drawing new borders, these are set for the table to allow for drawing borders across multiple cells. Setting the border of merged cells is not possible unless the edge of the cells is at the end of the merged region.

Borders are represeted using the `Border` class that can be initialised with line width, color and line style:

``` python
border = Border(4.0, RGB(0, 162, 255), "solid"))
```

Valid values for the line `style` parameter are `"solid"`, `"dashes"`, `"dots"` and `"none"`.

#### Reading Cell Borders

Cells have a property `border` which itself has the properties `top`, `right`, `bottom` and `left`, each of which is a `Border` class representing the line type for that cell. Cells with no border set at all, and merged cells which are inside the range of the merge return `None` for these cells. The absence of a specified border is different from no border in Numbers which is a valid `Border` class with `style="none"`.

#### Writing Cell Borders

The `Table` method `set_cell_border()` sets the border for a cell edge or a range of cells:

``` python
table.set_cell_border("C1", ["top", "left"], Border(0.0, RGB(0, 0, 0), "none"))
table.set_cell_border(0, 4, "right", Border(1.0, RGB(0, 0, 0), "solid"), 3)
```

The last positional parameter specifies the length of the border and defaults to 1. A single call to `set_cell_border()` can set the borders to one or more sides of the cell as above. Like `Table.write()`, `set_cell_border()` supports both row/column and Excel-style cell references.

## Writing Numbers files

Whilst support for writing numbers files has been stable since version 3.4.0, you are highly recommened not to overwrite working Numbers files and instead save data to a new file.

### Limitations

Current limitations to write support are:

* Creating cells of type `BulletedTextCell` is not supported
* Formats cannot be defined for `DurationCell` or `DateCell`
* New tables are inserted with a fixed offset below the last table in a worksheet which does not take into account title or caption size
* New sheets insert tables with formats copied from the first table in the previous sheet rather than default table formats
* Style editing is limited to paragraph styles.

### Cell values

`numbers-parser` will automatically empty rows and columns for any cell references that are out of range of the current table. The `write` method accepts the same cell numbering notation as `cell` plus an additional argument representing the new cell value. The type of the new value will be used to determine the cell type.

``` python
doc = Document("old-sheet.numbers")
sheets = doc.sheets
tables = sheets[0].tables
table = tables[0]
table.write(1, 1, "This is new text")
table.write("B7", datetime(2020, 12, 25))
doc.save("new-sheet.numbers")
```

Sheet names and table names can be changed by assigning a new value to the `name` of each:

```python
sheets[0].name = "My new sheet"
tables[0].name = "Edited table"
````

### Adding tables and sheets

Additional tables and worksheets can be added to a `Document` before saving. If no sheet name or table name is supplied, `numbers-parser` will use `Sheet 1`, `Sheet 2`, etc.

```python
doc = Document()
doc.add_sheet("New Sheet", "New Table")
sheet = doc.sheets["New Sheet"]
table = sheet.tables["New Table"]
table.write(1, 1, 1000)
table.write(1, 2, 2000)
table.write(1, 3, 3000)

doc.save("sheet.numbers")
```

### Table geometries

`numbers-parser` can query and change the position and size of tables. Changes made to a table's row height or column width is retained when files are saved.

####  Row and column sizes

Row heights and column widths are queried and set using the `row_height` and `col_width` methods:

```python
doc = Document("sheet.numbers")
table = doc.sheets[0].tables[0]
print(f"Table size is {table.height} x {table.width}")
print(f"Table row 1 height is {table.row_height(0)}")
table.row_height(0, 40)
print(f"Table row 1 height is now {table.row_height(0)}")
print(f"Table column A width is {table.col_width(0)}")
table.col_width(0, 200)
print(f"Table column A width is {table.col_width(0)}")
```

####  Header row and columns

When new tables are created, `numbers-parser` follows the Numbers convention of creating a table with one row header and one column header. You can change the number of headers by modifying the appopriate property:

```python
doc = Document("sheet.numbers")
table = doc.sheets[0].tables[0]
table.num_header_rows = 2
table.num_header_cols = 0
doc.save("saved.numbers")
```

A zero header count will remove the headers from the table. Attempting to set a negative number of headers, or using more headers that rows or columns in the table will raise a `ValueError` exception.

#### Positioning tables

By default, new tables are positioned at a fixed offset below the last table vertically in a sheet and on the left side of the sheet. Large table headers and captions may result in new tables overlapping existing ones. The `add_table` method takes optional coordinates for positioning a table. A table's height and coordinates can also be queried to help aligning new tables:

```python
(x, y) = sheet.table[0].coordinates
y += sheet.table[0].height + 200.0
new_table = sheet.add_table("Offset Table", x, y)
```

### Editing paragraph styles

Cell text styles, known as paragraph styles, are those applied by the Text tab in Numbers Format pane. To simplify the API, when writing documents, it is not possible to make ad hoc changes to cells without assigning an existing style or creating a new one. This differs to the Numbers interface where cells can have modified styles on a per cell basis. Such styles are read correctly when reading Numbers files.

Character styles, which allow formatting changes within cells such as "This is **bold** text" are not supported.

Styles are created using the `Document`'s `add_style` method, and can be applied to cells either as part of a `write` or using `set_cell_style`:

``` python
red_text = doc.add_style(
    name="Red Text",
    font_name="Lucida Grande",
    font_color=RGB(230, 25, 25),
    font_size=14.0,
    bold=True,
    italic=True,
    alignment=Alignment("right", "top"),
)
table.write("B2", "Red", style=red_text)
table.set_cell_style("C2", red_text)
```

New styles are automatically added to the list of styles selectable in the Numbers Text pane.

Cell styles can also be referred to by name in both `Table.write` and `Table.set_cell_style`. A `dict` of available styles is returned by `Document.styles`. This contains key value pairs of style names and `Style` objects. Any changes to `Style` objects in the document are written back such that those styles are changed for all cells that use them.

``` python
doc = Document("styles.numbers")
styles = doc.styles
styles["Title"].font_size = 20.0
```

Since `Style` objects are shared, changing `Cell.style.font_size` will have the effect of changing the font size for that style and will in turn affect the styles of all cells using that style.

## Command-line scripts

When installed from [PyPI](https://pypi.org/project/numbers-parser/), a command-like script `cat-numbers` is installed in Python's scripts folder. This script dumps Numbers spreadsheets into Excel-compatible CSV format, iterating through all the spreadsheets passed on the command-line.

``` text
usage: cat-numbers [-h] [-T | -S | -b] [-V] [--debug] [--formulas]
                   [--formatting] [-s SHEET] [-t TABLE] [document ...]

Export data from Apple Numbers spreadsheet tables

positional arguments:
  document                 Document(s) to export

optional arguments:
  -h, --help               show this help message and exit
  -T, --list-tables        List the names of tables and exit
  -S, --list-sheets        List the names of sheets and exit
  -b, --brief              Don't prefix data rows with name of sheet/table (default: false)
  -V, --version
  --debug                  Enable debug output
  --formulas               Dump formulas instead of formula results
  --formatting             Dump formatted cells (durations) as they appear in Numbers
  -s SHEET, --sheet SHEET  Names of sheet(s) to include in export
  -t TABLE, --table TABLE  Names of table(s) to include in export
```

Note: `--formatting` will return different capitalisation for 12-hour times due to differences between Numbers' representation of these dates and `datetime.strftime`. Numbers in English locales displays 12-hour times with 'am' and 'pm', but `datetime.strftime` on macOS at least cannot return lower-case versions of AM/PM.

## Numbers File Formats

Numbers uses a proprietary, compressed binary format to store its tables.
This format is comprised of a zip file containing images, as well as
[Snappy](https://github.com/google/snappy)-compressed
[Protobuf](https://github.com/protocolbuffers/protobuf) `.iwa` files containing
metadata, text, and all other definitions used in the spreadsheet.

### Protobuf updates

As `numbers-parser` includes private Protobuf definitions extracted from a copy of Numbers, new versions of Numbers will inevitably create `.numbers` files that cannot be read by `numbers-parser`. As new versions of Numbers are released, running `make bootstrap` will perform all the steps necessary to recreate the protobuf files used `numbers-parser` to read Numbers spreadsheets.

The default protobuf package installation may not include the C++ optimised version which is required by the bootstrapping scripts to extract protobufs. You will receive the following error during build if this is the case:

 `This script requires the Protobuf installation to use the C++ implementation. Please reinstall Protobuf with C++ support.`

 To include the C++ support, download a released version of Google protobuf [from github](https://github.com/protocolbuffers/protobuf). Build instructions are described in [`src/README.md`](https://github.com/protocolbuffers/protobuf/blob/main/src/README).These have changed greatly over time, but as of April 2023, this was useful:

``` shell
bazel build :protoc :protobuf
cmake . -DCMAKE_CXX_STANDARD=14
cmake --build . --parallel 8
export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=cpp
export LD_LIBRARY_PATH=../bazel-bin/src/google
cd python
python3 setup.py -q bdist_wheel --cpp_implementation --warnings_as_errors --compile_static_extension
```

This can then be used `make bootstrap` in the `numbers-parser` source tree. The signing workflow assumes that you have an Apple Developer Account and that you have created provisioning profile that includes iCloud. Using a self-signed certificate does not seem to work, at least on Apple Silicon (a working PR contradicting this is greatly appreciated).

`make bootstrap` requires [PyObjC](https://pypi.org/project/pyobjc/) to genetrate font maps, but this dependency is excluded from Poetry to ensure that tests can run on non-Mac OSes. You can run `poetry run pip install PyObjC` to get the required packages.

## Credits

`numbers-parser` was built by [Jon Connell](http://github.com/masaccio) but relies heavily on from [prior work](https://github.com/psobot/keynote-parser) by [Peter Sobot](https://petersobot.com) to read the IWA format archives used by Apple's iWork family of applications, and to regenerate the mapping files required for Python. Both modules are derived from [previous work](https://github.com/obriensp/iWorkFileFormat/blob/master/Docs/index.md) by [Sean Patrick O'Brien](http://www.obriensp.com).

Decoding the data structures inside Numbers files was helped greatly by [Stingray-Reader](https://github.com/slott56/Stingray-Reader) by [Steven Lott](https://github.com/slott56).

Formula tests were adapted from JavaScript tests used in
[fast-formula-parser](https://github.com/LesterLyu/fast-formula-parser).

Decimal128 conversion to and from byte storage was adapted from work done by the
[SheetsJS project](https://github.com/SheetJS/sheetjs). SheetJS also helped greatly with some of the steps required to successfully save a Numbers spreadsheet.

## License

All code in this repository is licensed under the [MIT License](https://github.com/masaccio/numbers-parser/blob/master/LICENSE.rst)
