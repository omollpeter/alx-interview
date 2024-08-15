#!/usr/bin/python3
"""
This script parses a log data and prints some statistics in a well
summarized format
"""


import re
import sys

input_format = r'^(\d{1,3}\.){3}\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\
\d{2}:\d{2}\.\d{6}\] "([^"]*)" \d{3} \d+$'


def check_if_valid_input(pattern, log_entry):
    """
    Checks if entry is has the valid input format
    """
    return re.match(pattern, log_entry)


def extact_code_and_filesize(log_entry):
    """
    Extracts and returns status code and file size from log entry in
    tuple format
    """
    fields = log_entry.split()
    return fields[-2], fields[-1]


if __name__ == "__main__":
    try:
        line_count = 0
        total_size = 0
        status_codes = []
        code_count = {
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
                status, size = extact_code_and_filesize(line)
                line_count += 1
                total_size += int(size)
                status_codes.append(status)

                if line_count > 0 and line_count % 10 == 0:
                    code_count["200"] = status_codes.count("200")
                    code_count["301"] = status_codes.count("301")
                    code_count["400"] = status_codes.count("400")
                    code_count["401"] = status_codes.count("401")
                    code_count["403"] = status_codes.count("403")
                    code_count["404"] = status_codes.count("404")
                    code_count["405"] = status_codes.count("405")
                    code_count["500"] = status_codes.count("500")

                    print(f"File size: {total_size}")
                    for key, value in code_count.items():
                        if value:
                            print(f"{key}: {value}")
            else:
                continue

    except KeyboardInterrupt:
        code_count["200"] = status_codes.count("200")
        code_count["301"] = status_codes.count("301")
        code_count["400"] = status_codes.count("400")
        code_count["401"] = status_codes.count("401")
        code_count["403"] = status_codes.count("403")
        code_count["404"] = status_codes.count("404")
        code_count["405"] = status_codes.count("405")
        code_count["500"] = status_codes.count("500")
        print(f"File size: {total_size}")
        for key, value in code_count.items():
            if value:
                print(f"{key}: {value}")
