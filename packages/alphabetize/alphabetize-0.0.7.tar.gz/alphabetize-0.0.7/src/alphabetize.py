import argparse
import re


def sort_variables(name=None):
    with open(name, 'r+') as file:
        file_lines = file.read().split('\n')
        updated_file = ''
        variable_lines = []
        variable_names = []
        # Loop over each line in the file
        for line in file_lines:
            # Locate variable in a line by '='
            if re.match('.* = .*', string=line):
                # Does the line use any other variables already listed before
                # The previous variable names array are looped over to check if referenced in the current line
                for name in variable_names:
                    # A match indicates it uses a previously defined variable, and thus shouldn't be part of ordering
                    # The variables found so far are ordered and added to the file, followed by the current matched line
                    # The variable name and line are reset to the current line as a variable is still present
                    if re.search(f"\\b({name})\\b", string=line):
                        variable_lines.sort()
                        for ordered_line in variable_lines:
                            updated_file += ordered_line + '\n'
                        variable_names = [re.findall('\\w*(?= = )', string=line)[0]]
                        variable_lines = [line]
                        break
                # No match means the variable is independent and can be added to the sort list
                else:
                    variable_names.append(re.findall('\\w*(?= = )', string=line)[0])
                    variable_lines.append(line)
            # No variable is found, so the variables array found before is sorted and added, before the current line
            # The variable name and line are reset to be empty as there are no variables present
            else:
                variable_lines.sort()
                for ordered_line in variable_lines:
                    updated_file += ordered_line + '\n'
                updated_file += line + '\n'
                variable_names = []
                variable_lines = []
        # Wipe file contents and write ordered contents
        file.seek(0)
        file.truncate()
        file.write(updated_file)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filename",
        nargs="*",
        metavar="FILENAME",
        default="",
        help="Filename to be sorted. Only works for .py files"
    )
    args = parser.parse_args()
    return args.filename[0]


def main():
    filename = parse_args()
    sort_variables(filename)
