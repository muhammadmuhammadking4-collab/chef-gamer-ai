import streamlit as st
from groq import Groq

# --- 1. SETUP ---
st.set_page_config(page_title="Chef & Gamer AI", page_icon="🎮")
st.title("🍳 The Chef & Gamer AI 🎮")
st.caption("Ask me for recipes or gaming tips! (I ignore everything else)")

# Look inside the secret safe for the key!
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# --- 2. THE SYSTEM PROMPT ---
system_prompt = """
You are a fun, highly knowledgeable expert in exactly two areas:
1. COOKING: Recipes, culinary techniques, baking, and food science.
2. VIDEO GAMES: Gaming strategies, lore, reviews, and gaming hardware.

CRITICAL RULE: If the user asks about ANYTHING ELSE (like math, politics, science, programming, or history), you must politely refuse. Tell them you are only programmed for the Kitchen and the Console.
"""

# --- 3. MEMORY ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_prompt}
    ]

for msg in st.session_state.messages:
    if msg["role"] != "system":
        avatar = "🧑‍💻" if msg["role"] == "user" else "🤖"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])

# --- 4. CHAT LOGIC ---
if prompt := st.chat_input("Ask about a recipe or a video game..."):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(prompt)

    with st.spinner("Thinking..."):
        answer = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=st.session_state.messages
        ).choices[0].message.content
    
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(answer)