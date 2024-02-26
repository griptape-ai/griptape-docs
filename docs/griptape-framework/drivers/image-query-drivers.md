# Image Query Drivers

Image Query Drivers are used by [Image Query Engines](../engines/image-query-engines.md) to execute natural language queries on the contents of images. You can specify the provider and model used to query the image by providing the Engine with a particular Image Query Driver.

## OpenAiVisionImageQueryDriver

!!! info
    This Driver defaults to using the `gpt-4-vision-preview` model. As other multimodal models are released, they can be specified using the `model` field. While the `max_tokens` field is optional, it is recommended to set this to a value that corresponds to the desired response length. Without an explicit value, the model will default to very short responses. See [OpenAI's documentation](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them) for more information on how to relate token count to response length.

The [OpenAiVisionImageQueryDriver](../../reference/griptape/drivers/image_query/openai_vision_image_query_driver.md) is used to query images using the OpenAI Vision API. Here is an example of how to use it:

```python
from griptape.drivers import OpenAiVisionImageQueryDriver
from griptape.engines import ImageQueryEngine
from griptape.loaders import ImageLoader

driver = OpenAiVisionImageQueryDriver(
    model="gpt-4-vision-preview",
    max_tokens=200,
)

engine = ImageQueryEngine(
    image_query_driver=driver,
)

with("tests/assets/mountain.png", "rb") as f:
    image_artifact = ImageLoader().load(f.read())

engine.run("Describe the weather in the image", [image_artifact])
```

