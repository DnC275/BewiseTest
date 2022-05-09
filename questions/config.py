from pydantic import BaseSettings


class DBSettings(BaseSettings):
    user: str
    password: str
    database: str
    host: str
    port: str

    class Config:
        env_prefix = "MYSQL_"
        env_file = ".env"