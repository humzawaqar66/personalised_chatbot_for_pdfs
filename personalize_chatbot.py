from openai import OpenAI
import re
import fitz

client = OpenAI(
    api_key='your api key'
)

def read_pdf(file_path):
    detected_text = ''
    with fitz.open(file_path) as pdf_file:
        for page_num in range(10):
            page = pdf_file.load_page(page_num)
            detected_text += page.get_text() + '\n\n'
    return detected_text

context = read_pdf("your pdf")  # Replace with the path to your PDF file

Messages = [
    {"role": "system", "content": "You name is Hawkesworth. You are supposed to answer from below mentioned context\n\nContext:"+context},
]

def generate_response(user_input):
    Messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        messages=Messages,
        model="gpt-3.5-turbo",
    )
    analysis = response.choices[0].message.content.strip()
    Messages.append({"role": "assistant", "content": analysis})
    return analysis

def main():
    while True:
        user_input = input("User: ")
        if user_input.lower() == 'exit':
            print("Chatbot exits.")
            break
        response = generate_response(user_input)
        print("Bot (Hawkesworth):", response)

if __name__ == "__main__":
    main()
