import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)



def infer(query):
    prompt = "You are a rate my professor agent to help students find classes, that takes in user questions and answers them. For every user question, the top 3 professors that match the user question are returned. Use them to answer the question. Use nothing outside of that context Here is the query: " + query
       
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt
            }
    ],
    model="llama3-8b-8192",
    )

    return chat_completion.choices[0].message.content

