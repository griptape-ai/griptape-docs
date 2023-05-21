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