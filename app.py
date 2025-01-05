import streamlit as st
from streamlit_extras.mention import mention

# st.markdown(
#     """
#     <style>
#         .main-title {
#             font-size: 2.8rem;
#             font-weight: bold;
#             text-align: center;
#             color: #ffffff;
#         }
#         .sub-text {
#             font-size: 1.2rem;
#             color: #555;
#             text-align: center;
#         }
#         .github-link {
#             display: flex;
#             justify-content: center;
#             margin-top: 20px;
#         }
#         .footer {
#             margin-top: 2rem;
#             text-align: center;
#             font-size: 0.9rem;
#             color: #777;
#         }
#         .custom-link {
#             font-size: 1.1rem;
#             text-align: center;
#             display: block; /* Ensures each link appears on a new line */
#             margin: 10px 0; /* Adds spacing between links */
#             color: #007BFF;
#             text-decoration: none;
#         }
#         .custom-link:hover {
#             color: #0056b3;
#             text-decoration: underline;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
st.markdown(
    """
    <style>
    .main-title {
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 2.8rem;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def main():
    st.markdown(
    "<div class='main-title'><a href='https://github.com/verneylmavt/ml-model' target='_blank'>ML Models Collection 📦</a></div>",
    unsafe_allow_html=True
    )
    st.divider()
    # st.title("ML Models Collection 📦")
    # st.markdown(
    #     "<div class='sub-text'>This application hosts a collection of machine learning models, allowing you to explore their functionality interactively.</div>",
    #     unsafe_allow_html=True,
    # )
    # st.divider()
    # st.markdown(
    #     """
    #     <div style="text-align: center;">
    #         <a href="https://verneylogyt-snt-analysis.streamlit.app/" target="_blank" class="custom-link">
    #             Sentiment Analysis
    #         </a>
    #         <a href="https://verneylogyt-pos-tagging.streamlit.app/" target="_blank" class="custom-link">
    #             POS Tagging
    #         </a>
    #         <a href="https://verneylogyt-nli.streamlit.app/" target="_blank" class="custom-link">
    #             Natural Language Inference (NLI)
    #         </a>
    #         <a href="https://verneylogyt-sn-parsing.streamlit.app/" target="_blank" class="custom-link">
    #             Syntactic Parsing
    #         </a>
    #         <a href="https://verneylogyt-sm-parsing.streamlit.app/" target="_blank" class="custom-link">
    #             Semantic Parsing
    #         </a>
    #         <a href="https://verneylogyt-ner.streamlit.app/" target="_blank" class="custom-link">
    #             Named Entity Recognition (NER)
    #         </a>
    #     </div>
    #     """,
    #     unsafe_allow_html=True,
    # )
    st.subheader("Natural Language Processing (NLP)", divider="grey")
    
    snt_analysis_1, snt_analysis_2 = st.columns(2)
    with snt_analysis_1:
        mention(
            label="Sentiment Analysis",
            icon="streamlit",
            url="https://verneylogyt-snt-analysis.streamlit.app/"
        )
    with snt_analysis_2:
        mention(
            label="verneylmavt/st-snt-analysis",
            icon="github",
            url="https://github.com/verneylmavt/st-snt-analysis"
        )
        
    pos_tagging_1, pos_tagging_2 = st.columns(2)
    with pos_tagging_1:
        mention(
            label="POS Tagging",
            icon="streamlit",
            url="https://verneylogyt-pos-tagging.streamlit.app/"
        )
    with pos_tagging_2:
        mention(
            label="verneylmavt/st-pos-tagging",
            icon="github",
            url="https://github.com/verneylmavt/st-pos-tagging"
        )
    
    nli_1, nli_2 = st.columns(2)
    with nli_1:
        mention(
            label="Natural Language Inference (NLI)",
            icon="streamlit",
            url="https://verneylogyt-nli.streamlit.app/"
        )
    with nli_2:
        mention(
            label="verneylmavt/st-nli",
            icon="github",
            url="https://github.com/verneylmavt/st-nli"
        )
    
    sn_parsing_1, sn_parsing_2 = st.columns(2)
    with sn_parsing_1:
        mention(
            label="Syntactic Parsing",
            icon="streamlit",
            url="https://verneylogyt-sn-parsing.streamlit.app/"
        )
    with sn_parsing_2:
        mention(
            label="verneylmavt/st-sn-parsing",
            icon="github",
            url="https://github.com/verneylmavt/st-sn-parsing"
        )
    
    sm_parsing_1, sm_parsing_2 = st.columns(2)
    with sm_parsing_1:
        mention(
            label="Semantic Parsing",
            icon="streamlit",
            url="https://verneylogyt-sm-parsing.streamlit.app/"
        )
    with sm_parsing_2:
        mention(
            label="verneylmavt/st-sm-parsing",
            icon="github",
            url="https://github.com/verneylmavt/st-sm-parsing"
        )
    
    ner_1, ner_2 = st.columns(2)
    with ner_1:
        mention(
            label="Named Entity Recognition (NER)",
            icon="streamlit",
            url="https://verneylogyt-ner.streamlit.app/"
        )
    with ner_2:
        mention(
            label="verneylmavt/st-ner",
            icon="github",
            url="https://github.com/verneylmavt/st-ner"
        )
        
        
    st.subheader("Others", divider="grey")
    mov_recsys_1, mov_recsys_2 = st.columns(2)
    with mov_recsys_1:
        mention(
            label="Movie Recommender System",
            icon="streamlit",
            url="https://verneylogyt-mov-recsys.streamlit.app/"
        )
    with mov_recsys_2:
        mention(
            label="verneylmavt/st-mov-recsys",
            icon="github",
            url="https://github.com/verneylmavt/st-mov-recsys"
        )
    sn_dgt_recognition_1, sn_dgt_recognition_2 = st.columns(2)
    with sn_dgt_recognition_1:
        mention(
            label="Single Digit Recognition",
            icon="streamlit",
            url="https://verneylogyt-sn-dgt-recognition.streamlit.app/"
        )
    with sn_dgt_recognition_2:
        mention(
            label="verneylmavt/st-sn-dgt-recognition",
            icon="github",
            url="https://github.com/verneylmavt/st-sn-dgt-recognition"
        )
    nba_vis_1, nba_vis_2 = st.columns(2)
    with nba_vis_1:
        mention(
            label="Single Digit Recognition",
            icon="streamlit",
            url="https://verneylogyt-nba-vis.streamlit.app/"
        )
    with nba_vis_2:
        mention(
            label="verneylmavt/st-nba-vis",
            icon="github",
            url="https://github.com/verneylmavt/st-nba-vis"
        )
        
    # st.divider()
    # st.info("If you encounter message 'This app has gone to sleep due to inactivity', click 'Yes, get this app back up!' button to wake the app back up.")    
    
    # st.divider()
    # st.markdown(
    #     """
    #     <div style="text-align: center;">
    #         <a href="https://verneylogyt-mov-recsys.streamlit.app/" target="_blank" class="custom-link">
    #             Movie Recommender System
    #         </a>
    #     </div>
    #     """,
    #     unsafe_allow_html=True,
    # )
    # st.divider()
    # st.markdown(
    #     """
    #     <div class="github-link">
    #         <a href="https://github.com/verneylmavt/ml-model" target="_blank">
    #             <img src="https://img.shields.io/badge/GITHUB PAGES-ffffff?style=for-the-badge&logo=github&logoColor=black"/>
    #         </a>
    #     </div>
    #     """,
    #     unsafe_allow_html=True,
    # )
    
    # st.markdown(
    #     """
    #     <div class="footer">
    #         Designed with ❤️ using Streamlit.
    #     </div>
    #     """,
    #     unsafe_allow_html=True,
    # )

if __name__ == "__main__":
    main()