import io
from PIL import Image


def to_bytes(file_name):
    with open(file_name, "rb") as f:
        return f.read()


def to_image(img_bytes):
    return Image.open(io.BytesIO(img_bytes))
