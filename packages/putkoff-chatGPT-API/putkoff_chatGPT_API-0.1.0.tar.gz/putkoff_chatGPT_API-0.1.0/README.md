## putkoff_chatGPT_API

`putkoff_chatGPT_API` is a Python module for interacting with OpenAI's GPT models. It simplifies the process of making API calls, managing API keys, and parsing responses, while also providing utility functions to work with timestamps and organize response data.

### Features

- Supports multiple GPT models and endpoints
- Automatically manages API keys using dotenv
- Generates prompts and handles token size restrictions
- Parses responses and handles JSON data
- Provides utility functions for timestamps and date formatting
- Organizes response data in a structured manner
- Includes a simple GUI for user interaction

### Usage

To use the module, import it and call the `send_query` function with the necessary parameters, such as prompt, endpoint, model, and max tokens. The module will handle the API call, process the response, and return the results.

Example:

```python
from putkoff_chatGPT_API import send_query

# Set up parameters
prompt = "What is the capital of France?"
endpoint = "/v1/chat/completions"
model = "gpt-3.5-turbo"
max_tokens = 50

# Send the query
response = send_query(prompt, endpoint, model, max_tokens)

# Process the response as needed
print(response)
# putkoff_chatGPT_API
