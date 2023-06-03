# Prompt Drivers

Prompt drivers are used by Griptape structures to make calls to the underlying foundation models. **OpenAiPromptDriver** is the default prompt driver used in all structures.

You can instantiate drivers and pass them to structures:

```python
Pipeline(
    prompt_driver=OpenAiPromptDriver(
        model="gpt-4"
    )
)
```

Or use them independently:

```python
OpenAiPromptDriver(
    model="gpt-4"
).run("Q: give me some ideas for writing a fantasy book\nA:")
```

## OpenAI

This driver connects to OpenAI [Text Completion](https://platform.openai.com/docs/guides/completion) and [Chat Completion](https://platform.openai.com/docs/guides/chat) APIs.

The **OpenAiPromptDriver** uses the following parameters:

| Parameter    | Description                                                                           | Required |
|--------------|---------------------------------------------------------------------------------------|----------|
| api_type     | Can be changed to use OpenAI models on Azure.                                         | NO       |
| api_version  | API version.                                                                          | NO       |
| api_base     | API URL.                                                                              | NO       |
| api_key      | API key to pass directly; by default uses `OPENAI_API_KEY_PATH` environment variable. | NO       |
| organization | OpenAI organization.                                                                  | NO       |
| tokenizer    | Custom `TiktokenTokenizer`                                                            | NO       |
| user         | OpenAI user.                                                                          | NO       |

## Cohere

This driver connects to Cohere [Generate](https://docs.cohere.ai/reference/generate) API..

The **CoherePromptDriver** uses the following parameters:

| Parameter | Description                              | Required |
|-----------|------------------------------------------|----------|
| api_key   | Cohere API key.                          | YES      |
| model     | Cohere model name. Defaults to `xlarge`. | NO       |
| client    | Custom `cohere.Client`.                  | NO       |
| tokenizer | Custom `CohereTokenizer`.                | NO       |

## Hugging Face Hub

This driver connects to the [Hugging Face API](https://huggingface.co/docs/hub/api). It supports models with the following tasks:

* text2text-generation
* text-generation

The **HuggingFaceHubPromptDriver** uses the following parameters:

| Parameter | Description                    | Required |
|-----------|--------------------------------|----------|
| repo_id   | Repository ID on Hugging Face. | YES      |
| api_token | Hugging Face Hub API token     | YES      |
| use_gpu   | Use GPU during model run.      | NO       |
| params    | Custom model run parameters.   | NO       |
| model     | Custom `CohereTokenizer`.      | NO       |
| client    | Custom `InferenceApi`.         | NO       |
| tokenizer | Custom `HuggingFaceTokenizer`. | NO       |

## Hugging Face Pipeline

This driver uses [Hugging Face Pipelines](https://huggingface.co/docs/transformers/main_classes/pipelines) for inference locally. It supports models with the following tasks:

* text2text-generation
* text-generation

The **HuggingFacePipelinePromptDriver** uses the following parameters:

| Parameter | Description                    | Required |
|-----------|--------------------------------|----------|
| model     | Hugging Face model name.       | YES      |
| params    | Custom model run parameters.   | NO       |
| tokenizer | Custom `HuggingFaceTokenizer`. | NO       |