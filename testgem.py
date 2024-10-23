import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel
import concurrent.futures

# Set up the project
project = "avid-folder-433719-s3"
vertexai.init(project=project)

# Streamlit interface
st.title("AI Chat App powered by Gemini")

# Display loading spinner while model is being initialized
with st.spinner('Loading AI model...'):
    try:
        # Load and start the model
        config = generative_models.GenerationConfig(temperature=0.8)
        model = GenerativeModel("gemini-pro", generation_config=config)
        chat = model.start_chat()
        st.success("Model loaded successfully!")
        st.write("Checkpoint 1: Model loaded.")
    except Exception as e:
        st.error(f"Failed to load AI model: {e}")
        st.stop()  # Stop execution if the model fails to load

# Debugging: Log the chat state
st.write("Checkpoint 2: Ready to interact with model.")

def llm_function(user_input, chat, timeout=10):
    """
    This function interacts with the LLM and returns the response.
    It also appends the user input and LLM response to the chat history.
    """
    try:
        # Use a timeout to prevent the app from hanging indefinitely
        st.write(f"Checkpoint 3: Sending message: {user_input}")
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(chat.send_message, user_input)
            response = future.result(timeout=timeout)  # Wait for the response or timeout
        st.write("Checkpoint 4: Received response.")
        return user_input, response.text
    except concurrent.futures.TimeoutError:
        st.error("The AI model took too long to respond. Please try again
