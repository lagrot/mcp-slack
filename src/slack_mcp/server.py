import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from slack_mcp.slack_client import SlackClient

# Load environment variables from .env file
load_dotenv()

mcp = FastMCP("Slack-MCP-Server")
_slack_client = None

def get_slack_client():
    global _slack_client
    if _slack_client is None:
        _slack_client = SlackClient()
    return _slack_client

@mcp.tool()
def ask_slack(question: str) -> str:
    """Sends a question/approval request to the configured Slack channel."""
    channel_id = os.environ.get("SLACK_CHANNEL_ID")
    if not channel_id:
        return "Error: SLACK_CHANNEL_ID not configured."
    
    try:
        get_slack_client().send_message(channel_id, question)
        return "Message sent to Slack successfully."
    except Exception as e:
        return f"Error sending message to Slack: {e}"

if __name__ == "__main__":
    mcp.run()
