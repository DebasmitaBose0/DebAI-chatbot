
# 💬 DebAI — Streamlit chatbot

Welcome to DebAI — a small, friendly Streamlit chatbot that streams responses from an Ollama model. 🤖✨

This workspace contains a minimal app: `chatbot.py`, which uses the `ollama` Python client to stream model responses and `streamlit` to provide a lightweight web UI.

## 🚀 Features
- ✅ Simple Streamlit chat UI (uses `st.chat_message`).
- ⚡ Streaming assistant tokens from `ollama.chat(..., stream=True, ...)` for responsive UX.
- 🧠 Conversation session state stored in `st.session_state` for history and continuity.

## 🛠️ Requirements
- Python 3.10+ (recommended)
- `streamlit` and `ollama` Python packages

Install into a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install --upgrade streamlit ollama
```

If you prefer not to use a venv, run the `pip install` commands in your system Python environment.

## ▶️ Run the app
From the project root run:

```powershell
streamlit run "e:\Chatbot(Infosys)\chatbot.py"
```

Open the Local URL printed by Streamlit (usually `http://localhost:8501` or `8502`). 🖥️

## ⚙️ Configuration
- The model used by the app is controlled by the `MODEL` constant at the top of `chatbot.py`.
  Update this value to point to the model you want running in your Ollama instance.

## 📝 Notes & Troubleshooting
- ❗ If your editor (e.g. VS Code + Pylance) shows "Import 'streamlit' could not be resolved",
  ensure the editor is using the same Python interpreter where you installed the packages.

- 🔌 If `ollama.chat(...)` fails, verify your Ollama server is running and the `ollama` client is
  configured properly. The app assumes local access or appropriate client configuration.

- 🗑️ The project previously included a background SVG (`assets/background.svg`). That file was
  removed on request; if you'd like a background or CSS gradient re-added, I can add one.

## 🧪 Development notes
- Conversation state is stored in `st.session_state['messages']` and streaming text is accumulated in
  `st.session_state['full_message']` while tokens arrive. The final assistant message is appended to
  the messages list after streaming completes.

- 🔁 If you observe repeated responses, it may come from duplicate tokens emitted by the model stream.
  We can reintroduce token/message de-duplication strategies or add logging to inspect the raw stream.

## 🤝 Contributing
If you'd like changes (UI tweaks, logo, theme, dedupe logic, logging, tests), open an issue or tell me what to implement next and I will make the edits. 💡

---
Generated: README for the DebAI project. ✨
