## House Prediction Price Analysis

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A Python project for analyzing house prediction data, including data cleaning, exploration, and visualization of properties based on bedrooms and society.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Contributing](#contributing)
- [License](#license)

## Features
- Load and clean house prediction data from CSV
- Filter properties by number of bedrooms
- Visualize distribution of 2-bedroom properties by society using seaborn and matplotlib

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/house-prediction-price.git
   cd house-prediction-price
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Place `house_prediction.csv` in the project directory.
2. Run the analysis:
   ```
   python main.py
   ```
   This will generate and display a countplot of 2-bedroom properties by society.

## Data
The project requires `house_prediction.csv` with columns such as:
- `bedRoom`: Number of bedrooms
- `society`: Society name
- Other relevant features for house prediction

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
