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
    if not question.strip():
        return "Error: Cannot send an empty message."

    channel_id = os.environ.get("SLACK_CHANNEL_ID")
    
    try:
        response = get_slack_client().send_message(channel_id, question)
        if response.get("ok"):
            return "Message sent to Slack successfully."
        else:
            error_msg = response.get("error", "Unknown error")
            return f"Error: Slack API returned an error: {error_msg}"
    except Exception as e:
        # Log the specific error internally in a real application
        return f"Error: Failed to send message to Slack. {str(e)}"

if __name__ == "__main__":
    # Validate required configuration at startup
    REQUIRED_ENV_VARS = ["SLACK_BOT_TOKEN", "SLACK_SIGNING_SECRET", "SLACK_CHANNEL_ID"]
    for var in REQUIRED_ENV_VARS:
        if not os.environ.get(var):
            raise EnvironmentError(f"Missing required environment variable: {var}")

    mcp.run()
