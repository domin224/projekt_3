"""
scraper.py: třetí projekt do Engeto Online Python Akademie

author: Dominik Šváb
email: dominik.svab123@gmail.com
"""
import argparse
import validators
import requests
import csv
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, parse_qs



def is_url_valid(url):
    return validators.url(url)

def get_arguments():
    parser = argparse.ArgumentParser(
        description="Czech 2017 Chamber of Deputies Election Results Scraper"
        )

    parser.add_argument(
        "url",
        type=str,
        help="URL of the electoral district to scrape."
        )
    
    parser.add_argument(
        "output_file",
        type=str,
        help="Enter the output CSV file name (e.g., benesov_results.csv)"
        )

    args = parser.parse_args()

    if not is_url_valid(args.url):
        print("Error: Invalid URL! Please provide a valid URL.")

    if not args.output_file.endswith(".csv"):
        print("Error: Invalid file name! Please provide valid file name ending with .csv (e.g., benesov_results.csv).")

    return args

def make_soup(url):
    server_response = requests.get(url)
    soup = BeautifulSoup(server_response.text, features="html.parser")
    return soup


def make_href_list(args):
    soup = make_soup(args.url)

    tags = soup.find_all("td", class_="cislo")
    href_list = []

    for tag in tags:
        link = tag.find('a')
        if link and 'href' in link.attrs:
            full_url = urljoin(args.url, link['href'])
            href_list.append(full_url)
    
    if not href_list:
        href_list = [args.url] #in case when we want to scrape abroad

    return href_list

def make_first_line(href_list):
    
    soup = make_soup(href_list[0])
    td = soup.find_all("td", class_="overflow_name")

    first_line = ["code","location","registered","envelopes","valid"]
    
    for i in td:
        clean_text = i.text.strip()
        first_line.append(clean_text)

    return first_line

def get_location_name(href):
    soup = make_soup(href)
    tag = soup.find_all("h3")
    try:
        location_name = tag[2].text.split(": ")[1]
        return location_name
    except IndexError:
        try:
            location_name = tag[1].text.split(": ")[1]
            return location_name
        except IndexError:
            try:
                location_name = tag[0].text.split(": ")[1]
                return location_name
            except IndexError:
                return None
            
def get_location_code(href):
    parsed_url = urlparse(href)
    parameters = parse_qs(parsed_url.query)
    location_code = parameters.get('xobec', [None])[0]
    return location_code

def scrape_table(href, attributes, is_table_1):
    table_data = []
    soup = make_soup(href)
    td_elements = soup.find_all("td", attrs=attributes)

    if not td_elements:
        print(f"Warning: No data found for attributes {attributes} in URL {href}.")

    for td in td_elements:
        cleaned_text = td.text.strip()
        table_data.append(cleaned_text)
    
    if is_table_1:
        table_data.pop(2)
            
    return table_data

def scrape_site(href_list):
    data = []
    first_line = make_first_line(href_list)
    data.append(first_line)
    
    for href in href_list:
        href_data = []

        location_code = get_location_code(href)
        href_data.append(location_code)

        location_name = get_location_name(href)
        href_data.append(location_name)

        table_1 = scrape_table(href, {"data-rel": "L1"}, True)
        href_data.extend(table_1)

        table_2 = scrape_table(href, {"headers": "t1sa2 t1sb3"}, False)
        href_data.extend(table_2)

        table_3 = scrape_table(href, {"headers": "t2sa2 t2sb3"}, False)
        href_data.extend(table_3)

        data.append(href_data)
    
    return data

def import_to_csv_file(data, args):
    filename = args.output_file

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)

args = get_arguments()
href_list = make_href_list(args)
data = scrape_site(href_list)
import_to_csv_file(data, args)

