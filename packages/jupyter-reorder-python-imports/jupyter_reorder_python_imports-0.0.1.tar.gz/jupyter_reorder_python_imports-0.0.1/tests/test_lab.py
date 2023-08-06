"""Tests for jupyter_black running in jupyter lab."""
import typing as t
from conftest import source_from_cell


def test_load_ext(lab: t.Callable[..., t.Dict[str, t.Any]]) -> None:
    """Test loading with `%load_ext jupyter_reorder_python_imports`"""
    cells = [
        {
            "source": ["%load_ext jupyter_reorder_python_imports"],
        },
        {
            "id": "imports1",
            "source": ["import re\nimport datetime"],
        },
        {
            "id": "imports2",
            "source": ["import datetime\nimport re"],
        },
    ]
    output = lab(cells)
    cell_imports1 = source_from_cell(output, "imports1")
    assert "".join(cell_imports1) == "import datetime\nimport re\n"
    cell_imports2 = source_from_cell(output, "imports2")
    assert "".join(cell_imports2) == "import datetime\nimport re\n"
