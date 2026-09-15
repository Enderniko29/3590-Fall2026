import streamlit as st
from mellea import start_session
from mellea.stdlib.sampling import RejectionSamplingStrategy


@st.cache_resource
def get_session():
    # Created once and reused across reruns so the model isn't reloaded each click
    return start_session()


st.set_page_config(page_title="Dr. Reis's Office Hours")
st.title("Dr. Reis's Office Hours")
st.caption("Local LLM via Ollama · granite4.1:3b · no API key")

task = st.text_area(
    "What should the model do?",
    "Write a two-sentence email inviting students to office hours.",
    height=100,
)

requirement = st.text_input(
    "Requirement (optional) — a rule the output must satisfy",
    "Mention the room number INV1 455",
)

retries = st.slider("Max retries if the requirement fails", 1, 5, 3)

if st.button("Generate", type="primary"):
    m = get_session()
    reqs = [requirement] if requirement.strip() else []

    with st.spinner("Thinking..."):
        result = m.instruct(
            task,
            requirements=reqs,
            strategy=RejectionSamplingStrategy(loop_budget=retries),
        )

    st.subheader("Output")
    st.write(str(result))

    if reqs:
        st.success(f"Passed requirement: “{requirement}”")