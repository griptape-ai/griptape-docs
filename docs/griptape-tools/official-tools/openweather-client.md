# OpenWeatherClient

The [OpenWeatherClient](../../reference/griptape/tools/openweather_client/tool.md) enables LLMs to use [OpenWeatherMap](https://openweathermap.org/).

```python
import os
from griptape.structures import Agent
from griptape.tools import OpenWeatherClient

agent = Agent(
    tools=[
        OpenWeatherClient(
            api_key=os.environ["OPENWEATHER_API_KEY"],
        )
    ]
)

agent.run("What's the weather currently like in San Francisco?")
```

```
[10/09/23 12:10:09] INFO     ToolkitTask fa8afb111a1a459cb89c48d365126f61
                             Input: What's the weather currently like in San Francisco?
[10/09/23 12:10:15] INFO     Subtask f8c0d2a64e1b483a8c9c329aa7e4b41d
                             Thought: I need to use the OpenWeatherClient tool to get the current weather in San Francisco. The
                             activity I should use is get_current_weather_by_location.
                             Action: {"type": "tool", "name": "OpenWeatherClient", "activity":
                             "get_current_weather_by_location", "input": {"values": {"location": "San Francisco"}}}
[10/09/23 12:10:16] INFO     Subtask f8c0d2a64e1b483a8c9c329aa7e4b41d
                             Observation: Output of "OpenWeatherClient.get_current_weather_by_location" was stored in memory
                             with memory_name "TextToolMemory" and artifact_namespace "edac2a72989249608320c323c6837ee8"
[10/09/23 12:10:33] INFO     Subtask abcf39cbaaf5400c8625f1552bd3d2d9
                             Thought: The weather data is stored in memory. I need to extract this data using the TextToolMemory
                             tool with the extract_json_objects activity. The memory_name is "TextToolMemory" and the
                             artifact_namespace is "edac2a72989249608320c323c6837ee8". The JSON schema I need to extract is the
                             weather data, which includes "temperature", "humidity", "wind_speed", and "description".
                             Action: {"type": "memory", "name": "TextToolMemory", "activity": "extract_json_objects", "input":
                             {"values": {"memory_name": "TextToolMemory", "artifact_namespace":
                             "edac2a72989249608320c323c6837ee8", "json_schema": {"type": "object", "properties": {"temperature":
                             {"type": "number"}, "humidity": {"type": "number"}, "wind_speed": {"type": "number"},
                             "description": {"type": "string"}}, "required": ["temperature", "humidity", "wind_speed",
                             "description"]}}}}
[10/09/23 12:10:36] INFO     Subtask abcf39cbaaf5400c8625f1552bd3d2d9
                             Observation: {'temperature': 64.11, 'humidity': 78, 'wind_speed': 4.61, 'description': 'broken
                             clouds'}
[10/09/23 12:10:39] INFO     ToolkitTask fa8afb111a1a459cb89c48d365126f61
                             Output: The current weather in San Francisco is 64.11°F with a humidity of 78%. The wind speed is
                             4.61 mph and the sky is covered with broken clouds.
```
