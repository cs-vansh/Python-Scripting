import os
import argparse

def list_files_with_extension(directory, extension, output_file):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if extension is None or file.endswith(extension):
                file_path = os.path.join(root, file)
                output_file.write(file_path + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Enumerate files with a specific extension in a directory and its subdirectories.')
    parser.add_argument('directory', help='The input directory path')
    parser.add_argument('-ext', '--extension', help='The file extension to search for (e.g., txt, jpg, etc.)')
    args = parser.parse_args()

    user_input_directory = args.directory
    user_input_extension = args.extension

    if os.path.exists(user_input_directory):
        output_file_path = f"files_with_{user_input_extension}_extension.txt" if user_input_extension else "directory_list.txt"
        with open(output_file_path, 'w') as output_file:
            output_file.write(f"Files{' with ' + user_input_extension + ' extension' if user_input_extension else ''} in {user_input_directory} and its subdirectories:\n")
            list_files_with_extension(user_input_directory, user_input_extension, output_file)

        print(f"File paths saved to {output_file_path}")
    else:
        print("Invalid directory path. Please provide a valid directory.")
