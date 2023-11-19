# This file contains code for finding occurrences of techniques in a hobby training log
#
# Author: Josh McIntyre
# 

import re
import csv

import config

# Build a regular expression from technique name variations
def build_regex(technique_variations):

    regex_str = "|".join(technique_variations) if len(technique_variations) > 1 else technique_variations[0]
    regex = re.compile(regex_str, re.IGNORECASE)
    
    return regex

# Find all instances of the specified regex
def count_instances(data, regex):
    
    count = 0
    for row in data:
        if regex.search(row[config.HEADER]):
            count += 1

    return count

# Parse the CSV log
def parse_log(log):

    data = []
    with open(log) as f:
        dr = csv.DictReader(f)
        for row in dr:
            data.append(row)

    return data

# The main entry point for the program
def main():

    data = parse_log(config.LOGFILE)
    for variation_list in config.TECHNIQUE_VARIATIONS:
        regex = build_regex(variation_list)
        name = variation_list[0]
        count = count_instances(data, regex)
        print(f"Instances of technique {name}: {count}")

if __name__ == "__main__":
    main()