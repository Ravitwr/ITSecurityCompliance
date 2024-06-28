from langchain_core.pydantic_v1 import SecretStr
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from settings import (
    EMBEDDING_MODEL_SMALL,
    EMBEDDING_MODEL_LARGE,
    CHAT_MODEL_NAME_4,
    CHAT_MODEL_NAME_35_TURBO,
    MODEL_MAX_TOKENS,
    MODEL_TEMPERATURE,
    OPENAI_API_KEY)


class GptWrapper:
    @classmethod
    def get_gpt_35(cls):
        return ChatOpenAI(
            api_key=SecretStr(OPENAI_API_KEY),
            model=CHAT_MODEL_NAME_35_TURBO,
            temperature=MODEL_TEMPERATURE,
            max_tokens=MODEL_MAX_TOKENS,
        )

    @classmethod
    def get_gpt_4(cls):
        return ChatOpenAI(
            api_key=SecretStr(OPENAI_API_KEY),
            model=CHAT_MODEL_NAME_4,
            temperature=MODEL_TEMPERATURE,
            max_tokens=MODEL_MAX_TOKENS,
        )

    @classmethod
    def get_ada_003_small(cls):
        return OpenAIEmbeddings(
            api_key=SecretStr(OPENAI_API_KEY),
            model=EMBEDDING_MODEL_SMALL
        )
    
    @classmethod
    def get_ada_003_large(cls):
        return OpenAIEmbeddings(
            api_key=SecretStr(OPENAI_API_KEY),
            model=EMBEDDING_MODEL_LARGE
        )
