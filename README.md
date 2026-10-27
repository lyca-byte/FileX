
# FileX

Offline multi-format file converter built with Python.

FileX is a command-line tool designed to convert supported file formats locally without uploading files to online conversion services.

## Features

- CLI-only interface
- Local file processing
- Command-line argument parsing
- Input validation
- Modular conversion architecture (in development)

## Requirements

- Python 3.11 or newer
- pip
- Git (optional)

## Installation

Clone the repository and navigate to the project directory.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install FileX in editable mode:

```bash
python -m pip install -e .
```

Install development dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

## Usage

Display help:

```bash
filex --help
```

Display the version:

```bash
filex --version
```

Example conversion command (conversion implementation is not available yet):

```bash
filex --file report.docx --to pdf
```

## Development

Run unit tests:

```bash
python -m pytest
```

## Project Status

FileX is currently under development.

The initial stage focuses on CLI setup and project foundations. Conversion engines and supported format implementations will be added incrementally.
