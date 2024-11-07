import pandas as pd
import sqlite3
import csv


def create_purpose(row):
    gpu = row['GPU']
    if gpu == 'No':
        return 'Office'
    if '4050' in gpu or '4060' in gpu or '4070' in gpu:
        return 'Design'
    else:
        return 'Gaming'

# Read the CSV file into a DataFrame
# csv_file_path = "/Users/sontung/Desktop/project/chatbot/test-bot/new_laptop_csv.csv"
# df = pd.read_csv(csv_file_path)
# df = df.drop(['id'],axis=1)
# df.to_csv('new_laptop_csv.csv',index=False)

# Upload to sqlite3

import sqlite3
# Connecting to the laptop database
connection = sqlite3.connect('laptop.db')
cursor = connection.cursor()

# Table Definition
create_table = '''CREATE TABLE laptop(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Laptop TEXT NOT NULL,
                Status TEXT NOT NULL,
                Brand TEXT NOT NULL,
                Model TEXT NOT NULL,
                CPU TEXT NOT NULL,
                RAM TEXT NOT NULL,
                Storage INTEGER NOT NULL,
                Storage_type TEXT NOT NULL,
                GPU INTEGER NOT NULL,
                Screen FLOAT NOT NULL,
                Touch TEXT NOT NULL,
                Final_Price INTEGER NOT NULL,
                purpose TEXT NOT NULL
                );
                '''
# # Creating the table into our 
# # database
# cursor.execute(create_table)
file = open('/Users/sontung/Desktop/project/chatbot/test-bot/new_laptop_csv.csv')
 
# Reading the contents of the 
# person-records.csv file
contents = csv.reader(file)
 
# SQL query to insert data into the laptop table
insert_records = "INSERT INTO laptop (Laptop, Status, Brand, Model, CPU, RAM, Storage, Storage_type, GPU, Screen, Touch, Final_Price, purpose) \
    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
 
# Importing the contents of the file into our laptop table
cursor.executemany(insert_records, contents)
select_all = "SELECT * FROM laptop"
rows = cursor.execute(select_all).fetchall()
 
# Output to the console screen
for r in rows:
    print(r)
 
# Committing the changes
connection.commit()
 
# closing the database connection
connection.close()

# df = pd.read_csv(csv_file_path)
# df['GPU'] = df['GPU'].fillna('No')
# df = df.reset_index().rename(columns={'index': 'id'})
# df['id'] = df['id'].astype(str)
# df['purpose'] = df.apply(create_purpose, axis=1)

# df.to_csv('new_laptop_csv.csv',index=False)
# # Convert DataFrame to a list of dictionaries (documents)
# documents = df.to_dict(orient='records')
# # Function to clean and validate documents
# def clean_and_validate_documents(docs):
#     cleaned_docs = []
#     for doc in docs:
#         # Convert all keys to strings and ensure proper JSON formatting
#         cleaned_doc = {str(k): (v if pd.notna(v) else None) for k, v in doc.items()}
#         cleaned_docs.append(cleaned_doc)
#     return cleaned_docs

# # Clean and validate the documents
# cleaned_documents = clean_and_validate_documents(documents)
# # print("Doc",documents)
# # Upload documents to the index
# try:
#     result = search_client.upload_documents(documents=cleaned_documents)
#     print(f"Upload result: {result}")
# except Exception as e:
#     print(f"Document upload failed: {e}")
