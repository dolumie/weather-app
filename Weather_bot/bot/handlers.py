from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text)
async def handle_text(message:Message):
    await message.answer(message.text)