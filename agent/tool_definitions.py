TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "fetch_url",
            "description": "Fetches the content of a URL. Use this to read official Python or React documentation pages before answering.",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "The full URL to fetch, e.g. https://react.dev/reference/react/useEffect"
                    }
                },
                "required": ["url"]
            }
        }
    }
]