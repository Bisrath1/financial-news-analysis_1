# Financial News Analysis

This repository contains the implementation of the 10 Academy Week 1 Challenge, analyzing the relationship between financial news sentiment and stock price movements for major tech companies (AAPL, AMZN, GOOG, META, MSFT, NVDA, TSLA). It includes exploratory data analysis (EDA), technical indicator calculations, sentiment analysis, correlation analysis, interactive visualizations, and a CI/CD pipeline using GitHub Actions.

## Table of Contents
- [Project Overview](#project-overview)
- [Visualizations](#visualizations)
- [Setup Instructions](#setup-instructions)
- [Repository Structure](#repository-structure)
- [CI/CD Pipeline](#cicd-pipeline)
- [Usage](#usage)
- [Progress](#progress)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

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

<<<<<<< HEAD
=======
## Usage
- View interactive visualizations in `notebooks/plots/*.html`.
- Use PNG images for presentations or LinkedIn posts.
- Explore `Data/processed/` CSVs for further analysis.

>>>>>>> c0e1f98dc6b02637e492a4209a66b96d63f262e0
## Progress
- **Task 1**: Initialized Git repository, set up Python environment, and conducted EDA (branch: `task-1`).
- **Task 2**: Implemented technical indicator calculations (SMA, RSI, MACD) using TA-Lib.
- **Task 3**: Added sentiment analysis, correlation analysis, visualizations, and unit tests (branch: `task-3`).

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License.

## Contact
Maintained by [Bisrath1](https://github.com/Bisrath1). For issues or questions, open a GitHub issue or contact the owner directly.

---

*Built as part of the 10 Academy Week 1 Challenge to demonstrate data analysis, visualization, and CI/CD skills.*
>>>>>>> c0e1f98dc6b02637e492a4209a66b96d63f262e0
