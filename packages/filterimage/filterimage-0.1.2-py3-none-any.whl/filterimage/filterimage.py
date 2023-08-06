"""This is the Relevantpackage.py script"""

# Import libraries
import os

class Filterimage():
    def __init__(self, image_matrix):
        self.image_matrix = image_matrix

    #Adds red stripes that run horizontally on the image
    #For red stripes, r value = 255
    def red_stripes(self):
        for row in range(len(self.image_matrix)):
            if (row // 50) % 2 == 0:
                for col in range(len(self.image_matrix[row])):
                    self.image_matrix[row][col][0] = 1.0
                    #1.0 = 255

        return self.image_matrix

    #Gradually darkens the given image
    def fade_to_black(self):
        #Dimensions of the image
        height, width, channels = self.image_matrix.shape
        for row in range(height):
            for col in range(width):
                for ch in range(channels):
                    self.image_matrix[row][col][ch] *= (col / width)

        return self.image_matrix

    #Distorts particles in the image to make a "hyper" effect
    def hyper_wave(self):
        #Dimensions of the image
        height, width, channels = self.image_matrix.shape
        for row in range(height):
            for col in range(width):
                for ch in range(channels):
                    self.image_matrix[row][col][ch] **= (col / width)

        return self.image_matrix

    #Darkens all pixels except for red values
    def red_distortion(self):
        height, width, channels = self.image_matrix.shape
        for row in range(height):
            for col in range(width):
                for ch in range(channels):
                    self.image_matrix[row][col][ch] **= (col * width)

        return self.image_matrix

    #Function returns a copy of the image with inverted colors
    def color_inversion(self):
        #Dimensions of the image
        height, width, channels = self.image_matrix.shape
        #Since image is a read-only -> create copy
        copy_image = self.image_matrix.copy()
        #Iterates over each pixel within the image
        for row in range(height):
            for col in range(width):
                for chl in range(channels):
                    #Every pixel/channel -> Subtract 1 to "flip" the values
                    copy_image[row][col][chl] = 1 - copy_image[row][col][chl]
        #Returns the inverted version
        return copy_image



# Read the image file
#img = mpimg.imread("valstrax.png")

# Create a Filters instance
#filters = Filters(img)

# Apply a filter
#filtered_img = filters.color_inversion()

# Display the filtered image using Matplotlib
#plt.imshow(filtered_img)
#plt.show()


