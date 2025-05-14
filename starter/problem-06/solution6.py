# Define the function
def isLandscape(width, height):
    if width > height:
        return "Landscape"
    else:
        return "Portrait"

# Example usage
print("When width=1920 and height=1080 then the image is: ",isLandscape(1920, 1080))  # Output: Landscape
print("When width=800 and height=1200 then the image is: ",isLandscape(800, 1200))   # Output: Portrait