import pandas as pd
from urlextract import URLExtract
from wordcloud import WordCloud
import emoji
from collections import Counter
import matplotlib.pyplot as plt

extract = URLExtract()

def fetch_stats(selected_user, df):
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]
    
    num_msgs = df.shape[0]
    
    words = []
    for message in df['message']:
        words.extend(message.split())
    num_words = len(words)
    
    num_days = df['only_date'].nunique()
    
    num_media = df[df['message'] == '<Media omitted>\n'].shape[0]
    
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))
    num_link = len(links)
    
    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])
    num_emojis = len(emojis)
    
    num_calls = df[df['message'].str.contains('call', case=False, na=False)].shape[0]
    
    if df.empty:
        most_active_hour = "No data"
    else:
        most_active_hour = df['hour'].mode()
        most_active_hour = str(most_active_hour.values[0]) if not most_active_hour.empty else "No data"

    return num_msgs, num_words, num_days, num_media, num_link, num_emojis, num_calls, most_active_hour

def peak_hour_info(selected_user, df):
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]
    if df.empty:
        return None
    
    hourly_counts = df['hour'].value_counts().sort_index()
    if hourly_counts.empty:
        return None
    
    peak_hr = hourly_counts.idxmax()
    count = hourly_counts.max()
    total = len(df)
    percent = (count / total) * 100 if total > 0 else 0
    
    h_12 = peak_hr % 12
    h_12 = 12 if h_12 == 0 else h_12
    ampm = "AM" if peak_hr < 12 else "PM"
    label = f"{h_12}:00 {ampm}"
    
    return label, count, percent

def most_talkative(df):
    x = df['user'].value_counts().head(5)
    df_percent = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index()
    df_percent.columns = ['Name', 'Percentage']
    
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(x.index, x.values, color='#25D366')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig, df_percent

def most_busy_day(selected_user, df):
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]
    return df['day_name'].value_counts()

def most_busy_hour(selected_user, df):
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]
    return df['hour'].value_counts().sort_index()

def most_busy_month(selected_user, df):
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]
    
    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))
    timeline['time'] = time
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(timeline['time'], timeline['message'], color='#128C7E', marker='o', linewidth=2)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xticks(rotation='vertical')
    plt.tight_layout()
    return fig

def most_busy_date(selected_user, df):
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]
    
    date_counts = df['only_date'].value_counts().head(10).sort_index()
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.bar(date_counts.index.astype(str), date_counts.values, color='#25D366')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

def create_wordcloud(selected_user, df):
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]
    
    with open('stop_hinglish.txt', 'r', encoding='utf-8') as f:
        stop_words = f.read().splitlines()
        
    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']
    
    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)
    
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    temp['message'] = temp['message'].apply(remove_stop_words)
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))
    return df_wc

def top_word(selected_user, df):
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]
        
    with open('stop_hinglish.txt', 'r', encoding='utf-8') as f:
        stop_words = f.read().splitlines()
        
    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']
    
    words = []
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)
                
    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df

def top_sticker(selected_user, df):
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]
        
    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])
        
    emoji_df = pd.DataFrame(Counter(emojis).most_common(20))
    if not emoji_df.empty:
        emoji_df.columns = ['Emoji', 'Count']
    return emoji_df

def most_active_user(df):
    x = df['user'].value_counts().head(10)
    return x