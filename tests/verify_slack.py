import os
import sys
from dotenv import load_dotenv
from slack_mcp.slack_client import SlackClient

def verify():
    load_dotenv()
    
    # Check for required environment variables
    missing = [v for v in ["SLACK_BOT_TOKEN", "SLACK_SIGNING_SECRET", "SLACK_CHANNEL_ID"] if not os.environ.get(v)]
    if missing:
        print(f"Error: Missing environment variables: {', '.join(missing)}")
        sys.exit(1)
        
    print("Connecting to Slack...")
    client = SlackClient()
    
    channel_id = os.environ.get("SLACK_CHANNEL_ID")
    try:
        response = client.send_message(channel_id, "Test message from Slack-MCP verification script.")
        if response.get("ok"):
            print("Success: Message sent to Slack!")
        else:
            print(f"Error: Slack API returned an error: {response.get('error')}")
            sys.exit(1)
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    verify()
