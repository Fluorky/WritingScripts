import os

def main():

    folder_path = r'/Users/maciej/music'

    # Uzyskaj listę plików w folderze
    file_names = os.listdir(folder_path)

    # Utwórz słownik z nazwami plików i ich rozmiarami
    file_size_dict = {file: os.path.getsize(os.path.join(folder_path, file)) for file in file_names}

    # Posortuj słownik według rozmiarów plików (od największego do najmniejszego)
    sorted_file_size_dict = dict(sorted(file_size_dict.items(), key=lambda item: item[1], reverse=True))

    # Wyświetl posortowany słownik
    print("Sorted file sizes (from largest to smallest):")
    for file, size in sorted_file_size_dict.items():
        print(f"{file}: {size} bytes")


if __name__ == '__main__':
    main()
