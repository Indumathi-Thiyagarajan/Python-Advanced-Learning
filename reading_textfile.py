#using generator to read and close file after reaeding
file_names = ['/Users/indu/EPAi/generator_Assignment/car-brands-1.txt', '/Users/indu/EPAi/generator_Assignment/car-brands-2.txt', '/Users/indu/EPAi/generator_Assignment/car-brands-3.txt']

def file_reader(files_list):
    for file_name in files_list:
        with open(file_name, 'r', encoding='ISO-8859-1') as file:
            yield file.read()
file_read = file_reader(file_names)

for content in file_read:
    print(content)
