from aiogram import Router, F
from aiogram.filters import Command, CommandStart 
from aiogram.types import (
    Message, ReplyKeyboardMarkup, KeyboardButton, 
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, FSInputFile
)


router = Router()

@router.message(CommandStart())
async def start(message: Message):
    description = (
        "Салам \n"
        "Добро пожаловать в наш Барбершоную \n"
        "/address - Адресс барбершопа \n"
        "/contacts - Контакты \n"
        "/grafic - График работы \n"
        "/price - Расценки \n"
        "/courses_barber - Курсы на барбера \n"
        "/feed_back - Отзывы \n"
        "/masters - Мастера - Барберы"
    )
    kb = [
        [KeyboardButton(text="/address"), KeyboardButton(text="/price")],
        [KeyboardButton(text="/contacts"), KeyboardButton(text="/courses_barber")],
        [KeyboardButton(text="/grafic"), KeyboardButton(text="/feed_back")],
        [KeyboardButton(text="/masters"), KeyboardButton(text="/end")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(description, reply_markup=keyboard)

# Обработчик для команды /end
@router.message(Command(commands=['end']))
async def end(message: Message):
    await message.answer("Спасибо, что воспользовались ботом! До новых встреч!", show_alert=True)

# ответ на address
@router.message(Command(commands=['address']))
async def address(message:Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data="back")]  # Кнопка назад
    ])
    await message.answer(
        "Адресс  \n"
        "Улица Ибраимова 115 \n"
        "Ссылка, на карту 2ГИС -  https://2gis.kg/bishkek/geo/15763234351114035/74.619759%2C42.874037?m=74.619759%2C42.873826%2F17.48 \n",
        reply_markup=keyboard
    )

@router.callback_query(F.data == "back")
async def go_back(callback: CallbackQuery):
    await callback.message.delete()  # Удаляем текущее сообщение
    await start(callback.message)   # Отправляем стартовое сообщение с основным меню


# ответ на contacts
@router.message(Command(commands=['contacts']))
async def contacts(message:Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data="back")]  # Кнопка назад
    ])
    await message.answer(
        "Контакты \n"
        "Тел: +996222368655 \n"
        "WhatsApp: wa.me/996222368655 \n"
        "Instagram: https://instagram.com/marshal_asanbai  \n",
        reply_markup=keyboard
    )

@router.callback_query(F.data == "back")
async def go_back(callback: CallbackQuery):
    await callback.message.delete()  # Удаляем текущее сообщение
    await start(callback.message)   # Отправляем стартовое сообщение с основным меню

# ответ на grafic
@router.message(Command(commands=['grafic']))
async def grafic(message:Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data="back")]  # Кнопка назад
    ])
    await message.answer(
        "График работы \n"
        "Понедельник - Суббота с 11:00 - 22:00 \n"
        "Выходной - Воскресенье", 
        reply_markup=keyboard
    )

@router.callback_query(F.data == "back")
async def go_back(callback: CallbackQuery):
    await callback.message.delete()  # Удаляем текущее сообщение
    await start(callback.message)   # Отправляем стартовое сообщение с основным меню


# from database.request import get_masters

# @router.message(Command(commands=['masters']))
# async def masters(message:Message):
#     masters_data = await get_masters()
#     response_text = "Мастера:\n"
#     for master in masters_data:
#         response_text += f"{master.first_name} {master.last_name}, возраст {master.age}, опыт: {master.experience}\n"
#     await message.answer(response_text)


# ответ на price
@router.message(Command(commands=['price']))
async def price(message: Message):
    price_list = (
        "Модельная стрижка - 500 сом \n"
        "Стрижка McgGreggor Style - 1000 сом \n"
        "Стрижка Leonardo Dicaprio - 1300 сом \n"
        "Стрижка Спортивная - 400 сомов \n"
        "Стрижка Buzzcut - 2300 сомов \n"
    )

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Модельная", callback_data="model")],
        [InlineKeyboardButton(text="McgGreggor Style", callback_data="mcgreggor")],
        [InlineKeyboardButton(text="Leonardo Dicaprio", callback_data="leo")],
        [InlineKeyboardButton(text="Спортивная", callback_data="sport")],
        [InlineKeyboardButton(text="Buzzcut", callback_data="buzzcut")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_price")]  # Кнопка назад к прайсу
    ])

    await message.answer(price_list, reply_markup=keyboard)

@router.callback_query(F.data == "leo")
async def send_leo_picture(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data="back_to_price")]  # Кнопка назад к прайсу
    ])
    await callback.message.delete()
    await callback.message.answer_photo(
        photo=FSInputFile("images/leo.jpg"),
        caption=(
            "Стрижка Leonardo Dicaprio - 1300 сом \n"
            "Адрес - Ибраимова 115 \n"
            "WhatsApp: wa.me/996222368655 \n"
            "Instagram: https://instagram.com/marshal_asanbai  \n"
        ),
        reply_markup=keyboard
    )

@router.callback_query(F.data == "back_to_price")
async def back_to_price(callback: CallbackQuery):
    await callback.message.delete()  # Удаляем текущее сообщение
    await price(callback.message)   # Отправляем сообщение с прайс-листом



@router.callback_query(F.data=="mcgreggor")
async def send_leo_picture(callback:CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data="back")]  # Кнопка назад
    ])
    await callback.message.delete()
    await callback.message.answer_photo(
        photo=FSInputFile("images/mc.webp"),
        caption=( # описание к фото
            "Стрижка McgGreggor Style - 1000 сом \n"
            "Адрес - Ибраимова 115 \n"
            "WhatsApp: wa.me/996222368655 \n"
            "Instagram: https://instagram.com/marshal_asanbai  \n"
        ),
        reply_markup=keyboard
    )

@router.callback_query(F.data == "back_to_price")
async def back_to_price(callback: CallbackQuery):
    await callback.message.delete()  # Удаляем текущее сообщение
    await price(callback.message)   # Отправляем сообщение с прайс-листом
