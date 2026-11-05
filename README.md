# MCP Tutorial 🧩

**My personal learning repo for the Model Context Protocol (MCP).**

This repo is where I'm working through MCP concepts and building small, real examples — servers, clients, and tools — as I learn how to connect LLMs to external systems using MCP.

[![GitHub followers](https://img.shields.io/github/followers/HaykSahakyan11?style=social)](https://github.com/HaykSahakyan11)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

## 💡 What's in here

A growing collection of hands-on MCP exercises and mini-projects, covering things like:

- Building a basic MCP server and exposing tools/resources to a client
- Connecting an LLM-based agent to an MCP server
- Working through real-world integration patterns (APIs, local tools, data sources)

## ▶️ Getting Started

### 🛠️ Prerequisites

- Python 3.10+
- Any Python package manager (uv, poetry, pipenv)
- Access to an LLM (local via Ollama, or a cloud provider such as OpenAI/Anthropic)

### ⚙️ Setup

```bash
git clone https://github.com/HaykSahakyan11/MCP_tutorial
cd MCP_tutorial
uv sync
```

Follow the commits for the step-by-step progression — `git log --oneline` shows the learning path.

## 📚 Learning Objectives

By working through this repo, the goal is to:

- Understand the Model Context Protocol and how it standardizes LLM-to-tool communication
- Build and run MCP servers exposing custom tools/resources
- Connect agents/clients to MCP servers and use them end-to-end
- Apply these patterns to real integrations beyond toy examples

---

**Author:** [HaykSahakyan11](https://github.com/HaykSahakyan11)

**Source/inspiration:** project structure and course materials adapted from [Eden Marco's LangChain course](https://github.com/emarco177/langchain-course).
