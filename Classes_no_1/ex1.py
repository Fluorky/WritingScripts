import time
import numpy as np

# Function for summing numbers from 0 to n using a loop
def sum_using_loop(n):
    result = 0
    for i in range(n + 1):
        result += i
    return result

# Function for summing numbers from 0 to n using NumPy
def sum_using_numpy(n):
    numbers = np.arange(n + 1)
    result = np.sum(numbers)
    return result

# Timing for summing using a loop
def check_time_sum_using_loop(n):
    start_time = time.time()
    result_using_loop = sum_using_loop(n)
    end_time = time.time()
    elapsed_time_loop = end_time - start_time
    return result_using_loop,elapsed_time_loop


# Timing for summing using NumPy
def check_time_sum_using_numpy(n):
    start_time = time.time()
    result_using_numpy = sum_using_numpy(n)
    end_time = time.time()
    elapsed_time_numpy = end_time - start_time
    return result_using_numpy,elapsed_time_numpy

def main():
    result_using_loop,elapsed_time_loop= check_time_sum_using_loop(1000000)
    print(f"Summing using a loop: {result_using_loop}, Execution time: {elapsed_time_loop} seconds")
    result_using_numpy,elapsed_time_numpy= check_time_sum_using_numpy(1000000)
    print(f"Summing using NumPy: {result_using_numpy}, Execution time: {elapsed_time_numpy} seconds")


if __name__ == '__main__':
    main()