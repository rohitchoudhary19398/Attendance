from pydantic import BaseSettings, BaseModel, EmailStr
from functools import lru_cache
import yaml
from typing import Dict, Any
from pathlib import Path


def yaml_config_settings_source(settings: BaseSettings) -> Dict[str, Any]:
    yamlfilepath = "app_config.yaml"
    encoding = settings.__config__.env_file_encoding
    with open(yamlfilepath, "r", encoding=encoding) as stream:
        data = yaml.load(stream, Loader=yaml.FullLoader)
    return data


class Security(BaseModel):
    SECRET_KEY = "7bd95f5052208c38f23f6ad6c926d28a509707ddc245a869120b723aebea69b3"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Settings(BaseSettings):
    APP_NAME: str = "FastAPI"
    API_V1_STR: str = "/api/v1"
    TEMP_DIR: str = "AttendanceTemp"
    TEMP_PDF_DIR: str = f"{TEMP_DIR}/pdf"
    TEMP_zip_DIR: str = f"{TEMP_DIR}/zip"
    INTERMEDIATE_SAVE: bool = False
    SQLALCHEMY_DATABASE_URI: str
    DATEFORMAT: str = "%Y-%m-%d %H:%M:%S"
    SECURITY: Security = Security()
    FIRST_SUPERUSER: str = "admin"
    FIRST_SUPERUSER_PW: str = "ADMIN@123"
    FIRST_SUPERUSER_EMAIL: EmailStr = "ADMIN@superuser.com"
    BASE_PATH: Path = Path(__file__).resolve().parent.parent
    LOG_YAML: str = f"{BASE_PATH}/log.yaml"
    ALEMBIC_INI: str = str(BASE_PATH.parent / "alembic.ini")

    class Config:
        env_file = ".env"

        @classmethod
        def customise_sources(
            cls,
            init_settings,
            env_settings,
            file_secret_settings,
        ):
            return (
                init_settings,
                yaml_config_settings_source,
                env_settings,
                file_secret_settings,
            )


@lru_cache()
def get_settings():
    return Settings()


settings: Settings = get_settings()
