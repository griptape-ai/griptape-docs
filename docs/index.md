# Griptape Docs

Welcome to Griptape Docs!

This documentation covers the fundamentals of the **Griptape** framework and describes how to use **Griptape Tools**.

## Griptape

The Griptape framework provides developers with the ability to create AI systems that operate across two dimensions: predictability and creativity. For predictability, Griptape enforces structures like sequential pipelines, DAG-based workflows, and long-term memory. To facilitate creativity, Griptape safely prompts LLMs with tools (keeping output data off prompt by using short-term memory), which connects them to external APIs and data stores. The framework allows developers to transition between those two dimensions effortlessly based on their use case.

Griptape not only helps developers harness the potential of LLMs but also enforces trust boundaries, schema validation, and tool activity-level permissions. By doing so, Griptape maximizes LLMs’ reasoning while adhering to strict policies regarding their capabilities.

[Learn more about griptape →](griptape-framework/)

## Griptape Tools

Griptape Tools a great way to start using Griptape to see how easy it can be to build applications that extend LLMs' creative capabilities. Agents (or any other structure for that matter) can be used to connect your pre-processed data to LLMs via tools. Griptape tools are Python classes with activities. Activities are Python methods decorated with the @activity decorator. Each activity has a description (used to provide context to the LLM) and the input schema that the LLM must follow in order to use the tool. Griptape validates LLM outputs against the schema to ensure each tool activity is used correctly.

[Learn more about griptape tools →](griptape-tools/)

## Examples

Check out Griptape examples for building agents, data retrieval, and more.

[Checkout Griptape examples →](examples/)

## Reference

[Griptape Reference→](reference/)
