try:
    from sentence_transformers import SentenceTransformer

    MODEL_NAME = "all-MiniLM-L6-v2"
    model = SentenceTransformer(MODEL_NAME)

except:
    MODEL_NAME = "light-mode"
    model = None


def get_model():
    return model


def load_model():
    return model