from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import models

from database import engine
from routes import router_websocket, router_categories, router_items

# Создание таблиц в БД
models.Base.metadata.create_all(bind=engine)

# Шаблоны
templates = Jinja2Templates(directory="templates")

# Создание экземпляра FastAPI
app = FastAPI(
    title="WebSocketChatCRUDNotify",
    summary="WebSocket Chat + Notifications of CRUD operations!",
    version="0.0.1",
)

# Обработчик корневого маршрута для отображения HTML
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Получение протокола HTTP и преобразование в протокол WebSocket
    http_protocol = request.headers.get("x-forwarded-proto", "http")
    ws_protocol = "wss" if http_protocol == "https" else "ws"
    server_urn = request.url.netloc
    return templates.TemplateResponse("index.html",
                                      {"request": request,
                                       "http_protocol": http_protocol,
                                       "ws_protocol": ws_protocol,
                                       "server_urn": server_urn})

# Подключение созданных роутеров к приложению
app.include_router(router_websocket)
app.include_router(router_categories)
app.include_router(router_items)

# Запуск приложения при выполнении как самостоятельный скрипт
if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
