import streamlit as st
import google.generativeai as genai

# Function to generate plant info
def generate_plant_info(query):
    try:
        genai.configure(api_key="AIzaSyD9UClG8tAdgNjWiGSyecdnjClSVerdskg")
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            system_instruction="You are an expert botanist. Answer user queries about plants.",
        )
        prompt = f"Answer the following query about plants: {query}."
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit UI
st.set_page_config(page_title="Plant Information Chatbot")

query = st.text_input("Enter your query:")
if st.button("Submit Query"):
    response_text = generate_plant_info(query)
    st.text_area("Response:", response_text, height=300)
