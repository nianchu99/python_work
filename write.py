filename = "/Volumes/bowenkei/test/log_file"
with open(filename, "a") as file_object:
	for i in range(20):
		file_object.write("line" + str(i) + "\n" )