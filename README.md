# 💊 Drug Side Effects Explorer

A Python CLI tool to explore drug side effects, interactions, and PubMed literature using open biomedical APIs like RxNav, DrugBank, and RxTerms.

---

## 🚀 Features

- ✅ RxNav interaction lookup  
- ✅ PubMed side effects search  
- ✅ DrugBank and RxTerms fallback  
- ✅ AI/MeSH-based relevance scoring  
- ✅ `--save` flag to store results (CSV/JSON)  
- ✅ `--brief` flag for summary-only output  
- ✅ Automatic `/outputs` subfolder  
- ✅ Batch mode for multiple drugs  
- ✅ Rich CLI formatting and logging  

---

## 🧪 Example Usage

```bash
# Run the explorer for a single drug
python main.py --save --brief

# Batch mode using drug names in a file
python main.py --batch drugs.txt --save
## Example Output
💊 Drug Side Effects Explorer
🔎 Enter a drug name: Ibuprofen

📦 RxNav Interactions:
1. Ibuprofen interacts with Aspirin – potential GI bleeding risk.

📚 Top PubMed Abstracts:
1. [PMID: 12345678] – NSAID-related gastric injury in chronic users.
2. [PMID: 87654321] – Role of Ibuprofen in renal impairment.

✔ Saved output to /outputs/Ibuprofen/

```
## **📁 Output Files**

-outputs/Ibuprofen.csv – CSV with interaction and abstract data

-outputs/Ibuprofen.json – JSON version of results

-Log file: drug_explorer.log

## **🔧 Requirements**

-Python 3.10+

-Install dependencies:

pip install -r requirements.txt

## **📡 APIs Used**

-RxNav

-PubMed via E-Utilities

-DrugBank

-RxTerms

## **🛠 Developer Notes**

-Modular code (main.py, pubmed_side_effects.py, rxnav_lookup.py, etc.)

-Uses rich for colored terminal output

-Built-in error handling and retry logic for unstable endpoints

## **🏷️ License**

MIT License

## **📦 Author**
Joseph Glory Mamani – @glorythe21st-web
