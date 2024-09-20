# Directory_Lister

## Overview

This Python script helps to enumerate files with a specific extension in a given directory and its subdirectories recursively. It utilizes the `os` and `argparse` modules to provide flexibility in specifying the input directory and desired file extension paths.


## Usage

The syntax for running the script is:

```
python RecursiveDirectoryLister.py directory_path [-ext extension]
```

Replace `extension`  with the required extension type(for .txt put txt, for .ipynb put ipynb). Specifying the `extension` is optional.


## Output

The output file will be created with either of these names:
  - directory_list.txt : If only directory has been given as an input. 
  - files_with_[extension_name]_extension.txt : If a specific extension has been given as an input along with `-ext` flag.
