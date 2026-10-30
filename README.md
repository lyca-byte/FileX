# FileX

Offline multi-format file converter built with Python. FileX processes files locally instead of uploading them to online conversion services.

## Supported formats

- Images: PNG, JPG/JPEG, WebP
- Documents: DOCX, PDF, ODT, RTF, TXT

Document conversions are attempted through LibreOffice. A format pair is available when the installed LibreOffice version supports importing the source and exporting the requested target. PDF-to-DOCX has a dedicated `pdf2docx` editable mode and a visual mode that embeds rendered PDF pages as images.

## Requirements

- Python 3.10 or newer
- LibreOffice (required for general document conversions)
- pip

LibreOffice must be available as `soffice` in PATH or installed in a standard Windows location, such as `C:\\Program Files\\LibreOffice\\program\\soffice.exe`.

## Installation

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
python -m pip install -r requirements-dev.txt
```

## Usage

```powershell
filex --help
filex --file report.docx --to pdf
filex --file report.docx --to odt
filex --file notes.odt --to rtf
filex --file notes.txt --to docx
filex --file report.pdf --to docx --mode editable
filex --file report.pdf --to docx --mode visual
```

Use `--output` to specify the output file or `--output-dir` to specify its directory. FileX does not overwrite an existing output file.

## Tests

```powershell
python -m pytest
```

## Notes

- Conversion fidelity depends on the source file and LibreOffice filters. Complex layouts, fonts, tables, and embedded objects may change.
- PDF import/export support depends on LibreOffice. PDF-to-DOCX uses the dedicated editable converter by default; `--mode visual` preserves page appearance by embedding page images, but the page content is not editable text.
- FileX does not upload files to an online conversion service. Conversion is performed by locally installed software.
