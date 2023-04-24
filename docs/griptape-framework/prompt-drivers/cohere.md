This driver connects to Cohere [Generate](https://docs.cohere.ai/reference/generate) API..

The **CoherePromptDriver** uses the following parameters:

| Parameter | Description                              | Required |
|-----------|------------------------------------------|----------|
| api_key   | Cohere API key.                          | YES      |
| model     | Cohere model name. Defaults to `xlarge`. | NO       |
| client    | Custom `cohere.Client`.                  | NO       |
| tokenizer | Custom `CohereTokenizer`.                | NO       |