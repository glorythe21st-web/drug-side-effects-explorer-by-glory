import requests

def get_rxnorm_id(drug_name):
    try:
        url = f"https://rxnav.nlm.nih.gov/REST/rxcui.json?name={drug_name}"
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        data = res.json()
        return data.get("idGroup", {}).get("rxnormId", [None])[0]
    except Exception:
        return None
