# acrosort-tex

`acrosort-tex` is a Python Command Line App to sort your acronyms in your `.tex` by their shortform.

## Installation

You can install acrosort-tex using pip (note the underscore):

```bash
pip install acrosort_tex
```

## Usage

To use `acrosort-tex`, you first need to create a `.tex` file with a list of acronyms (see in `examples` for an example file).

It doesn't matter if there are other TeX commands before or after the `acronym` block.

To sort the acronyms, run the following command:

```bash
acrosort <input_file.tex> <output_file.tex>
```

For example:

```bash
acrosort examples/List_Of_Abbreviations.tex acronyms.tex
```

This will create a new `.tex` file called `sorted_acronyms.tex` with the sorted acronyms, while everything else isn't touched.

It will also find the longest key to set the width of the shortform column in the acronym block.

## License

`acrosort_tex` is licensed under the MIT License. See the LICENSE file for more information.
