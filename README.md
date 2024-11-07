Building Chatbot for Laptop store/ E-commerce
=======

## Chatbot description
- Recommend an appropriate laptop based on the customer's desires. Users send their requirements or the features they are looking for in a laptop, and the chatbot will recommend some options and explain why those products are suitable.
- Engage in chit-chat, interact with users, and answer questions that are not related to the laptop domain.
- The chatbot can interact with users through both text and voice.

## Flow chart of Chatbot
![Alt text](images/Chatbot_pipeline.png?raw=true "Chatbot workflow")

## How to run the Chatbot:
- Run `pip install -r requirements.txt` to install all dependencies
- Run `python get_api.py --openai_key="YOUR_OPENAPI_KEY"` to start the LLM part which will answer the user's question
- In `bot.py`, fill line 18 and 19 with your own AZURE_SPEECH_KEY and AZURE_SPEECH_REGION
- Run `python app.py` to start the Chatbot


## Testing the bot using Bot Framework Emulator

[Bot Framework Emulator](https://github.com/microsoft/botframework-emulator) is a desktop application that allows bot developers to test and debug their bots on localhost or running remotely through a tunnel.

- Install the Bot Framework Emulator version 4.3.0 or greater from [here](https://github.com/Microsoft/BotFramework-Emulator/releases)

### Connect to the bot using Bot Framework Emulator

- Launch Bot Framework Emulator
- Enter a Bot URL; for example `http://localhost:3978/api/messages`


## Screenshot of Demo
- When input is text:
![Alt text](images/Text_input.png?raw=true "User ask Chatbot with text")

- When input is speech:
![Alt text](images/Speech_input.png?raw=true "User ask Chatbot with speech")
>>>>>>> 27ab232 (First commit)
>>>>>>> 981142d (Chatbot version 1)
