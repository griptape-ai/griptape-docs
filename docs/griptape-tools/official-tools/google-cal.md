# GoogleCalendarClient

The GoogleCalendarClient tool allows you to interact with Google Calendar.

```python
from griptape.tools import GoogleCalendarClient
from griptape.structures import Agent

# Create the GoogleCalendarClient tool
google_calendar_tool = GoogleCalendarClient(
    service_account_credentials={
        "type": "service_account",
        "project_id": "YOUR_PROJECT_ID",
        "private_key_id": "YOUR_PRIVATE_KEY_ID",
        "private_key": "YOUR_PRIVATE_KEY",
        "client_email": "YOUR_CLIENT_EMAIL",
        "client_id": "YOUR_CLIENT_ID",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "YOUR_CERT_URL"
    }
)

# Set up an agent using the GoogleCalendarClient tool
agent = Agent(
    tools=[google_calendar_tool]
)

# Task: Get upcoming events from a Google calendar
get_events_result = agent.run({
    "description": "Get the next 10 upcoming events",
    "tool": "GoogleCalendarClient",
    "activity": "get_upcoming_events",
    "values": {
        "calendar_id": "primary",
        "calendar_owner_email": "youremail@gmail.com",
        "max_events": 10
    }
})

if isinstance(get_events_result, ErrorArtifact):
    print(f"Error occurred: {get_events_result}")
else:
    for event in get_events_result:
        print(f"Event: {event.data}")
```
