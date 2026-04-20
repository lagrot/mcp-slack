import pytest
from unittest.mock import MagicMock, patch
from slack_mcp.server import ask_slack

@patch("slack_mcp.server.get_slack_client")
def test_ask_slack_success(mock_get_client):
    # Setup mock client
    mock_instance = MagicMock()
    mock_get_client.return_value = mock_instance
    
    # Mocking environment variables for test
    with patch.dict("os.environ", {"SLACK_CHANNEL_ID": "C123"}):
        mock_instance.send_message.return_value = {"ok": True}
        
        result = ask_slack("Test question?")
        
        assert "Message sent to Slack successfully" in result
        mock_instance.send_message.assert_called_with("C123", "Test question?")

@patch("slack_mcp.server.get_slack_client")
def test_ask_slack_failure(mock_get_client):
    # Setup mock client
    mock_instance = MagicMock()
    mock_get_client.return_value = mock_instance
    
    # Mocking environment variables for test
    with patch.dict("os.environ", {"SLACK_CHANNEL_ID": "C123"}):
        mock_instance.send_message.return_value = {"ok": False, "error": "channel_not_found"}
        
        result = ask_slack("Test question?")
        
        assert "Error: Slack API returned an error: channel_not_found" in result

def test_ask_slack_empty():
    result = ask_slack("")
    assert "Error: Cannot send an empty message" in result
