"""
This script reads a file containing numbers and converts 
each number to its binary and hexadecimal representation.
"""
import os
import sys
import time


def get_filename_without_extension(path):
    """
    Extracts the filename without its extension from a given file path.

    Parameters:
    path (str): The full file path.

    Returns:
    str: The filename without its extension.
    """
    base = os.path.basename(path)
    filename = os.path.splitext(base)[0]
    return filename


def read_numbers_from_file(filename):
    """
    Reads lines from a file and converts them to floating-point numbers, 
    ignoring invalid data.

    Parameters:
    filename (str): The name of the file to read from.

    Returns:
    list[float]: A list of numbers read from the file.
    """
    numbers = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                number = float(line.strip())
                numbers.append(number)
            except ValueError:
                print(
                    f"Invalid data '{line.strip()}' found and will be ignored.")
    return numbers


def calculate_mean(numbers):
    """
    Calculates the mean (average) of a list of numbers.

    Parameters:
    numbers (list[float]): A list of numbers.

    Returns:
    float: The mean of the list of numbers.
    """
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    """
    Calculates the median of a list of numbers.

    Parameters:
    numbers (list[float]): A list of numbers.

    Returns:
    float: The median of the list of numbers.
    """
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    return (numbers[mid] if n % 2 != 0 else (numbers[mid - 1] + numbers[mid]) / 2)


def calculate_mode(numbers):
    """
    Calculates the mode(s) of a list of numbers. If there are multiple modes,
    it returns all of them.

    Parameters:
    numbers (list): A list of numbers.

    Returns:
    The mode of the list of numbers.
    """
    frequency = {}
    for number in numbers:

        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

    max_key = max(frequency, key=frequency.get)
    return max_key

# Example of usage


def calculate_variance(numbers, mean):
    """
    Calculates the variance of a list of numbers.

    Parameters:
    numbers (list[float]): A list of numbers.
    mean (float): The mean of the list of numbers.

    Returns:
    float: The variance of the list of numbers.
    """
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)


def calculate_std_dev(variance):
    """
    Calculates the standard deviation from the variance.

    Parameters:
    variance (float): The variance of a list of numbers.

    Returns:
    float: The standard deviation.
    """
    return variance ** 0.5


def write_results_to_file(filename, results):
    """
    Writes a list of strings to a file.

    Parameters:
    filename (str): The name of the file to write to.
    results (list[str]): A list of strings to write to the file.

    Returns:
    None.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        for line in results:
            file.write(line + '\n')


def main():
    """
    The main function of the script, orchestrating the reading of data, 
    calculation of statistics, and writing results to a file.

    Parameters: None.
    Returns: None.
    """
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
        f"{filename}  COUNT: {len(numbers)}",
        f"{filename}  MEAN: {mean}",
        f"{filename}  MEDIAN: {median}",
        f"{filename}  MODE: {mode}",
        f"{filename}  SD: {std_dev}",
        f"{filename}  VAR: {variance}",
        f"{filename}  Time Elapsed: {elapsed_time} seconds"

    ]

    for line in results:
        print(line)

    write_results_to_file('StatisticsResults.txt', results)


if __name__ == "__main__":
    main()
