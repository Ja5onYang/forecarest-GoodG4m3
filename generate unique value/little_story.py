import openai

#need a key
openai.api_key = "<API_KEY>"

training_data = """
    this guy has a basket of apples
    this guy knows a lot about astronomy
    this guy won the first prize in a game
    this guy has six sisters and five brothers
"""

request_params = {
    "model": "text-davinci-002",
    "prompt": "This guy is very talented.",
    "temperature": 0.2,
    "max_tokens": 30,
    "n": 1,
    "stop": "."
}

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=request_params["prompt"], 
    max_tokens=request_params["max_tokens"], 
    n=request_params["n"], 
    temperature=request_params["temperature"], 
    stop=request_params["stop"],
    )

story = response.choices[0].text.strip()

print("Generated story: " + story)