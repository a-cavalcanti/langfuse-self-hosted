from langfuse.decorators import observe
from langfuse.openai import openai # OpenAI integration
from dotenv import load_dotenv

load_dotenv()

@observe()
def story():
    return openai.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=100,
        messages=[
          {"role": "system", "content": "You are a great storyteller."},
          {"role": "user", "content": "Once upon a time in a galaxy far, far away..."}
        ],
    ).choices[0].message.content
 
@observe()
def main():
    result = story()
    print(result)
    return result
 
main()