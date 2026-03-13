import streamlit as st
from collections import Counter
import re

st.title("Document Analyzer")

st.write("**Upload two documents to analyze common words.**")

###### remove the puntuation from docs
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9]", " ", text)
    words = text.split()
    return words

file1 = st.file_uploader("**Upload Document 1**", type=["txt"])
file2 = st.file_uploader("**Upload Document 2**", type=["txt"])

if file1 and file2:
    text1 = file1.read().decode("utf-8")
    text2 = file2.read().decode("utf-8")

    words1 = clean_text(text1)
    words2 = clean_text(text2)

    ### count of each words in docs
    freq1 = Counter(words1)
    freq2 = Counter(words2)

    ### common words in both docs
    common_words = set(words1) & set(words2)

    ### Removing stop_words
    stop_words = {"is", "the", "it", "are", "and", "a", "an", "to", "in", "of", "for", "on", "with"}
    for word in stop_words:
        if word in common_words:
            common_words.remove(word)

    ### count of common word in both docs
    common_freq = {}
    for word in common_words:
        common_freq[word] = freq1[word] + freq2[word]

    ### top 10 common words
    top_words = sorted(common_freq.items(), key=lambda x: x[1], reverse=True)[:10]

    st.subheader("Most Common Words in Both Documents")
    for word, count in top_words:
        st.write(word, ":", count)

    keywords = [word for word, count in top_words[:5]]

    st.subheader("Analysis Note")

    st.write(
        "Both documents frequently discuss topics related to: \n"
        + ", ".join(keywords)
        + ". This suggests both documents focus mainly on these topics."
    )

############## fun work ##############
st.markdown("""
<style>
.stApp {
    background-color: #276CF5;
}
</style>
""", unsafe_allow_html=True)