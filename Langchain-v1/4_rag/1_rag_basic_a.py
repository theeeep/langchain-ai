import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

# Define the folder path and the persist_directory
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "documents", "Dracula.txt")
persistent_directory = os.path.join(current_dir, "db", "chroma_db")

# Check if the Chroma vector store already exists
if not os.path.exists(persistent_directory):
    print("Persisting Chroma vector store doesn't exitst. Initializing...")

    # Ensure the text file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    # Load the text file
    loader = TextLoader(file_path)
    documents = loader.load()

    # Split the documents into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)

    # Display information about the loaded documents
    print("\n--- Document Chunks Information ---")
    print(f"Loaded {len(docs)} documents.")
    print(f"Sample Chunk: \n{docs[0].page_content}...\n")

    # Create Embeddings
    print("\n--- Creating embeddings ---")
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )  # Update to a valid embedding model if needed
    print("\n--- Finished creating embeddings ---")

    # Create a Chroma vector store
    print("\n--- Creating Chroma vector store ---")
    db = Chroma.from_documents(docs, embeddings, persist_directory=persistent_directory)
    print("\n--- Finished creating Chroma vector store ---")

else:
    print("Chroma vector store already exists. Loading...")
    db = Chroma(
        persist_directory=persistent_directory, embedding_function=OpenAIEmbeddings()
    )
