import PIL
from PIL import Image, ImageChops, ImageFilter 
from matplotlib import pyplot as plt

# Function to blur images.
def blur(image):
    blurredImage = image.filter(ImageFilter.GaussianBlur(radius=1))
    print("Blur applied successfully.\n")
    return blurredImage

# Function to rotate images by an inputted angle.
def rotate(image):
    angle = int(input("Enter the angle you would like to rotate the image by:\n"))
    rotatedImage = image.rotate(angle)
    print(f"Image rotated by {angle} degrees successfully.\n")
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
def multiply(image):
    num = int(input("How many more images would you like to multiply to the base image?\n"))
    for i in range(num):
        if i == 0:                                                                                                 
            name = input(f"Enter the {i+1} image name.\n")
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
    print("            Enter the base image you would like to change/manipulate.\n")
    print("        (Make sure the image is in the same directory as this python file!)\n")  
    
    baseString = str(input())
    

    
    baseImage = Image.open(baseString)
    image = None
    flag = True
    outputName = "alteredImage"                                                                                     # Default name if user does not want to create a name for the image.
    
    while(flag == True):   
        print("""        
    Multiply images first before applying other effects for better results!
             
                         1.) Invert Image
                         2.) Convert to Greyscale
                         3.) Multiply images together
                         4.) Rotate image
                         5.) Blur image
                         6.) Apply all of the above
                         7.) Exit / Save image
        """)        
        ask = int(input())
        if (ask == 1):
            baseImage = invert(baseImage)
             
        elif (ask == 2):
            baseImage = greyscale(baseImage)

        elif (ask == 3):
            baseImage = multiply(baseImage)
            
        elif (ask == 4):
            rotatedImage = rotate(baseImage)
            baseImage = rotatedImage
            
        elif (ask == 5):
            baseImage = blur(baseImage)
            
        elif (ask == 6):
            baseImage = multiply(baseImage)
            baseImage = blur(baseImage)
            baseImage = greyscale(baseImage)
            baseImage = invert(baseImage)
            baseImage = rotate(baseImage)
            
        elif (ask == 7):
            flag = False
            ask = input("Would you like to view the image? y/n \n")                                                             # Branch to view image.
            if ask == "y":
                plt.axis("off")
                plt.imshow(baseImage)
        
            ask = input("Would you like to save the image? y/n \n")                                                             # Branch to save image.
            if ask == "y":
                nameInput = input("What would you like to name the image? y/n \n")   
                if (nameInput == "y"):
                    name = input("Enter what you would like to name the image: \n")
                    imageName = name+".png"
                    baseImage.save(imageName)
                    print("\n")
                    print("File saved as:" + imageName)
                
            print("Exiting...")
    
    
main()
