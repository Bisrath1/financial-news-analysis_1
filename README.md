
## Project Overview
- **Objective**: Investigate how news sentiment correlates with stock returns using historical stock prices and news headlines.
- **Data**:
  - Stock prices from Yahoo Finance (`Data/raw/*.csv`).
  - News headlines from `raw_analyst_ratings.csv`.
- **Tasks**:
  - **Task 1 (EDA)**: Analyzed stock price trends and news publication frequency.
  - **Task 2 (Quantitative Analysis)**: Computed technical indicators (SMA, RSI, MACD) using TA-Lib.
  - **Task 3 (Correlation Analysis)**: Calculated news sentiment using TextBlob and correlated it with daily stock returns.
- **Visualizations**:
  - Candlestick chart with SMA, RSI, MACD for AAPL.
  - Sentiment vs. daily returns scatter plot.
  - Correlation heatmap between sentiment and returns.
  - News publication frequency over time.
- **CI/CD**: Automated unit tests via GitHub Actions to ensure code quality.

## Visualizations
Interactive plots and static images are available in `notebooks/plots/`:
- [AAPL Stock Analysis](notebooks/plots/AAPL_indicators.html) ([PNG](notebooks/plots/AAPL_indicators.png))
- [Sentiment vs. Returns](notebooks/plots/sentiment_vs_returns.html) ([PNG](notebooks/plots/sentiment_vs_returns.png))
- [Correlation Heatmap](notebooks/plots/correlation_heatmap.html) ([PNG](notebooks/plots/correlation_heatmap.png))
- [Publication Trends](notebooks/plots/publication_trends.html) ([PNG](notebooks/plots/publication_trends.png))

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Bisrath1/financial-news-analysis_1.git
   cd financial-news-analysis_1
   ```
2. **Create and Activate Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Install TA-Lib** (Windows):
   - Download `ta_lib-0.6.3-cp311-cp311-win_amd64.whl` from [TA-Lib releases](https://github.com/TA-Lib/ta-lib-python/releases).
   - Install: `pip install ta_lib-0.6.3-cp311-cp311-win_amd64.whl`.
5. **Run Scripts**:
   - Prepare data: `python scripts/prepare_news_stock.py`
   - Compute indicators: `python scripts/compute_indicators.py`
   - Generate visualizations: `python scripts/visualizations.py`
   - Run tests: `pytest tests/`

## Repository Structure
```
financial-news-analysis_1/
├── Data/
│   ├── raw/                     # Raw stock and news data
│   ├── processed/               # Processed CSVs (news_stock_merged.csv, stock_indicators.csv)
├── notebooks/plots/             # Visualizations (HTML and PNG)
├── scripts/                     # Data processing and visualization scripts
├── tests/                       # Unit tests for data loading and indicators
├── .github/workflows/           # CI/CD pipeline (unittests.yml)
├── requirements.txt             # Dependencies
├── README.md                    # Project documentation
```

## CI/CD Pipeline
Unit tests are automatically run on every push/pull request using GitHub Actions (see `.github/workflows/unittests.yml`). Tests validate data loading and indicator calculations.

## Usage
- View interactive visualizations in `notebooks/plots/*.html`.
- Use PNG images for presentations or LinkedIn posts.
- Explore `Data/processed/` CSVs for further analysis.

## Contributing
=======

# Project Title
*Financial News Analysis*

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Repository Structure](#repository-structure)
- [Usage](#usage)
- [Progress](#progress)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview
A brief description of the project, its purpose, and its goals. Mention the context (e.g., 10 Academy Week 1 Challenge) and what the project achieves (e.g., financial news and stock market data analysis).

Example:  
This repository contains code and analysis for the 10 Academy Week 1 Challenge, focusing on analyzing financial news and stock market trends using Python, with visualizations for stock prices, SMA, RSI, MACD, and daily returns.

## Features
List key functionalities or highlights of the project in bullet points.

- Data fetching using `yfinance`.
- Visualizations for stock prices, SMA, RSI, MACD, and daily returns).
- Automated unit testing with GitHub Actions.
- Modular code structure with reusable scripts.

## Setup Instructions
Step-by-step guide to set up the project locally.

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Bisrath1/financial-news-analysis_1.git
   ```
2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv
   ```
3. **Activate the Virtual Environment**:
   - On Unix/Linux/MacOS:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Repository Structure
Describe the directory layout and purpose of each folder/file.

```
├── .github/workflows/   # GitHub Actions for CI/CD (e.g., unit testing)
├── .vscode/             # VS Code settings
├── notebooks/            # Jupyter notebooks for EDA and visualizations
├── scripts/                # Utility scripts (e.g., for data fetching with yfinance)
├── src/                    # Reusable Python scripts
├── tests/                    # Unit tests
├── .gitignore              # Files/folders to exclude from Git
├── README.md            # Project documentation
├── requirements.txt       # Python dependencies
```

## Usage
Explain how to run the project or specific components.

- Launch Jupyter notebooks for analysis:
  ```bash
  jupyter lab
  ```
- Run data fetching scripts:
  ```bash
  python scripts/fetch_data.py
  ```
- Execute unit tests:
  ```bash
  pytest tests/
  ```

## Progress
Summarize completed tasks and milestones.

- **Task 1**: Initialized Git, set up Python environment, and conducted EDA (branch: `task-1`).
- **Task 3**: Added visualizations for stock metrics and merged changes (branch: `task-3`, commit: `294f216`).

## Contributing
Guidelines for contributing to the project.

>>>>>>> f9bf461754889cb0a9bd3932d6ff4be10fe455f3
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

<<<<<<< HEAD
## Contact
Maintained by [Bisrath1](https://github.com/Bisrath1). For issues or questions, open a GitHub issue or contact the owner directly.

## License
This project is licensed under the MIT License.

---

*Built as part of the 10 Academy Week 1 Challenge to demonstrate data analysis, visualization, and CI/CD skills.*
=======
## License
Specify the project's license.

This project is licensed under the [MIT License](LICENSE).

## Contact
Provide contact details for the maintainer.

Maintained by [Bisrath1](https://github.com/Bisrath1). For issues or questions, open a GitHub issue or contact the owner directly.

---



