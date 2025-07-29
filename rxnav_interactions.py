import requests

def get_interactions(rxcui, drug_name=""):
    try:
        url = f"https://rxnav.nlm.nih.gov/REST/interaction/interaction.json?rxcui={rxcui}"
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        data = res.json()
        descs = []
        for group in data.get("interactionTypeGroup", []):
            for t in group.get("interactionType", []):
                for pair in t.get("interactionPair", []):
                    descs.append(pair.get("description", ""))
        return descs
    except Exception:
        return [f"❌ RxNav API failed for {drug_name}"]
