import faiss
import numpy as np

# Exemplo de vetorização usando embeddings do OpenAI
# Transformando texto em vetores (embedding)
texto = "Exemplo de texto extraído"
embedding = model.get_embedding(texto)  # Supondo que você tenha o modelo

# Criação do índice FAISS
dim = len(embedding)  # Tamanho do vetor
index = faiss.IndexFlatL2(dim)  # Índice com distância L2
index.add(np.array([embedding]))  # Adiciona o vetor ao índice

# Realizando busca
D, I = index.search(np.array([embedding]), k=1)  # k = número de resultados desejados
