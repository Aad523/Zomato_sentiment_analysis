import streamlit as st
import pickle

# Load model
with open("sentiment_model.pkl", "rb") as f:
    model = pickle.load(f)

# Page config
st.set_page_config(
    page_title="Zomato Sentiment Analysis",
    page_icon="🍽️",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

/* FULL PAGE BACKGROUND */
html, body, [class*="css"] {
    background-color: #0e1117 !important;
    color: #ffffff;
}

/* MAIN CONTAINER */
.main {
    background-color: #0e1117;
    padding: 2rem;
}

/* REMOVE WHITE BLOCKS */
section[data-testid="stSidebar"],
div[data-testid="stAppViewContainer"],
div[data-testid="stHeader"],
div[data-testid="stToolbar"] {
    background-color: #0e1117 !important;
}

/* TITLE */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #ffffff;
}

/* SUBTITLE */
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #cfcfcf;
    margin-bottom: 30px;
}

/* TEXT AREA */
textarea {
    background-color: #1c1f26 !important;
    color: white !important;
    border-radius: 10px;
    border: 1px solid #333;
}

/* BUTTON */
.stButton > button {
    background-color: #ff4b4b;
    color: white;
    font-size: 16px;
    border-radius: 8px;
    padding: 0.6rem 1.2rem;
}
.stButton > button:hover {
    background-color: #ff2b2b;
}

/* RESULT CARD */
.result {
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    padding: 18px;
    border-radius: 12px;
    margin-top: 25px;
}

.positive {
    background-color: #1f7a1f;
}

.neutral {
    background-color: #b38f00;
}

.negative {
    background-color: #a11a1a;
}

</style>
""", unsafe_allow_html=True)

# App UI
st.markdown('<div class="title">🍽️ Zomato Review Sentiment Analysis</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter a food review and find out the sentiment</div>', unsafe_allow_html=True)

review = st.text_area("✍️ Write your review here:", height=120)

if st.button("🔍 Predict Sentiment"):
    if review.strip() == "":
        st.warning("⚠️ Please enter a review first!")
    else:
        prediction = model.predict([review])[0]

        if prediction.lower() == "positive":
            st.markdown('<div class="result positive">😊 Positive Review</div>', unsafe_allow_html=True)
        elif prediction.lower() == "neutral":
            st.markdown('<div class="result neutral">😐 Neutral Review</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result negative">😞 Negative Review</div>', unsafe_allow_html=True)
