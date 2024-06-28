## Интерфейс на FastAPI

### Запустить проект:
- клонировать репозиторий:
```angular2html
git clone https://github.com/akorsunov23/web_page_analyzer.git
```
- перейти в каталог с проектом:
```
cd web_page_analyzer/
```
- собрать и запустить контейнер (swagger 127.0.0.1:8000/docs):
```angular2html
docker build -t web_page .&& docker run -d -p 8000:8000 --name fast_api web_page
```
- запустить тесты:
```angular2html
docker exec -it fast_api pytest
```

### Описание:
В проекте доступна одна ручка 'web_page/source_code/' которая принимает URL и записывает в БД исходный код страницы.
