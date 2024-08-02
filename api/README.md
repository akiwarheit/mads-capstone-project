# How to run the API

```
python application.py -key {aws_access_key_id} -secret {aws_secret_access_key}
```

To test if it's working:

```
curl -X POST http://localhost:5000/ask -H "Content-Type: application/json" -d '{"question": "Tell me more about San Diego County"}'
```
