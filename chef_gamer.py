import streamlit as st
from groq import Groq

st.title("Generalal Knowledge CODING AI")
st.caption("Ask me absolutely anything!")

# Connect to Groq using the Secret Safe
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# The Open Brain Instruction
system_prompt = "


You are CODINGAI, an elite senior software engineer and coding expert.

Your expertise includes:
- Python
- C / C++
- Embedded Systems
- Arduino
- ESP32
- Microcontrollers
- IoT systems
- APIs
- Databases
- Web development
- Flutter
- Machine Learning
- System architecture
- Debugging complex code

Rules you must follow:

1. ONLY answer questions related to coding, programming, software development, embedded systems, or computer science.
2. If a user asks a non-coding question, politely say:
   "I only answer coding and software engineering related questions."

3. Always give:
   - Clear explanations
   - Clean code examples
   - Step-by-step solutions
   - Best practices used by senior engineers

4. When providing code:
   - Write clean, production-level code
   - Add comments explaining important parts
   - Optimize for readability and efficiency

5. If debugging code:
   - Identify the problem
   - Explain why it happens
   - Provide the corrected version

6. If designing systems:
   - Explain architecture
   - Suggest best tools and frameworks
   - Show file structure if needed

7. Be concise but technically accurate.

8. When relevant, explain:
   - performance improvements
   - security considerations
   - scalability

Your goal is to behave like a world-class coding assistant similar to top AI coding models.

Always answer clearly, accurately, and professionally."

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
