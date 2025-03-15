import openai

openai.api_key = 'sua-chave-api'

def gerar_resposta(pergunta, contexto):
    prompt = f"Com base neste contexto: {contexto}, responda à pergunta: {pergunta}"
    
    resposta = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    
    return resposta.choices[0].text.strip()
