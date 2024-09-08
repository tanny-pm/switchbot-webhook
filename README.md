Cloud FunctionsでSwitchbotのWebhookを受け取る
https://zenn.dev/tanny/articles/e03e28d1bbd37b

# Usage

1. Install `uv`

2. Setup `.env`
```
SWITCHBOT_ACCESS_TOKEN=
SWITCHBOT_SECRET=
WEBHOOK_URL=
```

3. Run Python script

```sh
❯ cd src/switchbot_webhook                                               

❯ uv run webhook.py setup                                                 
{'statusCode': 100, 'body': {}, 'message': 'success'}

❯ uv run webhook.py query                                                 
{'statusCode': 100, 'body': {'urls': ['https://ADDRESS/test-webhook']}, 'message': 'success'}

❯ uv run webhook.py delete                                                
{'statusCode': 100, 'body': {}, 'message': 'success'}
```

### Reference
- https://github.com/OpenWonderLabs/SwitchBotAPI?tab=readme-ov-file#webhook