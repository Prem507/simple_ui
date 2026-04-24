# simple_ui
📄 Advanced NLP – Document Question Answering Web App

This project is an **AI-powered Document Question Answering System** that allows users to ask questions from multiple PDF documents through a **web interface**.

It uses **semantic search, FAISS vector database, and Streamlit UI** to retrieve the most relevant answers efficiently.

---

## 🚀 Features

- 📥 Extracts text from multiple PDF documents  
- ✂️ Splits text into sentences  
- 🧠 Uses **semantic chunking with overlap** for better context  
- 🧠 Generates embeddings using **Sentence Transformers**  
- ⚡ Stores embeddings in **FAISS vector database**  
- 🔍 Performs **fast similarity search**  
- 🌐 Interactive **Streamlit web interface**  
- 📊 Displays **Top-K (3) relevant answers with scores**  
- ⚡ Optimized using **Streamlit caching**  

---

## 🛠️ Technologies Used

- Python  
- Streamlit  
- Sentence Transformers  
- FAISS  
- NumPy  
- NLTK  
- PyPDF2  

---

## ⚙️ How It Works

1. Load PDF documents and extract text  
2. Split text into sentences  
3. Generate embeddings for each sentence  
4. Create **semantic chunks with overlap**:
   - Group similar sentences  
   - Add overlap for context continuity  
5. Convert chunks into embeddings  
6. Store embeddings in **FAISS index**  
7. Convert user query into embedding  
8. Retrieve **Top-K relevant chunks** using FAISS  
9. Display results in the **Streamlit UI**  

---

## ▶️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/Prem507/Advanced-NLP.git
cd Advanced-NLP
Install dependencies:
Bash
pip install streamlit nltk numpy faiss-cpu sentence-transformers PyPDF2 scikit-learn
Run the app:
Bash
streamlit run app.py
Open the browser and start asking questions.
💡 Example
Input:

What is leave policy?
Output:

1. Employees are entitled to leave as per company policy...
   Distance: 0.42

2. Leave rules are defined in the employee handbook...
   Distance: 0.55
📂 Project Structure

Advanced-NLP/
│── data/ (PDF files)
│── app.py
│── main.py
│── README.md
📈 Key Improvements
Keyword search → Semantic search (embeddings)
Fixed chunking → Semantic chunking + overlap
Linear search → FAISS vector search
CLI-based → Interactive web application (Streamlit)
📈 Future Improvements
Integrate LLM (OpenAI / Llama) → complete RAG system
Add source references (page number, document name)
Upload custom PDFs via UI
Improve UI/UX design
Deploy on Streamlit Cloud / AWS
👨‍💻 Author
Prem Chandh
Aspiring Generative AI Engineer
GitHub: https://github.com/Prem507⁠�
⭐ Summary
This project demonstrates how to build a scalable AI-powered document search system using semantic embeddings, FAISS, and a web interface—forming the foundation of real-world RAG applications.
