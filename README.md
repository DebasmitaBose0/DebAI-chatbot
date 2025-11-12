# DebAI — Streamlit chatbot

A small Streamlit-based chatbot UI that streams responses from an Ollama model.

This workspace contains a minimal app: `chatbot.py` which uses the `ollama` Python
client to stream model responses and `streamlit` to provide a lightweight web UI.

## Features
- Simple Streamlit chat UI (uses `st.chat_message`).
- Streams assistant tokens from `ollama.chat(..., stream=True, ...)`.
- Basic session state handling for conversation history.

## Requirements
- Python 3.10+ (recommended)
- `streamlit` and `ollama` Python packages

Install the packages in your active environment (recommended: create a venv):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install --upgrade streamlit ollama
```

If you prefer not to create a venv, run the `pip install` command in your system Python.

## Run the app
Start the Streamlit app from the project root:

```powershell
streamlit run "e:\Chatbot(Infosys)\chatbot.py"
```

Open the local URL printed by Streamlit (usually http://localhost:8501 or 8502).

## Configuration
- The model used by the code is defined by the `MODEL` constant at the top of `chatbot.py`.
  Change it to another model name supported by your Ollama instance if needed.

## Notes & Troubleshooting
- If your editor (e.g. VS Code with Pylance) reports "Import 'streamlit' could not be resolved",
  make sure the editor is using the same Python interpreter where you installed the packages.

- If `ollama.chat(...)` fails, verify your Ollama server/agent is running and the `ollama` client
  is configured correctly for your environment. The project assumes a local Ollama setup or
  the client environment is properly authenticated.

- The project previously included a background SVG (`assets/background.svg`). That file has
  been removed on request — the app no longer references it. If you want a background
  or a CSS-based gradient, I can re-add a small CSS snippet or a new asset.

## Development notes
- Conversation state is stored in `st.session_state['messages']` and the streaming buffer is
  built in `st.session_state['full_message']` while tokens are being received. The code
  appends the final assistant message into the messages list after the streaming completes.

- If you see repeated responses, it may be caused by the model/stream emitting duplicate
  tokens. The project contains safeguards that were experimented with; if duplication
  persists we can reintroduce refined token/message de-duplication strategies.

## Contributing
If you'd like changes (UI tweaks, logo, theme, robust dedupe, logging, tests), open an issue
or tell me what to implement next and I will make the edits.

---
Generated: README for the DebAI project.
