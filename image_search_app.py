import streamlit as st
import image_search_lib as glib
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Ensure the image database is initialized
if len(glib.image_database) == 0:
    from populate_image_collection import initialize_collection
    initialize_collection('images_with_embeddings.json')

st.set_page_config(page_title="Image Search", layout="wide")
st.title("Image Search")

search_images_tab, find_similar_images_tab = st.tabs(["Image search", "Find similar images"])

with search_images_tab:
    search_col_1, search_col_2 = st.columns(2)

    with search_col_1:
        input_text = st.text_input("Search for:")
        search_button = st.button("Search", type="primary")

    with search_col_2:
        if search_button:
            st.subheader("Results")
            with st.spinner("Searching..."):
                response_content = glib.get_similarity_search_results(search_term=input_text)
                
                for res in response_content:
                    st.image(res, width=250)

with find_similar_images_tab:
    find_col_1, find_col_2 = st.columns(2)

    with find_col_1:
        uploaded_file = st.file_uploader("Select an image", type=['png', 'jpg'])
        
        if uploaded_file:
            uploaded_image_preview = uploaded_file.getvalue()
            st.image(uploaded_image_preview)
    
        find_button = st.button("Find", type="primary")

    with find_col_2:
        if find_button and uploaded_file:
            st.subheader("Results")
            with st.spinner("Finding..."):
                response_content = glib.get_similarity_search_results(search_image=uploaded_file.getvalue())
                
                for res in response_content:
                    st.image(res, width=250)