from PIL import Image
from pillow_heif import register_heif_opener
import os

#help(register_heif_opener)
register_heif_opener()

# Usage example
heic_file_path = "/Users/anne1/Downloads/IMG_5842.heic"
pdf_file_path = "/Users/anne1/Downloads/item_3.pdf"

temp_image = Image.open(heic_file_path)
png_photo = heic_file_path.replace('.HEIC','png')
#temp_image.save(png_photo)
im1 = temp_image.convert('RGB')
im1.save(pdf_file_path)
print("done")

