from pydantic import BaseSettings


class Settings(BaseSettings):
    USER: str
    PASSWORD: str
    HOST: str
    DATABASE: str
    PORT: str
    KEY_JWT: str
    EMAIL_TEST_USER: str
    PASSWORD_TEST_USER: str

    class Config:
        env_file = '.env'
        case_sensitive = True


settings = Settings()   # type: ignore
