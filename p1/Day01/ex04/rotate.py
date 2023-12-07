import numpy as np

def rotate(img, start_x, end_x, start_y, end_y):
	"""Rotate a part of an image"""
	zoomed_img_arr = img[start_y:end_y, start_x:end_x]
	gray_img = np.dot(zoomed_img_arr[..., :3], [0.2989, 0.5870, 0.1140])
	rotated = np.array([list(row)[::1] for row in zip(*gray_img)])
	return rotated
