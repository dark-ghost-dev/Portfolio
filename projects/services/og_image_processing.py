from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

def process_og_image(image_file):
    image = Image.open(image_file)

    if image.mode != 'RGB':
        image = image.convert('RGB')

    target_width = 1200
    target_height = 630
    target_ratio = target_width / target_height
    img_ratio = image.width / image.height

    # Crop centrado
    if img_ratio > target_ratio:
        new_width = int(image.height * target_ratio)
        left = (image.width - new_width) / 2
        image = image.crop((left, 0, left + new_width, image.height))

    elif img_ratio < target_ratio:
        new_height = int(image.width / target_ratio)
        top = (image.height - new_height) / 2
        image = image.crop((0, top, image.width, top + new_height))

    # Resize
    image = image.resize((target_width, target_height), Image.Resampling.LANCZOS)

    buffer = BytesIO()
    image.save(buffer, format='JPEG', quality=90)
    buffer.seek(0)

    return ContentFile(buffer.read())