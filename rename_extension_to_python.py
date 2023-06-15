import os

path = "./submissions"

def rename_file_extension(path):
	directorys = os.listdir(path)
	for directory in directorys:
		directory_path = path + '/' + directory
		files = os.listdir(directory_path)
		for file in files:
			if os.path.isdir(directory_path + '/' + file):
				continue
			name, extension = os.path.splitext(file)
			if extension != '.py':
				new_file = name + ".py"
				os.rename(directory_path + '/' + name + extension, directory_path + '/' + new_file)

path = "./submissions"
rename_file_extension(path)