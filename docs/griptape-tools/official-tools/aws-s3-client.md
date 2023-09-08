# AwsS3Client

This tool enables LLMs to make AWS S3 API requests.

```python
import boto3
from griptape.structures import Agent
from griptape.tools import AwsS3Client

# Initialize the AWS S3 client
aws_s3_client = AwsS3Client(session=boto3.Session())

# Create an agent with the AWS S3 client tool
agent = Agent(
    tools=[aws_s3_client]
)

# Run the agent with a specific task to list all the AWS S3 buckets
buckets_response = agent.run("list all AWS S3 buckets")

# Print out all listed buckets
for bucket in buckets_response:
    print(bucket)

# Get ACL for a specific bucket, let's assume the bucket's name is 'my-sample-bucket'
acl_response = agent.run({
    "bucket_name": "my-sample-bucket",
    "description": "get an access control list (ACL) of an AWS S3 bucket"
})

print(acl_response)
```
