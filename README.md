
# Czech 2017 Chamber of Deputies Election Results Scraper

This project is a scraper for downloading election results of the Czech Chamber of Deputies from 2017. The script extracts data from a given electoral district ("Územní úroveň") URL and saves it into a CSV file.

## Author
- **Name**: Dominik Šváb
- **Email**: dominik.svab123@gmail.com

---

## Installation

1. **Download the repository as ZIP file**:

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

1. Choose one electroral district ("Územní úroveň") from this web page https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ
   
2. Click on the "X" in the "Výběr obce" column. A new web page opens.
   
3. Copy the URL of the web page.

4. Run the script with the following arguments:
   1. URL of the election district page to scrape. 
   2. The name of the output CSV file.

### Example:
```bash
python scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5202" "results.csv"
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
- The input URL must be a valid page containing data for the 2017 Chamber of Deputies election. The page should have an overview of all towns (obec) within the selected district (okres).
- The output file must have a `.csv` extension.
