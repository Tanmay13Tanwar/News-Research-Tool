from sentence_transformers import SentenceTransformer
import numpy as np



# Load the extracted text content
with open("extracted_content.txt", "r", encoding="utf-8") as file:
    extracted_content = file.read()

# Load the Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create embeddings for the extracted content
embeddings = model.encode(extracted_content, show_progress_bar=True)

# Save the embeddings to a file (optional)
np.save("content_embeddings.npy", embeddings)

print("Embeddings created and saved successfully.")