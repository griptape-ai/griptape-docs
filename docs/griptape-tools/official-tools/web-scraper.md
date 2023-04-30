# WebScraper

This tool enables LLMs to scrape web pages for full text, summaries, authors, titles, and keywords. It can also execute search queries to answer specific questions about the page. This tool uses OpenAI APIs for some of its activities, so in order to use it provide a valid API key in `openai_api_key`.

```python
WebScraper(
    openai_api_key=config("OPENAI_API_KEY")
)
```