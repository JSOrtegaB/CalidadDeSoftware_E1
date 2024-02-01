"""
This script reads a file containing numbers 
and converts each number to its 
binary and hexadecimal 
representation."""

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


def to_binary(number, bits=32):
    """Converts an integer to its binary representation using 
    basic algorithms, including negative numbers."""
    if number >= 0:
        return bin(number)[2:].zfill(bits)
    else:
        return bin(number & (2**bits - 1))[2:]


def to_hexadecimal(number, bits=32):
    """Converts an integer to its hexadecimal representation 
    using basic algorithms, including negative numbers."""
    if number >= 0:
        return hex(number)[2:].upper()
    else:
        return hex(number & (2**bits - 1))[2:].upper()


def process_file(filename):
    """Processes each line in the file, converting numbers to 
    binary and hexadecimal."""
    start_time = time.perf_counter()
    results = []
    header = f"\n{get_filename_without_extension(filename)} \
        {'NUMBER':<10} {'BIN':<40} {'HEX':<10}"
    results.append(header)
    index = 1

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                number = int(line.strip())
                binary = to_binary(number)
                hexadecimal = to_hexadecimal(number)
                results.append(
                    f"{index:<13}{number:<10}{binary:<41}{hexadecimal:<10}")
                index += 1
            except ValueError:
                print(f"Invalid data encountered and skipped: {line.strip()}")

    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return results, execution_time


def main():
    """ Main script that processes a file containing numbers"""
    if len(sys.argv) < 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    filename = sys.argv[1]
    results, execution_time = process_file(filename)

    with open('ConversionResults.txt', 'a', encoding='utf-8') as result_file:
        for result in results:
            print(result)
            result_file.write(result + '\n')
        result_file.write(f"Execution Time: {execution_time:} seconds\n")

    print(f"Execution Time: {execution_time:} seconds")


if __name__ == "__main__":
    main()
