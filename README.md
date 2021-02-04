# AWS Uploader

Created for CS493. Uploads files and directories (even if they have sub-directories) to AWS S3 with a mediocre graphical interface.

## Requirements

Python 3 and pre-configured AWS credentials in ~/.aws


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
> pip install -r requirements.txt
```

Verify the test suite passes (you must run this from the root project directory)
```bash
> pytest
```

Run the program
```bash
> python main.py
```

## Usage

When the interface opens, first enter an AWS profile (or leave it blank to use your default profile) and click "set" (even if you are using the default).

Select a bucket from the dropdown.

Select either a file or directory, and click upload.
