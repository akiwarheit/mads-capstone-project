# How to run the API

```
python app.py
```

You can then test it using the following command:

```
curl -X POST http://localhost:5000/ask -H "Content-Type: application/json" -d '{"question": "What is the median family income in East Machias town, Maine?"}'
```
