import os
from spleeter.separator import Separator

def split_mp3(input_path, output_dir):
    if not os.path.isfile(input_path):
        print(f"Error: The input file {input_path} does not exist.")
        return

    if not os.path.isdir(output_dir):
        print(f"Error: The output directory {output_dir} does not exist.")
        return

    try:
        separator = Separator('spleeter:2stems')
        separator.separate_to_file(input_path, output_dir)
        
        print("Files have been successfully split into vocals and accompaniment.")
    except Exception as e:
        print(f"An error occurred: {e}")

input_mp3 = r'C:\Users\gtafu\Downloads\lunay1.mp3'
output_directory = r'C:\Users\gtafu\Downloads'

print(f"Input MP3 path: {input_mp3}")
print(f"Output directory: {output_directory}")

split_mp3(input_mp3, output_directory)
