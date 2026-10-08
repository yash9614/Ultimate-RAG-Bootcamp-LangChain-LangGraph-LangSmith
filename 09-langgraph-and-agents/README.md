# 09 — LangGraph and agents

LangGraph is the control layer. RAG is one node.

## Concepts

- **State.** The typed object passed between nodes. Question, docs, answer.
- **Node.** A function `(state) -> partial state`.
- **Edge.** Fixed, or conditional on a grade.
- **ReAct.** Thought, tool, observation loop. Retrieval can be the tool.
- **Multi-agent.** Router sends the question to a specialist. Easy to overbuild.
- **Streaming.** Token stream vs node stream. Different events.
- **Guardrails.** Block or redact before the tool call, not after the answer is shown.

## Files

| File | What it covers |
| --- | --- |
| `simple-graph.ipynb` | One node, one edge. Start here. |
| `chains.ipynb` | A chain expressed as a graph. |
| `dataclass-state.ipynb` | State as a dataclass. |
| `pydantic-state.ipynb` | State as a Pydantic model. **Important:** schema is the contract between nodes. |
| `chatbot.ipynb` | Messages in state. |
| `react.ipynb` | ReAct loop. |
| `react-agents.ipynb` | ReAct with tools, longer notebook. |
| `multi-agent.ipynb` | Supervisor and workers. |
| `streaming.ipynb` | Stream modes. |
| `guardrails.ipynb` | Input and output checks. |
| `llm-gateway.ipynb` | One interface over more than one model. |
| `debugging/` | `langgraph.json` and a small agent for LangGraph Studio. |
| `langchain-updated/` | Newer LangChain 1.x style notebooks (models, tools, middleware). Middleware is where retries and PII redaction belong. |
| `sample-crewai-dataset.txt` | Notes used by the multi-agent demo. |
