# Griptape Docs

Welcome to Griptape Docs!

This documentation covers the fundamentals of the **Griptape** framework and describes how to use **Griptape Tools**.

## griptape-flow

**griptape-flow** is a Python framework for creating workflow DAGs and pipelines that use large language models (LLMs) such as GPT, Claude, Titan, and Cohere.

[Learn more about griptape-flow →](griptape_flow/)

## griptape-core

**griptape-core** is a Python framework that enables developers to integrate other services and functionality into LLMs as tools; run tools in any environment (local, containerized, cloud, etc.); convert tools into underlying middleware abstractions, such as ChatGPT Plugins, LangChain tools, and Fixie.ai agents.

[Learn more about griptape-core →](griptape_core/)

## griptape-tools

**griptape-tools** is an official collection of tools built with Griptape. You can run Griptape tools in [griptape-flow](griptape_flow/index.md), [LangChain](https://github.com/hwchase17/langchain), or as [ChatGPT Plugins](https://platform.openai.com/docs/plugins/introduction). Griptape tools are a great way to start using Griptape to see how easy it can be to build applications that extend the capabilities of LLMs. If you have an OPEN AI API KEY, you can be up and running in a few minutes with Griptape using our [QuickStart Guide](griptape_tools/index.md). 

| Tool      | Description                          |  
| ----------- | ------------------------------------ |
| [AWS CLI](griptape_tools/official_tools/aws_cli.md)  | This tool allows the LLM to invoke AWS CLI commands restricted by a policy. |
| [Calculator](griptape_tools/official_tools/calculator.md)       | An exmaple of a simple tool that the LLM can use for basic mathematical calculations.  | 
| [Email Client](griptape_tools/official_tools/email_client.md)    | The EmailClient tool gives the LLM access to send emails using SMTP or search a mailbox using IMAP |
| [SQL Client](griptape_tools/official_tools/sql_client.md) | The SQL Client tool gives the LLM access to execute SQL queries on a give DB or `engine` |
| [Web Search](griptape_tools/official_tools/web_search.md) | The Web Seach tools allows the LLM to make search engine queries to forumate better output |
| [Web Scraper](griptape_tools/official_tools/web_scraper.md) | The Web Scraper tool gives the LLM access to scrape a webpage for things like the title, the full page, or keyword searches within the page |