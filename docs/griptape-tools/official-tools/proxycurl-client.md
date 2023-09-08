# ProxycurlClient

The ProxycurlClient tool is a tool for interacting with the [Proxycurl API](https://proxycurl.com/).

```python
from griptape.tools import ProxycurlClient
from griptape.structures import Agent
from griptape.artifacts import ErrorArtifact

# Create the ProxycurlClient tool
proxycurl_tool = ProxycurlClient(
    proxycurl_api_key="YOUR_PROXYCURL_API_KEY"
)

# Set up an agent using the ProxycurlClient tool
agent = Agent(
    tools=[proxycurl_tool]
)

# Task: Fetch LinkedIn profile information
profile_result = agent.run({
    "description": "Get LinkedIn profile",
    "tool": "ProxycurlClient",
    "activity": "get_profile",
    "values": {
        "profile_id": "PROFILE_ID"  # replace PROFILE_ID with actual profile id
    }
})

if isinstance(profile_result, ErrorArtifact):
    print(f"Error occurred: {profile_result}")
else:
    print(f"Profile Data: {profile_result.data}")
```