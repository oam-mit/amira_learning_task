import streamlit as st
from llm import get_response
from dotenv import load_dotenv
import json
import uuid



load_dotenv()

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state["messages"] = []

# Function to convert content to JSON format
def convert_to_json(content, indent):
    return json.dumps(content, indent=indent, ensure_ascii=False)

# Function to handle chat submissions
def handle_submission(prompt, show_messages = False):
    try:
        # Add user's message to the session
        st.session_state.messages.append({"role": "user", "content": prompt})
        if show_messages:
            with st.chat_message("user"):
                st.write(prompt)
        response = get_response(st.session_state.messages)

        # Add assistant's message to the session
        st.session_state.messages.append({"role": "assistant", "content": convert_to_json(response, indent=None)})

        if show_messages:
            with st.chat_message("assistant"):
                st.write(response)
                st.download_button(
                    key=uuid.uuid4(),
                    label="Download Response as JSON",
                    data=convert_to_json(response, indent=3),
                    file_name="response.json",
                    mime="application/json"
                )
    except Exception as e:
        st.session_state.messages.append({"role": "assistant", "content": str(e)})
        if show_messages:
            show_messages_chat()

def show_messages_chat():
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            if message["role"] == "assistant":
                st.write(json.loads(message["content"]))
                st.download_button(
                    key=uuid.uuid4(),
                    label="Download Response as JSON",
                    data=convert_to_json(message["content"], indent=3),
                    file_name="response.json",
                    mime="application/json"
                )
            else:
                st.write(message["content"])

# Show form when no chat messages exist
if len(st.session_state["messages"]) == 0:
    st.title("Amira Intervention Challenge")

    # Function to handle the form submission
    def submit_initial(word, sentence, level, native_language):
        # Create a prompt from form inputs
        prompt = {
            "word": word,
            "sentence": sentence,
            "level": level,
            "native_language": native_language
        }
        handle_submission(json.dumps(prompt))

    # Input fields for form
    word = st.text_input("Enter the word")
    sentence = st.text_input("Enter the sentence")
    level = st.selectbox("Select the level to which the child needs to be taught", ["low", "high"])
    native_language = st.text_input("Enter the native language")


    st.button("Submit", on_click=lambda: submit_initial(word, sentence, level, native_language), 
              disabled=not word or not sentence or not level or not native_language)

# Show chat interface when there are messages
else:
    show_messages_chat()

    # Chat input for follow-up questions
    if prompt := st.chat_input("Follow up"):
        handle_submission(prompt, show_messages=True)
