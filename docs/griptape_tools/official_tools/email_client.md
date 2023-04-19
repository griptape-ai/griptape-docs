# EmailClient

This tool enables LLMs to send emails.

```python
email_client = EmailClient(
    host=config("SMTP_HOST"),
    port=config("SMTP_PORT"),
    password=config("SMTP_PASSWORD"),
    from_email=config("FROM_EMAIL"),
    use_ssl=config("SMTP_USE_SSL", cast=bool)
)
```

For debugging purposes, you can run a local SMTP server that the LLM can send emails to:

```shell
python -m smtpd -c DebuggingServer -n localhost:1025
```
