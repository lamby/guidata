# -*- coding: utf-8 -*-
#
# Licensed under the terms of the BSD 3-Clause
# (see guidata/LICENSE for details)

"""
All guidata item/group features demo
"""

# guitest: show

import atexit
import shutil
import tempfile

import numpy as np

from guidata.dataset.dataitems import (
    BoolItem,
    ChoiceItem,
    ColorItem,
    DictItem,
    DirectoryItem,
    FileOpenItem,
    FileSaveItem,
    FilesOpenItem,
    FloatArrayItem,
    FloatItem,
    ImageChoiceItem,
    IntItem,
    MultipleChoiceItem,
    StringItem,
    TextItem,
)
from guidata.dataset.datatypes import (
    BeginGroup,
    BeginTabGroup,
    DataSet,
    EndGroup,
    EndTabGroup,
    ObjectItem,
)
from guidata.dataset.qtitemwidgets import DataSetWidget
from guidata.dataset.qtwidgets import DataSetEditLayout, DataSetShowLayout
from guidata.env import execenv
from guidata.qthelpers import qt_app_context

# Creating temporary files and registering cleanup functions
TEMPDIR = tempfile.mkdtemp(prefix="test_")
atexit.register(shutil.rmtree, TEMPDIR)
FILE_ETA = tempfile.NamedTemporaryFile(suffix=".eta", dir=TEMPDIR)
atexit.register(FILE_ETA.close)
FILE_CSV = tempfile.NamedTemporaryFile(suffix=".csv", dir=TEMPDIR)
atexit.register(FILE_CSV.close)


class SubDataSet(DataSet):
    dir = DirectoryItem("Directory", TEMPDIR)
    fname = FileOpenItem("Single file (open)", ("csv", "eta"), FILE_CSV.name)
    fnames = FilesOpenItem("Multiple files", "csv", FILE_CSV.name)
    fname_s = FileSaveItem("Single file (save)", "eta", FILE_ETA.name)


class SubDataSetWidget(DataSetWidget):
    klass = SubDataSet


class SubDataSetItem(ObjectItem):
    klass = SubDataSet


DataSetEditLayout.register(SubDataSetItem, SubDataSetWidget)
DataSetShowLayout.register(SubDataSetItem, SubDataSetWidget)


class Parameters(DataSet):
    """
    DataSet test
    The following text is the DataSet 'comment': <br>Plain text or
    <b>rich text<sup>2</sup></b> are both supported,
    as well as special characters (α, β, γ, δ, ...)
    """

    dict_ = DictItem(
        "dict_item",
        {
            "strings_col": ["a", "b", "c"],
            "_col": [1, 2.0, 3],
            "float_col": 1.0,
        },
    )
    string = StringItem("String")
    text = TextItem("Text")
    _bg = BeginGroup("A sub group")
    float_slider = FloatItem(
        "Float (with slider)", default=0.5, min=0, max=1, step=0.01, slider=True
    )
    fl1 = FloatItem(
        "Current", default=10.0, min=1, max=30, unit="mA", help="Threshold current"
    )
    fl2 = FloatItem(
        "Float (col=1)", default=1.0, min=1, max=1, help="Help on float item"
    ).set_pos(col=1)
    fl3 = FloatItem("Not checked float").set_prop("data", check_value=False)
    bool1 = BoolItem("Boolean option without label")
    bool2 = BoolItem("Boolean option with label", "Label").set_pos(col=1, colspan=2)
    color = ColorItem("Color", default="red")
    choice1 = ChoiceItem(
        "Single choice (radio)",
        [(16, "first choice"), (32, "second choice"), (64, "third choice")],
        radio=True,
    ).set_pos(col=1, colspan=2)
    choice2 = ChoiceItem(
        "Single choice (combo)",
        [(16, "first choice"), (32, "second choice"), (64, "third choice")],
    ).set_pos(col=1, colspan=2)
    _eg = EndGroup("A sub group")
    floatarray = FloatArrayItem(
        "Float array", default=np.ones((50, 5), float), format=" %.2e "
    ).set_pos(col=1)
    g0 = BeginTabGroup("group")
    mchoice1 = MultipleChoiceItem(
        "MC type 1", ["first choice", "second choice", "third choice"]
    ).vertical(2)
    mchoice2 = (
        ImageChoiceItem(
            "MC type 2",
            [
                ("rect", "first choice", "gif.png"),
                ("ell", "second choice", "txt.png"),
                ("qcq", "third choice", "file.png"),
            ],
        )
        .set_pos(col=1)
        .set_prop("display", icon="file.png")
    )
    mchoice3 = MultipleChoiceItem("MC type 3", [str(i) for i in range(10)]).horizontal(
        2
    )
    eg0 = EndTabGroup("group")
    integer_slider = IntItem(
        "Integer (with slider)", default=5, min=-50, max=-50, slider=True
    )
    integer = IntItem("Integer", default=5, min=3, max=6).set_pos(col=1)


def test_all_features():
    """Test all guidata item/group features"""
    with qt_app_context():
        e = Parameters()
        e.floatarray[:, 0] = np.linspace(-5, 5, 50)
        execenv.print(e)

        if e.edit():
            e.edit()
            execenv.print(e)
        e.view()

        f = Parameters.create(integer=10101010, string="Using create class method")
        print(f)

        execenv.print("OK")


if __name__ == "__main__":
    test_all_features()
