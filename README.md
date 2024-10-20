# AI Web Search Agent

This project is an AI-powered assistant designed to answer user queries by first checking an internal database and, if necessary, searching the web to gather relevant information. The assistant provides accurate responses with appropriate source citations when information is retrieved from online.


# Frameworks Used

- **Swarm**: OpenAI Swarm framework form building Agent.
- **URL Collection**: Integrates with DuckDuckGo for gathering URLs.
- **Web Scraping**: Uses the `Crawl4AI` library for web scraping to collect data from various websites.
- **Text Splitting**: Implements the `SemanticTextSplitter` library to divide large text into manageable chunks.
- **Embeddings**: Utilizes sentence transformer models for generating embeddings of the text.
- **Hybrid Search**: Employs a hybrid search technique to retrieve the most relevant chunks based on user queries.
- **Response Protocol**: The AI agent is designed to first check an internal database before searching online. It strictly follows this protocol and includes URLs or source details when providing answers from external sources.

## Instructions to Run

1. **Install dependencies**:
   Ensure you have Python installed and run the following command to install the necessary libraries:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Agent**:

    ```bash
    python assistant.py
    ```

**You need to add your OPENAI_API_KEY in the .env file.**