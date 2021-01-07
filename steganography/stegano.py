import numpy as np
from PIL import Image


def encode(data: str, input_img: Image):
    offset = 0

    width, height = input_img.size
    rgb_img = input_img.convert("RGB")
    
    max_size = width * height
    if len(data) > max_size:
        raise RuntimeError(f"Dane maja za duzy rozmiar. Maksymalny rozmiar moze wynosic {max_size}B")

    for x in range(0, width):
        for y in range(0, height):
            r, g, b = rgb_img.getpixel((x, y))
            pixel = [r, g, b]
            for i in range(0, 3):
                if offset < len(data):
                    mask = ~1
                    pixel[i] = pixel[i] & mask | int(data[offset])
                    offset += 1
            print(pixel)
            rgb_img.putpixel((x, y), tuple(pixel))
    
    rgb_img.save("secret.png", "PNG")


def decode(data_length: int, secret_img: Image) -> str:
    offset = 0
    extracted_bin = []

    width, height = secret_img.size
    rgb_img = secret_img.convert("RGB")

    for x in range(0, width):
        for y in range(0, height):
            r, g, b = rgb_img.getpixel((x, y))
            pixel = [r, g, b]
            for i in range(0, 3):
                if offset < data_length:
                    extracted_bin.append(pixel[i] & 1)
                    offset += 1
    data = "".join([str(x) for x in extracted_bin])
    return data


if __name__ == '__main__':
    data = "011011000110010101100100011001110110010101110010"
    
    src_img = Image.open("python.png")
    encode(data, src_img)

    secret_img = Image.open("secret.png")
    encrypted_data = decode(len(data), secret_img)
    print(f"encrypted_data: {encrypted_data}")
