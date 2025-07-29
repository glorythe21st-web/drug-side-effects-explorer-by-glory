import requests

try:
    response = requests.get("https://www.google.com", timeout=5)
    print(f"✅ Internet working. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"❌ Internet test failed: {e}")