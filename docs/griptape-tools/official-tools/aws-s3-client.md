# AwsS3Client

This tool enables LLMs to make AWS S3 API requests.

```python
memory = TextToolMemory()

AwsS3Client(
    session=boto3.Session(),
    input_memory=[memory]
)
```
