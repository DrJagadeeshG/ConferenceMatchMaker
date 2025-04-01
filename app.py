import streamlit as st
from Matcher.search import find_matches

st.title("🔍 EGU Matchmaker – Find Your People")

# Developer information
st.markdown("---")
st.markdown(
    """
    #### 👨‍💻 About the Developer  
    This tool is developed by [Dr. Jagadeesh G](https://www.linkedin.com/in/jagadeesh-gaddam-iit-tp/),  
    a recent PhD graduate in **Smart Water Management**.  
    💌 For suggestions or collaborations, reach out at: **saijagadeeshg@gmail.com**

    ⭐ If you found this helpful, consider giving the project a star on [GitHub](https://github.com/DrJagadeeshG/ConferenceMatchMaker)!
    """
)

st.markdown("---")
# Input fields for title and abstract
title = st.text_input("Enter your abstract title:")
abstract = st.text_area("Paste your abstract content:")

# Input for number of similar abstracts to retrieve
num_articles = st.number_input("Number of similar abstracts to find:", min_value=1, max_value=50, value=5)

if st.button("Find Similar Abstracts"):
    if not title or not abstract:
        st.warning("Please fill both fields.")
    else:
        try:
            # Fetching results dynamically based on user input
            results = find_matches(title, abstract, k=num_articles)
            
            if not results:
                st.warning("No similar abstracts found. Try refining your input.")
            else:
                st.success(f"Top {len(results)} similar abstracts found:")

                # Displaying each result
                for i, res in enumerate(results, start=1):
                    # Safely handle missing fields with `.get()` method
                    result_title = res.get('title', 'Title not available')
                    authors = res.get('authors', [])
                    affiliations = res.get('affiliations', [])
                    abstract_content = res.get('abstract_content', 'Abstract content not available')
                    url = res.get('url', '#')  # Default to "#" if URL is missing
                    score = res.get('score', 0.0)  # Default score to 0.0 if missing

                    # Remove duplicate authors and affiliations while preserving order
                    unique_authors = list(dict.fromkeys(authors))
                    unique_affiliations = list(dict.fromkeys(affiliations))

                    # Display result details
                    st.markdown(f"### {i}. {result_title}")
                    st.markdown(f"**Authors**: {', '.join(unique_authors) if unique_authors else 'Authors not available'}")
                    st.markdown(f"**Affiliations**: {', '.join(unique_affiliations) if unique_affiliations else 'Affiliations not available'}")
                    st.markdown(f"**Abstract**: {abstract_content}")
                    st.markdown(f"[🔗 View Abstract Online]({url})")
                    st.markdown(f"**Similarity Score**: `{score:.4f}`")
                    st.markdown("---")
        except Exception as e:
            st.error(f"An error occurred while fetching results: {e}")

st.markdown("---")
st.markdown(
    """
    ## Acknowledgments

    Special thanks to:
    - [EGU](https://www.egu.eu) for making abstracts publicly accessible.
    - [SentenceTransformers](https://www.sbert.net) and [FAISS](https://github.com/facebookresearch/faiss) for the amazing tools.
    """
)