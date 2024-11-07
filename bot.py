# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount
import requests
import json
from prompt_chain import *
from tabulate import tabulate
import sqlite3
import azure.cognitiveservices.speech as speechsdk


connection = sqlite3.connect('laptop.db')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

speech_key = 'YOUR_AZURE_SPEECH_KEY'
service_region = 'YOUR_AZURE_SPEECH_KEY_REGION'

# def test_query(input_text):
#     prompt = f'''
#     ### Instruction: Answer this sentence in natural way
#     ### Sentence: {input_text}
#     ### Answer:
#     '''
#     return prompt
def request_gpt_api(prompt):
    url = 'http://127.0.0.1:5001/api/messages'
    payload = {
            'query': prompt
        }
    headers = {
            'Content-Type': 'application/json'
        }

    # Make the POST request
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Check the response
    if response.status_code == 200:
        print('Response:', response.json())
        res = response.json()
        answer = res.get('text')
    else:
        print('Failed to get a response. Status code:', response.status_code)
        print('Error:', response.text)
    
    return answer

def convert_to_markdown(rows):
    if rows:
        headers = rows[0].keys()  # Correctly get the headers from the Row object
        data = [tuple(row) for row in rows]
        return tabulate(data, headers, tablefmt="github")
    else:
        return "No data available"


class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.
    def __init__(self):
        self.speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)


    async def on_message_activity(self, turn_context: TurnContext):
        if turn_context.activity.attachments:
            attachment = turn_context.activity.attachments[0]
            audio_url = attachment.content_url
            result = self.process_speech_input(audio_url)
            # Process speech 
            if result.reason == speechsdk.ResultReason.RecognizedSpeech:
                input_text = result.text
            else:
                answer = "Cannot process text file"
        else:
            # Process text input
            input_text = self.process_text_input(turn_context.activity.text)

        # turn_context.activity.text
        # Process RAG here
        # Extract Intent with prompt
        user_intent = request_gpt_api(prompt=classify_intent_prompt(input_text))
        print("User intent: ",user_intent)
        if 'ChitChat' in user_intent:
            print("ChitChat Intent")
            answer = request_gpt_api(prompt=answer_chitchat_prompt(input_text))
            # answer = 'ChitChat Intent'
        elif 'AskForRecommend' in user_intent:
            print('AskForRecommend Intent')
            # answer = 'AskForRecommend Intent'
        else:
            answer = 'Cannot find the intent of user. Ask user for more details'

        # If intent = recommendation
        if 'AskForRecommend' in user_intent:
            dict_entity = request_gpt_api(prompt=extract_entity_prompt(input_text))
            print(dict_entity)

            sql_query = request_gpt_api(prompt=generate_sql_prompt(dict_entity))
            print('SQL query: ',sql_query)
            # Convert text to sql
            full_query = f"SELECT * FROM laptop WHERE {sql_query} ORDER BY Final_Price DESC"
            # Query table in AI search
            rows = cursor.execute(full_query).fetchmany(3)
            markdown_table = convert_to_markdown(rows)
            print("Markdown table:\n",markdown_table)
            answer = request_gpt_api(prompt=consult_prompt(input_text, markdown_table))
        
            
        # get table head(5). Put into prompt to generate final answer. 
        await turn_context.send_activity(answer)
        # await turn_context.send_activity(f"You said '{ turn_context.activity.text }'")


    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")

    def process_text_input(self, input_text):       
        return input_text
    
    def process_speech_input(self, audio_url):
        audio_data = self.download_audio(audio_url)
        with open("temp_audio.wav", "wb") as f:
            f.write(audio_data)

        audio_config = speechsdk.audio.AudioConfig(filename="temp_audio.wav")
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=self.speech_config, audio_config=audio_config)
        
        result = speech_recognizer.recognize_once_async().get()
        return result

    def download_audio(self, audio_url: str) -> bytes:
        response = requests.get(audio_url)
        return response.content