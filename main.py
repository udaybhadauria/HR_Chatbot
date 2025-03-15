# main.py

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Initialize the model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Example documents (replace with your actual documents)
documents = ["Document 1 text", "Document 2 text", "Document 3 text"]  # Replace with real documents

# Generate embeddings for the documents
document_embeddings = model.encode(documents)

# Create a FAISS index (using L2 distance metric for simplicity)
d = document_embeddings.shape[1]  # Get the embedding size (dimension)
index = faiss.IndexFlatL2(d)  # Create the FAISS index using L2 distance

# Add the document embeddings to the index
index.add(np.array(document_embeddings).astype(np.float32))

# Save the index to a file (make sure the path exists)
faiss.write_index(index, 'models/faiss_index.index')
