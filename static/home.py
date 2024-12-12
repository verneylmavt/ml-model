import streamlit as st

def run():
    st.title("Welcome to My Machine Learning Models Collection")
    st.write("""
        ## Overview
        This website is a collection of machine learning models developed by **Elvern Neylmav T**. 
        Each page represents a different model with its unique functionalities and capabilities.

        ## Available Models
        - **HybridCNNRNN200:** A hybrid Convolutional Neural Network and Recurrent Neural Network model for sentiment analysis.
        - **Another Model:** (Coming Soon) Description of another machine learning model.

        ## How to Use
        Navigate to the **Models** section using the sidebar to access and interact with each model.
    """)
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=300)

run()