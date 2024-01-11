import pathlib
import textwrap

# Adapted from https://github.com/koaning/mktestdocs


def check_py_string(source: str) -> None:
    """Exec the python source given in a new module namespace

    Does not return anything, but exceptions raised by the source
    will propagate out unmodified
    """
    try:
        exec(source, {"__MODULE__": "__main__"})
    except Exception:
        print(source)
        raise


def check_code_block(block: str, lang: str = "python") -> str:
    """Cleans the found codeblock and checks if the proglang is correct.

    Returns an empty string if the codeblock is deemed invalid.

    Args:
        block: the code block to analyse
        lang: if not None, the language that is assigned to the codeblock
    """
    first_line = block.split("\n")[0]
    if lang:
        if first_line[3:] != lang:
            return ""
    return "\n".join(block.split("\n")[1:])


def get_code_blocks(docstring: str, lang: str = "python") -> list[str]:
    """Given a docstring, grab all the markdown codeblocks found in docstring.

    Args:
        docstring: the docstring to analyse
        lang: if not None, the language that is assigned to the codeblock
    """
    docstring = textwrap.dedent(docstring)
    in_block = False
    block = ""
    codeblocks = []
    for line in docstring.split("\n"):
        if line.startswith("```"):
            if in_block:
                codeblocks.append(check_code_block(block, lang=lang))
                block = ""
            in_block = not in_block
        if in_block:
            block += line + "\n"
    return [c for c in codeblocks if c != ""]


def get_all_code_blocks() -> list[dict]:
    return [
        {"id": f"{str(fpath)}-{block_num + 1}", "code": code_block}
        for fpath in pathlib.Path("docs").glob("**/*.md")
        for block_num, code_block in enumerate(get_code_blocks(fpath.read_text()))
    ]
