💬 WhatsApp Chat Analyzer

A Streamlit-based WhatsApp Chat Analyzer that transforms an exported WhatsApp .txt chat into meaningful statistics, visualizations, and conversation insights.

Upload your WhatsApp chat export, select a user, and explore your conversation through messages, activity, words, emojis, people, and cleaned data — all from an interactive web interface.

📸 Project Preview

Place your screenshot in the project folder with the name ss1.png.



✨ Features

📊 Chat Overview

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

📁 Project Structure

whatsapp-chat-analyzer/
│
├── app.py
├── preprocessing.py
├── helper.py
├── stop_hinglish.txt
├── ss1.png
└── README.md

If your main Python file has a different name, keep that filename in the structure instead of app.py.

🔄 How It Works

The project follows a simple data-analysis pipeline:

WhatsApp Exported .txt File
            ↓
     Message Parsing
            ↓
      Data Cleaning
            ↓
    Date & User Extraction
            ↓
     Feature Extraction
            ↓
     Statistical Analysis
            ↓
   Charts & Visualizations
            ↓
      Streamlit Dashboard

1. Upload Chat

The application accepts an exported WhatsApp .txt file from the sidebar.

2. Preprocess the Chat

The preprocessing module uses regular expressions to identify WhatsApp timestamps and separates:

Date

Time

User

Message

It supports both 12-hour (AM/PM) and 24-hour WhatsApp timestamp formats.

3. Create Analysis Features

Additional columns are generated for:

Date

Year

Month

Day

Day name

Hour

Minute

4. Analyze the Conversation

The helper functions calculate statistics and generate visualizations for activity, words, emojis, and users.

5. Explore the Dashboard

The Streamlit application organizes the analysis into five sections:

📊 Overview
📈 Activity
📝 Words & Emojis
👥 People
📋 Data

🚀 Getting Started

1. Clone the Repository

git clone <your-repository-url>
cd whatsapp-chat-analyzer

2. Create a Virtual Environment

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

3. Install Dependencies

pip install streamlit pandas matplotlib wordcloud urlextract emoji

4. Run the Application

streamlit run app.py

The application will open in your browser.

📱 How to Export a WhatsApp Chat

From WhatsApp:

Open Chat
   ↓
Chat Options
   ↓
Export Chat
   ↓
Without Media
   ↓
Save the .txt file

Then upload the exported .txt file into the application.

🧩 Main Modules

app.py

Handles the Streamlit interface and connects all parts of the project.

It includes:

Page configuration

Custom WhatsApp-inspired styling

File upload

User selection

Dashboard tabs

Metrics

Charts

Cleaned-data display

CSV download

preprocessing.py

Responsible for converting the raw WhatsApp text into a structured Pandas DataFrame.

The preprocessing step identifies timestamps, users, messages, and derives date/time features.

helper.py

Contains the main analysis functions, including:

fetch_stats()

peak_hour_info()

most_talkative()

most_busy_day()

most_busy_hour()

most_busy_month()

most_busy_date()

create_wordcloud()

top_word()

top_sticker()

most_active_user()

📊 Example Insights

After uploading a chat, the dashboard can answer questions such as:

Who sent the most messages?

How many messages were exchanged?

Which day was the most active?

What hour had the highest messaging activity?

Which month had the most activity?

What words were used most frequently?

Which emojis were used the most?

How many links were shared?

How many media messages were sent?

Which users were the most active?

🎨 UI

The application uses a WhatsApp-inspired design with:

WhatsApp green theme

Sidebar navigation

Metric cards

Interactive tabs

Charts and tables

Clean white dashboard layout

CSV download option

📌 Important Files

stop_hinglish.txt

This file is used by the word cloud and most-common-word analysis to filter out common Hinglish/stop words.

Make sure it is present in the same project directory when running the application.

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
