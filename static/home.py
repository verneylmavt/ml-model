import streamlit as st

def run():
    st.title("Welcome to My ML Models Collection")
    st.write(
        """
        This application hosts a collection of machine learning models, allowing you to explore their functionality interactively.
        """
    )
    st.markdown(
        """
        **If you encounter any issues or errors**, please check the repository for troubleshooting:
        [GitHub Repository](https://github.com/verneylmavt/ml-model)
        """
    )
    st.write("Feel free to fork or clone the repository, install the requirements, and run the app locally if needed.")
    st.divider()
    st.info("Navigate through the app to explore various models and their features.")
    
run()