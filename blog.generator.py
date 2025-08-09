import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}"


def generate_blog(topic):
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"Write a detailed blog post about: {topic}"
                    }
                ]
            }
        ]
    }

    response = requests.post(url, headers = headers, json = data)
    result = response.json()

    if "error" in result:
       return f"Error from Gemini: {result['error']['message']}"
    
    if "candidates" in result and len(result["candidates"]) > 0:
       return result["candidates"][0]["content"]["parts"][0]["text"]
    
    return "No blog text found in Gemini's response."

if __name__ == "__main__":
    topic = input("Enter a blog topic: ")
    blog = generate_blog(topic)
    print("\nGenerated Blog:\n")
    print(blog)

keep_writing = True

while keep_writing:
  answer = input('Write a paragraph? y for yes, anything else for no. ')
  if (answer == 'y'):
    paragraph_topic = input('What should this paragraph talk about? ')
    print(generate_blog(paragraph_topic))
  else:
    keep_writing = False