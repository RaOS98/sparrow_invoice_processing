import os
from embeddings.agents.llamaindex import LlamaIndexIngest

def ingest_multiple_pdfs(pdf_directory, index_name):
    # Initialize the LlamaIndexIngest class
    ingest = LlamaIndexIngest()

    # Check if the directory exists
    if not os.path.isdir(pdf_directory):
        print(f"Directory does not exist: {pdf_directory}")
        return

    # Iterate over all PDF files in the directory
    for pdf_file in os.listdir(pdf_directory):
        if pdf_file.lower().endswith(".pdf"):
            pdf_path = os.path.join(pdf_directory, pdf_file)
            print(f"Processing file: {pdf_path}")
            
            # Run the ingestion process for each PDF file
            try:
                ingest.run_ingest(payload="", file_path=pdf_path, index_name=index_name)
            except Exception as e:
                print(f"Failed to process file {pdf_path}: {e}")

# Define the directory containing your PDF files and the index name
# Using Unix-style path for WSL
pdf_directory = "/mnt/c/Users/Renzo/Desktop/Coding/sparrow_invoice_processing/sparrow-ml/llm/data"
index_name = "InvoiceIndex"

# Run the ingestion process for all PDF files in the directory
ingest_multiple_pdfs(pdf_directory, index_name)
