# repo-reader

### Table of Contents

1. [Installation](#installation)
2. [Project motivation](#motivation)
3. [Instructions](#instructions)
4. [Licensing, Authors and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

- To install all required packages and run tests you need run from root directory:
    - Install dependencies from requirements.txt:
        - `pip install -r requirements.txt`
    - Make modules visible locally:
        - `pip install .`
    - Run tests:
        - `pytest`

## Project Motivation <a name="motivation"></a>

This project is a simple Python excercise that allow you to clone multiple repositories at one time.
The idea came when I was re-installing system and realised that I have around 30 repositories with RimWorld mods,
not mentioning the code repositories. Also I had a mental tech debt to Udacity Nanodegree where I didn't 
finished non-mandatory excercise with own Python PIP package.

## Instructions <a name="instructions"></a>

When steps from the [installation](#installation) section were finished you should be able to use this package
directly from your console.

Getting help:
- `repo-cloner --help` to see the instructions what to do.

Cloning repositories:
- `repo-cloner --repo-file <*.yml>` - will clone repositories to directory of running this command. Currently the .yml
configuration file should contain only list of git repo URL's to clone.


## Licensing, Authors, and Acknowledgements <a name="licensing"></a>

This package is released under MIT license. Please report any feedback to me if this package was useful to You.
