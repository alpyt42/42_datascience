def slice_me(family: list, start: int, end: int) -> list:
	assert isinstance(family, list), "family is not a list: %r" % family
	assert isinstance(start, int), "start is not an int: %r" % start
	assert isinstance(end, int), "end is not an int: %r" % end
	for i in range(len(family) - 1):
		assert len(family[i]) == len(family[i + 1]), "family is not a matrix: %r" % family
	print("My shape is : (" + str(len(family)) + ", " + str(len(family[0])) + ")")
	print("My new shape is : (" + str(len(family[start:end])) + ", " + str(len(family[start:end][0])) + ")")
	return family[start:end]