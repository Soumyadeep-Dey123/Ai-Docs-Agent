from openai import OpenAI
import os
from dotenv import load_dotenv
from agent.prompts import SYSTEM_PROMPT
from agent.tool_definitions import TOOLS
from agent.tools import fetch_url
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)
messages = [
    {"role": "system", "content": SYSTEM_PROMPT},     
]

def chat(user_input: str) -> str:
    messages.append({"role": "user", "content": user_input})

    # print the messages in a readable format
    print(f"Messages till now: {messages}", end="")

    # Round 1 — send messages + available tools
    response = client.chat.completions.create(
        model="openai/gpt-oss-safeguard-20b",
        messages=messages,
        tools=TOOLS,
        tool_choice="auto"  # model decides whether to use a tool or not
    )

    message = response.choices[0].message
    
    # Check if the model wants to call a tool
    if message.tool_calls:
        for tool_call in message.tool_calls:
            tool_name = tool_call.function.name
            tool_args = json.loads(tool_call.function.arguments)

            print(f"\n[fetching {tool_args['url']}...]\n")

            # Execute the tool
            if tool_name == "fetch_url":
                tool_result = fetch_url(tool_args["url"])

            # Append model's tool call + your tool result to messages
            messages.append(message)
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": tool_result
            })

        # Round 2 — send everything back, model now answers using the fetched content
        response = client.chat.completions.create(
            model="openai/gpt-oss-safeguard-20b",
            messages=messages,
            tools=TOOLS,
        )
        
        assistant_reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": assistant_reply})
        return assistant_reply

    # If no tool calls, just return the model's message
    messages.append({"role": "assistant", "content": message.content})
    # return the assistant's reply
    return message.content

def main():
    print("Agent ready. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "exit":
            print("Bye!")
            break

        response = chat(user_input)
        # response = chat("How to add two numbers in python")
        print(f"\nAgent: {response}\n")


if __name__ == "__main__":
    main()
