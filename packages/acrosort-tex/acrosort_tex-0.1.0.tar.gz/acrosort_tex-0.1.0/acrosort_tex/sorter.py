import argparse
import re

from rich.console import Console


def _load_file(filename: str) -> list:
    """
    Load .tex file with abbreviations and return a list of lines.

    Args:
        filename (str): .tex file path

    Returns:
        list: List of all lines in the .tex file
    """
    with open(filename, "r") as f:
        tex_lines = f.readlines()
    return tex_lines


def _find_acronym_block(tex_lines: list) -> tuple:
    """
    Find the start and end of the acronym block in the .tex file and find the longest shortform key.
    Longest shortform key is needed to set the width of the shortform column in the acronym block.

    Args:
        tex_lines (list): List of all lines in the .tex file

    Returns:
        tuple: (Index of Start Block of Acronyms, Index of End Block of Acronyms, Longest Shortform Key)
    """
    acronym_block_start = None
    acronym_block_end = None
    longest_shortform_key = None
    longest_shortform_len = 0

    for i, line in enumerate(tex_lines):
        if "\\begin{acronym}" in line:
            acronym_block_start = i
            longest_shortform_key = re.findall(r"\[([^\]]+)\]", line)[0]
        elif "\\end{acronym}" in line:
            acronym_block_end = i
            break
        else:
            match = re.search(r"\\acro\{(.+?)\}\[(.+?)\]\{(.+?)\}", line)
            if match:
                shortform_len = len(match.group(2))
                if shortform_len > longest_shortform_len:
                    longest_shortform_key = match.group(1)
                    longest_shortform_len = shortform_len

    return acronym_block_start, acronym_block_end, longest_shortform_key


def _extract_acronym_lines(
    acronym_block_start: int, acronym_block_end: int, tex_lines: list
) -> list:
    """
    Extract only the acronym block.

    Args:
        acronym_block_start (int): Index of Start Block of Acronyms
        acronym_block_end (int): Index of End Block of Acronyms
        tex_lines (list):

    Returns:
        list: List of all lines in the .tex file
    """
    acronym_lines = tex_lines[acronym_block_start : acronym_block_end + 1]
    acronym_lines = [line.strip() for line in acronym_lines]
    return acronym_lines


def _extract_acronyms(acronym_lines: list) -> dict:
    """
    Extract all acronyms from block

    Args:
        acronym_lines (list): List of all acronym lines.

    Returns:
        dict: Key-Value Pair of acronyms. Key is the shortform, Value is a tuple of (key_in_file, long_form)
    """
    acronyms = {}
    for line in acronym_lines:
        match = re.search(r"\\acro\{(.+?)\}\[(.+?)\]\{(.+?)\}", line)
        if match:
            key = match.group(1)
            key_in_file = match.group(2)
            long_form = match.group(3)
            acronyms[key] = (key_in_file, long_form)
    return acronyms


def _sort_acronyms(acronyms: dict) -> list:
    """
    Sort acronyms by their shortform in ascending order.

    Args:
        acronyms (dict): Dictionary of all acronyms

    Returns:
        list: Sorted acronyms by shortform
    """
    return sorted(acronyms.items(), key=lambda x: x[1][0].lower())


def _replace_old_acronym_block_with_new_one(
    acronym_block_start: int,
    acronym_block_end: int,
    tex_lines: list,
    sorted_acronyms: list,
    longest_shortform_key: str,
) -> list:
    """
    Replace the old acronym block with the new one.

    Args:
        acronym_block_start (int): Index of Start Block of Acronyms
        acronym_block_end (int): Index of End Block of Acronyms
        tex_lines (list): List of all lines in the .tex file
        sorted_acronyms (list): Acronyms in ascending order
        longest_shortform_key (str): Longest shortform key to set the width of the shortform column in the acronym block

    Returns:
        list: All lines with the new acronym block
    """
    new_acronym_lines = [f"\\begin{{acronym}}[{longest_shortform_key}]\n"]
    for key, (key_in_file, long_form) in sorted_acronyms:
        new_line = f"\\acro{{{key}}}{{{key_in_file}}}{{{long_form}}}\n"
        new_acronym_lines.append(new_line)
    new_acronym_lines.append("\\end{acronym}\n")

    tex_lines = (
        tex_lines[:acronym_block_start]
        + new_acronym_lines
        + tex_lines[acronym_block_end + 1 :]
    )

    return tex_lines


def _write_file(output_filename: str, tex_lines: list) -> None:
    """
    Write the new .tex file.

    Args:
        output_filename (str): Filename of outputted .tex file
        tex_lines (list): All lines with the new acronym block
    """
    with open(output_filename, "w") as f:
        f.writelines(tex_lines)


def main():
    parser = argparse.ArgumentParser(description="Sort Acronyms with Acrosort")
    parser.add_argument(
        "input_file", type=str, help="filename of your file containing the acronyms"
    )
    parser.add_argument("output_file", type=str, help="filename of your output file")

    args = parser.parse_args()

    tex_lines = _load_file(args.input_file)

    acronym_block_start, acronym_block_end, longest_shortform_key = _find_acronym_block(
        tex_lines
    )

    acronym_lines = _extract_acronym_lines(
        acronym_block_start, acronym_block_end, tex_lines
    )

    acronyms = _extract_acronyms(acronym_lines)

    acronyms = _sort_acronyms(acronyms)

    tex_lines = _replace_old_acronym_block_with_new_one(
        acronym_block_start,
        acronym_block_end,
        tex_lines,
        acronyms,
        longest_shortform_key,
    )

    _write_file(args.output_file, tex_lines)

    console = Console()
    console.print(
        f"[bold green]Successfully sorted acronyms and wrote to {args.output_file} [/bold green]"
    )
