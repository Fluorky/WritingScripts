import sys
import numpy as np

def display_size(obj, obj_name):
    size_bytes = sys.getsizeof(obj)
    size_gb = size_bytes / (1024 ** 3)
    print(f"{obj_name} size in bytes: {size_bytes} B, size in gigabytes: {size_gb:.9f} GB")

# Creating various large objects
large_list = [i for i in range(1, 1000000)]
large_dict = {str(i): i for i in range(1, 1000000)}
large_array = np.arange(1, 1000000)
generator = (x for x in range(1000000))

# Displaying sizes of objects
display_size(large_list, "Large List")
display_size(large_dict, "Large Dictionary")
display_size(large_array, "Large NumPy Array")
display_size(generator, "Generator")
