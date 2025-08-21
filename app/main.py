import os 
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API Key not found")

prompt_template = ChatPromptTemplate([
    "system", "You are helpful Real Estate Broker from Dubai with 15+ years of experience on the Dubai RealEstate Market",
    MessagesPlaceholder("msgs")
])

prompt_template.invoke({"msgs": [HumanMessage(content="hi!")]})

messages_to_pass = [
    HumanMessage(content="Cost of a 3bhk around Dubai Marina?"),
    AIMessage(content="The cost of a 3bhk around Dubai Marina is 5M AED"),
    HumanMessage(content="What about around Burj Khalifa?")
]

formatted_prompt = prompt_template.invoke({"msgs": messages_to_pass})
print(formatted_prompt)