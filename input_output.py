data_array = []

with open ("data.txt", "r") as data_file:
	for i in data_file.readlines():
		data_array.append(str(i))

with open ("data_export.txt", "w") as data_export_file:
	for i in data_array:
		if int(i) > 50:
			data_export_file.writelines(str(i))


