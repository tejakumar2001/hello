import streamlit as st

# Custom CSS for styling
custom_css = """
<style>
    .stApp {
        background-color: #FFB6C1; /* Light pink background */
        color: #333333;
    }
    .header {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .header img {
        max-width: 100px; /* Adjust the width as needed */
        margin-right: 20px;
    }
    .header .title {
        font-size: 2em;
        font-weight: bold;
        color: #FF1493; /* Heavy pink color for the title text */
    }
    .button-css {
        background-color: white;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 10px 20px;
        margin: 5px;
        cursor: pointer;
        color: #FF1493;
    }
    .pink-text-input input {
        background-color: #FFB6C1; /* Light pink background */
        color: #FF1493; /* Pink text color */
        border: 1px solid #FF1493; /* Pink border color */
        border-radius: 5px;
        padding: 8px 12px;
    }
    .stSidebar {
        background-color: #FFB6C1; /* Light pink background */
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Sidebar logo
st.sidebar.image("C:/Users/91630/python/logo.png", caption="Logo", use_column_width=True, output_format="PNG")

# Title with image beside it
st.markdown("""
<div class='header'>
    <img src='C:/Users/91630/python/logo.png' alt='Logo'>
    <div class='title'>Go Pink: AI Can Think<br>ABOUT BREAST CANCER</div>
</div>
""", unsafe_allow_html=True)

# Prefilled questions and answers
questions = {
    "What are the early signs of breast cancer?": "The early signs of breast cancer include a lump in the breast, change in breast shape, dimpling of the skin, fluid coming from the nipple, and a red or scaly patch of skin.",
    "How can I perform a breast self-exam?": "To perform a breast self-exam, you should visually inspect your breasts for any changes, use your hands to feel for lumps or abnormalities in a systematic way, and repeat this process lying down.",
    "What treatment options are available for breast cancer?": "Treatment options for breast cancer include surgery, radiation therapy, chemotherapy, hormone therapy, targeted therapy, and immunotherapy. The choice of treatment depends on the stage and type of cancer.",
    "What are the risk factors for breast cancer?": "Risk factors for breast cancer include gender, age, family history of breast cancer, genetic mutations, personal health history, and lifestyle factors such as alcohol consumption and obesity.",
    "How can I reduce my risk of breast cancer?": "To reduce your risk of breast cancer, you can maintain a healthy weight, exercise regularly, limit alcohol intake, avoid smoking, and consider the risks of hormone replacement therapy."
}

# Simple questions and their answers
simple_questions_answers = {
    "What is breast cancer?": "Breast cancer is a disease in which cells in the breast grow out of control.",
    "Is breast cancer common?": "Yes, breast cancer is one of the most common cancers in women worldwide.",
    "Can men get breast cancer?": "Yes, men can get breast cancer, although it is much less common than in women.",
    "What is a mammogram?": "A mammogram is an X-ray picture of the breast used to detect early signs of breast cancer.",
    "When should I start getting mammograms?": "It is generally recommended to start getting mammograms at age 40, but you should discuss your specific risk factors with your doctor."
}

# Merging both prefilled and simple questions
all_questions = {**questions, **simple_questions_answers}

# Display prefilled questions with buttons
for question, answer in questions.items():
    if st.button(question, key=question):
        st.write(f"Answer: {answer}")

# Custom question input
custom_question = st.text_input("Go Pink AI can answer:", key="custom_question", help="Pink text input")
custom_answer = st.empty()

if st.button("Submit Custom Question"):
    if custom_question:
        if custom_question in all_questions:
            custom_answer.write(f"Answer: {all_questions[custom_question]}")
        else:
            custom_answer.write("No answer found for this question. Please try one of the prefilled questions.")
    else:
        st.write("Please type a question.")
