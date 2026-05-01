# AI Docs Agent

Started: 2026-04-17 | Deadline: 2026-05-01

Goal: Build a project that answers questions about a certain framework(for now sticking to laravel) from their official docs official docs

## Progress

- [x] Stage 1 — Fetch a simple response from gemini api
- [x] Stage 2 — Creation of system prompt, structured answer display
- [x] Stage 3 — Feed extra data(manually) and display a structured response -> skipped
- [x] Stage 4 — Use a webscraper to fetch data and feed it along with the response
- [ ] Stage 5 — Make it agentic. Add thinking and add a way to store the fetched data(in a db)
- [x] Stage 6 — Work on memory, make the data available for later uses (only possible during one chat session)
- [ ] Stage 7 — Improve responses, make it produce and retain more info

## Outcome

- Did the entire project by myself and understood what i didnt, previously
- Using basic openai sdk, an object is created, containing api endpoint and key, an api call gets established. Things like model name, messages, and optionally list of tools and `tool_choice` argument is passed. `client.chat.completions.create` makes the api call possible.
- In a chat, the memory is mostly stored inside of a list named message, different types of messages like the `system_prompt`, user prompt, whatever the assistant(or ai) generated.
- The response contains a lot of info, but the main part of the response is stored in `response.choices[0].message`
- Tool/function calling in llms (generative/agentic ai) happens when functions created with specific purpose (simple python methods in this case), are made available to the llm. The llm chooses if it needs to use any function, and if it does, the response is re-fed into a loop, where it gets dissected into individual variables, and then the python script makes the call, and then the response is given to the ai again and it generates the final output
- And all of this happens, as per the guardrails in `system_prompt`, and the messages stored in the `messages` list variable.
- The only thing left was a way to store this data into a db or somewhere, which would make it re-fecthable and make it reusbale for the model
- Another important thing was the fact that too many tokens were getting used (most probably), which needed to be solved

---

[Reference Output file](./docs/ai-final-output.md)

---

> Made using uv, python  
> _By - Soumyadeep Dey_
