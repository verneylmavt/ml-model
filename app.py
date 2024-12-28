import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
        .main-title {
            font-size: 2.8rem;
            font-weight: bold;
            text-align: center;
            color: #ffffff;
        }
        .sub-text {
            font-size: 1.2rem;
            color: #555;
            text-align: center;
        }
        .github-link {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        .footer {
            margin-top: 2rem;
            text-align: center;
            font-size: 0.9rem;
            color: #777;
        }
        .custom-link {
            font-size: 1.1rem;
            text-align: center;
            display: block; /* Ensures each link appears on a new line */
            margin: 10px 0; /* Adds spacing between links */
            color: #007BFF;
            text-decoration: none;
        }
        .custom-link:hover {
            color: #0056b3;
            text-decoration: underline;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    st.markdown("<div class='main-title'>ML Models Collection</div>", unsafe_allow_html=True)
    # st.markdown(
    #     "<div class='sub-text'>This application hosts a collection of machine learning models, allowing you to explore their functionality interactively.</div>",
    #     unsafe_allow_html=True,
    # )
    st.divider()
    st.markdown(
        """
        <div style="text-align: center;">
            <a href="https://verneylogyt-snt-analysis.streamlit.app/" target="_blank" class="custom-link">
                Sentiment Analysis
            </a>
            <a href="https://verneylogyt-pos-tagging.streamlit.app/" target="_blank" class="custom-link">
                POS Tagging
            </a>
            <a href="https://verneylogyt-nli.streamlit.app/" target="_blank" class="custom-link">
                Natural Language Inference (NLI)
            </a>
            <a href="https://verneylogyt-sn-parsing.streamlit.app/" target="_blank" class="custom-link">
                Syntactic Parsing
            </a>
            <a href="https://verneylogyt-sm-parsing.streamlit.app/" target="_blank" class="custom-link">
                Semantic Parsing
            </a>
            <a href="https://verneylogyt-ner.streamlit.app/" target="_blank" class="custom-link">
                Named Entity Recognition (NER)
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.divider()
    st.markdown(
        """
        <div style="text-align: center;">
            <a href="https://verneylogyt-mov-recsys.streamlit.app/" target="_blank" class="custom-link">
                Movie Recommender System
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.divider()
    st.markdown(
        """
        <div class="github-link">
            <a href="https://github.com/verneylmavt/ml-model" target="_blank">
                <img src="https://img.shields.io/badge/GITHUB PAGES-ffffff?style=for-the-badge&logo=github&logoColor=black"/>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        """
        <div class="footer">
            Designed with ❤️ using Streamlit.
        </div>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()