import streamlit as st
import nltk
from app import main

# Baixar recursos necessários do NLTK
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
    nltk.data.find('corpora/wordnet')
    print("Recursos NLTK já estão disponíveis.")
except LookupError:
    print("Baixando recursos NLTK...")
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    print("Recursos NLTK baixados com sucesso!")

# Executar a aplicação principal
if __name__ == "__main__":
    main()
