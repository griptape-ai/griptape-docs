# GoogleCalendarClient

The GoogleCalendarClient tool allows you to interact with Google Calendar.


```python
import os
from griptape.tools import GoogleCalendarClient
from griptape.structures import Agent

# Create the GoogleCalendarClient tool
google_calendar_tool = GoogleCalendarClient(
    service_account_credentials={
        "type": os.environ["YOUR_ACCOUNT_TYPE"],
        "project_id": os.environ["YOUR_PROJECT_ID"],
        "private_key_id": os.environ["YOUR_PRIVATE_KEY_ID"],
        "private_key": os.environ["YOUR_PRIVATE_KEY"],
        "client_email": os.environ["YOUR_CLIENT_EMAIL"],
        "client_id": os.environ["YOUR_CLIENT_ID"],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": os.environ["YOUR_CERT_URL"]
    }
)

# Set up an agent using the GoogleCalendarClient tool
agent = Agent(
    tools=[google_calendar_tool]
)

# Task: Get upcoming events from a Google calendar
agent.run("Get me the details of the next upcoming event from my primary calendar. My email is example@email.com")
```
```
[09/08/23 15:00:57] INFO     Task 7e9130c1f8364d1f859710bc0ca13040              
                             Input: Get me the details of the next upcoming     
                             event from my primary calendar. My email is        
                             example@email.com                                   
[09/08/23 15:01:05] INFO     Subtask 207917b4f9c24703b61e97a93a5a2353           
                             Thought: To get the details of the next upcoming   
                             event from the user's primary calendar, I can use  
                             the GoogleCalendarClient tool with the             
                             get_upcoming_events activity. I will set the       
                             max_events input to 1 to ensure that only the next 
                             event is returned.                                 
                                                                                
                             Action: {"type": "tool", "name":                   
                             "GoogleCalendarClient", "activity":                
                             "get_upcoming_events", "input": {"values":         
                             {"calendar_id": "primary", "calendar_owner_email": 
                             "example@email.com", "max_events": 1}}}             
[09/08/23 15:01:07] INFO     Subtask 207917b4f9c24703b61e97a93a5a2353           
                             Observation: Output of                             
                             "GoogleCalendarClient.get_upcoming_events" was     
                             stored in memory with memory_name "TextToolMemory" 
                             and artifact_namespace                             
                             "9522035207c743b987f2eb3815a98ae7"                 
[09/08/23 15:01:15] INFO     Subtask 8bcb892f56684a52bff8eb5ca4c586f1           
                             Thought: The output of the                         
                             GoogleCalendarClient.get_upcoming_events action was
                             stored in memory. I can retrieve this information  
                             using the TextToolMemory tool with the summarize   
                             activity.                                          
                             Action: {"type": "memory", "name":                 
                             "TextToolMemory", "activity": "summarize", "input":
                             {"values": {"memory_name": "TextToolMemory",       
                             "artifact_namespace":                              
                             "9522035207c743b987f2eb3815a98ae7"}}}              
[09/08/23 15:01:18] INFO     Subtask 8bcb892f56684a52bff8eb5ca4c586f1           
                             Observation: The text is a JSON object that        
                             contains information about a calendar event. The   
                             event is a meeting in Malibu and will cover housing
                             options in the area. The event was created and     
                             updated on September 8, 2023. The start and end    
                             times of the event are September 8, 2023, from 4:00
                             PM to 5:00 PM in the America/Los_Angeles time zone.
                             The event has a unique ID and is confirmed. The    
                             event creator and organizer have the email address 
                             example@email.com. The event has a Google Calendar  
                             link and an iCalUID. The event has no reminders and
                             is of the default event type.                      
[09/08/23 15:01:29] INFO     Task 7e9130c1f8364d1f859710bc0ca13040              
                             Output: The next upcoming event on your calendar is
                             a meeting in Malibu about housing options in the   
                             area. The event was created and updated on         
                             September 8, 2023. It will take place from 4:00 PM 
                             to 5:00 PM in the America/Los_Angeles time zone on 
                             the same day. The event is confirmed, and you,     
                             example@email.com, are the creator and organizer.   
                             The event has a unique ID, a Google Calendar link, 
                             and an iCalUID. There are no reminders set for this
                             event, and it is of the default event type. 
```
