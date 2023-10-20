# AwsS3Client

This tool enables LLMs to make AWS S3 API requests.

```python
import boto3
from griptape.structures import Agent
from griptape.tools import AwsS3Client

# Initialize the AWS S3 client
aws_s3_client = AwsS3Client(
    session=boto3.Session()
)

# Create an agent with the AWS S3 client tool
agent = Agent(
    tools=[aws_s3_client]
)

# Task to list all the AWS S3 buckets
agent.run("List all my S3 buckets.")
```
```
[09/11/23 16:49:35] INFO     Task 8bf7538e217a4b5a8472829f5eee75b9              
                             Input: List all my S3 buckets.                     
[09/11/23 16:49:41] INFO     Subtask 9fc44f5c8e73447ba737283cb2ef7f5d           
                             Thought: To list all S3 buckets, I can use the     
                             "list_s3_buckets" activity of the "AwsS3Client"    
                             tool. This activity doesn't require any input.     
                                                                                
                             Action: {"type": "tool", "name": "AwsS3Client",    
                             "activity": "list_s3_buckets"}                     
[09/11/23 16:49:42] INFO     Subtask 9fc44f5c8e73447ba737283cb2ef7f5d           
                             Observation: Output of                             
                             "AwsS3Client.list_s3_buckets" was stored in memory 
                             with memory_name "ToolMemory" and              
                             artifact_namespace                                 
                             "f2592085fd4a430286a46770ea508cc9"                 
[09/11/23 16:49:50] INFO     Subtask 0e9bb639a432431a92ef40a8c085ca0f           
                             Thought: The output of the "list_s3_buckets"       
                             activity is stored in memory. I can retrieve this  
                             information using the "summarize" activity of the  
                             "ToolMemory" tool.                             
                             Action: {"type": "memory", "name":                 
                             "ToolMemory", "activity": "summarize", "input":
                             {"values": {"memory_name": "ToolMemory",       
                             "artifact_namespace":                              
                             "f2592085fd4a430286a46770ea508cc9"}}}              
[09/11/23 16:49:52] INFO     Subtask 0e9bb639a432431a92ef40a8c085ca0f           
                             Observation: The text consists of multiple         
                             dictionaries, each containing a 'Name' and         
                             'CreationDate' key-value pair. The 'Name'          
                             represents the name of a resource or bucket, while 
                             the 'CreationDate' represents the date and time    
                             when the resource or bucket was created.           
[09/11/23 16:50:03] INFO     Task 8bf7538e217a4b5a8472829f5eee75b9              
                             Output: The names of your S3 buckets are as        
                             follows:                                           
                             1. Bucket Name: 'example-bucket-1', Creation Date: 
                             '2022-01-01T00:00:00Z'                             
                             2. Bucket Name: 'example-bucket-2', Creation Date: 
                             '2022-01-02T00:00:00Z'                             
                             3. Bucket Name: 'example-bucket-3', Creation Date: 
                             '2022-01-03T00:00:00Z'                             
                             Please note that the creation dates are in UTC.  
```