import argparse
import os
import json
import csv
from rxnorm_lookup import get_rxnorm_id
from rxnav_interactions import get_interactions
from pubmed_side_effects import get_pubmed_abstracts

from rich import print
from rich.console import Console
console = Console()

parser = argparse.ArgumentParser(description="💊 Drug Side Effects Explorer CLI")
parser.add_argument('--save', action='store_true', help='Save results as CSV and JSON in outputs/')
parser.add_argument('--brief', action='store_true', help='Show brief summaries only (300 chars)')
parser.add_argument('--batch', type=str, help='Path to a .txt file with one drug per line')
args = parser.parse_args()

os.makedirs("outputs", exist_ok=True)

def process_drug(drug_name):
    console.rule(f"[bold blue]🔎 Exploring: {drug_name}")

    rxcui = get_rxnorm_id(drug_name)
    if not rxcui:
        console.print(f"[red]❌ Could not fetch RxCUI for {drug_name}")
        return

    interactions = get_interactions(rxcui, drug_name)
    console.print(f"[green]\n📦 Rx Interactions ({len(interactions)} found):")
    for i, desc in enumerate(interactions, 1):
        console.print(f"{i}. {desc}")

    abstracts = get_pubmed_abstracts(drug_name)
    top_abstracts = sorted(abstracts, key=lambda x: x.get("score", 0), reverse=True)[:10]

    console.print(f"\n📚 PubMed Abstracts (Top {len(top_abstracts)}):")
    for i, ab in enumerate(top_abstracts, 1):
        console.print(f"\n[i]{i}.[/i] PMID: [cyan]{ab['pmid']}[/cyan]")
        console.print(f"🔗 https://pubmed.ncbi.nlm.nih.gov/{ab['pmid']}/")
        if args.brief:
            console.print(f"📝 {ab['abstract'][:300]}...")
        else:
            console.print(f"📝 {ab['abstract']}")

    if args.save:
        base = f"outputs/{drug_name.replace(' ', '_').lower()}"
        with open(base + ".csv", "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["pmid", "abstract", "score"])
            writer.writeheader()
            writer.writerows(top_abstracts)

        with open(base + ".json", "w", encoding="utf-8") as f:
            json.dump(top_abstracts, f, indent=2)

        console.print(f"\n💾 Saved to [green]{base}.csv[/green] and [green]{base}.json[/green]")

if args.batch:
    with open(args.batch, "r", encoding="utf-8") as f:
        drugs = [line.strip() for line in f if line.strip()]
    for drug in drugs:
        process_drug(drug)
else:
    drug_name = input("🔎 Enter a drug name: ").strip()
    if drug_name:
        process_drug(drug_name)
