def main():
    linux_distribution_dict = {}

    # a) Read the distros.txt file and count the number of lines
    file_path = 'distros.txt'
    with open(file_path, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)

    print(f"a) Number of lines in the file {file_path}: {num_lines}")

    # b) Create the linux_distribution_dict dictionary
    for line in lines:
        # Assuming lines in the file have the format: "name version release_date"
        parts = line.split('\t')  # Assuming tabs separate the values
        name_and_version = f"{parts[0]} {parts[1]}"
        release_date = parts[2].strip()
        linux_distribution_dict[name_and_version] = release_date

    print("b) Dictionary linux_distribution_dict:")
    print(linux_distribution_dict)

if __name__ == '__main__':
    main()