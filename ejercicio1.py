"""
This is a simple Python script that prints 'hola' to the console.
"""
import os
import sys
import time

def get_filename_without_extension(path):
    base = os.path.basename(path)  # Removes the directory path
    filename = os.path.splitext(base)[0]  # Splits the filename and extension and takes the first part
    return filename

def read_numbers_from_file(filename):
    numbers = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                number = float(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Invalid data '{line.strip()}' found and will be ignored.")
    return numbers

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    return (numbers[mid] if n % 2 != 0 else (numbers[mid - 1] + numbers[mid]) / 2)

def calculate_mode(numbers):
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    max_freq = max(frequency.values())
    modes = [number for number, freq in frequency.items() if freq == max_freq]
    return modes

def calculate_variance(numbers, mean):
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_std_dev(variance):
    return variance ** 0.5

def write_results_to_file(filename, results):
    with open(filename, 'a', encoding='utf-8') as file:
        for line in results:
            file.write(line + '\n')

def main():
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        return

    start_time = time.time()
    numbers = read_numbers_from_file(sys.argv[1])
    if not numbers:
        print("No valid data to process.")
        return

    mean = calculate_mean(numbers)
    median = calculate_median(numbers)
    mode = calculate_mode(numbers)
    variance = calculate_variance(numbers, mean)
    std_dev = calculate_std_dev(variance)
    elapsed_time = time.time() - start_time

    filename = get_filename_without_extension(sys.argv[1])
    results = [
        f"{get_filename_without_extension(sys.argv[1])}  Mean: {mean}",
        f"{filename}  Median: {median}",
        f"{filename}  Mode: {mode}",
        f"{filename}  Standard Deviation: {std_dev}",
        f"{filename}  Variance: {variance}",
        f"{filename}  Time Elapsed: {elapsed_time} seconds"
    ]

    for line in results:
        print(line)

    write_results_to_file('StatisticsResults.txt', results)

if __name__ == "__main__":
    main()
