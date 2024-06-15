import PIL
from PIL import Image, ImageChops, ImageFilter 
from matplotlib import pyplot as plt

# Function to blur images.
def blur(image):
    blurredImage = image.filter(ImageFilter.GaussianBlur(radius=1))
    return blurredImage

# Function to rotate images by an inputted angle.
def rotate(image):
    angle = input("Enter the angle you would like to rotate the image by:\n")
    rotatedImage = image.rotate(angle)
    return rotatedImage

# Function to invert the colour of images.
def invert(image):
    invertedImage = ImageChops.invert(image)
    print("Invert operation successful\n")
    return invertedImage
    
# Function to convert given image to greyscale (black & white)
def greyscale(image):                                                   
    greyscale = image.convert('1')
    print("Greyscale operation successful\n")
    return greyscale
    
# Function to multiply images over each other.
def multiply():
    num = int(input("How many images would you like to multiply?\n"))
    for i in range(num):
        if i == 0:                                                                                                  # Condition to warn user about better image fitting.
            name = input(f"Enter the {i+1} image name. Input the largest image first for better results!\n")
            image2 = Image.open(name)            
            image = image2;
            merged = ImageChops.multiply(image,image2)
            image = merged            
        else:
            name = input(f"Enter the {i+1} image name:\n")
            image2 = Image.open(name)         
            image2 = image2.resize(image.size)                                                                      # Make all subsequent images the same size as the first one for better results.
            merged = ImageChops.multiply(image,image2)
            image = merged
    
    print("\nMultiply operation successful\n")
    return image



def main():
    
    print("\n                      Welcome to Image manipulator!\n")
    print("                      Please select an option below.\n")
    
    print("""        Make sure the image is in the same directory as this python file!\n                 
                     1.) Invert Image
                     2.) Convert to Greyscale
                     3.) Multiply images together
                     4.) Rotate image
                     5.) Blur image
                     6.) Apply all of the above
    """)
    
    image = Image.open("sky.png") 
    image = image.filter(ImageFilter.GaussianBlur(radius=1))
    #image = None
    #ask = input()
    
    #if (ask == 1):
    #    invertImage = invert(greyImage)
    
    
    ask = input("Would you like to view the image? y/n \n")                                                             # Branch to view image.
    if ask == "y":
        plt.axis("off")
        plt.imshow(image)

    ask = input("Would you like to save the image? y/n \n")                                                             # Branch to save image.S
    if ask == "y":
        image.save("Image.png")
        print("\n")
    print("Exiting...")

main()