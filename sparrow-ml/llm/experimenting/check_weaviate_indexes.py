import weaviate
import box
import yaml

def list_weaviate_indexes():
    # Import config vars
    with open('config.yml', 'r', encoding='utf8') as ymlfile:
        cfg = box.Box(yaml.safe_load(ymlfile))

    # Connect to Weaviate
    client = weaviate.Client(cfg.WEAVIATE_URL)
    
    # Retrieve the schema
    schema = client.schema.get()
    
    # List the class names (indexes)
    if 'classes' in schema:
        print("Existing indexes in Weaviate:")
        for class_schema in schema['classes']:
            print(f" - {class_schema['class']}")
    else:
        print("No indexes found in Weaviate.")

# Run the listing function
list_weaviate_indexes()
