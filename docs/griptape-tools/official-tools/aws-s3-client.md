# AwsS3Client

This tool enables LLMs to make AWS S3 API requests.

```python
import boto3
from griptape.tools import AwsS3Client
from griptape.memory.tool import TextToolMemory

memory = TextToolMemory()

AwsS3Client(
    session=boto3.Session(),
    input_memory=[memory]
)
```
