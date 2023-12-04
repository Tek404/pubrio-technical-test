import requests
from bs4 import BeautifulSoup

def scrape_and_save_to_txt(url, output_file):
    response = requests.get(url)

    if response.status_code == 200:
        # extract data from html
        soup = BeautifulSoup(response.text, 'html.parser')
        data_to_store = soup.get_text()

        # remove empty lines
        lines = [line.strip() for line in data_to_store.splitlines() if line.strip()]

        # save data into text file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write('\n'.join(lines))

        print(f"Scraping successful. Data saved to {output_file}")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

website_url = 'https://techcrunch.com/2023/10/27/x-is-launching-new-premium-and-basic-subscription-tiers/'
output_txt_file = 'output.txt'

scrape_and_save_to_txt(website_url, output_txt_file)
