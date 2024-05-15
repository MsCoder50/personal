from PIL import Image

def resize_image(image_path, width, new_height):
    # Open the image file
    image = Image.open(image_path)
    
    # Calculate the aspect ratio of the original image
    original_width, original_height = image.size
    aspect_ratio = original_width / original_height
    
    # Calculate the new height based on the desired width and aspect ratio
    new_height = int(width / aspect_ratio)
    
    # Resize the image
    resized_image = image.resize((width, new_height))
    
    # Save the resized image
    resized_image.save("resized_image.png")  # Change the file format if needed

# Example usage:
if __name__ == "__main__":
    image_path = input("Enter Image Name")  # Replace with the path to your image
    width = float(input("Enter Width: "))
    new_height = float(input("Enter Height: "))
    resize_image(image_path, width, new_height)
