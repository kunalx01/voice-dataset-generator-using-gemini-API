import google.generativeai as genai

#api_key="AIzaSyCc2CdfNLqxXOPl2Y_2imi09TBOaPnavpd"
#api_key=input("inter your api key")
genai.configure(api_key="AIzaSyCc2CdfNLqxXOPl2Y_2imi09TBOaPnavpc")

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[])


counter=int(input("enter the number of sentences:"))
prompt=input("enter propmt for text generation(eg. generate one line random sentence containing 15 - 20 words):")

def generator():
    texts=[]
    for i in range(counter):
        convo.send_message(prompt)
        responce = convo.last.text
        texts.append(responce)
    return texts
generator()
