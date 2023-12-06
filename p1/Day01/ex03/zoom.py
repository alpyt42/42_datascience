def zoom(img: list[int | float], start_x: int, end_x: int, start_y: int, end_y: int):
	"""Zoom in on an image"""
	zoomed_img_arr = img[start_y:end_y, start_x:end_x]
	return zoomed_img_arr