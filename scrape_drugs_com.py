import requests
from bs4 import BeautifulSoup

def scrape_side_effects(drug_name):
    drug_name = drug_name.lower().replace(" ", "-")
    url = f"https://www.drugs.com/sfx/{drug_name}-side-effects.html"
    res = requests.get(url)
    
    if res.status_code != 200:
        return ["❌ Unable to retrieve drug page."]

    soup = BeautifulSoup(res.text, "html.parser")
    side_effects = []

    for ul in soup.select("div.contentBox > ul"):
        for li in ul.find_all("li"):
            side_effects.append(li.text.strip())

    return side_effects[:10] if side_effects else ["No side effects found on page."]
