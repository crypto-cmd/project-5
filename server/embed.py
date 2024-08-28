from sentence_transformers import SentenceTransformer

encoder_model = SentenceTransformer("moka-ai/m3e-base")

def embed(sentence):
    return encoder_model.encode(sentence)