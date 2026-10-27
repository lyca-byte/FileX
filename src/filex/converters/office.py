
"""Local DOCX and PDF conversion using LibreOffice."""

import shutil
import subprocess
import tempfile
from pathlib import Path

from filex.exceptions import FileXError


def find_libreoffice() -> Path:
    """Find the LibreOffice executable."""
    executable = shutil.which("soffice")

    if executable:
        return Path(executable)

    candidates = [
        Path("C:/Program Files/LibreOffice/program/soffice.exe"),
        Path("C:/Program Files (x86)/LibreOffice/program/soffice.exe"),
    ]

    for candidate in candidates:
        if candidate.is_file():
            return candidate

    raise FileXError(
        "LibreOffice was not found. Install LibreOffice to convert DOCX and PDF."
    )


class OfficeConverter:
    """Convert DOCX to PDF and PDF to DOCX locally."""

    def convert(
        self,
        input_path: Path,
        output_path: Path,
        target_format: str,
    ) -> None:
        soffice = find_libreoffice()
        input_path = input_path.resolve()
        output_path = output_path.resolve()

        with tempfile.TemporaryDirectory(prefix="filex_") as temp:
            temp_dir = Path(temp)
            result_dir = temp_dir / "result"
            profile_dir = temp_dir / "profile"
            result_dir.mkdir()
            profile_dir.mkdir()

            command = [
                str(soffice),
                "--headless",
                f"-env:UserInstallation={profile_dir.as_uri()}",
                "--convert-to",
                target_format,
                "--outdir",
                str(result_dir),
                str(input_path),
            ]

            try:
                process = subprocess.run(
                    command,
                    capture_output=True,
                    text=True,
                    timeout=120,
                    check=False,
                )
            except subprocess.TimeoutExpired as exc:
                raise FileXError(
                    "Document conversion timed out after 120 seconds."
                ) from exc
            except OSError as exc:
                raise FileXError(
                    f"Could not start LibreOffice: {exc}"
                ) from exc

            generated_file = result_dir / (
                f"{input_path.stem}.{target_format}"
            )

            if process.returncode != 0 or not generated_file.is_file():
                details = (process.stderr or process.stdout).strip()
                raise FileXError(
                    "Document conversion failed."
                    + (f" Details: {details}" if details else "")
                )

            try:
                with generated_file.open("rb") as source:
                    with output_path.open("xb") as destination:
                        shutil.copyfileobj(source, destination)
            except FileExistsError as exc:
                raise FileXError(
                    f"Output file already exists: {output_path}"
                ) from exc
            except OSError as exc:
                output_path.unlink(missing_ok=True)
                raise FileXError(
                    f"Could not save converted document: {exc}"
                ) from exc
