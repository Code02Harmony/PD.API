from openai import AzureOpenAI
api_base = "https://pdai.openai.azure.com"
api_key = '7f49ee34d5bb4fca8ffd938146bb00c0'
deployment_name = "piapi"
api_version = "2023-06-01-preview"


client = AzureOpenAI(
    api_key=api_key,
    api_version=api_version,
    base_url=f"{api_base}/openai/deployments/{deployment_name}",


)


def getOutput(messages):

    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a medical scientist"},
            {"role": "system", "content": "You parkinson's disease very well"},
            {"role": "system", "content": "You give suggestions to avoid parkinson's disease for a person of any age , sex and from any country"},
            {"role": "system", "content": "You need to give recommendation, message along with a list of things one should do to avoid parkinson's disease when someone tells you their name,age,sex,country."},
            {"role": "system", "content": "You give personalised pd prevention recommendations"},
            {"role": "system", "content": "The recomendations should be based on age,location, sex and whether the person has PD or not. Be specific, use numbers to explain"},
            {"role": "system", "content": "The output should contain, a hello messsage with 4-5 recommendations in a list"},

        ] + messages,
    )
    return completion


def displayCompletion(completion):
    print(completion.choices[0].message.content)


def getRecommendation(name, age, location,pd):
    out = getOutput([
        {"role": "user", "content": f"""My name is {name}, I'm from {location} , my age is {age} and I {"" if pd else "don't"} have PD"""},
    ])
    return out.choices[0].message.content