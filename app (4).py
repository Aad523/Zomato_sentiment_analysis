import streamlit as st
import pickle

# Load trained model
with open("sentiment_model.pkl", "rb") as f:
    model = pickle.load(f)

# App title
st.title("🍽️ Zomato Review Sentiment Analysis")

st.write("Enter a Zomato food review and predict its sentiment")

# Text input
review = st.text_area("✍️ Enter your review here:")

# Button
if st.button("Predict Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review")
    else:
        prediction = model.predict([review])[0]

        if prediction == "positive":
            st.success("😊 Positive Review")
        elif prediction == "neutral":
            st.info("😐 Neutral Review")
        else:
            st.error("😡 Negative Review")
            
            