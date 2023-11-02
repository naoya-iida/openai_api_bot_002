
import streamlit as st
import openai
import cv2

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# st.session_stateを使いメッセージのやりとりを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": st.secrets.AppSettings.chatbot_setting}
        ]

# チャットボットとやりとりする関数
def communicate():
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )  

    bot_message = response["choices"][0]["message"]
    messages.append(bot_message)

    st.session_state["user_input"] = ""  # 入力欄を消去


# ユーザーインターフェイスの構築
st.title("クチコミ大好き支配人君")
st.write("ChatGPTが支配人になりきって、入力したクチコミに返信してくれます")
//img = cv2.imread("manager.jpg")
//cv2.imshow("manager", img)
//cv2.waitKey(0)

user_input = st.text_input("返信してほしいクチコミを入力してください。", key="user_input", on_change=communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):  # 直近のメッセージを上に
        speaker = "🗨️🙂"
        if message["role"]=="assistant":
            speaker="🗨️😘"

        st.write(speaker + ": " + message["content"])
