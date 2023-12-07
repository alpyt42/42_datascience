import numpy as np
import matplotlib.pyplot as plt
import array

def ft_invert(array) -> array:
	"""Inverts the colors of an image"""
	inverted_array = 255 - array
	return inverted_array

def ft_red(array):
	"""
	Sets the red color of an image to maximum and the other colors to 0.
	
	Parameters:
	- array: NumPy array representing the image (assuming RGB format).
	
	Returns:
	- red_array: NumPy array with red channel set to maximum and other channels set to 0.
	"""
	# Make a copy of the input array to avoid modifying the original image
	red_array = np.copy(array)
	
	# Set green and blue channels to 0
	red_array[:,:,1] = 0  # Green channel
	red_array[:,:,2] = 0  # Blue channel
	
	return red_array

def ft_green(array) -> array:
	"""Sets the green color of an image to maximum and the other colors to 0"""
	green_array = np.copy(array)
	green_array[:,:,0] = 0
	green_array[:,:,2] = 0
	return green_array

def ft_blue(array) -> array:
	"""Sets the blue color of an image to maximum and the other colors to 0"""
	blue_array = np.copy(array)
	blue_array[:,:,0] = 0
	blue_array[:,:,1] = 0
	return blue_array

def ft_grey(array) -> array:
	"""Sets the grey color of an image to maximum and the other colors to 0"""
	grey_array = np.copy(array)
	grey_array[:,:,0] = grey_array[:,:,0] * 0.2989
	grey_array[:,:,1] = grey_array[:,:,1] * 0.5870
	grey_array[:,:,2] = grey_array[:,:,2] * 0.1140
	return grey_array