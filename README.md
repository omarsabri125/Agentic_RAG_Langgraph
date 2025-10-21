# Agentic RAG with LangGraph

A sophisticated Retrieval-Augmented Generation (RAG) system built with LangGraph, featuring multiple specialized agents for intelligent document processing and query handling.

<p float="left">
  <img src="assets\AgentWorkflow.png" width="600" />
</p>

## 🌟 Overview

This project implements an agentic RAG system that leverages multiple AI agents to handle complex queries through intelligent routing, grading, and answer generation. The system uses LangGraph workflows to orchestrate agent interactions and maintain conversation flow.

## 🏗️ Architecture

The system consists of several specialized agents:

- **RouterAgent**: Routes incoming queries to appropriate agents
- **RetrieverAgent**: Retrieves relevant documents from the vector database
- **GradeAgent**: Evaluates document relevance and quality
- **AnswerGrader**: Assesses generated answers for accuracy
- **HallucinationAgent**: Detects and prevents hallucinations
- **RewriteAgent**: Reformulates queries for better results
- **SearchAgent**: Performs web searches for external information
- **GenerateAnswer**: Produces final answers based on context

## 📁 Project Structure

```
Agentic_RAG_Langgraph/
├── assets/
│   └── workflow.png              # Workflow visualization
├── data/
│   └── chroma.db/               # Vector database
│       └── chroma.sqlite3       # ChromaDB storage
├── langgraphenv/                # Virtual environment
├── notebooks/
│   └── Agentic_RAG_With_Langgraph.ipynb
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── AnswerGrader.py     # Answer quality evaluation
│   │   ├── GenerateAnswer.py   # Answer generation
│   │   ├── GradeAgent.py       # Document grading
│   │   ├── HallucinationAgent.py  # Hallucination detection
│   │   ├── RetrieverAgent.py   # Document retrieval
│   │   ├── RewriteAgent.py     # Query reformulation
│   │   ├── RouterAgent.py      # Query routing
│   │   └── SearchAgent.py      # Web search
│   ├── data_pipline/           # Data processing pipeline
│   ├── graph/                  # LangGraph workflow definitions
│   ├── utils/                  # Utility functions
│   ├── __init__.py
│   └── main.py                 # Main application entry
├── .env                        # Environment variables
├── .env.example               # Example environment configuration
├── .gitignore
├── README.md
└── requirements.txt           # Python dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip or conda
- API keys for LLM services (OpenAI, Anthropic, etc.)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/omarsabri125/Agentic_RAG_Langgraph.git
   cd Agentic_RAG_Langgraph
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv langgraphenv
   
   # Windows
   langgraphenv\Scripts\activate
   
   # Linux/Mac
   source langgraphenv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys
   ```
   
### Configuration

Edit the `.env` file with your credentials:

```env
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
LANGCHAIN_API_KEY=your_langchain_key_here
LANGCHAIN_TRACING_V2=true
```

## 💻 Usage

### Running the Main Application

```bash
python src/main.py
```

The application will:
1. Load environment variables
2. Initialize the workflow
3. Process queries through the agent system
4. Display structured output from each node

### Example Query

```python
from dotenv import load_dotenv
from graph.workflow import create_workflow

load_dotenv()
app = create_workflow()

inputs = {
    "query": "What are the types of agent memory?"
}

for output in app.stream(inputs):
    for key, value in output.items():
        print(f"Output from node '{key}':")
        print(value, indent=2, width=80, depth=None)
        print("\n---\n")
```

### Using the Jupyter Notebook

Launch Jupyter and open the notebook:

```bash
jupyter notebook notebooks/Agentic_RAG_With_Langgraph.ipynb
```

## 🔧 Key Features

### Intelligent Query Routing
The RouterAgent analyzes incoming queries and routes them to the most appropriate processing path.

### Multi-Stage Document Grading
Documents are evaluated for relevance before being used to generate answers, ensuring high-quality responses.

### Hallucination Prevention
A dedicated agent checks generated answers against source documents to prevent hallucinations.

### Adaptive Query Rewriting
If initial retrieval fails, queries are automatically reformulated for better results.

### Web Search Fallback
When local knowledge is insufficient, the system can search the web for additional information.

### Workflow Visualization
LangGraph provides visual representation of the agent workflow for better understanding and debugging.

## 🛠️ Development

### Adding New Agents

1. Create a new agent file in `src/agents/`
2. Implement the agent logic
3. Update the workflow in `src/graph/workflow.py`
4. Register the agent in `src/agents/__init__.py`

### Customizing the Workflow

Modify `src/graph/workflow.py` to adjust:
- Agent connections
- Conditional edges
- Processing logic
- State management

## 📊 Agent Types Explained

### RouterAgent
Determines the optimal path for query processing based on query characteristics.

### RetrieverAgent
Searches the vector database for relevant documents using semantic similarity.

### GradeAgent
Evaluates retrieved documents for relevance to the query.

### GenerateAnswer
Produces natural language answers based on graded documents.

### AnswerGrader
Checks if the generated answer adequately addresses the query.

### HallucinationAgent
Verifies that answers are grounded in retrieved documents.

### RewriteAgent
Reformulates queries to improve retrieval performance.

### SearchAgent
Performs external web searches when needed.

## 📝 Dependencies

Key libraries used:
- `langgraph` - Workflow orchestration
- `langchain` - LLM framework
- `chromadb` - Vector database
- `dotenv` - Environment management
- `pprint` - Output formatting

See `requirements.txt` for complete list.

## 🙏 Acknowledgments

- LangChain team for the excellent framework
- LangGraph for workflow orchestration
- ChromaDB for vector storage
- The open-source community
---

**Built using LangGraph and LangChain**