import streamlit as st
import re
import nltk
from nltk.tokenize import word_tokenize
import pickle

nltk.download('punkt')
nltk.download('punkt_tab')
def preprocess_and_tokenize(paragraph):
    cleaned_text = re.sub(r'[^A-Za-z\s]', '', paragraph).lower()
    words = word_tokenize(cleaned_text)
    return words

def calculate_similarity(paragraph1, paragraph2):
    words1 = preprocess_and_tokenize(paragraph1)
    words2 = preprocess_and_tokenize(paragraph2)
    matching_words = [word for word in words2 if word in words1]
    matching_count = len(matching_words)
    similarity_percentage = (matching_count / len(words2)) * 100
    return similarity_percentage, matching_words

st.title("Text Plagiarism Checker")
st.write("This application checks the similarity between two texts, where the first text is the primary one. The plagiarism is calculated as the percentage of similarity between the second text and the first text, i.e., how much of the second text is present in the first text .")
paragraph1 = st.text_area("**Enter the first text:**")
paragraph2 = st.text_area("**Enter the second text:**")

if st.button("Check Plagiarism"):
    if not paragraph1.strip() or not paragraph2.strip():
        st.warning("Please enter both paragraphs to check plagiarism.")
    else:
        similarity_percentage, matching_words = calculate_similarity(paragraph1, paragraph2)
        pickle.dump(similarity_percentage, open("similarity_percentage.pkl", "wb"))
        pickle.dump(matching_words, open("matching_words.pkl", "wb"))
        st.write(f"**Plagiarism Percentage:** {similarity_percentage:.2f}%")
        if similarity_percentage == 100:
            st.write(" Your's 100% text is avialable in first para .")
        elif similarity_percentage <=40:
            st.write("Both are different.")