# AwsIamClient

This tool enables LLMs to make AWS IAM API requests.

```python
import boto3
from griptape.tools import AwsIamClient

AwsIamClient(
    session=boto3.Session()
)
```
