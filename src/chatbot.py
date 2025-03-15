def chatbot():
    while True:
        pergunta = input("Faça sua pergunta (ou 'sair' para encerrar): ")
        if pergunta.lower() == "sair":
            break
        # Acesse o conteúdo extraído dos PDFs e gere a resposta
        resposta = gerar_resposta(pergunta, texto_dos_pdfs)  # `texto_dos_pdfs` é o conteúdo processado
        print(f"Resposta: {resposta}")
