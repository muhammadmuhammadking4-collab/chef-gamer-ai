import streamlit as st
from groq import Groq

# 1. SETUP
st.title("🍳 Chef & Gamer AI 🎮")
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Shortened the rules to one simple sentence
system_prompt = "You ONLY talk about COOKING and VIDEO GAMES. Refuse all other topics politely."

# 2. MEMORY
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_prompt}]

# 3. SHOW PAST MESSAGES (Hiding the secret system prompt)
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# 4. NEW MESSAGE LOGIC
if prompt := st.chat_input("Ask a recipe or game question..."):
    
    # Save and draw user text
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Ask Groq for the answer
    answer = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages
    ).choices[0].message.content
    
    # Save and draw AI text
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
