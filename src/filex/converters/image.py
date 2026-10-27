"""Local image format conversion."""

from pathlib import Path

from PIL import Image, UnidentifiedImageError

from filex.exceptions import FileXError


PIL_FORMATS = {
    "png": "PNG",
    "jpg": "JPEG",
    "webp": "WEBP",
}


class ImageConverter:
    """Convert images using Pillow."""

    def convert(
        self,
        input_path: Path,
        output_path: Path,
        target_format: str,
    ) -> None:
        """Convert an image to the requested format."""
        try:
            with Image.open(input_path) as image:
                image.load()

                if target_format == "jpg":
                    if image.mode in ("RGBA", "LA") or (
                        image.mode == "P" and "transparency" in image.info
                    ):
                        rgba = image.convert("RGBA")
                        background = Image.new(
                            "RGB", rgba.size, (255, 255, 255)
                        )
                        background.paste(
                            rgba, mask=rgba.getchannel("A")
                        )
                        converted = background
                    else:
                        converted = image.convert("RGB")
                elif target_format == "png":
                    converted = image.convert(
                        "RGBA" if "A" in image.getbands() else "RGB"
                    )
                else:
                    converted = image.convert("RGB")

                converted.save(
                    output_path,
                    format=PIL_FORMATS[target_format],
                )

        except (UnidentifiedImageError, OSError, ValueError) as exc:
            output_path.unlink(missing_ok=True)
            raise FileXError(
                f"Could not convert image: {exc}"
            ) from exc