import pandas as pd

with open('tweets.json', 'r') as file:
    data = pd.read_json(file)

to_search = input("Anahtar kelime : ")

query_result = data['links'].apply(lambda x: to_search in x.get('otherPropertiesMap', {}).get('tweet_text', '').lower())

result_df = data[query_result]

for index, row in result_df.iterrows():
    print("URL:", row['links'].get('otherPropertiesMap', {}).get('full_url', 'N/A'))
    print("Olusturulma Tarihi:", row['links'].get('otherPropertiesMap', {}).get('created_at', 'N/A'))
    print("Tweet Metni:", row['links'].get('otherPropertiesMap', {}).get('tweet_text', 'N/A'))
    print()

print("Total Tweets: ", result_df.count())