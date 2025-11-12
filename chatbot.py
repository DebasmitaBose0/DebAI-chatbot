import streamlit as st
import ollama

MODEL = "gemma3:1b"

# App title (user-facing) — show chatbot name only, not the model
st.set_page_config(page_title="DebAI", page_icon="💬")
st.title("💬DebAI")

# Ensure messages list exists in session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "full_message" not in st.session_state:
    st.session_state["full_message"] = ""


for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


def generate_response():
    # Call the ollama chat stream and yield tokens
    try:
        response_iter = ollama.chat(model=MODEL, stream=True, messages=st.session_state["messages"])
    except Exception as e:
        raise RuntimeError(f"Failed to call ollama.chat: {e}") from e

    # Simple extractor for common chunk shapes
    def _extract_token(c):
        if isinstance(c, dict):
            m = c.get("message") or c
            if isinstance(m, dict):
                return m.get("content") or m.get("text") or ""
            return str(m)
        # objects with .message or .content
        if hasattr(c, "message"):
            msg = getattr(c, "message")
            if hasattr(msg, "content"):
                return getattr(msg, "content")
            if isinstance(msg, dict):
                return msg.get("content") or msg.get("text") or ""
        if hasattr(c, "content"):
            return getattr(c, "content")
        return str(c)

    for chunk in response_iter:
        token = _extract_token(chunk) or ""
        if not token:
            continue
        st.session_state["full_message"] += token
        yield token


if prompt := st.chat_input("What is on your mind?"):
    # append user message
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # prepare assistant response
    st.session_state["full_message"] = ""
    with st.chat_message("assistant"):
        placeholder = st.empty()
        try:
            for _ in generate_response():
                placeholder.markdown(st.session_state["full_message"])
        except Exception as e:
            placeholder.error(f"Error generating response: {e}")
            st.session_state["messages"].append({"role": "assistant", "content": f"<error> {e}"})
        else:
            final_text = st.session_state["full_message"]
            st.session_state["messages"].append({"role": "assistant", "content": final_text})