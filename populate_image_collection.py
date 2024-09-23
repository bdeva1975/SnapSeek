import json
import os
from image_search_lib import add_image_to_database, image_database, save_database
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def initialize_collection(source_json_file):
    global image_database
    if len(image_database) == 0:
        with open(source_json_file) as json_file:
            source_json = json.load(json_file)
            
            for item in source_json:
                add_image_to_database(item['document'])
        
        save_database(image_database)
    
    print(f"Initialized image database with {len(image_database)} images")

# Usage
if __name__ == "__main__":
    initialize_collection('images_with_embeddings.json')