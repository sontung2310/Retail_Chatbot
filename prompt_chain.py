def generate_sql_prompt(entity_dict):
    dict_temp = '{"purpose":"Design", "final_price":"lower than 1500"}'
    prompt = f'''### System: Your role is generating SQL query to interact with SQLite3 database.
### Instruction: You receive input which is the Dictionary of entity. You need to based on that dictionary to generate appropriate SQL query sentence to run correctly in SQLite3.
### Fewshot:
```
Dictionary of entity: {dict_temp}
SQL query: SELECT * FROM laptop WHERE purpose = 'Design' and final_price < 1500
```
### Dictionary of entity: {entity_dict}
### SQL query: SELECT * FROM laptop WHERE'''
    return prompt

def extract_entity_prompt(utterance):
    dict_temp = '{"Brand":"Asus", "purpose":"Gaming"}'
    prompt = f'''### System: Your role is extracting entity based on provided field.
### Instruction: You receive input as an user utterence. You need to extract exactly the entity appeared in input utterance. The entities you need to check including "Brand", "Laptop_name","final_price","RAM","CPU","GPU","Storage type","purpose".
There are 3 purpose: [Gaming, Design, Office].
Brand field have values such as: ["Asus","Macboook","MSI","Razer","Lenovo"...]
RAM field have values such as: [16,32,64]
CPU field have values such as: [Intel Core i7, Intel Core i5...]
GPU field have values such as: [RTX 3080, RTX 4080, RTX 4060, No...]
### Fewshot:
```
User utterence: I want to find an Asus laptop which strong enough to play computer game.
Dictionary of entity: {dict_temp}
```
### User utterence: {utterance}
### Dictionary of entity:
'''
    return prompt

def classify_intent_prompt(utterance):
    prompt = f'''### System: Please act as a robust and well-trained intent classifier that can identify the most likely PRECISE, SHORT and GENERIC intent behind a user's query WITHOUT USING the proper and common noun subject from the user's query.
### Instruction: You need to classify intent of user utterance into one of two those intents: ['ChitChat', 'AskForRecommend']. Intent 'AskForRecommend' is used when customer ask for LAPTOP recommendation. If user ask for something not related to laptop recommendation, it is ChitChat intent.
### Fewshot:
```
===
User utterence: Find me a MSI laptop which price less than 500, for my children to study.
Intent: AskForRecommend
===
User utterence: Where your store located?
Intent: ChitChat
```
### User utterence: {utterance}
### Intent:
'''
    return prompt

def consult_prompt(utterance, markdown_product):
    prompt = f'''###System: Please act as a consultant of a laptop store. Your role is provide the appropriate recommendation to user/customer
### Instruction: You need to recommend suitable products to user based on their utterance and provided products in form of markdown. It will be better if you recommend more than one options to user.
### User utterence: {utterance}
### Provied product: {markdown_product}
### Consultant:'''
    return prompt

def answer_chitchat_prompt(utterance):
    prompt = f'''###System: Please act as a consultant of a laptop store named 'Deakin laptop store' which located in Waurn Ponds. Answer user utterance in natural and friendly way
### User utterence: {utterance}
### Answer:'''
    return prompt