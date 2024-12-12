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
            st.Page("static/st-analysis.py", title="Sentiment Analysis"),
            st.Page("static/others.py", title="Others"),
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
