from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    deepseek_api_key: str
    deepseek_base_url: str = "https://api.deepseek.com/v1"
    deepseek_model: str = "deepseek-chat"
    database_path: Path = BASE_DIR / "data" / "assistant.db"
    faiss_index_path: Path = BASE_DIR / "data" / "faiss_index"
    embedding_model: str = "BAAI/bge-small-zh-v1.5"


settings = Settings()
