# Doubly linked list (dll) Package

## Overview
This Python package contains an implementation of the doubly linked list based on the queue's push/pop mechanism. This package also contains a CLI for interacting with this dll.

## Features
- Can be tested via `pytest`

## Installation
You can install the package via pip in two simple steps:

1. clone the repo
```sh
git clone https://gitlab.com/fbvt/pythoncourse_dz02.git dll-lib
```

2. install lib with pip

```sh
pip install ./dll-lib/
```

3. clean up the installation meta data

```sh
python ./dll-lib/setup.py clean
```

## Requirements
- Python >= 3.9
- See `requirements.txt` for detailed package dependencies.

## Usage example

```python
from dll import DoublyLinkedList

# Create a new doubly linked list
dll = DoublyLinkedList[int]()

# Insert elements
dll.push(1)
dll.push(2)
dll.push(3)

# Remove an element from the front
dll.pop()

# Insert another dll
other_dll = DoublyLinkedList[int]([4, 5])
other_dll.insert(dll, 0)
```

### Command Line Interface (CLI)
A command line interface is also provided to perform operations on the doubly linked list. You can use it as follows:

* for help
```sh
dll-cli --help
```
* example
```sh
dll-cli push 6 2 3 5 4 pop sort print
```
## Development

### Setting Up the Development Environment
To contribute to the project, set up your local development environment:

1. Clone the repository:
   ```sh
   git clone https://gitlab.com/fbvt/pythoncourse_dz02.git dll-lib
   ```

2. Navigate to the project directory:
   ```sh
   cd dll-lib
   ```

3. Create a virtual environment:
   ```sh
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Linux/macOS:
     ```sh
     source venv/bin/activate
     ```
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```

5. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

6. Install development lib:
   ```sh
   pip install -e .
   ```

### Running Tests
You can run the test suite with `pytest`:

in project's root dir run
```sh
pytest
```

Make sure all tests pass before contributing.

## Contributing
Contributions are welcome! Feel free to submit issues, feature requests, or merge requests.

To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```sh
   git checkout -b feature/my-feature
   ```
3. Commit your changes and push them to your fork:
   ```sh
   git commit -m "Add my new feature"
   git push origin feature/my-feature
   ```
4. Submit a merge request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
- **Author**: Uglovskii Artem
- **Email**: [not.real@mail.dom](mailto:not.real@mail.dom)

## Project Links
- **Repository**: [GitLab](https://gitlab.com/fbvt/pythoncourse_dz02.git)
- **PyTest**: [PyTest](https://github.com/pytest-dev/pytest)

