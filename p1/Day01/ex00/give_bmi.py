def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	if (len(height) != len(weight)):
		raise ValueError("height and weight must have the same length")
	for i in range(len(height)):
		assert height[i] > 0 and weight[i] > 0 and isinstance(height[i], (int, float)), "height and weight must be positive numbers"
		assert isinstance(weight[i], (int, float)), "height and weight must be positive numbers"
	bmi = []
	for i in range(len(height)):
		bmi.append(weight[i] / height[i] ** 2)
	return bmi

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	assert isinstance(limit, int), "limit must be an integer"
	assert isinstance(bmi, list), "bmi must be a list"
	assert limit > 0, "limit must be a positive number"
	bmi_bool = []
	for i in range(len(bmi)):
		assert isinstance(bmi[i], (int, float)), "bmi must be a list of positive numbers"
		assert bmi[i] > 0, "bmi must be a positive number"
		if (bmi[i] > limit):
			bmi_bool.append(True)
		else:
			bmi_bool.append(False)
	return bmi_bool