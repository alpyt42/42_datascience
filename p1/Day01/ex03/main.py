from load_image import ft_load
from zoom import zoom
import matplotlib.pyplot as plt

def print_image_info(img_arr):
	print(f"The shape of the image is: {img_arr.shape}")
	print("Pixel content of the image:")
	print(img_arr)

def main():
	try:
		arr = ft_load("/home/alric/Code/42_datascience/p1/Day01/animal.jpeg")
		print_image_info(arr)
		arr_zoomed = zoom(arr, 455, 890, 71, 458)
		print("New shape of image is: ", arr_zoomed.shape)
		print(arr_zoomed)
		plt.imshow(arr_zoomed)
		plt.show()
	except Exception as e:
		print("Error: ", e)

if __name__ == "__main__":
	main()