from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str
    POSTINGS_PATH: str
    SKILLS_PATH: str
    CACHE_PATH: str
    MAPBOX_ACCESS_TOKEN: str
    LOCATIONIQ_API_KEY: str

    class Config:
        env_file = '.env'


def get_settings():
    return Settings()
