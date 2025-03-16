import io
from PIL import Image


def parse(file_name):
    with open(file_name, "rb") as f:
        return f.read()


def read(img_bytes):
    return Image.open(io.BytesIO(img_bytes))
