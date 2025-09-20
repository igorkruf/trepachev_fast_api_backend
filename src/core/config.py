from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig(BaseModel):
    host: str = "0.0.0.0" 
    port: int = 8000

class RouterPrefix(BaseModel):
    api: str = "/api"

class DatabaseConfig(BaseModel):
    url:PostgresDsn
    echo:bool = False
    echo_pool:bool = False
    max_overflow: int = 50
    pool_size: int = 10
    

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=('.env-template', '.env'),
        env_file_encoding='utf-8',
        #  используется, чтобы избежать ошибок при загрузке .env, 
        # где есть настройки не только для FastAPI, но и для PostgreSQL и PGAdmin.
        # только что создал файл .env в папке src моего приложения 
        # так- что параметр exstra можно удалить но я оставил
        extra='ignore', 
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="MY_APP_CONFIG__",

    )
    run: RunConfig = RunConfig()
    router_prefix: RouterPrefix = RouterPrefix()
    db: DatabaseConfig 
    


settings = Settings()
print(settings.db.url)
