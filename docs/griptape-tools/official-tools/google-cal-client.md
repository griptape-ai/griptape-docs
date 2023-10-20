# GoogleCalendarClient

The GoogleCalendarClient tool allows you to interact with Google Calendar.


```python
import os
from griptape.tools import GoogleCalendarClient
from griptape.structures import Agent

# Create the GoogleCalendarClient tool
google_calendar_tool = GoogleCalendarClient(
    service_account_credentials={
        "type": os.environ["GOOGLE_ACCOUNT_TYPE"],
        "project_id": os.environ["GOOGLE_PROJECT_ID"],
        "private_key_id": os.environ["GOOGLE_PRIVATE_KEY_ID"],
        "private_key": os.environ["GOOGLE_PRIVATE_KEY"],
        "client_email": os.environ["GOOGLE_CLIENT_EMAIL"],
        "client_id": os.environ["GOOGLE_CLIENT_ID"],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": os.environ["GOOGLE_CERT_URL"]
    },
    owner_email=os.environ["GOOGLE_OWNER_EMAIL"]
)

# Set up an agent using the GoogleCalendarClient tool
agent = Agent(
    tools=[google_calendar_tool]
)

# Task: Get upcoming events from a Google calendar
agent.run(
    "Get me the details of the next upcoming event from my primary calendar.",
)
```
```
[10/04/23 14:02:14] INFO     ToolkitTask 83fb147c05534d2c9de83b2cdf3f66ef       
                             Input: Get me the details of the next upcoming     
                             event from my primary calendar.                    
[10/04/23 14:02:23] INFO     Subtask 88b3934bae504a1792cce04a25cdceef           
                             Thought: To get the details of the next upcoming   
                             event from the primary calendar, I can use the     
                             GoogleCalendarClient tool with the                 
                             get_upcoming_events activity. I will set the       
                             calendar_id as 'primary' and max_events as 1 to get
                             the next upcoming event.                           
                                                                                
                             Action: {"type": "tool", "name":                   
                             "GoogleCalendarClient", "activity":                
                             "get_upcoming_events", "input": {"values":         
                             {"calendar_id": "primary", "max_events": 1}}}      
[10/04/23 14:02:24] INFO     Subtask 88b3934bae504a1792cce04a25cdceef           
                             Observation: Output of                             
                             "GoogleCalendarClient.get_upcoming_events" was     
                             stored in memory with memory_name "ToolMemory" 
                             and artifact_namespace                             
                             "c23b03911b6e46eeb47627fe8ed89466"                 
[10/04/23 14:02:40] INFO     Subtask 46ed5976c6374ed6a8aa474470432971           
                             Thought: The output of the                         
                             GoogleCalendarClient.get_upcoming_events activity  
                             has been stored in memory. I can use the           
                             ToolMemory.extract_json_objects activity to    
                             extract this information from memory and provide   
                             the details of the next upcoming event.            
                                                                                
                             Action: {"type": "memory", "name":                 
                             "ToolMemory", "activity":                      
                             "extract_json_objects", "input": {"values":        
                             {"memory_name": "ToolMemory",                  
                             "artifact_namespace":                              
                             "c23b03911b6e46eeb47627fe8ed89466", "json_schema": 
                             {"type": "object", "properties": {"start_datetime":
                             {"type": "string"}, "start_time_zone": {"type":    
                             "string"}, "end_datetime": {"type": "string"},     
                             "end_time_zone": {"type": "string"}, "title":      
                             {"type": "string"}, "description": {"type":        
                             "string"}, "attendees": {"type": "array"},         
                             "location": {"type": "string"}}}}}}                
[10/04/23 14:02:43] INFO     Subtask 46ed5976c6374ed6a8aa474470432971           
                             Observation: {'start_datetime':                    
                             '2023-10-04T16:00:00-07:00', 'start_time_zone':    
                             'America/Los_Angeles', 'end_datetime':             
                             '2023-10-04T17:00:00-07:00', 'end_time_zone':      
                             'America/Los_Angeles', 'title': 'Have to meet      
                             clients for design review', 'description': '',     
                             'attendees': [], 'location': 'Malibu, CA, USA'}    
[10/04/23 14:02:52] INFO     ToolkitTask 83fb147c05534d2c9de83b2cdf3f66ef       
                             Output: The next upcoming event on your primary    
                             calendar is titled "Have to meet clients for design
                             review". It is scheduled to start at 4:00 PM on    
                             October 4, 2023, and end at 5:00 PM on the same    
                             day. The event will take place in Malibu, CA, USA. 
                             The time zone for the event is America/Los_Angeles.
                             There are no attendees listed for this event.   
```
