# SnapSeek

SnapSeek is an AI-powered image search tool that allows users to find visuals using text or image inputs. It understands context for precise results, making it perfect for designers, researchers, and anyone needing quick, accurate image discovery.

## Features

- **Text-based Image Search**: Find images by describing them in natural language.
- **Image-based Search**: Upload an image to find similar ones in the database.
- **AI-powered Understanding**: Utilizes OpenAI's advanced models to understand context and nuance in search queries.
- **Efficient Indexing**: Creates a searchable index of images for quick retrieval.
- **User-friendly Interface**: Built with Streamlit for a smooth, interactive experience.

## How It Works

SnapSeek creates a searchable index of images by:

1. Reading each image file in a specified directory.
2. Using OpenAI's multimodal model to generate a numerical representation (embedding) of each image.
3. Saving the embedding and metadata (including the path to the original image file) to a local JSON database.

When searching for images, SnapSeek:

1. Converts the user's search expression or uploaded image to a numerical representation using the same AI model.
2. Searches the database for the closest matches using vector similarity.
3. Returns and displays the closest matching images.

## Use Cases

SnapSeek is ideal for:

- Image collection search
- Finding similar or identical images in a collection
- Classifying images based on similarity to existing examples
- Streamlining visual asset management for designers and content creators
- Enhancing research processes that rely on image analysis

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/bdeva1975/snapseek.git
   cd snapseek
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key:
   Create a `.env` file in the project root and add your API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

5. Prepare your image collection:
   Place your images in a directory, then update the `images_with_embeddings.json` file with the paths to your images.

## Usage

1. Run the Streamlit app:
   ```
   streamlit run image_search_app.py
   ```

2. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

3. To search for images using text:
   - Go to the "Image search" tab.
   - Enter your search query in the text box.
   - Click the "Search" button.

4. To find similar images:
   - Go to the "Find similar images" tab.
   - Upload an image file.
   - Click the "Find" button.

5. View the results displayed on the right side of the interface.

## Project Structure

- `image_search_app.py`: Main Streamlit application file.
- `image_search_lib.py`: Core functionality for image embedding and searching.
- `populate_image_collection.py`: Script to initialize the image database.
- `image_database.json`: JSON file storing image embeddings and metadata (please create your own)
- `images_with_embeddings.json`: JSON file containing paths to your image collection (please create your own)

## Contributing

We welcome contributions to SnapSeek! Here's how you can help:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/AmazingFeature`).
3. Make your changes and commit them (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

Please make sure to update tests as appropriate and adhere to the existing coding style.

## License

Distributed under the MIT License. See `LICENSE` file for more information.

## Acknowledgements

- [OpenAI](https://www.openai.com/) for providing the AI models used in this project.
- [Streamlit](https://streamlit.io/) for the user interface framework.

## Contact

Your Name - [@your_twitter](https://twitter.com/your_twitter) - email@example.com

Project Link: [https://github.com/yourusername/snapseek](https://github.com/yourusername/snapseek)
