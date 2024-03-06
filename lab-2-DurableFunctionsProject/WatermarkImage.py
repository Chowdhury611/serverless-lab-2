# Import necessary modules
from PIL import Image, ImageDraw, ImageFont
import io

def watermark_image(input_image_bytes, watermark_text):
    # Convert input image bytes to PIL image object
    input_image = Image.open(io.BytesIO(input_image_bytes))
    
    # Add watermark text to the image
    draw = ImageDraw.Draw(input_image)
    font = ImageFont.truetype("arial.ttf", 36)  # Choose a font and font size
    draw.text((10, 10), watermark_text, fill=(255, 255, 255), font=font)  # Adjust position as needed
    
    # Save the modified image to a bytes-like object
    output_image_bytes = io.BytesIO()
    input_image.save(output_image_bytes, format='JPEG')
    output_image_bytes.seek(0)
    
    return output_image_bytes.read()
