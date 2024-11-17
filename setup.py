from setuptools import setup, find_packages, Command
import os
import shutil

MODULE_NAME='dll'

current_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(current_dir, 'README.md')) as f:
    long_description = f.read()

class CleanUpCommand(Command):
    description = 'Remove *.egg-info and other metainfo directories after installation.'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        for dir_path in ['dll.egg-info', 'build']:
            full_dir_path = os.path.join(current_dir, dir_path)
            if os.path.exists(full_dir_path):
                shutil.rmtree(full_dir_path)

setup(
    name=MODULE_NAME,
    version="0.0.1",
    author="Uglovskii Artem",
    author_email="not.real@mail.dom",
    description="Lib with doubly linked list which behaves like a queue",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/fbvt/pythoncourse_dz02.git",
    project_urls={
        "Pytest": "https://github.com/pytest-dev/pytest",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    license="MIT",
    keywords="doubly linked list data structure",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.9",
    install_requires=open(os.path.join(current_dir, "requirements.txt")).read().splitlines(),
    entry_points={
        "console_scripts": [
            "dll-cli=dll.dll_cli:main",
        ],
    },
    cmdclass={
        'clean': CleanUpCommand,
    },
)