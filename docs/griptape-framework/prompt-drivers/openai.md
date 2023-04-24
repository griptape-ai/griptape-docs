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