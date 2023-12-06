def NULL_not_found(object: any) -> int:
	if object is None:
		print("Nothing: None", type(object))
	elif isinstance(object, float) and object != object:
		print("Garlic: nan", type(object))
	elif object == 0:
		print("Zero:", object, type(object))
	elif isinstance(object, str) and not object.strip():
		print("Empty:", type(object))
	elif isinstance(object, bool) and not object:
		print("Fake:", object, type(object))
	else:
		print("Type not Found")
		return 1
	return 0