import io
import os

import pytest
from utils.code_blocks import get_all_code_blocks, check_py_string

code_path = os.environ.get("INTEG_CODE_PATH", "**/*.md")
all_code_blocks = get_all_code_blocks(code_path)


@pytest.mark.parametrize(
    "block", all_code_blocks, ids=[f["id"] for f in all_code_blocks]
)
def test_code_block(block, monkeypatch):
    # Send some stdin for tests that use the Chat util
    monkeypatch.setattr("sys.stdin", io.StringIO("Hi\nexit\n"))

    check_py_string(block["code"])
