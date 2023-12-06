from PIL import Image
from array import array
import numpy as np

def ft_load(path: str) -> array:
	"""Load an image from a file as a 3D numpy array"""
	img = Image.open(path)
	img_arr = np.array(img)
	return img_arr
