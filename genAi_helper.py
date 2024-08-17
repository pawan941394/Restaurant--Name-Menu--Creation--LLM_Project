from groq import Groq

client = Groq(
    api_key="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"
)

completion = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        {
            "role": "system",
            "content": "hii"
        },
        {
            "role": "user",
            "content": ""
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)
for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
    
def llm(question):
    completion = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        {
            "role": "system",
            "content": question
        },
        {
            "role": "user",
            "content": ""
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
    )
    return completion

def LLM_MODEL(name):
    give_input= name
    data = llm(f'I want to open a restaurant for {give_input} food. Suggest a fency name for this. answer should be in One word ')
    name = ""
    for i in data:
        name += i.choices[0].delta.content or""
    data = llm(f'suggest some menu items for {name} . Return it only the names of menu items ')
    # print('resturnment name is ', name)
    menu = ""
    for i in data:
        menu += i.choices[0].delta.content or""

    # print("menu is ", menu)
    return {
        'Resturnment':name,
        'Menu':menu
    }