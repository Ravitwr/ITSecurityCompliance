import os

# from dotenv import load_dotenv

# load_dotenv()
# MYSQL
MYSQL_HOST = os.environ.get("MYSQL_HOST")
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")

# common model parameters
MODEL_TEMPERATURE = 0
MODEL_MAX_TOKENS = 1000

# text embedding model
EMBEDDING_MODEL_SMALL = "text-embedding-3-small"
EMBEDDING_MODEL_LARGE = "text-embedding-3-large"


# model variables gpt-3.5
CHAT_MODEL_NAME_35_TURBO = "gpt-3.5-turbo-0125"

# model variables gpt-4
CHAT_MODEL_NAME_4 = "gpt-4-0125-preview"

PERSIST_DIRECTORY = "xxxxxxxxxxxxxxxxxxxxx"
DOCUMENT_COUNT=2
CHUNK_SIZE = 2500
CHUNK_OVERLAP = 500










