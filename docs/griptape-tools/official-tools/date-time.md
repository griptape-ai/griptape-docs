# DateTime

This tool enables LLMs to get current date and time.

```python
from griptape.structures import Agent
from griptape.tools import DateTime

# Initialize the DateTime tool
datetime_tool = DateTime()

# Create an agent with the DateTime tool
agent = Agent(
    tools=[datetime_tool]
)

# Fetch the current date and time
agent.run({
    "description": "What is the current date and time?"
})
```
```
[09/11/23 15:26:02] INFO     Task d0bf49dacd8849e695494578a333f6cc              
                             Input: {'description': 'What is the current date   
                             and time?'}                                        
[09/11/23 15:26:06] INFO     Subtask 1c6c8d43926d4eff81992886301d5655           
                             Thought: The user wants to know the current date   
                             and time. I can use the DateTime tool with the     
                             get_current_datetime activity to find this         
                             information.                                       
                                                                                
                             Action: {"type": "tool", "name": "DateTime",       
                             "activity": "get_current_datetime"}                
                    INFO     Subtask 1c6c8d43926d4eff81992886301d5655           
                             Observation: 2023-09-11 15:26:06.767997            
[09/11/23 15:26:08] INFO     Task d0bf49dacd8849e695494578a333f6cc              
                             Output: The current date and time is September 11, 
                             2023, 15:26:06.
```