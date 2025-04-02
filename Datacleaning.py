import json

def is_definitely_broken(entry):
    title = entry.get("title", "").strip().lower()
    return title == "title not found"

def deduplicate_authors(authors):
    return list(dict.fromkeys([a.strip() for a in authors]))

def truncate_text(text, word_limit=250):
    words = text.split()
    if len(words) > word_limit:
        return " ".join(words[:word_limit]) + " ..."
    return text

def clean_abstracts(input_path, output_cleaned, output_rejected):
    with open(input_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)

    cleaned = []
    rejected = []

    for entry in raw_data:
        if is_definitely_broken(entry):
            rejected.append(entry)
        else:
            entry['authors'] = deduplicate_authors(entry.get('authors', []))
            entry['abstract_content'] = truncate_text(entry.get('abstract_content', ""))
            cleaned.append(entry)

    with open(output_cleaned, 'w', encoding='utf-8') as f:
        json.dump(cleaned, f, indent=2, ensure_ascii=False)

    with open(output_rejected, 'w', encoding='utf-8') as f:
        json.dump(rejected, f, indent=2, ensure_ascii=False)

    print(f"✅ Cleaned abstracts: {len(cleaned)}")
    print(f"🗑️ Removed entries with 'Title Not Found': {len(rejected)}")

if __name__ == "__main__":
    clean_abstracts(
        input_path="data/abstracts1.json",
        output_cleaned="data/abstracts2.json",              # Overwrites with cleaned + truncated version
        output_rejected="data/abstracts_rejected.json"
    )
