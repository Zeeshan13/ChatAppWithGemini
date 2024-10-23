# Gemini Explorer: AI Chatbot Powered by Google Gemini

Welcome to **Gemini Explorer**, a conversational AI chatbot powered by Google's Gemini LLM and built using Streamlit and Vertex AI. This application allows you to interact with ReX, an intelligent assistant designed to provide engaging responses, complete with emojis for a more interactive experience.

## Features
- Conversational AI powered by Google Gemini.
- Responsive chat interface built with Streamlit.
- Emoji tray for fun and interactive responses.
- Automatic scrolling in the chat window.
- Dynamic backgrounds for a fresh visual experience in each session.


## Installation & Setup

### Prerequisites:
- Python 3.x
- Streamlit
- Google Cloud Vertex AI

### Install the necessary packages:
```bash
pip install streamlit
pip install google-cloud-aiplatform
```

### Set up Google Cloud Vertex AI:
1. Enable Vertex AI API
2. Initialize your Google Cloud project in the Python script:
      project = "your-google-cloud-project-id"

##  Run the Streamlit app:
```bash
streamlit run gemini_explorer.py
```

This will launch the chatbot app locally, and you can interact with ReX in your browser.


#### 4. **How to Use:**

**Start the app:**
On launching the app, ReX will introduce itself.

**Ask questions:**
Type your queries in the chat box, and ReX will respond in real-time.

**Add emojis:**
Use the paperclip icon 📎 to access the emoji tray and add fun elements to your messages.


## Dynamic Background
The background of the app changes dynamically on each run, giving it a fresh visual each time. However, for the same session, the background remains fixed.


## Project Structure
- `gemini_explorer.py`: Main application file containing the logic for the chatbot.

## Future Enhancements
### 1. Dynamic backgrounds:
   Automatically change backgrounds for each session.
### 2. Improved UI/UX:
   Additional aesthetic improvements like personalized themes.


## Contribution
Feel free to fork this repository and create pull requests if you'd like to contribute. Suggestions and improvements are welcome!




