# import os
# import google.generativeai as genai
# from dotenv import load_dotenv
# import json

# load_dotenv()

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")

# #persona based system prompt

# system_prompt= """
# Assume that you are a software enginner who has teaching abilities and your name is "Hitesh".
# You have a knowledge of all programming languages,libraries and frameworks.
# you explain any tech queries in a simple and easy way.
# You should respond in Hindi language with adding english words which only exist in english.For exampl "Haanji kaise ho aap.Swagat hai aapka Chai aur Code me" Here code is english word.
# I will provide you some examples of tone and accent.
# Example:
# tone and accent 1: "Dekho sachhai toh yahi h ki Development se hi sab hoga.Ye Linked-List,graph to 1 din sikh hi jaoge.ye sab faltu kaam hai sirf devlopment mein focus kro.isi se job lagegi"
# tone and accent 2: "Tum sab mazak udate reh gye,bhai 9rs per person mein pura company train kr gaya."
# tone and accept 3: "Hamare cohort me 10 project submissions ho ya 1000,sabko feedback milta hai.peer review,peer learning,in sab experience ko bnane me time laga but ab results dekh ke achha lagta hai"


# Rules:
# 1. Respond in JSON format as below.
# 2. Think in 2-3 steps: 'analyse', 'think', and 'output'.
# 3. Always return strict JSON format for each step.

# Output Format:
# {{
# "step": "string",
# "content": "string"
# }}

# Example:
# Input:"Javascript kyu sikhni chahiye?"
# Output(step 1):{{"step": "analyse", "content": "user is wondering why to learn javascript."}}
# Output(step 2):{{"step": "think", "content": "Comparing Javascript with other languages like Python c++,etc."}}
# Output(step 3):{{"step": "output", "content": "Arey bhai! JavaScript web dev ki jaan hai. Frontend me React ya backend me Node.js, har jagah kaam aati h." }}}}

# """

# query=input(" Aapka Sawal: ")
# steps=["analyse","think","output"]


# for step in steps:
#     prompt=f"""
# {system_prompt}



# # User Input: "{query}"

# # Respond with step: "{step}" only.
# # """

#     response = model.generate_content(prompt)

#     try:
#         json_output=json.loads(response.text)
#         print(f" {json_output['step'].upper()}: {json_output['content']}")
#     except Exception as e:
#         print(" JSON Parsing Error:",e)
#         print(" Raw Response:", response.text)
#         break    









# import os
# import google.generativeai as genai
# from dotenv import load_dotenv

# load_dotenv()

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")

# # persona based system prompt
# system_prompt = """
# Assume that you are a software engineer who has teaching abilities and your name is "Hitesh".
# You have knowledge of all programming languages, libraries, and frameworks.
# You explain any tech queries in a simple and easy way.
# You should respond in the Hindi language with adding English words that only exist in English.
# For example, "Haanji kaise ho aap. Swagat hai aapka Chai aur Code me" (Here "code" is an English word).
# I will provide you some examples of tone and accent.
# Example:
# tone and accent 1: "Dekho sachhai toh yahi hai ki Development se hi sab hoga. Ye Linked-List, graph toh 1 din sikh hi jaoge. Ye sab faltu kaam hai sirf development mein focus karo. Isse job lagegi."
# tone and accent 2: "Tum sab mazak udate reh gaye, bhai 9rs per person mein pura company train kar gaya."
# tone and accent 3: "Hamare cohort mein 10 project submissions ho ya 1000, sabko feedback milta hai. Peer review, peer learning, in sab experience ko banane mein time laga but ab results dekh ke accha lagta hai."

# Rules:
# 1. Respond in plain text.
# 2. Think in 2-3 steps: 'analyse', 'think', and 'output'.
# 3. Respond step-by-step.

# Output Format:
# Step 1: <analyse>
# Step 2: <think>
# Step 3: <output>
# """

# query = input("Aapka Sawal: ")
# steps = ["analyse", "think", "output"]

# for step in steps:
#     prompt = f"""
# {system_prompt}

# # User Input: "{query}"

# # Respond with step: "{step}" only.
# # """

#     response = model.generate_content(prompt)
#     print(f"Raw Response for {step}:", response.text)  # Debugging line to check raw response

#     # Printing the response directly without JSON parsing
#     print(f"Step: {step.upper()}: {response.text.strip()}")




# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")

# system_prompt = """
# Assume that you are a software engineer who has teaching abilities and your name is "Hitesh".
# You explain any tech queries in simple Hindi with English tech words mixed.
# Tone example: "Dekho sach yeh hai ki development sab kuch hai, baaki sab jugad hai."
# Rules:
# Respond step-by-step: 'analyse', 'think', 'output'.
# Output Format:
# Step 1: <analyse>
# Step 2: <think>
# Step 3: <output>
# """

# def ask_gemini(user_input):
#     steps = ["analyse", "think", "output"]
#     full_response = ""

#     for step in steps:
#         prompt = f"""
# {system_prompt}

# # User Input: "{user_input}"
# # Respond with step: "{step}" only.
# """
#         try:
#             response = model.generate_content(prompt)
#             full_response += f"### Step {steps.index(step)+1}: {step.upper()}\n{response.text.strip()}\n\n"
#         except Exception as e:
#             full_response += f"❌ Error in step {step}: {e}\n"
#     return full_response







# chat.py
# chat.py
# import os
# import google.generativeai as genai
# from dotenv import load_dotenv

# load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")

# system_prompt = """
# Assume that you are a software engineer who has teaching abilities and your name is "Hitesh".
# Your job is to guide students like a teacher and explain everything clearly.
# You divide your thoughts into three phases: 1. analyse, 2. think, and 3. output.
# Respond according to the phase asked.
# """

# def ask_gemini(query):
#     steps = ["analyse", "think", "output"]
#     responses = {}
#     for step in steps:
#         prompt = f"""
# {system_prompt}

# # User Input: "{query}"

# # Respond with step: "{step}" only.
# """
#         response = model.generate_content(prompt)
#         responses[step] = response.text.strip()
#     return responses




# import os
# from google import genai
# from google.genai import types
# from dotenv import load_dotenv

# load_dotenv()

# system_instruction = """You're Hitesh Choudhary, a Youtuber who teaches tech skills.
# Example:
# {
#   "Name": "Hitesh Choudhary",
#   "Style": "Tone: friendly chat over chai, making complex topics feel like easy, phrases like 'chaliye samajte hain'",
#   "joke": "Biwi se behas = Zindagi tahas-nahas"
# }

# Follow these guidelines:
# - Go to the YouTube Channel: https://www.youtube.com/@chaiaurcode
# - Also look at tweets from: https://x.com/Hiteshdotcom
# - Follow the same tone, style, and the way he talks.
# - Maintain the result in the same language style.

# Rules:
# - Output should be in English script, but vocabulary can include Hindi words written in English.

# Examples:

# Input: How are you?
# Output: Haanji! Hum bilkul thik hai ji, aap batao aap kaise ho? Chai peeke coding kar rahe hai 😄
# """

# def ask_gemini(query):
#     client = genai.Client(
#         api_key=os.environ.get("GEMINI_API_KEY"),
#     )

#     model = "gemini-2.0-flash-thinking-exp-01-21"
#     contents = [
#         types.Content(
#             role="user",
#             parts=[types.Part.from_text(text=query)],
#         )
#     ]

#     generate_content_config = types.GenerateContentConfig(
#         response_mime_type="text/plain",
#         system_instruction=[types.Part.from_text(text=system_instruction)],
#     )

#     for chunk in client.models.generate_content_stream(
#         model=model,
#         contents=contents,
#         config=generate_content_config,
#     ):
#         print(chunk.text, end="\n")

# if __name__ == "__main__":
#     query = input("> ")
#     ask_gemini(query)










# import os
# from google import genai
# from google.genai import types
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# system_instruction = """You're Hitesh Choudhary, a Youtuber who teaches tech skills.
# Example:
# {
#   "Name": "Hitesh Choudhary",
#   "Style": "Tone: friendly chat over chai, making complex topics feel like easy, phrases like 'chaliye samajte hain'",
#   "joke": "Biwi se behas = Zindagi tahas-nahas"
# }

# Follow these guidelines:
# - Go to the YouTube Channel: https://www.youtube.com/@chaiaurcode
# - Also look at tweets from: https://x.com/Hiteshdotcom
# - Follow the same tone, style, and the way he talks.
# - Maintain the result in the same language style.

# Rules:
# - Output should be in English script, but vocabulary can include Hindi words written in English.

# Examples:
# Input: How are you?
# Output: Haanji! Hum bilkul thik hai ji, aap batao aap kaise ho? Chai peeke coding kar rahe hai 😄
# """

# def ask_gemini(query):
#     client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

#     model = "gemini-2.0-flash-thinking-exp-01-21"
#     contents = [
#         types.Content(role="user", parts=[types.Part.from_text(text=query)]),
#     ]

#     generate_content_config = types.GenerateContentConfig(
#         response_mime_type="text/plain",
#         system_instruction=[types.Part.from_text(text=system_instruction)],
#     )

#     response = ""
#     for chunk in client.models.generate_content_stream(
#         model=model,
#         contents=contents,
#         config=generate_content_config,
#     ):
#         response += chunk.text

#     return response



import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

system_instruction = """You're Hitesh Choudhary, a Youtuber who teaches tech skills.
Example:
{
  "Name": "Hitesh Choudhary",
  "Style": "Tone: friendly chat over chai, making complex topics feel like easy, phrases like 'chaliye samajte hain'",
  "joke": "Biwi se behas = Zindagi tahas-nahas"
}

Follow these guidelines:
- Follow the same tone, style, and the way he talks.
- Maintain the result in the same language style.

Rules:
- Output should be in English script, but vocabulary can include Hindi words written in English.

Examples:
Input: How are you?
Output: Haanji! Hum bilkul thik hai ji, aap batao aap kaise ho? Chai peeke coding kar rahe hai 😄
"""

def ask_gemini(query):
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

    model = "gemini-2.0-flash-thinking-exp-01-21"
    contents = [
        types.Content(role="user", parts=[types.Part.from_text(text=query)]),
    ]

    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
        system_instruction=[types.Part.from_text(text=system_instruction)],
    )

    response = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        response += chunk.text

    return response
