import streamlit as st
import google.generativeai as genai
genai.configure(api_key=st.secrets["API_KEY"])
nontu_model = genai.GenerativeModel("gemini-2.5-flash")
st.title(" Feature List to Landing Page Copy")
product = st.text_input(" List of product features")
if st.button("Submit"):
    if product:
        prompt = f"Create persuasive landing page content for a {product} with these features"
        response = nontu_model.generate_content(prompt)
        st.markdown(response.text) 
else:
    st.warning("Create persuasive")

    
