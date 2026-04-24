import streamlit as st
import asyncio
import PyPDF2
import nltk
import numpy as np
import faiss

from nltk.tokenize import sent_tokenize
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

files = [
    r"D:\Desktop\CSV\AnnualHealthCheck.pdf",
    r"D:\Desktop\CSV\LeavePolicy.pdf",
    r"D:\Desktop\CSV\NoticePeriod.pdf",
    r"D:\Desktop\CSV\OfficeTime.pdf",
    r"D:\Desktop\CSV\Separation.pdf",
    r"D:\Desktop\CSV\Travel.pdf",
    r"D:\Desktop\CSV\USA_Employee_Handbook-Freely_Available.pdf"
]

@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

@st.cache_data
def load_data():
    model = load_model()
    documents = []
    for file in files:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        documents.append(text)

    sentences = []
    for doc in documents:
        sentences.extend(sent_tokenize(doc))

    sentence_embeddings = model.encode(sentences, show_progress_bar=False)

    similarity_threshold = 0.7
    overlap_size = 1
    chunks = []
    current_chunk = [sentences[0]]

    for i in range(1, len(sentences)):
        sim = cosine_similarity([sentence_embeddings[i-1]], [sentence_embeddings[i]])[0][0]
        if sim > similarity_threshold:
            current_chunk.append(sentences[i])
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = current_chunk[-overlap_size:] + [sentences[i]]

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    chunk_embeddings = model.encode(chunks, show_progress_bar=False)
    embeddings = np.array(chunk_embeddings).astype("float32")
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    return chunks, index

# ---- UI ----
st.title("Document Q&A")

with st.spinner("Loading..."):
    chunks, index = load_data()

st.write("Ask a question from the documents below.")

query = st.text_input("Your Question:")

if st.button("Get Answer") and query:
    model = load_model()
    query_vector = np.array(model.encode([query])).astype("float32")
    distances, indices = index.search(query_vector, 3)

    st.subheader("Answers:")
    for i, idx in enumerate(indices[0]):
        st.write(f"**{i+1}.** {chunks[idx]}")
        st.caption(f"Distance: {distances[0][i]:.4f}")
        st.divider()
