from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot as plt

def print_image_info(img_arr):
	print(f"The shape of the image is: {img_arr.shape}")
	print("Pixel content of the image:")
	print(img_arr)

def main():
	try:
		arr = ft_load("p1/Day01/landscape.jpg")

		# Print original image info
		print("Original Image:")
		print_image_info(arr)

		# Invert the colors
		inverted_arr = ft_invert(arr)

		# Set only the red color to the maximum
		red_arr = ft_red(arr)

		# Set only the green color to the maximum
		green_arr = ft_green(arr)
  
		# Set only the blue color to the maximum
		blue_arr = ft_blue(arr)

		# Create subplots
		plt.figure(figsize=(12, 9))

		# Original image
		plt.subplot(2, 3, 1)
		plt.imshow(arr)
		plt.title("Original Image")

		# Inverted image
		plt.subplot(2, 3, 2)
		plt.imshow(inverted_arr)
		plt.title("Inverted Image")

		# Red channel set to maximum
		plt.subplot(2, 3, 3)
		plt.imshow(red_arr)
		plt.title("Red version")

		# Green channel set to maximum on a new line
		plt.subplot(2, 3, 4)
		plt.imshow(green_arr)
		plt.title("Green version")
  
		# Blue channel set to maximum on a new line
		plt.subplot(2, 3, 5)
		plt.imshow(blue_arr)
		plt.title("Blue version")
  
		# Grey version
		plt.subplot(2, 3, 6)
		plt.imshow(ft_grey(arr))
		plt.title("Grey version")

		# Show the subplots
		plt.show()


	except Exception as e:
		print("Error: ", e)

if __name__ == "__main__":
	main()
