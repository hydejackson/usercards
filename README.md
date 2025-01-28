# CardsMaker Project

This project generates namecards for new hires by reading data from an Excel file and inserting it into a Word template.

## Files

- `main.py`: Main script to run the project.
- `CreateFile.py`: Contains functions to create and combine Word documents.
- `PutData.py`: Contains functions to insert data into Word documents.
- `PasswordGenerator.py`: Generates random passwords.
- `ReadExcel.py`: Reads data from Excel files.
- `ColClass.py`: Processes columns from Excel data.
- `RowClass.py`: Processes rows from Excel data.
- `templates/`: Directory containing template files (`cards.docx`, `randomwords.csv`).

## Usage

To run the project, use the following command:

```sh
python main.py <path_to_excel_file> [--word <path_to_word_template>]
```

- `<path_to_excel_file>`: Path to the Excel file containing new hire data.
- `--word <path_to_word_template>` (optional): Path to the Word template file (default: `templates/cards.docx`).

## Configuration

The configuration file should contain:

1. Excel file path (line 1)
2. Word file path (line 2, optional)

## Output

The generated Word files will be saved in the `output` directory with the current date appended to the filename.

## Example

```sh
python main.py data/new_hires.xlsx --word templates/custom_template.docx
```

## References

- [python-docx Documentation](https://python-docx.readthedocs.io/en/latest/)
- [pandas Documentation](https://pandas.pydata.org/docs/reference/index.html#api)
