#pip install streamlit
#pip install google-cloud-aiplatform

import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession




# Set up the project
project = "avid-folder-433719-s3"
vertexai.init(project=project)


# Load and start the model
config = generative_models.GenerationConfig(
    temperature=0.8
)
model = GenerativeModel(
    "gemini-pro",
    generation_config=config
)
chat = model.start_chat()

def llm_function(user_input, chat):
    """
    This function interacts with the LLM and returns the response.
    It also appends the user input and LLM response to the chat history.
    """
    # Send the user input to the model and get the response
    response = chat.send_message(user_input)
    
    # Return both user input and model response
    return user_input, response.text

# Streamlit interface
st.title("AI Chat App powered by Gemini")

# Initialize chat history and emoji input
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'emoji_input' not in st.session_state:
    st.session_state.emoji_input = ""

# Step 1: Introduce ReX if the chat history is empty
if len(st.session_state.chat_history) == 0:
    initial_prompt = "I am ReX, your assistant powered by Google Gemini. :) Ask me anything! I use emojis to be more interactive.0"
    
    # Send the initial prompt to the chat
    user_message, llm_response = llm_function(initial_prompt, chat)
    
    # Add the initial introduction message to the chat history
    st.session_state.chat_history.append({"role": "gemini", "content": llm_response})

# Function to auto-adjust text area height based on content
def calculate_height(message):
    # Estimate the height of the text area based on the length of the content
    lines = len(message.split('\n'))
    return min(400, max(50, lines * 20))  # Adjust as per your preference

# Display chat history
for i, message in enumerate(st.session_state.chat_history):
    key = f"{message['role']}_{i}"  # Combine role and index for a unique key
    if message["role"] == "user":
        st.text_area("You:", value=message["content"], height=calculate_height(message["content"]), key=key, disabled=True)
    else:
        st.text_area("Gemini:", value=message["content"], height=calculate_height(message["content"]), key=key, disabled=True)

# Emoji tray visibility toggle
if 'show_emoji_tray' not in st.session_state:
    st.session_state.show_emoji_tray = False

# Attachment icon button
attachment_clicked = st.button("📎")  # Create attachment button

# Toggle the visibility of the emoji tray
if attachment_clicked:
    st.session_state.show_emoji_tray = not st.session_state.show_emoji_tray

# Emoji tray with buttons (visible only if the attachment icon is clicked)
if st.session_state.show_emoji_tray:
    st.write("Click an emoji to add it to your message:")
    
    # Define a list of emojis to display
    emoji_list = ['😊', '😂', '❤️', '👍', '🔥', '🎉', '💡', '💬', '😎', '🙌']
    
    # Create clickable emoji buttons
    cols = st.columns(len(emoji_list))  # Display emojis in a row
    for i, emoji in enumerate(emoji_list):
        if cols[i].button(emoji):
            st.session_state.emoji_input += emoji  # Append clicked emoji to the input state

# Create a form for user input with automatic clearing upon submission
with st.form(key='input_form', clear_on_submit=True):
    user_input = st.text_input(
        "You:",
        placeholder="I am your personal assistant, ask me what you want to know.",
        value=st.session_state.emoji_input  # Pre-fill with emojis if clicked
    )
    submit_button = st.form_submit_button(label='Send')

    if submit_button:
        if user_input.strip():
            # Use llm_function to process the user input and get the response
            user_message, llm_response = llm_function(user_input, chat)
            
            # Append the user message and LLM response to the chat history
            st.session_state.chat_history.append({"role": "user", "content": user_message})
            st.session_state.chat_history.append({"role": "gemini", "content": llm_response})
            
            # Reset the emoji_input state after submission
            st.session_state.emoji_input = ""
            
            # Rerun the app to refresh the chat history and scroll to the bottom
            st.rerun()

# JavaScript to scroll to the bottom of the page automatically
#scroll_script = """
#    <script>
#        var chatDiv = window.parent.document.getElementsByClassName('main')[0];
#        chatDiv.scrollTo(0, chatDiv.scrollHeight);
#    </script>
#"""
#st.markdown(scroll_script, unsafe_allow_html=True)
