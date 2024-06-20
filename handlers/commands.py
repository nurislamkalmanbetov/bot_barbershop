from aiogram import Router, F, Bot, Dispatcher
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
        "/masters - Мастера - Барберы \n"
        "/zapisatsya - Записаться на стрижу"
    )
    kb = [
        [KeyboardButton(text="/address"), KeyboardButton(text="/price")],
        [KeyboardButton(text="/contacts"), KeyboardButton(text="/courses_barber")],
        [KeyboardButton(text="/grafic"), KeyboardButton(text="/feed_back")],
        [KeyboardButton(text="/masters"), KeyboardButton(text="/zapisatsya")],
        [KeyboardButton(text="/end")],
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


from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from main import *
# test

ADMIN_CHAT_ID = ("1782718756")  # вставляете свой chat id
bot_instance: Bot = None  # Глобальная переменная для хранения экземпляра бота


class Form(StatesGroup):
    name = State()  # Состояние для ФИО
    phone_number = State()  # Состояние для номера телефона


def setup_routers(dispatcher: Dispatcher, bot: Bot):
    global bot_instance
    bot_instance = bot  # Сохраняем экземпляр бота для использования в хэндлерах
    dispatcher.include_router(router)


@router.message(Command("zapisatsya"))
async def cmd_zapisatsya(message: Message, state: FSMContext):
    await message.answer("Пожалуйста, введите ваше ФИО:")
    await state.set_state(Form.name)

@router.message(Form.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Спасибо! Теперь введите ваш номер телефона:")
    await state.set_state(Form.phone_number)


@router.message(Form.phone_number)
async def process_phone_number(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    data = await state.get_data()

    # Отправляем сообщение пользователю
    await message.answer(
        f"Спасибо за регистрацию!\nФИО: {data['name']}\nНомер телефона: {data['phone_number']}"
    )
    
    # Отправляем сообщение администратору
    user = message.from_user
    admin_message = (
        f"Новый клиент! Позвоните ему! \n"
        f"ФИО: {data['name']}\n"
        f"Номер телефона: {data['phone_number']}"
    )
    # await message.answer(ADMIN_CHAT_ID, admin_message)
    await bot_instance.send_message(ADMIN_CHAT_ID, admin_message)

    await state.clear()
