import streamlit as st
import matplotlib.pyplot as plt
import preprocessing
import helper
import zipfile
import io


st.set_page_config(
    page_title="WhatsApp Analyzer",
    layout="wide"
)


st.markdown(
    """
    <style>

    .stApp {
        background-color: #FFFFFF;
        color: #111111;
    }

    .main {
        background-color: #FFFFFF;
    }

    .stMarkdown,
    .stText,
    p,
    label,
    span {
        color: #111111;
    }

    .main-title {
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        color: #128C7E !important;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    .sub-title {
        text-align: center;
        color: #555555 !important;
        margin-bottom: 30px;
        font-size: 16px;
    }

    section[data-testid="stSidebar"] {
        background-color: #075E54 !important;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] div {
        color: #FFFFFF !important;
    }

    section[data-testid="stFileUploader"] {
        background-color: #128C7E !important;
        border-radius: 12px !important;
        padding: 12px !important;
    }

    section[data-testid="stFileUploader"] label {
        color: #FFFFFF !important;
    }

    section[data-testid="stFileUploader"] span {
        color: #FFFFFF !important;
    }

    section[data-testid="stFileUploader"] small {
        color: #FFFFFF !important;
    }

    section[data-testid="stFileUploader"] button {
        background-color: #25D366 !important;
        color: #111111 !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
    }

    section[data-testid="stFileUploader"] button:hover {
        background-color: #20BD5A !important;
        color: #FFFFFF !important;
    }

    div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        color: #111111 !important;
        border-radius: 8px !important;
    }

    div[data-baseweb="select"] input {
        color: #111111 !important;
    }

    div[data-baseweb="select"] span {
        color: #111111 !important;
    }

    button[data-baseweb="tab"] {
        color: #075E54 !important;
        font-weight: 600 !important;
        background-color: transparent !important;
    }

    button[data-baseweb="tab"] p,
    button[data-baseweb="tab"] span {
        color: #075E54 !important;
        font-weight: 600 !important;
    }

    button[data-baseweb="tab"][aria-selected="true"],
    button[data-baseweb="tab"][aria-selected="true"] p,
    button[data-baseweb="tab"][aria-selected="true"] span {
        color: #128C7E !important;
        font-weight: 700 !important;
    }

    div[data-baseweb="tab-highlight"] {
        background-color: #25D366 !important;
    }

    h1, h2, h3, h4 {
        color: #111111 !important;
    }

    div[data-testid="stMetric"] {
        background-color: #F0F2F5 !important;
        border-left: 5px solid #25D366;
        border-radius: 12px;
        padding: 15px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    }

    div[data-testid="stMetricLabel"],
    div[data-testid="stMetricLabel"] * {
        color: #555555 !important;
    }

    div[data-testid="stMetricValue"],
    div[data-testid="stMetricValue"] * {
        color: #111111 !important;
        font-weight: 700 !important;
    }

    .stButton > button {
        background-color: #25D366 !important;
        color: #111111 !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
    }

    .stButton > button:hover {
        background-color: #128C7E !important;
        color: #FFFFFF !important;
    }

    .stDownloadButton button {
        background-color: #25D366 !important;
        color: #111111 !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: 700 !important;
    }

    .stDownloadButton button:hover {
        background-color: #128C7E !important;
        color: #FFFFFF !important;
    }

    div[data-testid="stDataFrame"] {
        border: 1px solid #25D366;
        border-radius: 10px;
        overflow: hidden;
        background-color: #FFFFFF !important;
    }

    div[data-testid="stAlert"] {
        border-radius: 10px;
    }

    section[data-testid="stSidebar"] div[data-baseweb="select"] > div,
    section[data-testid="stSidebar"] div[data-baseweb="select"] * {
        color: #111111 !important;
        -webkit-text-fill-color: #111111 !important;
    }

    section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
    }

    section[data-testid="stSidebar"] div[data-baseweb="select"] svg {
        fill: #111111 !important;
    }

    div[data-baseweb="popover"],
    div[data-baseweb="popover"] ul,
    div[data-baseweb="popover"] li,
    div[data-baseweb="popover"] * {
        background-color: #FFFFFF !important;
        color: #111111 !important;
    }

    div[data-baseweb="popover"] li:hover {
        background-color: #E7F9EE !important;
    }

    section[data-testid="stFileUploaderDropzone"],
    div[data-testid="stFileUploaderDropzone"] {
        background-color: #128C7E !important;
        border: 1px dashed #FFFFFF !important;
        border-radius: 12px !important;
    }

    div[data-testid="stFileUploaderDropzone"] *,
    div[data-testid="stFileUploaderDropzone"] small,
    div[data-testid="stFileUploaderDropzone"] span {
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }

    div[data-testid="stFileUploaderDropzone"] button,
    div[data-testid="stFileUploaderDropzone"] button * {
        background-color: #25D366 !important;
        color: #111111 !important;
        -webkit-text-fill-color: #111111 !important;
    }

    div[data-testid="stFileUploaderFile"] *,
    div[data-testid="stFileUploaderFileName"] {
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stAlert"],
    section[data-testid="stSidebar"] div[data-testid="stAlert"] * {
        color: #0B3D2E !important;
    }

    div[data-testid="stCaptionContainer"],
    div[data-testid="stCaptionContainer"] * {
        color: #555555 !important;
    }

    div[data-testid="stAlert"] * {
        color: #111111 !important;
    }

    div[data-testid="stMetricDelta"],
    div[data-testid="stMetricDelta"] * {
        color: #128C7E !important;
    }

    .st-key-peak_metric div[data-testid="stMetricValue"],
    .st-key-peak_metric div[data-testid="stMetricValue"] * {
        font-size: 1.5rem !important;
        white-space: nowrap !important;
    }

    .st-key-peak_metric div[data-testid="stMetricDelta"],
    .st-key-peak_metric div[data-testid="stMetricDelta"] * {
        font-size: 0.8rem !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    '<div class="main-title"> WhatsApp Chat Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Understand your conversations through messages, activity, words and people</div>',
    unsafe_allow_html=True
)


st.sidebar.title(" WhatsApp Analyzer")

st.sidebar.markdown("###  Upload Chat")


uploaded_file = st.sidebar.file_uploader(
    "Choose WhatsApp exported ZIP file",
    type=["zip"]
)


if uploaded_file is not None:

    try:

        zip_data = zipfile.ZipFile(
            io.BytesIO(uploaded_file.getvalue())
        )

        txt_files = [
            file
            for file in zip_data.namelist()
            if file.lower().endswith(".txt")
        ]

        if not txt_files:
            st.error(
                "No WhatsApp chat .txt file found inside the ZIP file."
            )
            st.stop()

        chat_file = txt_files[0]

        data = zip_data.read(chat_file).decode(
            "utf-8",
            errors="ignore"
        )

    except Exception as e:

        st.error(
            f"Unable to read ZIP file: {e}"
        )

        st.stop()


    try:

        df = preprocessing.preprocessing(data)

    except Exception as e:

        st.error(
            f"Unable to process this WhatsApp file: {e}"
        )

        st.stop()


    user_list = (
        df["user"]
        .dropna()
        .unique()
        .tolist()
    )


    if "group_notification" in user_list:
        user_list.remove("group_notification")


    user_list.sort()

    user_list.insert(
        0,
        "overall"
    )


    selected_user = st.sidebar.selectbox(
        " Analyze User",
        user_list
    )


    st.sidebar.markdown("---")


    if selected_user == "overall":

        st.sidebar.success(
            " Analyzing entire chat"
        )

    else:

        st.sidebar.success(
            f" Analyzing: {selected_user}"
        )


    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            " Overview",
            " Activity",
            "Words & Emojis",
            "People",
            " Data"
        ]
    )


    with tab1:

        (
            num_msgs,
            num_words,
            num_days,
            num_media,
            num_link,
            num_emojis,
            num_calls,
            most_active_hour
        ) = helper.fetch_stats(
            selected_user,
            df
        )


        st.subheader("Chat Overview")

        st.caption(
            "A quick summary of your WhatsApp conversation"
        )


        col1, col2, col3, col4 = st.columns(4)


        with col1:

            st.metric(
                "Messages",
                f"{num_msgs:,}"
            )


        with col2:

            st.metric(
                " Words",
                f"{num_words:,}"
            )


        with col3:

            st.metric(
                " Active Days",
                f"{num_days:,}"
            )


        with col4:

            st.metric(
                "Media",
                f"{num_media:,}"
            )


        col1, col2, col3, col4 = st.columns(4)


        with col1:

            st.metric(
                " Links",
                f"{num_link:,}"
            )


        with col2:

            st.metric(
                "Emojis",
                f"{num_emojis:,}"
            )


        with col3:

            st.metric(
                " Calls",
                f"{num_calls:,}"
            )


        with col4:

            peak = helper.peak_hour_info(
                selected_user,
                df
            )


            with st.container(key="peak_metric"):

                if peak is None:

                    st.metric(
                        " Peak Hour",
                        "No data"
                    )

                else:

                    label, count, percent = peak

                    st.metric(
                        " Peak Hour",
                        label,
                        f"{count:,} msgs · {percent:.0f}%",
                        delta_color="off"
                    )


        st.divider()


        if selected_user == "overall":

            st.subheader(
                " Most Talkative Users"
            )


            fig, new_df = helper.most_talkative(
                df
            )


            st.pyplot(
                fig,
                use_container_width=True
            )


            st.dataframe(
                new_df,
                use_container_width=True,
                hide_index=True
            )


        else:

            st.info(
                f" Showing statistics for **{selected_user}**"
            )


    with tab2:

        st.subheader(
            " Chat Activity"
        )

        st.caption(
            "See when the conversation was most active"
        )


        col1, col2 = st.columns(2)


        with col1:

            st.markdown(
                "###  Messages by Day"
            )


            day_data = helper.most_busy_day(
                selected_user,
                df
            )


            fig, ax = plt.subplots(
                figsize=(7, 4)
            )


            ax.bar(
                day_data.index,
                day_data.values,
                color="#25D366"
            )


            ax.set_ylabel(
                "Messages"
            )


            ax.spines["top"].set_visible(
                False
            )

            ax.spines["right"].set_visible(
                False
            )


            plt.xticks(
                rotation=45
            )

            plt.tight_layout()


            st.pyplot(
                fig,
                use_container_width=True
            )


        with col2:

            st.markdown(
                "###  Messages by Hour"
            )


            hour_data = helper.most_busy_hour(
                selected_user,
                df
            )


            fig, ax = plt.subplots(
                figsize=(7, 4)
            )


            ax.plot(
                hour_data.index,
                hour_data.values,
                marker="o",
                color="#128C7E",
                linewidth=2
            )


            ax.set_xlabel(
                "Hour"
            )

            ax.set_ylabel(
                "Messages"
            )


            ax.spines["top"].set_visible(
                False
            )

            ax.spines["right"].set_visible(
                False
            )


            plt.tight_layout()


            st.pyplot(
                fig,
                use_container_width=True
            )


        st.markdown(
            "### Monthly Activity"
        )


        fig = helper.most_busy_month(
            selected_user,
            df
        )


        st.pyplot(
            fig,
            use_container_width=True
        )


        st.markdown(
            "###  Top 10 Busiest Dates"
        )


        fig = helper.most_busy_date(
            selected_user,
            df
        )


        st.pyplot(
            fig,
            use_container_width=True
        )


    with tab3:

        st.subheader(
            " Words & Emojis"
        )


        col1, col2 = st.columns(2)


        with col1:

            st.markdown(
                "###  Word Cloud"
            )


            wordcloud = helper.create_wordcloud(
                selected_user,
                df
            )


            if wordcloud is not None:

                fig, ax = plt.subplots(
                    figsize=(8, 6)
                )


                ax.imshow(
                    wordcloud
                )

                ax.axis("off")


                st.pyplot(
                    fig,
                    use_container_width=True
                )

            else:

                st.info(
                    "No words available for word cloud."
                )


        with col2:

            st.markdown(
                "###  Most Common Words"
            )


            new_df = helper.top_word(
                selected_user,
                df
            )


            if not new_df.empty:

                fig, ax = plt.subplots(
                    figsize=(8, 5)
                )


                ax.bar(
                    new_df[0],
                    new_df[1],
                    color="#25D366"
                )


                ax.set_ylabel(
                    "Frequency"
                )


                ax.spines["top"].set_visible(
                    False
                )

                ax.spines["right"].set_visible(
                    False
                )


                plt.xticks(
                    rotation=90
                )

                plt.tight_layout()


                st.pyplot(
                    fig,
                    use_container_width=True
                )

            else:

                st.info(
                    "No words found."
                )


        st.divider()


        st.markdown(
            "###  Most Used Emojis"
        )


        em_df = helper.top_sticker(
            selected_user,
            df
        )


        if not em_df.empty:

            pie_df = em_df.head(10)


            col1, col2 = st.columns(2)


            with col1:

                st.dataframe(
                    em_df,
                    use_container_width=True,
                    hide_index=True
                )


            with col2:

                fig, ax = plt.subplots()


                ax.pie(
                    pie_df["Count"],
                    labels=pie_df["Emoji"],
                    autopct="%1.1f%%"
                )


                ax.set_title(
                    "Emoji Distribution"
                )


                st.pyplot(
                    fig,
                    use_container_width=True
                )


        else:

            st.info(
                "No emojis found."
            )


    with tab4:

        st.subheader(
            " People Analysis"
        )


        if selected_user == "overall":

            user_data = helper.most_active_user(
                df
            )


            st.markdown(
                "###  Most Active People"
            )


            st.dataframe(
                user_data,
                use_container_width=True
            )


            st.markdown(
                "### User-wise Message Count"
            )


            fig, ax = plt.subplots(
                figsize=(10, 5)
            )


            ax.bar(
                user_data.index,
                user_data.values,
                color="#25D366"
            )


            ax.set_ylabel(
                "Messages"
            )


            ax.spines["top"].set_visible(
                False
            )

            ax.spines["right"].set_visible(
                False
            )


            plt.xticks(
                rotation=45
            )

            plt.tight_layout()


            st.pyplot(
                fig,
                use_container_width=True
            )


        else:

            st.info(
                f" You are currently analyzing: {selected_user}"
            )


    with tab5:

        st.subheader(
            "Cleaned Chat Data"
        )


        st.dataframe(
            df,
            use_container_width=True
        )


        st.download_button(
            "Download Cleaned CSV",
            data=df.to_csv(
                index=False
            ).encode("utf-8"),
            file_name="whatsapp_cleaned.csv",
            mime="text/csv"
        )


        st.divider()


        st.subheader(
            "Media & Links"
        )


        media_links_df = helper.media_and_links(
            df
        )


        st.dataframe(
            media_links_df,
            use_container_width=True,
            hide_index=True
        )


        st.download_button(
            "Download Media & Links CSV",
            data=media_links_df.to_csv(
                index=False
            ).encode("utf-8"),
            file_name="whatsapp_media_links.csv",
            mime="text/csv"
        )
