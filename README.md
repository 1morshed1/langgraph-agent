# langgraph agent

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68.0%2B-green.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.20.0%2B-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A sophisticated AI agent orchestration platform that leverages the power of Langchain and Langgraph to enable seamless interaction with multiple AI models. Built with a modern tech stack, it features a user-friendly Streamlit interface, real-time web search capabilities, and customizable system prompts for specialized agent behavior.

## ✨ Features

🤖 **Multi-Model Support**

- Seamlessly switch between different AI models including LLaMA and GPT variants
- Easy integration of new models through modular architecture
- Configurable model parameters and settings

🌐 **Web Search Integration**

- Real-time web search capabilities powered by Serper API
- Up-to-date information retrieval during conversations
- Configurable search parameters and filtering

🎯 **Customizable Agents**

- Define custom system prompts to create specialized AI assistants
- Role-based agent configurations
- Chain-of-thought prompting support

💫 **Modern UI & UX**

- Intuitive Streamlit interface for easy interaction
- Real-time response streaming
- Mobile-responsive design
- Chat history management

🐳 **Enterprise-Ready Deployment**

- Docker support for consistent deployment across environments
- Jenkins integration for automated CI/CD pipeline
- Scalable architecture supporting multiple instances
- Comprehensive logging and monitoring

🏗️ **Robust Architecture**

- Clean, modular codebase with clear separation of concerns
- RESTful API design with FastAPI
- Efficient error handling and recovery
- Extensive documentation and type hints

## Architecture

## 🏗️ Architecture

The system follows a robust client-server architecture, ensuring scalability and maintainability:

```
┌─────────────┐   HTTP API   ┌─────────────┐
│ Streamlit   │◄────────────►│  FastAPI    │
│ Frontend    │              │  Backend    │
└─────────────┘              └─────────────┘
                                   │
                           ┌───────▼───────┐
                           │ Langchain     │
                           │ Langgraph     │
                           │ AI Agents     │
                           └───────────────┘
```

### 📦 Components

- **Frontend** (`app/frontend/ui.py`):

  - Streamlit web interface for user interaction
  - Model selection, prompt input, and chat history

- **Backend** (`app/backend/api.py`):

  - FastAPI server handling REST API requests
  - Orchestrates agent logic and model inference

- **Core** (`app/core/ai_agent.py`):

  - AI agent implementation using Langchain and Langgraph
  - Handles prompt engineering, model switching, and web search integration

- **Configuration** (`app/config/settings.py`):

  - Application settings and environment variables
  - Supports `.env` file for secrets and API keys

- **Common** (`app/common/`):
  - Shared utilities (logging, custom exceptions)
  - Error handling and monitoring

## Prerequisites

**Python**: 3.10 or higher
**Groq API key**: Required for LLM access
**Serper API key**: Required for web search functionality
**Docker**: (Optional) For containerized deployment
**Jenkins**: (Optional) For CI/CD pipeline

## Installation

1. **Clone the repository**

```bash
git clone <repository-url>
cd langgraph-agent
```

2. **Create a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install --upgrade pip
pip install -e .
```

4. **Configure environment variables**
   Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

## Usage

### 🚀 Running the Application

Start the application:

```bash
python app/main.py
```

This launches:

- Backend API server (FastAPI) on port `9999`
- Streamlit frontend on port `8501`

### 🖥️ Using the Web Interface

1. Open [http://localhost:8501](http://localhost:8501) in your browser
2. Enter a system prompt to define agent behavior
3. Select your preferred AI model
4. Toggle web search as needed
5. Type your query and click **Ask Agent**
6. View responses and chat history

### 🔗 API Endpoints

The backend exposes a REST API for programmatic access:

- `POST /chat` : Send a message to the AI agent

  - **Request Body:** `{ "message": "your query", "model": "llama|gpt|...", "web_search": true|false }`
  - **Response:** `{ "response": "agent reply" }`

- Request body:
  ```json
  {
    "model_name": "llama-3.3-70b-versatile",
    "system_prompt": "You are a helpful assistant...",
    "messages": ["Your query here"],
    "allow_search": true
  }
  ```
- Response:
  ```json
  {
    "response": "AI agent's response"
  }
  ```

## Docker Deployment

The application includes Docker support for easy deployment:

1. Build the Docker image:

   ```bash
   docker build -t langgraph-agent .
   ```

2. Run the container:
   ```bash
   docker run -p 8501:8501 -p 9999:9999 --env-file .env langgraph-agent
   ```

The application will be accessible at the same ports as when running locally.

## CI/CD Pipeline

The project includes a Jenkins pipeline configuration (`Jenkinsfile`) for automated building and deployment. The pipeline includes:

1. Cloning the GitHub repository
2. (Optional) SonarQube code analysis
3. (Optional) Docker image building and pushing to ECR
4. (Optional) Deployment to ECS Fargate

To use the Jenkins pipeline:

1. Set up Jenkins with the required plugins
2. Configure credentials for GitHub, AWS, and other services
3. Create a new pipeline job pointing to the Jenkinsfile

## Project Structure

```
langgraph-agent/
├── app/
│   ├── __init__.py
│   ├── main.py              # Application entry point
│   ├── backend/
│   │   ├── __init__.py
│   │   └── api.py           # FastAPI server
│   ├── core/
│   │   ├── __init__.py
│   │   └── ai_agent.py      # AI agent implementation
│   ├── frontend/
│   │   ├── __init__.py
│   │   └── ui.py            # Streamlit interface
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py      # Configuration settings
│   └── common/
│       ├── __init__.py
│       ├── logger.py        # Logging utility
│       └── custom_exception.py # Custom exceptions
├── custom_jenkins/
│   └── Dockerfile           # Jenkins Docker image
├── Dockerfile               # Application Docker image
├── Jenkinsfile              # CI/CD pipeline
├── requirements.txt         # Python dependencies
├── setup.py                 # Package setup
└── .env                     # Environment variables (not included in repo)
```

## Configuration

The application uses environment variables for configuration:

- `GROQ_API_KEY`: Required for accessing Groq AI models
- `SERPER_API_KEY`: Required for web search functionality

These should be set in a `.env` file in the project root.

## Supported Models

Currently supported AI models:

- `llama-3.3-70b-versatile`
- `openai/gpt-oss-120b`

## Logging

The application includes comprehensive logging for debugging and monitoring. Logs are generated in the `logs/` directory.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write tests if applicable
5. Commit your changes
6. Push to the branch
7. Create a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Langchain](https://github.com/hwchase17/langchain) for AI framework
- [Langgraph](https://github.com/langchain-ai/langgraph) for agent workflow
- [Streamlit](https://streamlit.io/) for the frontend framework
- [FastAPI](https://fastapi.tiangolo.com/) for the backend framework
- [Groq](https://groq.com/) for AI model inference
- [Serper](https://serper.dev/) for web search API
