import pytest

from collections import defaultdict
from pytest_check import check

from numbers_parser import Document, MergedCell
from numbers_parser.cell import Border, xl_rowcol_to_cell, Cell, BorderType, RGB


def check_border(cell: Cell, side: str, test_value: str) -> bool:
    border_value = getattr(cell.border, side, None)
    if test_value == "None":
        valid = check.is_none(border_value)
        ref = "None"
    else:
        values = test_value.split(",")
        values[0] = float(values[0])
        values[1] = eval(values[1].replace(";", ","))
        if border_value is None:
            return False
        ref = Border(values[0], values[1], values[2])
        valid = check.equal(border_value, ref)
    if not valid:
        cell_name = xl_rowcol_to_cell(cell.row, cell.col)
        print(f"@{cell_name}[{cell.row},{cell.col}].{side}: {border_value} != {ref}")
    return valid


TAG_TO_BORDER_MAP = {"T": "top", "R": "right", "B": "bottom", "L": "left"}
BORDER_TO_TAG_MAP = {v: k for k, v in TAG_TO_BORDER_MAP.items()}
ALL_BORDERS = ["top", "right", "bottom", "left"]


def unpack_test_string(test_value):
    # Cell test values are of the form:
    #
    # T=1,(0;162;255),dashes
    # R=1,(0;162;255),dashes
    # B=1,(0;162;255),dashes
    # L=1,(0;162;255),dashes
    #
    # Merge cells have multiple values T0, T1, etc.
    tests = test_value.split("\n")
    test_values = {}
    for test in tests:
        tag = TAG_TO_BORDER_MAP[test[0]]
        if test[1] == "=":
            test_values[tag] = test[2:]
        else:
            if tag not in test_values:
                test_values[tag] = defaultdict()
            offset = int(test[1])
            test_values[tag][offset] = test[3:]
    return test_values


def test_exceptions():
    with pytest.raises(TypeError) as e:
        _ = Border(width="invalid")
    assert "width must be a float number" in str(e)
    with pytest.raises(TypeError) as e:
        _ = Border(width="invalid")
    assert "width must be a float number" in str(e)

    with pytest.raises(TypeError) as e:
        _ = Border(color=(0, 0, 0, 0))
    assert "RGB color must be an RGB" in str(e)
    with pytest.raises(TypeError) as e:
        _ = Border(color=(0, 0, 1.0))
    assert "RGB color must be an RGB" in str(e)

    with pytest.raises(TypeError) as e:
        _ = Border(style="invalid")
    assert "invalid border style" in str(e)

    style = Border(style=BorderType(3))
    assert str(style) == "Border(width=0.35, color=RGB(r=0, g=0, b=0), style=none)"

    doc = Document()
    with pytest.raises(TypeError) as e:
        doc.sheets[0].tables[0].set_cell_border("A1", 1)
    assert "invalid number of arguments to border_value()" in str(e)

    with pytest.raises(TypeError) as e:
        doc.sheets[0].tables[0].set_cell_border("A1", 1, 2, 3, 4)
    assert "invalid number of arguments to border_value()" in str(e)

    with pytest.raises(TypeError) as e:
        doc.sheets[0].tables[0].set_cell_border("A1", "invalid", Border(1.0, RGB(0, 0, 0), "solid"))
    assert "side must be a valid border segment" in str(e)

    with pytest.raises(TypeError) as e:
        doc.sheets[0].tables[0].set_cell_border("A1", "left", object())
    assert "border value must be a Border object" in str(e)

    with pytest.raises(TypeError) as e:
        doc.sheets[0].tables[0].set_cell_border(
            "A1", "left", Border(1.0, RGB(0, 0, 0), "solid"), "invalid"
        )
    assert "border length must be an int" in str(e)


def run_border_tests(filename):
    doc = Document(filename)

    for sheet_name in ["Borders", "Large Borders"]:
        table = doc.sheets[sheet_name].tables[0]

        with pytest.warns() as record:
            table.cell(0, 0).border = object()
        assert len(record) == 1
        assert "cell border values cannot be set" in str(record[0])

        for row_num, row in enumerate(table.iter_rows()):
            for col_num, cell in enumerate(row):
                if not cell.value or isinstance(cell, MergedCell):
                    continue
                tests = unpack_test_string(cell.value)
                if cell.is_merged:
                    valid = []
                    row_start = row_num
                    row_end = row_num + cell.size[0] - 1
                    col_start = col_num
                    col_end = col_num + cell.size[1] - 1
                    offset = 0
                    for merge_row_num in range(row_start, row_end + 1):
                        merge_cell = table.cell(merge_row_num, col_num)
                        valid.append(check_border(merge_cell, "left", tests["left"][offset]))
                        merge_cell = table.cell(merge_row_num, col_end)
                        valid.append(check_border(merge_cell, "right", tests["right"][offset]))
                        offset += 1

                    offset = 0
                    for merge_col_num in range(col_start, col_end + 1):
                        merge_cell = table.cell(row_num, merge_col_num)
                        valid.append(check_border(merge_cell, "top", tests["top"][offset]))
                        merge_cell = table.cell(row_end, merge_col_num)
                        valid.append(check_border(merge_cell, "bottom", tests["bottom"][offset]))
                        offset += 1
                else:
                    valid = [
                        check_border(cell, "top", tests["top"]),
                        check_border(cell, "right", tests["right"]),
                        check_border(cell, "bottom", tests["bottom"]),
                        check_border(cell, "left", tests["left"]),
                    ]
                assert valid


def test_borders():
    run_border_tests("tests/data/test-styles.numbers")


def test_empty_borders():
    doc = Document("tests/data/test-styles.numbers")
    sheet = doc.sheets["Large Borders"]
    table = sheet.tables[0]

    assert table.cell("F10").border.right is None
    assert table.cell("F10").border.bottom is None
    assert table.cell("F13").border.top is None
    assert table.cell("F13").border.right is None
    assert table.cell("H10").border.left is None
    assert table.cell("H10").border.bottom is None
    assert table.cell("H13").border.left is None
    assert table.cell("H13").border.top is None


def test_edit_borders(configurable_save_file):
    doc = Document()
    sheet = doc.sheets[0]
    table = sheet.tables[0]

    table.set_cell_border("B6", "left", Border(8.0, RGB(29, 177, 0), "solid"), 3)
    table.set_cell_border(6, 1, "right", Border(5.0, RGB(29, 177, 0), "dashes"))
    table.merge_cells(["C3:F4", "C10:F11"])
    table.merge_cells("C3:F4")
    table.set_cell_border("C3", ALL_BORDERS, Border(3.0, RGB(0, 162, 255), "dots"))
    table.set_cell_border("C10", ALL_BORDERS, Border(3.0, RGB(29, 177, 0), "dots"))
    table.set_cell_border("B2", ALL_BORDERS, Border(4.0, RGB(0, 0, 0), "solid"))

    doc.save(configurable_save_file)

    new_doc = Document(configurable_save_file)
    sheet = new_doc.sheets[0]
    table = sheet.tables[0]
    assert (
        str(table.cell("B6").border.left)
        == "Border(width=8.0, color=RGB(r=29, g=177, b=0), style=solid)"
    )
    assert (
        str(table.cell("B7").border.right)
        == "Border(width=5.0, color=RGB(r=29, g=177, b=0), style=dashes)"
    )
    assert table.cell("C4").border.right is None

    ref = "Border(width=3.0, color=RGB(r=0, g=162, b=255), style=dots)"
    assert str(table.cell("C3").border.bottom) == ref
    assert str(table.cell("C3").border.right) == ref
    assert all([str(table.cell(4, col_num).border.top) == ref for col_num in range(2, 6)])


def invert_border_test(test):
    if test == "None":
        return None, None
    else:
        values = test.split(",")
        width = float(values[0])
        color = eval(values[1].replace(";", ","))
        style = values[2]
        if width < 4.0:
            width = round(width * 2.0, 1)
        else:
            width = round(width / 2.0, 1)

        color = (abs(200 - color[0]), abs(200 - color[1]), abs(200 - color[2]))

        if style == "solid":
            style = "dashes"
        elif style == "dashes":
            style = "dots"
        elif style == "dots":
            style = "none"
            width = 0.0
            color = (0, 0, 0)
        elif style == "none":
            style = "solid"

        border = Border(width, color, style)

        color = "(" + ";".join([str(x) for x in color]) + ")"
        test_value = ",".join([str(width), color, style])
        return test_value, border


def invert_tests(tests):
    new_tests = []
    new_borders = []
    test_string = ""
    for side, test in tests.items():
        if isinstance(test, str):
            (new_test, border) = invert_border_test(test)
            new_tests.append(new_test)
            new_borders.append(border)
            test_string += BORDER_TO_TAG_MAP[side] + "=" + str(new_tests[-1]) + "\n"
        else:
            for i in range(len(test)):
                (new_test, border) = invert_border_test(test[i])
                new_tests.append(new_test)
                new_borders.append(border)
                test_string += BORDER_TO_TAG_MAP[side] + f"{i}=" + str(new_tests[-1]) + "\n"
    return test_string.strip(), new_tests, new_borders


@pytest.mark.experimental
def test_resave_borders(configurable_save_file):
    doc = Document("tests/data/test-styles.numbers")

    style = doc.add_style(font_size=8.0, bold=False, name="Border Test Style")
    # for sheet_name in ["Borders", "Large Borders"]:
    for sheet_name in ["Borders"]:
        table = doc.sheets[sheet_name].tables[0]

        for row_num, row in enumerate(table.iter_rows()):
            for col_num, cell in enumerate(row):
                if not cell.value or isinstance(cell, MergedCell):
                    continue
                tests = unpack_test_string(cell.value)
                (test_string, new_tests, borders) = invert_tests(tests)
                table.write(row_num, col_num, test_string, style=style)
                for i, side in enumerate(tests):
                    if cell.is_merged:
                        if side in ["left", "right"]:
                            length = cell.size[0]
                        else:
                            length = cell.size[1]
                    else:
                        length = 1
                    if borders[i] is not None:
                        table.set_cell_border(row_num, col_num, side, borders[i], length)

    doc.save(configurable_save_file)
    run_border_tests(configurable_save_file)
