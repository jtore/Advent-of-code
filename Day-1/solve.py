def get_file_data(input):
    with open(input) as file: 
        data = file.read()
    return data

file = get_file_data("input.txt")

print(file)