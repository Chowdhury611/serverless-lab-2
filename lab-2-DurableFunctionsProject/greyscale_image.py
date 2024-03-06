# Import necessary modules
import numpy as np
import cv2

def main(input_image_bytes):
    # Convert input image bytes to numpy array
    nparr = np.frombuffer(input_image_bytes, np.uint8)
    # Decode numpy array to OpenCV image
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Convert image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Encode grayscale image to bytes
    success, grayscale_image_bytes = cv2.imencode('.jpg', grayscale_image)
    
    # Check if encoding was successful
    if not success:
        raise Exception("Error encoding grayscale image")
    
    # Convert grayscale image bytes to bytes-like object
    grayscale_image_bytes = grayscale_image_bytes.tobytes()
    
    # Return grayscale image bytes
    return grayscale_image_bytes
