import numpy as np

def rotate(img, start_x, end_x, start_y, end_y):
	"""Rotate a part of an image"""
	zoomed_img_arr = img[start_y:end_y, start_x:end_x]
	rotated = np.array([list(row)[::1] for row in zip(*zoomed_img_arr)])
	return rotated
