import requests

def get_rxnorm_id(drug_name):
    url = f"https://rxnav.nlm.nih.gov/REST/rxcui.json?name={drug_name}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("idGroup", {}).get("rxnormId", [None])[0]
    except requests.exceptions.Timeout:
        print("❌ Connection timed out. Check your network or try again later.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Request error: {e}")
    return None
