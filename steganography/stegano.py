from PIL import Image
from typing import List


def encode(data: str, input_img: Image):
    width, height = input_img.size
    rgb_img = input_img.convert("RGB")

    binary_data = _str_to_bits_str(data)
    
    # each pixel can store 3 bits of data
    max_size = width * height * 3 / 8
    if len(data) > max_size:
        raise RuntimeError(f"Dane maja za duzy rozmiar. Maksymalny rozmiar moze wynosic {max_size}B")

    offset = 0
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = rgb_img.getpixel((x, y))
            pixel = [r, g, b]
            for i in range(0, 3):
                if offset < len(binary_data):
                    # ~1 is a bit mask 11111110
                    pixel[i] = pixel[i] & ~1 | int(binary_data[offset])
                    offset += 1
            rgb_img.putpixel((x, y), tuple(pixel))
    
    rgb_img.save("secret.png", "PNG")


def decode(data_length: int, secret_img: Image) -> str:
    width, height = secret_img.size
    rgb_img = secret_img.convert("RGB")

    offset = 0
    extracted_bits = []
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = rgb_img.getpixel((x, y))
            pixel = [r, g, b]
            for i in range(0, 3):
                if offset < data_length:
                    extracted_bits.append(pixel[i] & 1)
                    offset += 1

    data = _bits_to_str(extracted_bits)
    return data


def _str_to_bits_str(input: str) -> List[int]:
    result = []
    for char in input:
        # expression [2:] removes prefix 0b
        bits = bin(ord(char))[2:]
        # extend to 8 bits
        bits = '00000000'[len(bits):] + bits
        # insert all bits to result array
        result.extend([int(b) for b in bits])
    return result


def _bits_to_str(bits: List[int]) -> str:
    result = []
    for b in range(len(bits) // 8):
        # read every 8 characters
        byte = bits[b*8:(b+1)*8]
        # convert 8 characters to int value and this int value to ASCII char
        char = chr(int(''.join([str(bit) for bit in byte]), 2))
        result.append(char)
    return ''.join(result)


if __name__ == '__main__':
    data = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris gravida."
    
    src_img = Image.open("python.png")
    encode(data, src_img)
    print('Data successfully encrypted')

    secret_img = Image.open("secret.png")
    decrypted_data = decode(len(data) * 8, secret_img)
    print(f"decrypted_data: {decrypted_data}")
