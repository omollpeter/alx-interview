#!/usr/bin/python3
"""
This script parses log data and prints statistics in a well-summarized
format.
"""

import re
import sys

# Corrected regex pattern for input format
input_format = r'^(\d{1,3}\.){3}\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] "([^"]*)" \d{3} \d+$'


def check_if_valid_input(pattern, log_entry):
    """
    Checks if the entry has a valid input format.
    """
    # Stripping the newline character and any leading/trailing whitespaces
    log_entry = log_entry.strip()
    return re.match(pattern, log_entry)


def extract_code_and_filesize(log_entry):
    """
    Extracts and returns status code and file size from log entry
    in tuple format.
    """
    fields = log_entry.split()
    return fields[-2], fields[-1]


if __name__ == "__main__":
    try:
        total_size = 0
        status_codes = {
            "200": 0,
            "301": 0,
            "400": 0,
            "401": 0,
            "403": 0,
            "404": 0,
            "405": 0,
            "500": 0
        }

        for line in sys.stdin:
            if check_if_valid_input(input_format, line):
                status, size = extract_code_and_filesize(line)
                total_size += int(size)
                
                if status in status_codes:
                    status_codes[status] += 1

                # Print the output every 10 lines
                if sum(status_codes.values()) % 10 == 0:
                    print(f"File size: {total_size}")
                    for key, value in status_codes.items():
                        if value:
                            print(f"{key}: {value}")

    except KeyboardInterrupt:
        pass

    # Print final output upon keyboard interruption
    finally:
        print(f"File size: {total_size}")
        for key, value in status_codes.items():
            if value:
                print(f"{key}: {value}")
