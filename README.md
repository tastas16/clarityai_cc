# ClarityAI Code Challenge

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Description

This Python tool, developed for the ClarityAI code challenge, is designed to parse log files containing host-to-host connections. It filters these connections based on specified datetime ranges and hostnames, helping to analyze network activities within any given period.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository to your local machine using `git clone https://github.com/tastas16/clarityai_cc.git`.
2. Navigate to the project directory.
3. Create a virtual environment with Python=3.10 and poetry.
3. Install the project and its dependencies with Poetry: `poetry install`

## Usage

To use the log parser, follow these steps:

1. Run the tool from the command line:

    `poetry run log-parser path/to/logfile "YYYY-MM-DD HH:MM:SS" "YYYY-MM-DD HH:MM:SS" hostname`

Replace `path/to/logfile` with the path to your log file, the date-time strings with your desired start and end times, and `hostname` with the host you're interested in.

2. Example command:

    `poetry run log-parser ./input_data/input-file-10000.txt "2019-08-12 22:00:04" "2019-08-13 21:59:58" Maronda`

This will output the hostnames that were connected to 'quark' between April 1, 2021, and April 2, 2021.

For more detailed usage examples, please refer to the included example files and test cases.

## Contributing

We welcome contributions from the community. To contribute:

1. Fork the project.
2. Create a new branch.
3. Make your changes and commit them with a clear and concise commit message.
4. Push your changes to the branch on your fork.
5. Submit a pull request detailing your changes.

## License

This project is licensed under the [MIT License](LICENSE).