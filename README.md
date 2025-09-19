# 📊 LangGraph AI Agent for Business Insights

## 📌 Overview

This project is a simple AI agent that analyzes basic business data (e.g., daily revenue, costs, and customers) using the **LangGraph** framework.

The agent can:
- 📈 Calculates daily profit
- 📉 Detects changes in revenue, cost, and CAC (Customer Acquisition Cost)
- 🤖 Provides actionable recommendations to improve business decisions

Built using:
- 🧠 LangGraph for graph-based workflow
- 🔁 Multi-step agent structure
- ✅ UV for fast package management and reproducible environments

---

## 🎯 Objectives

- Understand how to use LangGraph to build modular AI agents
- Apply basic business metrics and logic (profit, CAC, trends)
- Generate practical, interpretable output
- Write test cases to ensure correctness

---

## 🧩 Features

- 🔢 **Profit Calculation**: Computes daily profit using revenue and cost
- 📊 **Trend Detection**: Compares today’s vs yesterday’s data
- 💰 **CAC Alerting**: Warns if customer acquisition cost increases
- 💡 **Smart Recommendations**: Offers suggestions like reducing costs or boosting marketing
- 🧪 **Test Coverage**: Pytest used to validate outputs

---
## 📉 Graph
<p align="center">
  <img width="220" alt="output_graph" src="https://github.com/user-attachments/assets/c4fbd225-7605-4321-8126-b04cb8bdffdc" />

</p>

---

## 🧪 LangGraph Studio Integration

Easily test and visualize your AI agent using **[LangGraph Studio](https://studio.langgraph.dev/)** — a web interface for debugging and observing LangGraph-based workflows.

### 🌐 How to Use with Studio

1. **Add `langgraph.json`** to your repo:

    ```
    json
    {
    "dependencies" : [
    "ipykernel>=6.29.5",
    "langchain-groq>=0.3.6",
    "langgraph>=0.5.2",
    "langgraph-cli[inmem]>=0.3.4",
    "pytest>=8.4.1",
    "python-dotenv>=1.1.1"
    ],
    "graphs": {
        "my_agent": "./agent.py:app"},
    "env": "./.venv"
    }

    ```

2. Provide any required environment variables like your API key.
3. Trigger your agent with sample data and view node-by-node execution.
4. Open Run a local server on LangGraph Studio [website](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/)

---


### 🎞️ Studio Walkthrough (Demo GIF)

<p align="center">
  <img width="1120" src="https://github.com/user-attachments/assets/9419e962-b5fd-4df9-a22e-d1ffb14d9a0e" width="700" alt="LangGraph Studio Demo" />
</p>


---

### 💡 Why Use LangGraph Studio?

- 🧭 **Visual debugging** — See exactly how data flows between nodes  
- 🚀 **Rapid iteration** — Run and test inputs live, no CLI needed  
- 🔒 **Secure** — Use environment variables without hardcoding secrets  

---

## 📂 Project Structure

```bash
.
├── src/
│   ├── main.py           # LangGraph agent logic
│   └── test_agent.py     # Pytest test cases
├── .gitignore
├── .env.example          # Safe env config example
├── pyproject.toml        # UV + dependencies
└── README.md
```
---

## 🧪 **Testing**
Run tests with:

``` bash
uv pip install pytest
pytest src/
```

