"""Модели для запросов к API"""

from pydantic import BaseModel
from typing import List


class Parameters(BaseModel):
    # Конкретные значения искомых параметров с их типом
    value: list
    # Оператор для запроса типа AND,OR и т.п.
    operator: str
    type: str


class Search(BaseModel):
    # Вспомогательная структура для описания объекта искомого значения
    operator: str
    parameters: List[Parameters]


class RequestBody(BaseModel):
    # Модель для проверки запросов к апи
    timeout_s: int
    max_rows_in_result: int
    search: Search
