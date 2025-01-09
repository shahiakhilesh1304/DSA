# Repository Usage Guide

A comprehensive guide to help you get started with and contribute effectively to this repository.

## Table of Contents
- [Clone the Repository](#1-clone-the-repository)
- [Configure pyproject.toml](#2-configure-pyprojecttoml)
- [Install the Project](#3-install-the-project)
- [Organize Your Code](#4-organize-your-code)
- [Utilize the Analyzer Module](#5-utilize-the-analyzer-module) (Note: Removed for the time being do not use this module)
- [Utilize the Test Case Module](#6-Utilize-the-Test-Case-Module) 
- [Upload to Git](#7-upload-to-git)

## 1. Clone the Repository

Start by cloning this repository to your local machine:

```bash
git clone <repository-url>
```

## 2. Configure pyproject.toml

Navigate to the project root directory and modify the `pyproject.toml` file according to your needs:

### Key Configuration Areas:
- Project Metadata
- Dependencies
- Optional Dependencies
- Python Version
- Package Definitions

### Example Configuration:
```toml
[project]
name = "YourProject"
version = "1.0.0"
description = "Your project description"
authors = [{name = "Your Name", email = "your-email@example.com"}]
python_requires = ">=3.7"

[tool.setuptools]
packages = ["your_package_name"]

[tool.setuptools.package-dir]
"your_package_name" = "your_package_directory"
```

## 3. Install the Project

Choose the appropriate installation method based on your environment:

### Production Installation
```bash
pip install .
```

### Development Installation
```bash
pip install -e .
```

## 4. Organize Your Code

### Required Folder Structure
```
YourProject/
│
├── Questions/
│   ├── Question1/
│   │   ├── Problem_Statement.pdf
│   │   └── Input_Output/
│   │       ├── test_case1.txt
│   │       └── test_case2.txt
│   └── Question2/
│       ├── Problem_Statement.docx
│       └── Input_Output/
│           ├── test_case1.txt
│           └── test_case2.txt
└── Solutions/
    ├── Question1/
    │   ├── code.py
    │   ├── solution.md
    │   └── SolutionScreenShots/
    │       ├── output1.png
    │       └── output2.png
    └── Question2/
        ├── code.py
        ├── solution.md
        └── SolutionScreenShots/
            ├── output1.png
            └── output2.png
```

### Structure Details
- **Questions Folder**: Contains individual question folders
  - Problem statement file (PDF/DOCX/TEXT)
  - Input_Output folder with test cases
- **Solutions Folder**: Contains solution folders matching question numbers
  - `code.py`: Solution implementation
  - `solution.md`: Detailed solution explanation
  - SolutionScreenShots folder: Output screenshots

## 5. Utilize the Analyzer Module

Use the `analyzer` module to analyze your code's time complexity.

### Example Implementation:
```python
from Ruler.Analyzer import BigOCalculator, analyze_complexity

length = int(input("Enter the length of the array: "))
array_input = input(f"Enter the space Separated values for an array max number can be {length}: ")
data = list(map(int, array_input.split()))[:length]

i = 0
@analyze_complexity(inputs=[[1],[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5],[1,2,3,4,5,6],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9,10]])
def main(data):
    result = []
    for j in range(len(data)-1,-1,-1):
        result.append(data[j])
    global i 
    i+=1
    return result

if __name__ == "__main__":
    result = main(data)
    print(f"Final output for the query is : {result}")
```

### Important Notes:
- Use inputs for actions instead of print statements
- Avoid print statements within performing functions
- Focus on input-based operations for accurate analysis


## 8. Utilize the Test Case Module
Use the `testCases` module to use all the test cases placed in questions for the particular question you are solving .
This will provide all the testcase that are available with the particular question in a dictionary format

### Example Implimentation
[Code which is using this starting from line number 12](Solution/Question5/leftRotation.py)
### Important Notes:
- Must organize the code in the way mentioned [Organize Your Code](#4-organize-your-code)
- Must have input and outputs input one is named as input00.txt then it's output should be named as output00.txt


## 7. Upload to Git

After completing your changes, commit and push to the repository:

```bash
git add .
git commit -m "Your commit message"
git push
```

**Note**: Ensure your commit messages are descriptive and relevant to the changes made.
