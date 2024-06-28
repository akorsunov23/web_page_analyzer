import logging

import httpx
from fastapi import APIRouter, status, HTTPException, Depends
from httpx import Response, ConnectTimeout
from pydantic import AnyHttpUrl
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_session
from src.web_page.models import WebPageSourceCode
from src.web_page.schemas import WebPageSourceCodeCreateResponse

log = logging.getLogger(__name__)

router = APIRouter(tags=['web_page'], prefix='/web_page')


@router.post(
    '/source_code/',
    status_code=status.HTTP_201_CREATED,
    response_model=WebPageSourceCodeCreateResponse
)
async def web_page_source_code_create(
    url: AnyHttpUrl,
    session: AsyncSession = Depends(get_session)
) -> WebPageSourceCodeCreateResponse:
    """Записываем исходный код страницы в БД."""
    url = str(url)
    log.info(f'Запросили исходный код: {url}')
    try:

        async with httpx.AsyncClient() as client:
            response: Response = await client.get(url)
            assert response.status_code == status.HTTP_200_OK
        source_code = WebPageSourceCode(url=url, source_code=response.text)
        session.add(source_code)
        await session.commit()
        await session.refresh(source_code)
        log.info(f'Исходный код: {url} успешно записан в БД - ID: {source_code.id}')

        return WebPageSourceCodeCreateResponse(id=source_code.id, url=url)

    except (ConnectTimeout, AssertionError) as exc:
        if isinstance(exc, ConnectTimeout):
            log.warning('Превышено ожидание ответа от сайта')
        else:
            log.warning(f'Запрос за исходным кодом: {url} завершился не успешно.')
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Не возможно получить данные с сайта.'
        )
