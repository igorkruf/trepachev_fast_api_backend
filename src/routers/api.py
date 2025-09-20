from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse

# Создаём роутер
router = APIRouter()

# Простой эндпоинт для получения информации о пользователе
@router.get("/", response_class=JSONResponse)
def get_page_users_main(req:Request):
    data={
        'message':'first message'
    }
    return data