# fetcharoo

fetcharoo is a Python library for downloading PDF files from a webpage. It provides support for specifying recursion depth and offers the option to merge downloaded PDFs into a single file.

## Features

- Download PDF files from a specified webpage.
- Specify recursion depth to control how many levels of links to follow when searching for PDFs.
- Choose to merge downloaded PDFs into a single file or store them as separate files.
- Simple and easy-to-use Python interface.

## Requirements

- Python 3.10 or higher
- Third-party libraries: `requests`, `PyMuPDF`

## Installation

### Using pip

You can install fetcharoo using pip:

```sh
pip install fetcharoo
```

### Using Poetry

If you are using Poetry to manage your project, you can install fetcharoo as a dependency:

```sh
poetry add fetcharoo
```
If you don't have Poetry installed, you can install it by following the instructions on the <a href="https://python-poetry.org/docs/#installation" target="_new">official Poetry website</a>.

### Getting Started

To get started with fetcharoo, follow these steps:

- Install the library using pip or Poetry (see the Installation section above).
- Import the `download_pdfs_from_webpage` function from the `fetcharoo` module.
- Use the function to download PDFs from a webpage, specifying the URL, recursion depth, mode (merge or separate), and output directory.

Here's a basic example:

```python
from fetcharoo import download_pdfs_from_webpage

# Download PDFs from a webpage and merge them into a single file
download_pdfs_from_webpage(
    url='https://example.com',
    recursion_depth=1,
    mode='merge',
    output_dir='output'
)
```
### Advanced Usage

fetcharoo provides additional options for customizing the behavior of the library:

- To download PDFs and store them as separate files, set the `mode` parameter to `separate`:

```python
download_pdfs_from_webpage(
    url='https://example.com',
    recursion_depth=1,
    mode='separate',
    output_dir='output'
)
```
To control the recursion depth, adjust the `recursion_depth` parameter. For example, to follow links up to two levels deep, set `recursion_depth`=2.

### Contributing
Contributions to fetcharoo are welcome! If you'd like to contribute, please follow these steps:

- Fork the repository on GitHub.
- Create a branch for your changes.
- Make your changes and commit them to your branch.
- Submit a pull request with your changes.
- We appreciate any contributions, whether it's fixing bugs, adding new features, or improving documentation.

### Support
If you encounter any issues or have questions about using fetcharoo, please open an issue on the GitHub repository. We'll do our best to assist you.

### Changelog
Please refer to the CHANGELOG.md file for a summary of changes in each release.

### Authors and Acknowledgments
fetcharoo was developed by Mark Lifson. I'd like to thank all contributors and users for their support.

### License
This project is licensed under the MIT License. See the LICENSE file for details. The MIT License allows for broad permissions, including use, modification, distribution, and sublicensing of the software.

## Update - May 7th, 2023

Added new features to fetcharoo:

- `merge_pdfs` function to merge multiple PDFs into a single file
