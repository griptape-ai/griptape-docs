# Griptape Docs

Welcome to Griptape Docs!

This documentation covers the fundamentals of the **griptape** framework and describes how to use **griptape-tools**.

## griptape

**griptape** is a modular Python framework for LLM workflows, tools, memory, and data that enables developers to:

1. 🤖 Build **AI agents**, sequential **LLM pipelines** and sprawling **DAG workflows** for complex use cases.
2. ⛓️ Augment LLMs with **chain of thought** capabilities.
3. 🧰️ Integrate other services and functionality into LLMs as [tools](https://github.com/griptape-ai/griptape-tools) (e.g., calculators, web scrapers, spreadsheet editors, and API connectors); run tools in any environment (local, containerized, cloud, etc.); use tools directly in **griptape** or convert them into middleware abstractions, such as ChatGPT Plugins, LangChain tools, or Fixie.ai agents.
4. 💾 Add **memory** to AI pipelines for context preservation and summarization.

[Learn more about griptape →](griptape-framework/)

## griptape-tools

**griptape-tools** is an official collection of tools built for **griptape**. You can run Griptape tools in **griptape**, [LangChain](https://github.com/hwchase17/langchain), or as [ChatGPT Plugins](https://platform.openai.com/docs/plugins/introduction). Griptape tools are a great way to start using Griptape to see how easy it can be to build applications that extend the capabilities of LLMs. If you have an OPEN AI API KEY, you can be up and running in a few minutes with Griptape using our [QuickStart Guide](griptape-tools/index.md).

| Tool      | Description                          |  
| ----------- | ------------------------------------ |
| [AWS CLI](griptape-tools/official-tools/aws_cli.md)  | This tool allows the LLM to invoke AWS CLI commands restricted by a policy. |
| [Calculator](griptape-tools/official-tools/calculator.md)       | An exmaple of a simple tool that the LLM can use for basic mathematical calculations.  | 
| [Email Client](griptape-tools/official-tools/email_client.md)    | The EmailClient tool gives the LLM access to send emails using SMTP or search a mailbox using IMAP |
| [SQL Client](griptape-tools/official-tools/sql_client.md) | The SQL Client tool gives the LLM access to execute SQL queries on a give DB or `engine` |
| [Web Search](griptape-tools/official-tools/web_search.md) | The Web Seach tools allows the LLM to make search engine queries to forumate better output |
| [Web Scraper](griptape-tools/official-tools/web_scraper.md) | The Web Scraper tool gives the LLM access to scrape a webpage for things like the title, the full page, or keyword searches within the page |

[Learn more about griptape tools →](griptape-tools/)