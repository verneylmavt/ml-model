import streamlit as st

# ----------------------
# Navigation Setup
# ----------------------
def main():
    pages = {
        "Home": [
            st.Page("static/home.py", title="Home")
        ],
        "Models": [
            st.Page("static/nn-text_analysis.py", title="Sentiment Analysis"),
            st.Page("static/regression-food_security.py", title="Regression Food Security"),
        ],
    }
    
    page = st.navigation(
        pages,
        position="sidebar",
        expanded=False
    )
    page.run()

if __name__ == "__main__":
    main()
