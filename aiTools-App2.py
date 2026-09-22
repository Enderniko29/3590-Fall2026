import streamlit as st
import mellea


st.title("🤖 AI Chatbot")

@st.cache_resource
def get_session():
    return mellea.start_session()

m = get_session()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Initial context / system instruction
if "context" not in st.session_state:

    st.session_state.context = m.instruct(
        """
        You are an AI assistant specialized in Artificial Intelligence.

        You can discuss topics such as:
        - Machine learning
        - Deep learning
        - Large language models
        - Generative AI
        - Computer vision
        - Natural language processing
        - AI ethics

        You must ONLY discuss topics related to Artificial Intelligence.

        If the user asks about something unrelated to AI,
        politely explain that you can only discuss Artificial Intelligence.
        """
    )


# Display conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# User input
prompt = st.chat_input("Ask me about AI...")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = m.instruct(
                f"""
                {st.session_state.context}

                User question:
                {prompt}
                """
            )

            answer = str(response)

        st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })