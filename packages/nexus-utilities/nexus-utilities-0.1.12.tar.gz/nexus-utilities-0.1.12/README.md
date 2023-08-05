# nexus-utilities<!-- omit in toc -->
This package is meant to hold various useful utilities for functionality I find myself using across multiple projects.  I will try to keep this documentation updated as I expand the toolkit.  Feel free to use these if you find them valuable and I welcome any feedback.

## Table of Contents <!-- omit in toc -->

- [Installation](#installation)
- [package\_utils.py](#package_utilspy)
  - [**add\_package\_to\_path()**](#add_package_to_path)
  - [**import\_relative(package\_root\_name, module\_path, import\_name, alias=None)**](#import_relativepackage_root_name-module_path-import_name-aliasnone)
- [About the Author](#about-the-author)

---

## Installation

```python
pip3 install nexus-utilities
```

After installation, use "import nexus_utils" to access the various functions.

---

## package_utils.py

This module contains functions for working with Python packages.

### **add_package_to_path()**

Arguments:
 * None

Programmatically determines the most likely root folder of the current running program, adds the parent folder to the system PATH, and returns the root folder name.  This can be helpful for resolving package-relative paths, particularly for programs with multiple possible entry points.  It achieves this by starting from the current working directory, and traversing upwards, counting the instances of the below files and folders:

```python
["src", "tests", "templates", "docs", "dist", "build", "readme.md", "license.txt", ".gitignore", "pyproject.toml", "requirements.txt", "poetry.lock", "setup.py", "manifest.in", ".editorconfig"]
```

In the case of a tie, it takes the folder deeper into the path.  The returned "package_root_name" is meant to be used with the "import_relative()" function below.

### **import_relative(package_root_name, module_path, import_name, alias=None)**

Example:  
***/app/flat_file_loader/src/utils/config_reader.py***

***import_relative('flat_file_loader', 'src.utils', 'config_reader', alias='cr')***

Arguments:
 * ***package_root_name(str):*** Folder name of package root folder.  Meant to be used with the output of the "add_package_to_path()" function
 * ***module_path(str):*** Dot-separated path from the package root to the library to be imported
 * ***import_name(str):*** Name of the object to be imported.  Can be a ".py" file name, or a function within a ".py" file (in the latter case, make sure the ".py" file name is part of the "module_path" above)
* ***alias(str):*** Optional alias for the imported library or function

Allows for importing package-relative libraries or functions given a programmatically-determined package root folder.  Useful for programs with multiple entry points and utilities called from multiple libraries.

***Important note: Pylance will show an error since the imports are done at runtime.  These can be avoided by attaching "# type: ignore" to any line using one of these relative imports.***

---

## About the Author

My name is James Larsen, and I have been working professionally as a Business Analyst, Database Architect and Data Engineer since 2007.  While I specialize in Data Modeling and SQL, I am working to improve my knowledge in different data engineering technologies, particularly Python.

[https://www.linkedin.com/in/jameslarsen42/](https://www.linkedin.com/in/jameslarsen42/)