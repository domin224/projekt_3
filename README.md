
# Czech 2017 Chamber of Deputies Election Results Scraper

This project is a scraper for downloading election results of the Czech Chamber of Deputies from 2017. The script extracts data from a given electoral district (e.g., okres) URL and saves it into a CSV file.

## Author
- **Name**: Dominik Šváb
- **Email**: dominik.svab123@gmail.com

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone <URL_TO_REPOSITORY>
   cd <PROJECT_DIRECTORY>
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the script with the following arguments:
1. URL of the election district page to scrape.
2. The name of the output CSV file.

### Example:
```bash
python scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=2111" "results.csv"
```

---

## Features

1. **URL Validation**: The script checks if the provided URL is valid.
2. **Data Extraction**: Downloads election results from the specified page and its subpages.
3. **Data Export**: Saves the data into a CSV file.

---

## Requirements

- **Python**: 3.6 or newer
- **Libraries**:
  - `argparse`
  - `validators`
  - `requests`
  - `csv`
  - `BeautifulSoup4`
  - `urllib.parse`

---

## Notes
- The input URL must be a valid (okres) page containing data for the 2017 Chamber of Deputies election.
- The output file must have a `.csv` extension.
