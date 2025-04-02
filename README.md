
# 🤝 ConferenceMatchMaker – EGU Abstract Matcher and Networking Tool

**ConferenceMatchMaker** is a smart tool designed for academic conferences like the **EGU General Assembly**, where thousands of researchers submit abstracts and want to connect with peers working on similar topics. This project aims to simplify the **matchmaking process** by scraping all publicly available abstracts and using NLP-based similarity matching to help researchers find potential collaborators before or during the conference.

## Running website
**https://conferencematchmaker.streamlit.app/**
---

## 📌 Features

- 🔍 Scrapes up to **25,000 abstracts** directly from the EGU website.
- 🧠 Uses state-of-the-art **Sentence Transformers** for semantic matching.
- ⚡ Efficient search with **FAISS**, optimized for large datasets.
- 🖥️ **Streamlit** frontend for easy user interaction.
- 📝 Outputs include **title, abstract content, authors, affiliations, and similarity score**.
- 📤 JSON-based outputs for integration or sharing.

---

## 🗂️ Project Structure

```
ConferenceMatchMaker/
│
├── Data/                           # Output data and embeddings
│   ├── abstracts.json              # Scraped abstracts
│   ├── abstracts_index.faiss      # FAISS vector index
│   └── matches.json               # Matched abstracts for a given user input
│
├── env/                           # (Optional) Python virtual environment
│
├── Matcher/                       # NLP pipeline
│   ├── embed.py                   # Embeds abstracts using Sentence Transformers
│   └── search.py                  # Searches FAISS index for closest matches
│
├── Scraper/                       # Web scraper for EGU abstract pages
│   └── scrape.py                  # Iterates from 00001 to 25000 and scrapes data
│
├── app.py                         # Streamlit app for UI and match display
├── run.py                         # Optional entry point for command-line interface
├── requirements.txt               # Required packages
├── .gitignore                     # Files to be ignored by Git
├── LICENSE                        # MIT license
└── readme.md                      # You are here 📖
```

---

## 🧰 Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/ConferenceMatchMaker.git
cd ConferenceMatchMaker
```

2. **Create a virtual environment (optional but recommended)**

```bash
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## 🚀 How It Works

### 1. **Scrape Abstracts**

```bash
python Scraper/scrape.py
```

- Scrapes abstracts from:  
  `https://meetingorganizer.copernicus.org/EGU25/EGU25-00001.html` → `EGU25-25000.html`
- Saves structured results into: `Data/abstracts.json`

---

### 2. **Generate Embeddings**

```bash
python Matcher/embed.py
```

- Loads `abstracts.json`
- Creates sentence embeddings using `sentence-transformers/all-MiniLM-L6-v2`
- Builds a **FAISS** index and saves it as `abstracts_index.faiss`

---

### 3. **Run the Matching App**

```bash
streamlit run app.py
```

- Enter your own **abstract title** and **abstract content**
- Finds and shows the **top 5 most similar abstracts** with:
  - Title
  - Authors
  - Affiliations
  - Abstract content
  - URL
  - Similarity score

---

## 🔎 Sample Usage

### User Input
> Title: **Smart Monitoring of Urban Floods Using IoT and AI**  
> Abstract: _This study introduces a hybrid AI system for detecting flood-prone zones in real time..._

### Output
```markdown
1. Flood Forecasting Using Machine Learning and Sensor Networks
   Authors: Dr. A. Kumar, Prof. L. Smith
   Affiliations: XYZ Institute of Hydrology
   Similarity Score: 0.8721
```

---

## 🔗 Technologies Used

- **Python 3.8+**
- **BeautifulSoup** – HTML parsing
- **Sentence Transformers** – NLP model for abstract similarity
- **FAISS** – Facebook AI similarity search
- **Streamlit** – UI framework
- **JSON** – Data storage

---

## 💡 Use Cases

- **Pre-conference networking** – Know who to meet before reaching the venue.
- **Collaboration hunting** – Find potential co-authors, reviewers, or experts.
- **Research discovery** – Discover adjacent fields related to your work.

---

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](./LICENSE) for more details.

---

## 🙌 Contributing

Contributions are welcome!  
Please open an issue or submit a pull request with improvements, bug fixes, or new features.

---

## ✉️ Contact

Built with ❤️ for the EGU 2025 scientific community.  
Have questions or suggestions? Reach out at:

- 📧 [saijagadeeshg@gmail.com]
- 🌐 [https://github.com/DrJagadeeshG/ConferenceMatchMaker]

---

## 📢 Acknowledgments

Special thanks to:
- [EGU](https://www.egu.eu) for making abstracts publicly accessible.
- [SentenceTransformers](https://www.sbert.net) and [FAISS](https://github.com/facebookresearch/faiss) for the amazing tools.

---
