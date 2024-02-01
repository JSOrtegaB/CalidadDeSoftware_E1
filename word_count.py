"""
This program reads a file containing words and counts 
the frequency of each distinct word in the file.
"""
import sys
import time
import os

def count_words(filepath):
    """Count the frequency of each distinct word in the file."""
    word_count_dict = {}  # Renamed to avoid shadowing
    try:
        with open(filepath, 'r', encoding='utf8') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    if word.isalpha():
                        lower_word = word.lower()  # Explicitly rename for clarity
                        if lower_word in word_count_dict:
                            word_count_dict[lower_word] += 1
                        else:
                            word_count_dict[lower_word] = 1
                    else:
                        print(f"Invalid word found and ignored: {word}")
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        sys.exit(1)
    return word_count_dict

def write_results(word_counts, result_file_name, time_elapsed):
    """Write the word counts to the console and a file."""
    output_file_path = "WordCountResults.txt"
    header = f"\nWord count results for {result_file_name}\n"
    footer = f"Total Unique Count: {len(word_counts)} \
            Execution and calculation took {time_elapsed:} seconds.\n"
    with open(output_file_path, 'a', encoding='utf8') as file:
        file.write(header)
        for word, count in sorted(word_counts.items()):
            result_line = f"{word}: {count}\n"
            print(result_line, end='')
            file.write(result_line)
        file.write(footer)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py <fileWithData.txt>")
        sys.exit(1)

    input_filepath = sys.argv[1]
    basename = os.path.basename(input_filepath)
    filename_without_extension = basename.split('.')[0]  # Renamed for clarity
    start_time = time.perf_counter()
    counts = count_words(input_filepath)  # Use of generic variable name to avoid shadowing
    end_time = time.perf_counter()
    elapsed = end_time - start_time  # Renamed to avoid shadowing
    write_results(counts, filename_without_extension, elapsed)
    print(f"Total Unique Count: {len(counts)}  Execution and calculation took {elapsed:} seconds.")
