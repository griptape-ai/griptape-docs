# AwsIamClient

This tool enables LLMs to make AWS IAM API requests.

```python
import boto3
from griptape.structures import Agent
from griptape.tools import AwsIamClient

# Initialize the AWS IAM client
aws_iam_client = AwsIamClient(session=boto3.Session())

# Create an agent with the AWS IAM client tool
agent = Agent(
    tools=[aws_iam_client]
)

# Run the agent with a high-level task
responses = agent.run(
    "List all users in AWS IAM"
)

for resp in responses:
    print(resp)
```
