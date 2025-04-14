
# import streamlit as st
# from chat_module import ask_gemini

# st.set_page_config(page_title="Chai Aur Code Bot ☕", layout="centered")
# st.title("☕ Hitesh-Style Gemini Bot")
# st.markdown("_Chaliye samajte hain... kya aapka sawaal hai?_ 😄")

# query = st.text_input("👉 Ask me anything:", placeholder="e.g., What is Docker?")

# if query:
#     with st.spinner("Typing like Hitesh bhaiya... ☕"):
#         response = ask_gemini(query)
#         st.success(response)








from chat_module import ask_gemini

import streamlit as st

st.set_page_config(page_title="Chai Aur Code Bot ☕", layout="centered")
st.title("☕ Hitesh Sir-Style Gemini Bot")
st.markdown("_Chaliye samajte hain... kya aapka sawaal hai?_ 😄")

query = st.text_input("👉 Ask me anything:", placeholder="e.g., What is Docker?")

if query:
    with st.spinner("Typing like Hitesh bhaiya... ☕"):
        response = ask_gemini(query)
        st.success(response)
