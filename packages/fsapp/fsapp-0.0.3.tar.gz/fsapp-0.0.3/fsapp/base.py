from fastapi import FastAPI

from fsapp.core.config import settings
from fsapp.api.routers import api_router
from fsapp.classes import BaseExecutor
from fsapp.core.config import create_settings_files
from fsapp.core.handlers import handlers

create_settings_files()

# Основной объект приложения
# todo argument comments
app = FastAPI(
    # todo required -> main
    title=settings.required.instance,
    # todo openapi_url -> ope_napi_url
    docs_url="/docs",
)

# Подключение всех эндпоинтов
app.include_router(api_router)
# Добавляем базовый класс обработчиков
app.base_class = BaseExecutor

