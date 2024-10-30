import streamlit as st
import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel
import requests
from PIL import Image
from io import BytesIO

# Initialize the Vertex AI project
project = "avid-folder-433719-s3"
vertexai.init(project=project)

# Load and start the model
config = generative_models.GenerationConfig(temperature=0.8)
model = GenerativeModel("gemini-pro", generation_config=config)
chat = model.start_chat()

def llm_function(user_input):
    """
    Interacts with the LLM and returns the response.
    """
    response = chat.send_message(user_input)
    return user_input, response.text

#def fetch_background_image():
    """
    Fetches a background image from Bing and returns it as a URL.
    """
    url = "https://www.bing.com/th?id=OHR.SunsetStream_EN-US0547403224_1920x1080.jpg"  # Example URL
    return url

def display_emoji_tray():
    """
    Displays an emoji tray that appears when the attachment icon is clicked.
    """
    if 'show_emoji_tray' not in st.session_state:
        st.session_state.show_emoji_tray = False

    attachment_clicked = st.button("📎")  # Create attachment button

    if attachment_clicked:
        st.session_state.show_emoji_tray = not st.session_state.show_emoji_tray

    if st.session_state.show_emoji_tray:
        st.write("Click an emoji to add it to your message:")
        
        emoji_list = ['😊', '😂', '❤️', '👍', '🔥', '🎉', '💡', '💬', '😎', '🙌']
        
        cols = st.columns(len(emoji_list))
        for i, emoji in enumerate(emoji_list):
            if cols[i].button(emoji):
                st.session_state.emoji_input += emoji

# Set up the background image
#background_image_url = fetch_background_image()
#st.markdown(f"""
#    <style>
#        .stApp {{
#            background: url({background_image_url});
#            background-size: cover;
#            background-attachment: fixed;
#            background-repeat: no-repeat;
#        }}
#    </style>
#""", unsafe_allow_html=True)

# Initialize chat history and emoji input
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'emoji_input' not in st.session_state:
    st.session_state.emoji_input = ""

# Introduce ReX if the chat history is empty
if len(st.session_state.chat_history) == 0:
    #initial_prompt = "I am ReX, your assistant powered by Google Gemini. 😊 Ask me anything! I use emojis to be more interactive. 💬"
    initial_prompt = "I am Xi, your AI assistant powered by Google Gemini. 😊 Ask me anything"
    
    user_message, llm_response = llm_function(initial_prompt)
    st.session_state.chat_history.append({"role": "gemini", "content": llm_response})

# Display chat history
for i, message in enumerate(st.session_state.chat_history):
    key = f"{message['role']}_{i}"  # Combine role and index for a unique key
    height = max(50, len(message["content"].split('\n')) * 30)  # Calculate height based on message length
    if message["role"] == "user":
        st.text_area("You:", value=message["content"], height=height, key=key, disabled=True)
    else:
        st.text_area("Gemini:", value=message["content"], height=height, key=key, disabled=True)

# Emoji tray
display_emoji_tray()

# Input form
with st.form(key='input_form', clear_on_submit=True):
    user_input = st.text_input(
        "You:",
        placeholder="I am your personal assistant, ask me what you want to know.",
        value=st.session_state.emoji_input
    )
    submit_button = st.form_submit_button(label='Send')

    if submit_button:
        if user_input.strip():
            user_message, llm_response = llm_function(user_input)
            st.session_state.chat_history.append({"role": "user", "content": user_message})
            st.session_state.chat_history.append({"role": "gemini", "content": llm_response})
            st.session_state.emoji_input = ""
            st.rerun()

# JavaScript to scroll to the bottom of the page automatically
scroll_script = """
    <script>
        var chatDiv = window.parent.document.getElementsByClassName('main')[0];
        chatDiv.scrollTo(0, chatDiv.scrollHeight);
    </script>
"""
st.markdown(scroll_script, unsafe_allow_html=True)
