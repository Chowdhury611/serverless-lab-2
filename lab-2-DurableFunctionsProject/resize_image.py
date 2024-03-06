import azure.functions as func
from PIL import Image
import io

def main(image_bytes: bytes) -> bytes:
    # Open the image from bytes
    image = Image.open(io.BytesIO(image_bytes))
    
    # Resize the image to a standard size (e.g., 1024x768 pixels)
    resized_image = image.resize((1024, 768))
    
    # Convert the resized image to bytes
    output_buffer = io.BytesIO()
    resized_image.save(output_buffer, format='JPEG')
    resized_image_bytes = output_buffer.getvalue()
    
    return resized_image_bytes
