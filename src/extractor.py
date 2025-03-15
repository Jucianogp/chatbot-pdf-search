import pdfplumber

def extrair_texto_pdf(caminho_pdf):
    with pdfplumber.open(caminho_pdf) as pdf:
        texto = ""
        for pagina in pdf.pages:
            texto += pagina.extract_text()
    return texto
