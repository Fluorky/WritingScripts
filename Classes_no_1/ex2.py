def read_file(path):
      
    file_path = path
    with open(file_path, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
    return file_path, num_lines, lines
    

def create_dictionary(input):

    linux_distribution_dict = {}  

    for line in input:
        # Assuming lines in the file have the format: "name version release_date"
        parts = line.split('\t')  # Assuming tabs separate the values
        name_and_version = f"{parts[0]} {parts[1]}"
        release_date = parts[2].strip()
        linux_distribution_dict[name_and_version] = release_date

    return linux_distribution_dict

def main():

    # a) Read the distros.txt file and count the number of lines

    file_path, num_lines, lines = read_file('distros.txt')
    print(f"a) Number of lines in the file {file_path}: {num_lines}")

    # b) Create the linux_distribution_dict dictionary
    linux_distribution_dict = create_dictionary(lines)
    print("b) Dictionary linux_distribution_dict:")
    print(linux_distribution_dict)

if __name__ == '__main__':
    main()