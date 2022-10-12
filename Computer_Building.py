# imports
import json
from datetime import datetime
from Data_Scraper.scraper import Scraper

def update_json(parts):
    scraper = Scraper()
    cpus = scraper.scrape_cpu()
    gpus = scraper.scrape_gpu()
    ram = scraper.scrape_ram()
    parts['cpu'] = cpus
    parts['gpu'] = gpus
    parts['ram'] = ram
    with open('Data.json', 'w') as file:
        json_string = json.dumps(parts, indent=4)
        file.write(json_string)
    file.close()

if __name__ == "__main__":
    s = Scraper()
    with open('Data.json', 'r') as file:
        parts = json.load(file)
    file.close()
    date1 = datetime.strptime(parts['Last Update'], "%Y-%m-%d")
    today = datetime.today()

    change = today - date1
    
    if change.days > 7:
        update_json(parts)