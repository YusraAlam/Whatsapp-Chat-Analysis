import re
import pandas as pd

def preprocessing(data):
    # Naye bracket format (with seconds) aur purane WhatsApp export formats ke liye patterns
    pattern_bracket = r'\[\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}:\d{2}\s[AP]M\]\s'
    pattern_12 = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s[AP]M\s-\s'
    pattern_24 = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'
    
    messages = re.split(pattern_bracket, data)
    if len(messages) <= 1:
        messages = re.split(pattern_12, data)
        if len(messages) <= 1:
            messages = re.split(pattern_24, data)
            pattern = pattern_24
        else:
            pattern = pattern_12
    else:
        pattern = pattern_bracket

    dates = re.findall(pattern, data)
    
    if len(messages) > len(dates):
        messages = messages[1:]

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    
    # Clean date string (brackets aur extra characters hatana)
    df['message_date'] = df['message_date'].fillna('').astype(str)
    df['message_date'] = df['message_date'].str.replace('[', '', regex=False)
    df['message_date'] = df['message_date'].str.replace(']', '', regex=False)
    df['message_date'] = df['message_date'].str.replace(' - ', '', regex=False)
    df['message_date'] = df['message_date'].str.strip()
    
    # Try parsing dates safely including seconds format (%I:%M:%S %p)
    try:
        df['date'] = pd.to_datetime(df['message_date'], format='%m/%d/%y, %I:%M:%S %p')
    except:
        try:
            df['date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M:%S %p')
        except:
            try:
                df['date'] = pd.to_datetime(df['message_date'], format='%m/%d/%y, %I:%M %p')
            except:
                try:
                    df['date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M %p')
                except:
                    try:
                        df['date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y, %I:%M %p')
                    except:
                        try:
                            df['date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %H:%M')
                        except:
                            df['date'] = pd.to_datetime(df['message_date'], errors='coerce')

    users = []
    msgs = []
    for message in df['user_message']:
        entry = re.split(r'([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            msgs.append(" ".join(entry[2:]))
        else:
            users.append('group_notification')
            msgs.append(entry[0])

    df['user'] = users
    df['message'] = msgs
    df.drop(columns=['user_message', 'message_date'], inplace=True)

    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day_name()
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    return df
