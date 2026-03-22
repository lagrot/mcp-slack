# Slack MCP Server

A lightweight, maintainable MCP server that bridges coding agent requests to a Slack channel for human-in-the-loop interactions.

## Why this architecture?
- **MCP (Model Context Protocol):** Provides a standardized interface for AI agents (like Claude Code, Cursor, or Gemini CLI) to communicate with external systems.
- **Slack-Bolt:** The official Slack framework, offering robust handling for events, messaging, and interactivity.
- **Tooling:**
    - **uv:** A fast, modern Python package installer and manager.
    - **ruff:** An extremely fast Python linter and formatter.
    - **pytest:** A feature-rich testing framework.

## Prerequisites
- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (recommended) or `pip`
- A Slack App created via the [Slack API Dashboard](https://api.slack.com/apps) with:
  - `chat:write` scope
  - `SLACK_BOT_TOKEN` (Bot User OAuth Token)
  - `SLACK_SIGNING_SECRET` (from Basic Information)
  - `SLACK_CHANNEL_ID` (ID of the channel to receive messages)

## Getting Started

### 1. Configuration
Create a `.env` file in the root directory:
```bash
SLACK_BOT_TOKEN=xoxb-...
SLACK_SIGNING_SECRET=...
SLACK_CHANNEL_ID=C...
```

### 2. Development Setup
Initialize the environment and dependencies using **uv**:
```bash
uv sync
```

### 3. Running the Server
Run the MCP server directly:
```bash
uv run python server.py
```

## Development & Maintenance
- **Linting/Formatting:** `uv run ruff check . --fix`
- **Testing:** `uv run pytest tests/`
