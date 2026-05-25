# LangChain Models (LLMs, Chat Models, Embeddings)

A small, script-based playground for trying LangChain with:

- **LLMs** (classic completion-style)
- **Chat models** (OpenAI / Anthropic / Google Gemini / Hugging Face)
- **Embeddings** (OpenAI + Hugging Face) and a simple cosine-similarity demo

This repo is intentionally simple: each file is a runnable example.

## Prerequisites

- Python 3.10+ recommended
- Windows / PowerShell instructions are included below (works on macOS/Linux too)

## Setup

### 1) Create & activate a virtual environment

PowerShell:

```powershell
python -m venv venv

# If activation is blocked in PowerShell:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

./venv/Scripts/Activate.ps1
```

### 2) Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3) Create a `.env` file

Most scripts call `load_dotenv()`, so put your keys in a `.env` file in the repo root.

Create `.env`:

```env
# OpenAI
OPENAI_API_KEY=YOUR_KEY_HERE

# Anthropic
ANTHROPIC_API_KEY=YOUR_KEY_HERE

# Google Gemini (langchain-google-genai)
GOOGLE_API_KEY=YOUR_KEY_HERE

# Hugging Face Inference API (HuggingFaceEndpoint)
HUGGINGFACEHUB_ACCESS_TOKEN=YOUR_TOKEN_HERE
```

Notes:

- If you don’t plan to run a provider’s scripts, you can omit that key.
- Model availability/permissions vary by account. If a script errors on the model name, edit the model string in that script.

## Quick sanity check

Verify LangChain is installed:

```powershell
python test.py
```

## Run the demos

All commands assume you are at the repo root.

### 1) LLM (OpenAI)

- File: `1.LLMs/1_llm_demo.py`

```powershell
python 1.LLMs/1_llm_demo.py
```

Uses `OpenAI(model='gpt-3.5-turbo-instruct')`.

### 2) Chat models

#### OpenAI chat

- File: `2.ChatModels/1_chatmodel_openai.py`

```powershell
python 2.ChatModels/1_chatmodel_openai.py
```

Uses `ChatOpenAI(model='gpt-4', temperature=0.9, max_tokens=10)`.

#### Anthropic chat

- File: `2.ChatModels/2_chatmodel_anthropic.py`

```powershell
python 2.ChatModels/2_chatmodel_anthropic.py
```

Uses `ChatAnthropic(model='claude-3-5-sonnet-20241022', temperature=0.9, max_tokens=10)`.

#### Google Gemini chat

- File: `2.ChatModels/3_chatmodel_google.py`

```powershell
python 2.ChatModels/3_chatmodel_google.py
```

Uses `ChatGoogleGenerativeAI(model='gemini-2.0-flash')`.

#### Hugging Face (hosted inference API)

- File: `2.ChatModels/4_chatmodel_hf_api.py`

```powershell
python 2.ChatModels/4_chatmodel_hf_api.py
```

Uses `HuggingFaceEndpoint` with `repo_id='mistralai/Mistral-7B-Instruct-v0.3'`.

#### Hugging Face (local pipeline)

- File: `2.ChatModels/5_chatmodel_hf_local.py`

```powershell
python 2.ChatModels/5_chatmodel_hf_local.py
```

This script sets `HF_HOME` to `D:/huggingface_cache`. Change that path if needed.

Local model notes:

- You will typically need **PyTorch** for `transformers` pipelines.
- If you hit an import error, install torch:

```powershell
pip install torch
```

### 3) Embeddings

#### OpenAI embeddings (single query)

- File: `3.EmbeddedModels/1_embedding_openai_query.py`

```powershell
python 3.EmbeddedModels/1_embedding_openai_query.py
```

#### OpenAI embeddings (documents)

- File: `3.EmbeddedModels/2_embedding_openai_docs.py`

```powershell
python 3.EmbeddedModels/2_embedding_openai_docs.py
```

#### Hugging Face embeddings (local)

- File: `3.EmbeddedModels/3_embedding_hf_local.py`

```powershell
python 3.EmbeddedModels/3_embedding_hf_local.py
```

Uses `sentence-transformers/all-MiniLM-L6-v2`.

#### Document similarity (cosine similarity)

- File: `3.EmbeddedModels/4_document_similarity.py`

```powershell
python 3.EmbeddedModels/4_document_similarity.py
```

This embeds a small list of cricket-related sentences and finds the closest one to the query using cosine similarity.

## Troubleshooting

### PowerShell can’t activate venv

Run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
./venv/Scripts/Activate.ps1
```

### Missing environment variables

Make sure you have a `.env` file in the repo root and that the variable names match exactly.

### Model name errors

Providers may rename/deprecate models. Update the `model=` value in the script you’re running.

---

If you want, tell me which provider(s) you’ll use most (OpenAI / Anthropic / Gemini / HF-local) and I can tune `requirements.txt` and the scripts for a smoother first run.
