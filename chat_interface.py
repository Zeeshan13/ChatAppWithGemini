import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel

# Ensure Vertex AI is properly initialized
def initialize_vertex_ai():
    # Adjust based on actual initialization requirements
    project = "avid-folder-433719-s3"
    config = generative_models.GenerationConfig(temperature=0.8)
    model = GenerativeModel("gemini-pro", generation_config=config)
    chat = model.start_chat()
    return chat

# Create chat instance
chat = initialize_vertex_ai()

def llm_function(user_input, chat):
    try:
        response = chat.send_message(user_input)
        return user_input, response.text
    except Exception as e:
        st.error(f"Error communicating with the model: {e}")
        return user_input, "Error: Unable to get response."

def display_chat_interface():
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Initialize initial message if chat history is empty
    if len(st.session_state.messages) == 0:
        initial_prompt = "Introduce yourself as ReX, an assistant powered by Google Gemini. You use emojis to be interactive."
        llm_function(initial_prompt, chat)

    # Display chat history
    for i, message in enumerate(st.session_state.messages):
        key = f"{message['role']}_{i}"
        if message["role"] == "user":
            st.text_area("You:", value=message["content"], height=50, key=key)
        else:
            st.text_area("Gemini:", value=message["content"], height=50, key=key)

    # Emoji picker
    if st.button("😊"):
        st.session_state.emoji_open = not st.session_state.get('emoji_open', False)

    if st.session_state.get('emoji_open', False):
        emojis = ["😊", "😂", "😍", "😢", "😡"]
        selected_emoji = st.selectbox("Choose an emoji", emojis)
        st.session_state.user_input += selected_emoji

    # User input box
    user_input = st.text_input("You: ", st.session_state.get('user_input', ""))

    if st.button("Send"):
        if user_input:
            user_message, llm_response = llm_function(user_input, chat)
            st.session_state.messages.append({"role": "user", "content": user_message})
            st.session_state.messages.append({"role": "gemini", "content": llm_response})
            st.session_state.user_input = ""
            st.experimental_rerun()
        else:
            st.warning("Please enter a message to send.")
