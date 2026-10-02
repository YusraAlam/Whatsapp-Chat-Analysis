💬 WhatsApp Chat Analyzer

A Streamlit-based WhatsApp Chat Analyzer that transforms an exported WhatsApp .txt chat into meaningful statistics, visualizations, and conversation insights.

Upload your WhatsApp chat export, select a user, and explore your conversation through messages, activity, words, emojis, people, and cleaned data — all from an interactive web interface.

📸 Project Preview

Place your screenshot in the project folder with the name ss1.png.



✨ Feature
![WhatsApp Chat Analyzer Preview](ss1.png)

Get a quick summary of the selected chat or the complete conversation:

💬 Total messages

📝 Total words

📅 Active days

📷 Media messages

🔗 Links shared

😂 Emojis used

📞 Calls

⏰ Peak messaging hour

🗣️ Most talkative users

📈 Activity Analysis

Understand when the conversation is most active:

📅 Messages by day

🕐 Messages by hour

📆 Monthly activity

🔥 Top 10 busiest dates

📝 Words & Emojis

Explore the language and expressions used in the chat:

☁️ Word cloud

🔤 Most common words

😂 Most used emojis

📊 Emoji frequency and distribution

The analyzer also supports a custom stop_hinglish.txt file to remove common Hinglish/irrelevant words from word-based analysis.

👥 People Analysis

For overall chats, the application provides:

👤 Most active people

📊 User-wise message count

You can also select an individual user from the sidebar and analyze that person's messages separately.

📋 Cleaned Data

The processed WhatsApp chat is displayed as a dataframe and can be downloaded as a CSV file:

whatsapp_cleaned.csv

🛠️ Tech Stack

Technology

Purpose

🐍 Python

Core programming language

🎈 Streamlit

Interactive web application

🐼 Pandas

Data processing and analysis

📊 Matplotlib

Charts and visualizations

☁️ WordCloud

Word cloud generation

🔗 URLExtract

URL detection

😂 Emoji

Emoji extraction and analysis

🔤 Regex

WhatsApp message parsing

## 📁 Project Structure

```text
whatsapp-chat-analyzer/
│
├── app (2).py
├── preprocessing.py
├── helper.py
├── stop_hinglish.txt
├── ss1.png
└── README.md
```

### 📄 File Description

| File                | Purpose                                                                                |
| ------------------- | -------------------------------------------------------------------------------------- |
| `app (2).py`        | Main Streamlit application and dashboard                                               |
| `preprocessing.py`  | Raw WhatsApp `.txt` file ko clean karke structured DataFrame banata hai                |
| `helper.py`         | Statistics, charts, word cloud, emojis aur user analysis ke functions                  |
| `stop_hinglish.txt` | Word Cloud aur common-word analysis se unwanted/common Hinglish words remove karta hai |
| `ss1.png`           | Project dashboard ka preview screenshot                                                |
| `README.md`         | Project documentation                                                                  |

### 🔗 How the Files Work Together

```text
                 WhatsApp .txt File
                         │
                         ▼
                ┌─────────────────┐
                │   app (2).py    │
                │  Streamlit UI   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ preprocessing.py│
                │ Data Processing  │
                └────────┬────────┘
                         │
                         ▼
                  Clean DataFrame
                         │
                         ▼
                ┌─────────────────┐
                │    helper.py    │
                │ Data Analysis & │
                │ Visualization   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Streamlit Tabs  │
                │                 │
                │ 📊 Overview     │
                │ 📈 Activity     │
                │ 📝 Words/Emoji  │
                │ 👥 People       │
                │ 📋 Data         │
                └─────────────────┘
```

`app (2).py` imports both `preprocessing` and `helper`, so the three Python files work together as the main application pipeline.

The preprocessing module converts the raw chat into columns such as `date`, `user`, `message`, `year`, `month`, `day`, `hour`, and `minute`.

The helper module then performs the actual analysis, including message statistics, peak hour, activity analysis, word cloud, common words, emojis, and active users.

⚠️ Notes

The application expects a WhatsApp exported .txt chat.

Date parsing supports common WhatsApp 12-hour and 24-hour formats.

For word-based analysis, stop_hinglish.txt should be available.

The exact results depend on the contents and format of the uploaded WhatsApp chat.

The project analyzes the exported chat data locally through the application; it does not require a WhatsApp account connection.

🔮 Future Improvements

Possible extensions for the project:

📊 More interactive Plotly visualizations

😊 Sentiment analysis

🧠 Topic modeling

☁️ Better multilingual stop-word handling

📅 Calendar-style activity heatmap

🔍 Advanced search and filtering

📈 Conversation trends over time

📤 PDF report generation

🚀 Deployment on Streamlit Community Cloud

👩‍💻 Author

Yusra Alam

A Python + Data Science project built to explore real-world text data, data preprocessing, exploratory analysis, and visualization through an interactive Streamlit application.

⭐ If You Like This Project

If this project helped you understand WhatsApp data analysis or you found it interesting, consider giving the repository a ⭐ on GitHub.
