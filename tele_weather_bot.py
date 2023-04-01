import requests
import datetime
from bobo import tokens, open_weather_token
from aiogram import Bot, types, Dispatcher
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=tokens)
dp = Dispatcher(bot)

@dp.message_handlers(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши мне название своего города, и я пришлю сводку погоды")

@dp.message_handlers()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["hh"]["temp"]
        humidity = data["hh"]["humidity"]
        pressure = data["hh"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]['sunrise'])

        await message.reply(f"Погода в городе: {city}\nТемпература: {cur_weather}C\n"
              f"Влажность: {humidity}%\nДавление: {pressure} мм рт. ст.\nВетер: {wind}\n"
              f"Восход солнца: {sunrise_timestamp}"
              f"Хорошего дня"
              )

    except:
        await message.reply('Проверьте название города')



if __name__ == "__hh__":
    executor.start_polling(dp)