"""Tests for image conversion."""

from PIL import Image

from filex.core.conversion import convert_file


def test_png_to_webp(tmp_path):
    source = tmp_path / "sample.png"
    destination = tmp_path / "sample.webp"

    Image.new("RGB", (16, 16), (255, 0, 0)).save(source)

    result = convert_file(source, "webp")

    assert result == destination
    assert destination.is_file()
    assert source.is_file()

    with Image.open(destination) as converted:
        assert converted.format == "WEBP"
        assert converted.size == (16, 16)


def test_png_to_jpg(tmp_path):
    source = tmp_path / "sample.png"
    Image.new("RGBA", (16, 16), (255, 0, 0, 128)).save(source)

    result = convert_file(source, "jpg")

    assert result.is_file()

    with Image.open(result) as converted:
        assert converted.format == "JPEG"
        assert converted.mode == "RGB"


def test_reject_same_format(tmp_path):
    source = tmp_path / "sample.png"
    Image.new("RGB", (16, 16)).save(source)

    try:
        convert_file(source, "png")
    except Exception as exc:
        assert "identical" in str(exc)
    else:
        raise AssertionError("Expected same-format conversion to fail")