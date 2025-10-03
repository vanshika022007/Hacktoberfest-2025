# Python Scripts Collection

![Hacktoberfest 2025](https://img.shields.io/badge/Hacktoberfest-2025-orange.svg)
![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)

This repository contains Python scripts designed to automate common tasks. It is beginner-friendly and open for contributions during Hacktoberfest 2025.

## Table of Contents

1. [About](#about)
2. [Getting Started](#getting-started)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [Project Structure](#project-structure)
6. [Contributors](#contributors)
7. [License](#license)
8. [Contact](#contact)

## About

The repository currently contains the following scripts:

- `file_renamer.py` — Rename all files in a folder with a specific prefix and optional extension filter.
- `image_compressor.py` — Compress images individually or in bulk using Pillow.
- `factorial_calculator.py` — Calculate the factorial of a non-negative integer.
  This collection aims to help users automate repetitive tasks efficiently and serve as an introduction to Python scripting and open-source contributions.

## Getting Started

### Prerequisites

Before running the scripts, ensure you have the following installed:

- Python 3.9+
- Git
- Optional: Node.js (for additional scripts or integration)

### Installation

1. **Fork the repository** on GitHub.
2. **Clone your fork** to your local machine:

```bash
git clone https://github.com/YOUR-USERNAME/Hacktoberfest-2025.git
cd Hacktoberfest-2025
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

If using Node.js scripts:

```bash
npm install
```

## Usage

1. File Renamer

```bash
from Scripts.file_renamer import rename_files
rename_files("documents", prefix="report", extension=".txt")
```

2. Image Compressor

```bash
from Scripts.image_compressor import compress_folder
compress_folder("images","compressed_images",quality=60)
```

3. Factorial Calculator

```bash
from Scripts.factorial_calculator import factorial
print(f"Factorial of 5: {factorial(5)}")
print(f"Factorial of 0: {factorial(0)}")
```

Both scripts include detailed docstrings and inline comments to guide usage.

## Contributing

We welcome contributions of all kinds from improving documentation to adding new scripts.

1. Review the [CONTRIBUTION.md]
   guide.
2. Create a new branch for your changes:

```bash
git checkout -b feat/your-feature-name
```

3. Commit your changes with a descriptive message:

```bash
git commit -m "docs: improve README and add usage examples"
```

4. Push your branch and open a Pull Request.

## Project Structure

.
├── Scripts/ # Contains Python scripts
│ ├── file_renamer.py
│ └── image_compressor.py
├── .gitignore # Files to ignore in Git
├── CONTRIBUTING.md # Contribution guidelines
├── LICENSE # MIT License file
├── README.md # This file
└── WORKFLOW.md # Git and GitHub workflow guide

## ✨ Contributors

Thanks to these wonderful people for their contributions!

<table>
  <tr>
    </tr>
</table>

## Contact

For questions or support, open an issue and tag the maintainer **@milansinghal2004**.
