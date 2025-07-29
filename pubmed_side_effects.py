from Bio import Entrez

Entrez.email = "mail.glory247@gmail.com"

def get_pubmed_abstracts(drug_name, max_results=20):
    try:
        handle = Entrez.esearch(db="pubmed", term=f"{drug_name} adverse effects", retmax=max_results)
        record = Entrez.read(handle)
        pmids = record["IdList"]
        if not pmids:
            return []

        fetch = Entrez.efetch(db="pubmed", id=",".join(pmids), rettype="medline", retmode="xml")
        records = Entrez.read(fetch)

        abstracts = []
        for article in records["PubmedArticle"]:
            citation = article["MedlineCitation"]
            pmid = citation["PMID"]
            mesh_terms = [m["DescriptorName"] for m in citation.get("MeshHeadingList", [])]
            relevance_score = 0

            for term in mesh_terms:
                if any(kw in term.lower() for kw in ["adverse", "effect", "toxicity", "interaction"]):
                    relevance_score += 1

            try:
                abstract = article["MedlineCitation"]["Article"]["Abstract"]["AbstractText"][0]
            except KeyError:
                continue

            abstracts.append({
                "pmid": str(pmid),
                "abstract": abstract,
                "score": relevance_score
            })

        return abstracts

    except Exception as e:
        print(f"[red]❌ PubMed error: {e}")
        return []
