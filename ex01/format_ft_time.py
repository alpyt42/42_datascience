import time

current_time = time.time()
formatted_time = "{:,.4f}".format(current_time)
scientific_notation = "{:.2e}".format(current_time)
current_date = time.strftime("%b %d %Y")

print("Seconds since January 1, 1970:", formatted_time, "or", scientific_notation, "in scientific notation")
print(current_date)
