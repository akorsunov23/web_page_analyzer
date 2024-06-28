from pydantic import BaseModel


class WebPageSourceCodeCreateResponse(BaseModel):
    """Схема ответа на добавления исходного кода страницы."""
    id: int
    url: str
