This page summarizes questions we were asked on [Discord](https://discord.gg/gnWRz88eym), Hacker News, and Reddit. Feel free to post a question to [Discord](https://discord.gg/gnWRz88eym) or open a discussion on our [Github Page](https://github.com/griptape-ai) or hit us up directly: [hello@griptape.ai](mailto:hello@griptape.ai). 

## 1. How is Griptape different from LangChain?

Griptape is an open source alternative to LangChain and differs in its approach to creating LLM pipelines and DAGs. In addition to agents, it uses more general-purpose DAGs and pipelines. A close proxy might be *Airflow for LLMs*. Griptape still implements chain of thought logic for prompt tasks that use "tools" but it also supports any type of input / output (images, audio, etc.). 

## 2. How are Griptape tools different from tools in LangChain?

Griptape Tools are designed to be decoupled from the caller logic and execution environments. For example, tools can be easily run in a Docker container or a Lambda function (as opposed to carelessly running LLM-generated Python code on a laptop or server). 

Tools can also be plugged into other LLM frameworks through Griptape Adapters. For example, you can convert any Griptape tool into a LangChain tool or generate a ChatGPT Plugin API with a single line of Python code. 

