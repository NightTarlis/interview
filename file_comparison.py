import os
import sys


def compare_files(first_file_path: str, second_file_path: str) -> None:
    """
    Takes two input files and compares their content.

    Args:
        first_file_path (str): Path to the first input file.
        second_file_path (str): Path to the second input file.

    Reads ASCII strings lexicographically sorted in the same order from both input files.
    Creates two output files:
    - The first output file contains only strings found in the first input file but not in the second one.
    - The second output file contains strings found in the second input file but not in the first one.
    """

    with open(first_file_path, 'r') as r_file1:
        with open(second_file_path, 'r') as r_file2:
            with open('./first_file_uniq_strings.txt', 'w') as w_file1:
                with open('./second_file_uniq_strings.txt', 'w') as w_file2:
                    line_first_file, line_second_file = r_file1.readline().strip(), r_file2.readline().strip()

                    while line_first_file and line_second_file:
                        if line_first_file < line_second_file:
                            w_file1.write(f'{line_first_file}\n')
                            line_first_file = r_file1.readline().strip()
                        elif line_first_file > line_second_file:
                            w_file2.write(f'{line_second_file}\n')
                            line_second_file = r_file2.readline().strip()
                        else:
                            line_first_file = r_file1.readline().strip()
                            line_second_file = r_file2.readline().strip()

                    while line_first_file:
                        w_file1.write(f'{line_first_file}\n')
                        line_first_file = r_file1.readline().strip()
                    while line_second_file:
                        w_file2.write(f'{line_second_file}\n')
                        line_second_file = r_file2.readline().strip()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <file1_path> <file2_path>")
    else:
        file1_path, file2_path = sys.argv[1], sys.argv[2]
        if not os.path.exists(file1_path):
            print(f'File {file1_path} not exists')
        elif not os.path.exists(file2_path):
            print(f'File {file2_path} not exists')
        else:
            compare_files(file1_path, file2_path)
            print(os.path.abspath('./first_file_uniq_strings.txt'))
            print(os.path.abspath('./second_file_uniq_strings.txt'))
