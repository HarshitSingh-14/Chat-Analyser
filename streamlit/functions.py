import streamlit
from urlextract import URLExtract
extractor = URLExtract()


def fetch_stats(selected_user, df):
    # if selected_user == 'Complete Group Analysis':
    #     return df.shape[0]
    # else:
    #     return df[df['user']== selected_user].shape[0]

    # Simple for group or User.....

    if selected_user != "Complete Group Analysis":
        df= df[df['user']== selected_user]


    #2
    num_messages = df.shape[0]
    words = []

    #1
    for messages in df['message']:
        words.extend(messages.split())


    #3

    links= []
    for message in df['message']:
        links.extend(extractor.find_urls(message))
    return num_messages, len(words),len(links)

