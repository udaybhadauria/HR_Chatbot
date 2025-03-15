import os
from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS
from document_loader import extract_text_from_pdf
import faiss
import numpy as np

# Function to create a FAISS index from the documents
def create_faiss_index(documents):
    # Initialize SentenceTransformer for generating embeddings
    model = SentenceTransformer('all-MiniLM-L6-v2')  # You can change this to any other model
    
    # Generate embeddings for each document
    embeddings = model.encode(documents)
    
    # Convert embeddings into numpy array (FAISS works with numpy arrays)
    embeddings_np = np.array(embeddings).astype('float32')
    
    # Initialize FAISS index (using a simple Flat index here, you can use other FAISS index types)
    index = faiss.IndexFlatL2(embeddings_np.shape[1])  # L2 distance for similarity search
    
    # Add embeddings to the FAISS index
    index.add(embeddings_np)
    
    # Create a FAISS object with the embedding function, index, docstore, and index_to_docstore_id
    faiss_index = FAISS(
        embedding_function=model.encode,   # Embedding function for future searches
        index=index,                       # The FAISS index itself
        docstore=None,                     # We don't need a docstore for now
        index_to_docstore_id=None          # This maps index entries to documents if needed
    )
    
    return faiss_index

# Function to save the FAISS index to a file
def save_faiss_index(faiss_index, index_path="models/faiss_index.index"):
    # Save the FAISS index to disk
    faiss.write_index(faiss_index.index, index_path)
    print(f"FAISS index saved to {index_path}")
