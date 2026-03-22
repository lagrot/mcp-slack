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
- A Slack App created via the [Slack API Dashboard](https://api.slack.com/apps).

### Finding Your Credentials
Finding these credentials can feel like a scavenger hunt if you haven't danced with the Slack API lately. You won't find these in your regular Slack desktop app; you’ll need to head over to the Slack App Directory.

#### 1. SLACK_BOT_TOKEN (xoxb-...)
This is the "identity" of your bot.
1. Go to your [Slack App Dashboard](https://api.slack.com/apps).
2. Select your App.
3. In the left-hand sidebar, click on **OAuth & Permissions**.
4. Scroll down to the **OAuth Tokens for Your Workspace** section.
   *Note: If you haven't installed the app to your workspace yet, you'll need to click "Install to Workspace" first to generate this token.*

#### 2. SLACK_SIGNING_SECRET
This is used to verify that requests coming to your server are actually from Slack.
1. On that same App Dashboard, stay in the left-hand sidebar.
2. Click on **Basic Information**.
3. Scroll down to the **App Credentials** section.
4. You’ll see "Signing Secret" there. Click **Show** to reveal it.

#### 3. SLACK_CHANNEL_ID (C...)
This is the unique ID for the specific channel where your bot will be hanging out.
1. Open the Slack Desktop App.
2. Right-click on the channel name in the sidebar.
3. Select **View channel details**.
4. Scroll to the very bottom of the pop-up window. You will see the Channel ID (it usually starts with a C or G).

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
Run the MCP server locally:
```bash
uv run python src/slack_mcp/server.py
```

## How to Use the Tool

Once the server is configured and running (either locally or via Gemini CLI), the `ask_slack` tool becomes available to your AI agent.

### Example Usage
When you are chatting with an agent (like Gemini CLI) and need to ask a human on Slack for approval or input, simply ask the agent to use the tool:

> **You:** "I've generated the migration script. Can you ask the team on Slack if this looks safe to apply?"

The agent will then trigger the `ask_slack` tool with your message.

### Tool Specification
- **Tool Name:** `ask_slack`
- **Argument:** `question` (string) - The message you want to send to your configured Slack channel.

**What happens:**
1. The agent calls `ask_slack(question="...")`.
2. The server sends your message to the Slack channel defined in `SLACK_CHANNEL_ID`.
3. You will see the message appear in your Slack channel, allowing you to reply or act accordingly.


## Integrating with Gemini CLI

You can register the Slack MCP server using the `gemini mcp add` command:

```bash
gemini mcp add slack-bridge uv run python /absolute/path/to/your/git/slack-mcp/src/slack_mcp/server.py
```

*Note: Replace `/absolute/path/to/your/git/slack-mcp/` with the actual path to your repository.*

The server will automatically load your `.env` file when it starts, so there is no need to pass credentials as command-line arguments. After running this command, Gemini CLI will automatically load the `ask_slack` tool and make it available for use in your coding sessions.


## Development & Maintenance
- **Linting/Formatting:** `uv run ruff check . --fix`
- **Testing:** `uv run pytest tests/`
