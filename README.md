# NeoGPT 🚀

Say goodbye to boring interactions with documents and YouTube videos. NeoGPT is your trusted companion to chat with local documents and lengthy YouTube videos effortlessly. Perfect for professionals, developers, researchers, and enthusiasts.

![NeoGPT Gif](https://github.com/neokd/NeoGPT/assets/71772185/82d5c63d-81b5-4b45-95d4-53641016bfdc)


<br/>

Note: NeoGPT is continuously evolving. Your feedback shapes its future.

# Table of Contents
- [Getting Started](#getting-started)
- [Supported Retriever](#supported-retriever)
- [Project Roadmap](#project-roadmap)
- [Features](#features)
- [Persona](#persona)
- [Contributing](#contributing)
- [License](#license)
- [Discord](#discord)

## 🎉 Join Us for Hacktoberfest 2023
![Hacktoberfest Banner](./asset/readme.png)

## Getting Started

1. **Installation:** Clone this repository and install the necessary dependencies.


   ```
   git clone https://github.com/neokd/NeoGPT.git
   cd NeoGPT
   pip install -r dev-requirements.txt
    ```
    Alternatively, using conda:

   ```
   git clone https://github.com/neokd/NeoGPT.git
    
   cd NeoGPT

   # Create a new Conda environment and specify the python version, for example, 'neogpt-env'
   conda create --name neogpt-env python=3.10

   # Activate the Conda environment
   conda activate neogpt-env

   # Now install the requirements using pip
   pip install -r requirements.txt
   ```


2. **Building Database** Currently NeoGPT supports local files and Youtube videos. To build the database add your local files to the documents directory and URL in the `builder.url` file. Then run the builder script.
    
    ```python
        python builder.py
    ```
    This will create a database file in the `db` folder. You can also specify the database to use `--db` flag.
    Supported databases are:
    - `Chroma` (default) 
    - `FAISS` 
    - `Pinecone` (experimental)

    Currently the database is built using 2 papers: 
    - [Attention Is All You Need](https://arxiv.org/pdf/1706.03762.pdf)
    - [HuggingGPT](https://arxiv.org/pdf/2303.17580.pdf)
    
    - Youtube Video from 1littlecoder: [22 AI News EXPLAINED!!!](https://www.youtube.com/watch?v=BPknz-hCnec)


3. **Run NeoGPT:** Run the CLI to start using NeoGPT. Requires `Python v3.10`. You can use the `--help` flag to view the available commands and options.
    ```python
        python main.py 
    ```
    You can also use `--ui` flag to run the Streamlit UI. 
    ```python
        python main.py --ui
    ```

## Supported Retriever 
- Local Retriever
- Web Retriever
- Hybrid Retriever (Ensemble Retriever)

## Project Roadmap
- ✓ RAG (Question Answering with local files) 📂
- ✓ Chat with Youtube Videos 🎥
- ✓ Web Based RAG (Search on Web and local files) 🌐📂
- ✓ Hybrid RAG (Keyword based and Semmantic Search) 🕵️‍♂️📂
- ✓ FAISS Support 📊
- ✓ Chromadb Support 🎵
- ✓ Build a user-friendly CLI ⌨️
- ✓ Upgrade Builder to support multiple file types including URLs 📦🌐
- ✓ User Interface 💻 (Streamlit)
- ☐ Chat with SQL DB 🤖
- ☐ Add support for other LLM types (Ollama) 🧠
- ☐ Add other database support (MongoDB, ElasticSearch, etc.) 📁🔍
- ☐ Support for other search engines (DuckDuckGo, Bing, etc.) 🔍
- ☐ Docker Support 🐳
- ☐ Better Documentation 📖
- ☐ Agent based chatbot 🤖

## Features

- **Task Automation:** NeoGPT can automate a wide range of tasks, from text generation to data analysis, making it a versatile tool for various domains.

- **Local Execution:** NeoGPT runs entirely on your local system, ensuring data privacy and security.

- **User-Friendly Interface:** NeoGPT is designed with a user-friendly command-line interface (CLI) that makes it accessible to users with varying levels of technical expertise.

- **Extensible:** You can easily extend NeoGPT's functionality by adding custom plugins or scripts.

- **Persona** You can add various persona to NeoGPT to make it more human like.


## Persona 

The persona feature allows you to customize NeoGPT's responses based on your preferences. You can choose from a variety of personas, each with its own unique characteristics. For example, if you want NeoGPT to be more friendly, you can choose the FRIEND persona. If you want NeoGPT to be more professional, you can choose the RECRUITER persona. You can also create your own persona by editing `neogpt/prompts/prompt.py` file. The following personas are currently available:


| Persona     | Description                                          |
|-------------|------------------------------------------------------|
| DEFAULT     | A helpful assistant with extensive knowledge.       |
| RECRUITER   | An experienced recruiter who finds the best candidates. |
| ACADEMICIAN | Engages in in-depth research and presents findings.  |
| FRIEND      | Provides comfort and encouragement as a friend.     |
| ML_ENGINEER | Explains complex ML concepts in an easy-to-understand manner. |
| CEO         | Acts as the CEO, making strategic decisions.        |
| RESEARCHER  | Analyzes, synthesizes, and provides insights.       |


## Contributing
We welcome contributions to NeoGPT! If you have ideas for new features or improvements, please open an issue or submit a pull request. For more information, see our [contributing guide](CONTRIBUTING.md).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. Let's innovate together! 🤖✨

## Discord
<a href = "https://discord.gg/JW7YD5Yt">
   <img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"/>
</a>
