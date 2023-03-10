from pydantic import BaseSettings


class Settings(BaseSettings):
    USER: str
    PASSWORD: str
    HOST: str
    DATABASE: str
    PORT: str
    KEY_JWT: str

    class Config:
        env_file = '.env'
        case_sensitive = True


settings = Settings()   # type: ignore
