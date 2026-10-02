import re
import pandas as pd


def preprocessing(data):

    pattern_bracket = (
        r'\[\d{1,2}/\d{1,2}/\d{2,4},\s*'
        r'\d{1,2}:\d{2}(?::\d{2})?\s*'
        r'(?:AM|PM|am|pm)\]\s?'
    )

    pattern_12 = (
        r'\d{1,2}/\d{1,2}/\d{2,4},\s*'
        r'\d{1,2}:\d{2}(?::\d{2})?\s*'
        r'(?:AM|PM|am|pm)\s*-\s*'
    )

    pattern_24 = (
        r'\d{1,2}/\d{1,2}/\d{2,4},\s*'
        r'\d{1,2}:\d{2}(?::\d{2})?\s*'
        r'-\s*'
    )

    messages = re.split(pattern_bracket, data)

    if len(messages) > 1:

        pattern = pattern_bracket

    else:

        messages = re.split(pattern_12, data)

        if len(messages) > 1:

            pattern = pattern_12

        else:

            messages = re.split(pattern_24, data)
            pattern = pattern_24


    dates = re.findall(pattern, data)


    if len(messages) > len(dates):
        messages = messages[1:]


    if len(messages) < len(dates):
        dates = dates[:len(messages)]


    df = pd.DataFrame({
        'user_message': messages,
        'message_date': dates
    })


    df['message_date'] = (
        df['message_date']
        .astype(str)
        .str.replace('[', '', regex=False)
        .str.replace(']', '', regex=False)
        .str.replace(' - ', '', regex=False)
        .str.strip()
    )


    # Remove extra spaces including narrow no-break spaces
    df['message_date'] = (
        df['message_date']
        .str.replace('\u202f', ' ', regex=False)
        .str.replace('\u00a0', ' ', regex=False)
        .str.replace(r'\s+', ' ', regex=True)
        .str.strip()
    )


    # Convert date and time
    # Handles:
    # 01/07/26, 10:16 PM
    # 01/07/26, 10:16:25 PM
    # 01/07/26, 22:16
    # 01/07/2026, 22:16
    # 1/7/26, 10:16 PM
    #
    df['date'] = pd.to_datetime(
        df['message_date'],
        errors='coerce'
    )


    users = []
    msgs = []


    for message in df['user_message']:

        entry = re.split(
            r'([\w\W]+?):\s',
            message,
            maxsplit=1
        )

        if len(entry) > 1:

            users.append(entry[1])
            msgs.append(entry[2])

        else:

            users.append('group_notification')
            msgs.append(entry[0])


    df['user'] = users
    df['message'] = msgs


    df.drop(
        columns=[
            'user_message',
            'message_date'
        ],
        inplace=True
    )


    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day_name()
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute


    return df
