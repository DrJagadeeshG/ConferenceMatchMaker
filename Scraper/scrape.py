import requests
from bs4 import BeautifulSoup
import re
import json

def scrape_abstract_content(abstract_url):
    """
    Scrapes the Session, Abstract ID, Title, Abstract, Authors, and Affiliations from the given URL.
    """
    try:
        response = requests.get(abstract_url)
        if response.status_code == 404:
            print(f"Abstract not found: {abstract_url}")
            return None
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching {abstract_url}: {e}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract Session
    session_tag = soup.find('a', href=re.compile(r'/session/\d+'))
    session = session_tag.text.strip() if session_tag else "Session Not Found"

    # Extract Abstract ID using regex
    abstract_id_match = re.search(r'EGU25-(\d+)', abstract_url)
    abstract_id = abstract_id_match.group(1) if abstract_id_match else "Abstract ID Not Found"

    # Extract Title
    title_tag = soup.find('div', class_='co_mto_htmlabstract-title')
    title = title_tag.text.strip() if title_tag else "Title Not Found"

    # Extract Authors
    authors_section = soup.find('div', class_='co_mto_htmlabstract-authors')
    authors = []
    if authors_section:
        for author in authors_section.find_all('nobr'):
            authors.append(author.text.strip())

    # Extract Affiliations
    affiliations_section = soup.find('ul', class_='affiliation-list')
    affiliations = []
    if affiliations_section:
        for li in affiliations_section.find_all('li'):
            affiliations.append(li.text.strip())

    # Extract Abstract Content
    abstract_section = soup.find('div', class_='co_mto_htmlabstract-content')
    paragraphs = abstract_section.find_all('p') if abstract_section else []
    abstract_content = ' '.join([p.text.strip() for p in paragraphs])

    return {
        "session": session,
        "abstract_id": abstract_id,
        "title": title,
        "abstract_content": abstract_content,
        "authors": authors,
        "affiliations": affiliations,
        "url": abstract_url
    }

def main():
    base_url = "https://meetingorganizer.copernicus.org/EGU25/EGU25-"
    all_data = []

    # Iterate through abstract IDs from 00001 to 25000
    for abstract_id in range(1, 25000):
        abstract_url = f"{base_url}{str(abstract_id).zfill(5)}.html"
        print(f"Scraping: {abstract_url}")
        data = scrape_abstract_content(abstract_url)
        if data:
            all_data.append(data)

    # Save data to JSON
    with open('data/abstracts.json', 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=4)
    print("Data saved to abstracts.json.")

if __name__ == "__main__":
    main()
