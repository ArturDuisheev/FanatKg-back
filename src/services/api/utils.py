from PIL import Image
from io import BytesIO


def convert_image_to_rgb(image):
    if image.mode != 'RGB':
        image = image.convert('RGB')
    return image


def compress_image(image):
    try:
        img = Image.open(image)
        img = convert_image_to_rgb(img)
        img.thumbnail((800, 800))
        output_buffer = BytesIO()
        img.save(output_buffer, format='JPEG', quality=30)
        output_buffer.seek(0)
        return output_buffer
    except Exception as e:
        raise e
