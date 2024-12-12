import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
        .main-title {
            font-size: 2.8rem;
            font-weight: bold;
            text-align: center;
            color: #86e0ff;
        }
        .sub-text {
            font-size: 1.2rem;
            color: #555;
            text-align: center;
        }
        .github-link {
            font-size: 1rem;
            font-weight: bold;
            text-align: center;
            color: #FF5722;
        }
        .footer {
            margin-top: 2rem;
            text-align: center;
            font-size: 0.9rem;
            color: #777;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def run():
    st.markdown("<div class='main-title'>Welcome to My ML Models Collection</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='sub-text'>This application hosts a collection of machine learning models, allowing you to explore their functionality interactively.</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div style="text-align: center; margin-top: 20px;">
            <a href="https://github.com/verneylmavt/ml-model" target="_blank" class="github-link">
                *If you encounter any issues, please check my GitHub repository.*
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )
    # st.markdown(
    #     "<div style='text-align: center; margin-top: 20px;'>Feel free to fork or clone the repository, install the requirements, and run the app locally if needed.</div>",
    #     unsafe_allow_html=True,
    # )
    st.divider()

    st.info("Navigate through the app to explore various models and their features.", icon="💡")

    # Footer with branding
    st.markdown(
        """
        <div class="footer">
            Designed with ❤️ using Streamlit.
        </div>
        """,
        unsafe_allow_html=True,
    )
run()


# def run():
#     st.title("Welcome to My ML Models Collection")
#     st.write(
#         """
#         This application hosts a collection of machine learning models, allowing you to explore their functionality interactively.
#         """
#     )
#     st.markdown(
#         """
#         **If you encounter any issues or errors**, please check the repository for troubleshooting:
#         [GitHub Repository](https://github.com/verneylmavt/ml-model)
#         """
#     )
#     st.write("Feel free to fork or clone the repository, install the requirements, and run the app locally if needed.")
#     st.divider()
#     st.info("Navigate through the app to explore various models and their features.")
    
# run()