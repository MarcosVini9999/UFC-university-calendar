import requests
from bs4 import BeautifulSoup
import json

page = requests.get('https://ufc.br/calendario-universitario')
soup = BeautifulSoup(page.text, 'html.parser')

months_years = soup.select('h3')
categories = soup.select(".category")
calendar = {}

for month_year_index in range(len(months_years)):  
  month_year = months_years[month_year_index].text
  calendar[month_year] = []
  category = categories[month_year_index]
  rows = category.select(".item")

  for row in rows:
    day = row.select(".cell:nth-child(1)")[0]
    description = row.select(".cell+ .cell")[0]
    calendar[month_year].append({"day":day.text.strip(), "description": description.text.strip() })

with open("data.json", "w", encoding="utf-8") as outfile:
    json.dump(calendar, outfile, ensure_ascii=False)