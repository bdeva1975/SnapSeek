import os
import base64
import json
from io import BytesIO
from openai import OpenAI
from PIL import Image
import numpy as np
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# File to store the image database
DATABASE_FILE = 'image_database.json'

# Load the database from file or initialize an empty one
def load_database():
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, 'r') as f:
            return json.load(f)
    return []

# Save the database to file
def save_database(database):
    with open(DATABASE_FILE, 'w') as f:
        json.dump(database, f)

# Initialize the database
image_database = load_database()

def get_multimodal_vector(input_image=None, input_text=None):
    if input_image:
        # Resize and convert image to base64
        img = Image.open(BytesIO(input_image)).convert('RGB')
        img = img.resize((512, 512))
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Describe this image in detail."},
                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_str}"}}
                    ],
                }
            ],
            max_tokens=300,
        )
        input_text = response.choices[0].message.content

    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=input_text,
    )
    return response.data[0].embedding

def add_image_to_database(image_path):
    global image_database
    with open(image_path, "rb") as f:
        img = f.read()
    embedding = get_multimodal_vector(input_image=img)
    image_database.append({"path": image_path, "embedding": embedding})
    save_database(image_database)

def get_vector_search_results(query_embedding, n_results=4):
    similarities = []
    for item in image_database:
        similarity = np.dot(query_embedding, item["embedding"])
        similarities.append((similarity, item["path"]))
    
    similarities.sort(reverse=True)
    return [path for _, path in similarities[:n_results]]

def get_similarity_search_results(search_term=None, search_image=None):
    if search_image:
        query_embedding = get_multimodal_vector(input_image=search_image)
    else:
        query_embedding = get_multimodal_vector(input_text=search_term)
    
    results = get_vector_search_results(query_embedding)
    
    results_images = []
    for res in results:
        with open(res, "rb") as f:
            img = BytesIO(f.read())
        results_images.append(img)
    
    return results_images

# Initialize the database when the module is imported
if not image_database:
    print("Initializing image database...")
    from populate_image_collection import initialize_collection
    initialize_collection('images_with_embeddings.json')
    image_database = load_database()
    print(f"Initialized image database with {len(image_database)} images")