import numpy as np
import cv2
import os

SUPPORTED_IMAGE_FORMAT = (".jpg", ".jpeg", ".png")

def display_blue_channel(img):
    print(f"Blue channel:")
    print(img[:,:,0])

def display_green_channel(img):
    print(f"Green channel:")
    print(img[:,:,1])

def display_red_channel(img):
    print(f"Red channel:")
    print(img[:,:,2])

def display_image(img):
    delay = 0
    cv2.imshow("Image", img)
    cv2.waitKey(delay)
    cv2.destroyAllWindows()

def main():
    image_path = input("Please enter full path to an image file in .jpg, .jpeg, and .png format or `quit` to exit the program: ")
    
    if image_path.lower() == "quit":
        print("Exiting the program...")
        return

    try:
        if not os.path.exists(image_path):
            print(f"Error: File does not exist - {image_path}")
            return

        if not image_path.lower().endswith(SUPPORTED_IMAGE_FORMAT):
            print(f"Error: Unsupported file format (supported formats are .jpg, .jpeg, and .png) - {image_path}")
            return
        
        img = cv2.imread(image_path)

        if img is None: 
            print(f"Error: Failed to read and load image file - {image_path}")
            return 
        
        print(f"Image type: {type(img)} and shape: {img.shape}")
        display_image(img)
        display_blue_channel(img)
        display_green_channel(img)
        display_red_channel(img)
            
    except Exception as e:
        print(f"Error occured: {str(e)}")
        
if __name__ == "__main__":
    main()
