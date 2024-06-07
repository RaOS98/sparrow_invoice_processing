import weaviate
import box
import yaml

def delete_weaviate_index(index_name):
    # Import config vars
    with open('config.yml', 'r', encoding='utf8') as ymlfile:
        cfg = box.Box(yaml.safe_load(ymlfile))

    # Connect to Weaviate
    client = weaviate.Client(cfg.WEAVIATE_URL)
    
    # Delete the specified index
    try:
        client.schema.delete_class(index_name)
        print(f"Index '{index_name}' deleted successfully.")
    except weaviate.exceptions.UnexpectedStatusCodeException as e:
        print(f"Failed to delete index '{index_name}'. Error: {e}")

# Specify the index name to delete
index_name = "InvoiceIndex"

# Run the deletion
delete_weaviate_index(index_name)
