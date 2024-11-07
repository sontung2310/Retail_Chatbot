from openai import OpenAI
from flask import Flask, request, jsonify
import argparse



app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Flask API!"

@app.route('/api/messages', methods=['POST'])
def bot_endpoint():
    data = request.get_json()
    query = data.get('query')
    print("Query: ",query)
    # if not user_message:
    #     return jsonify({'error': 'No message provided'}), 400
    try:
        response = client.chat.completions.create(
          model=MODEL,
          messages=[
            {"role": "user", "content": query}
          ]
        )
        # response = base_model.complete(query=query, max_generated_token_count=500).generated_output
        return jsonify({'type': 'message', 'text': response.choices[0].message.content, 'from':{'id':'3ec2cdef-8925-41d9-a859-7996cec05093', 'role':'system'}}), 200
        # return jsonify({'message': [{'role':'system', 'content':response}]}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=5001, help='Specify the port number')
    parser.add_argument('--openai_key', type=str, help='Specify OpenAI key')

    args = parser.parse_args()

    port_num = args.port
    client = OpenAI(api_key=args.openai_key)
    MODEL="gpt-3.5-turbo"
    # print("Starting Llama bot...\n This may take a while.")
    # prepareLlamaBot()
    print(f"App running on port {port_num}")
    app.run(port=port_num)

# completion = client.chat.completions.create(
#   model=MODEL,
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant that helps me with my math homework!"},
#     {"role": "user", "content": "Hello! Could you solve 20 x 5?"}
#   ]
# )
# print("Assistant: " + completion.choices[0].message.content)

# import os
# import azure.cognitiveservices.speech as speechsdk


# def recognize_from_microphone():
#     # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
#     speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
#     speech_config.speech_recognition_language="en-US"

#     audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
#     speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

#     print("Speak into your microphone.")
#     speech_recognition_result = speech_recognizer.recognize_once_async().get()

#     if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
#         print("Recognized: {}".format(speech_recognition_result.text))
#     elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
#         print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
#     elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
#         cancellation_details = speech_recognition_result.cancellation_details
#         print("Speech Recognition canceled: {}".format(cancellation_details.reason))
#         if cancellation_details.reason == speechsdk.CancellationReason.Error:
#             print("Error details: {}".format(cancellation_details.error_details))
#             print("Did you set the speech resource key and region values?")

# recognize_from_microphone()
# import requests
# import json

# url = 'http://127.0.0.1:5001/api/messages'

# prompt = '''### System: Your role is generating SQL query to interact with SQLite3 database.
# ### Instruction: You receive input which is the Dictionary of entity. You need to based on that dictionary to generate appropriate SQL query sentence to run correctly in SQLite3.
# ### Fewshot:
# ```
# Dictionary of entity: {"purpose":'Design', "price":"lower than 1500"}
# SQL query: SELECT * FROM new_laptop_csv WHERE purpose = 'Design' and final_price < 1500
# ```
# ### Dictionary of entity: {"purpose":'Gaming', "Brand":"Asus"}
# ### SQL query: SELECT * FROM new_laptop_csv WHERE'''

# payload = {
#             'query': prompt
#         }

# headers = {
#             'Content-Type': 'application/json'
#         }

# # Make the POST request
# response = requests.post(url, headers=headers, data=json.dumps(payload))

# # Check the response
# if response.status_code == 200:
#     print('Response:', response.json())
#     res = response.json()
#     answer = res.get('text')
# else:
#     print('Failed to get a response. Status code:', response.status_code)
#     print('Error:', response.text)

