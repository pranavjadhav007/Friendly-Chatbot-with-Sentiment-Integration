import streamlit as st

if "Sentiment_chatbot" not in st.session_state:
    from chatbot import Sentiment_chatbot
    st.session_state.Sentiment_chatbot=Sentiment_chatbot()

def generate_output(text):
    try:
        answer,sentime=st.session_state.Sentiment_chatbot.generate_final_answer(text)
        return answer,sentime
    except:
        return "Sorry, I didn't understand that. Please try again."


st.title("Human Friendly Chatbot with Sentiment Configuration")

inp = st.chat_input("What the query?")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if inp:
    print("got in inp")
    st.session_state.chat_history.append({"role": "user", "response": inp})
    answe,senti=generate_output(inp)
    # print(answer)
    # answe,senti="answer","negative"
    print("model ans end ")
    st.session_state.chat_history.append({"role": "chatbot", "response": answe,"sentiment":senti})

for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(
            f"<h3><span style='color:#4652DD; font-weight:bold;'>You: {chat['response']}</span></h3>", 
            unsafe_allow_html=True
        )    
    else:
        st.markdown(
            f"<i>(Sentiment Detected: {chat['sentiment']}) </i><br> <span style='color:white; font-weight:bold;'>Bot: {chat['response']}</span>", 
            unsafe_allow_html=True
        )  

