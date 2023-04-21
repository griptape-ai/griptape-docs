This driver uses [Hugging Face Pipelines](https://huggingface.co/docs/transformers/main_classes/pipelines) for inference locally. It supports models with the following tasks:

- text2text-generation
- text-generation

The **HuggingFacePipelinePromptDriver** uses the following parameters:

| Parameter | Description                    | Required |
|-----------|--------------------------------|----------|
| model     | Hugging Face model name.       | YES      |
| params    | Custom model run parameters.   | NO       |
| tokenizer | Custom `HuggingFaceTokenizer`. | NO       |