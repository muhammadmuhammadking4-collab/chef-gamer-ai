import streamlit as st
from groq import Groq

st.title("🌍 Farm AI")
st.caption("Ask me absolutely anything!")

# Connect to Groq using the Secret Safe
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# The Open Brain Instruction
system_prompt = "You are a highly intelligent, friendly, and helpful AI assistant. Answer only base on farm user asks clearly and accurately."

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_prompt}]

for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    answer = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages
    ).choices[0].message.content
    
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
