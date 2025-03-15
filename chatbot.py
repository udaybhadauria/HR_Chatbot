# chatbot.py

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load the pre-trained model (ensure this model is already installed in your environment)
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Load the FAISS index (adjust the path if necessary)
index = faiss.read_index('models/faiss_index.index')  # Ensure the path is correct

# Example documents (make sure these match the ones used for indexing)
documents = ["Company working hours are from 9 AM to 6 PM.",
             "Company holiday schedule: 1st Jan, 25th Dec.",
             "Company’s office is located at XYZ Street."]  # This should be your actual documents

def generate_response(query):
    """
    Function to generate a response based on the FAISS index.
    """
    # Generate the embedding for the query
    query_embedding = model.encode([query])  # Model generates embeddings for the query
    
    # Perform FAISS search
    D, I = index.search(np.array(query_embedding).astype(np.float32), k=1)  # Search for nearest neighbors
    
    # Retrieve the document using the index returned by FAISS
    retrieved_document = documents[I[0][0]]  # Get the document based on the index returned from FAISS
    
    return retrieved_document
