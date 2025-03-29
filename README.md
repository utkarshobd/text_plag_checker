https://textplagchecker-bfpavftak2hpeygmptyo68.streamlit.app/
# Text Plagiarism Checker

This is a simple **Text Plagiarism Checker** application built using **Streamlit** and **NLTK**. The application compares two pieces of text and calculates the percentage of similarity between them. It also provides feedback based on the similarity percentage.

## Features
- Accepts two text inputs: the first text is treated as the primary reference, and the second text is compared against it.
- Calculates the **plagiarism percentage** based on the similarity of words between the two texts.
- Provides feedback:
  - If the plagiarism percentage is `100%`, it indicates that the second text is identical to the first.
  - If the plagiarism percentage is `<= 40%`, it indicates that the texts are significantly different.
- Saves the plagiarism percentage and matching words using **Pickle** for further use.

## Technologies Used
- **Python**: Core programming language.
- **Streamlit**: For building the web interface.
- **NLTK**: For text preprocessing and tokenization.
- **Pickle**: For saving results.

## Installation

### Prerequisites
- Python 3.12 or higher
- Conda or virtual environment (optional but recommended)


To clone the repository:
[   ```bash
   git clone https://github.com/<your-username>/<your-repository-name>.git
   cd <your-repository-name>](https://github.com/utkarshobd/text_plag_checker)
