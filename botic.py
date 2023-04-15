from aiogram import Bot, types, executor, Dispatcher
import emoji
from aiogram.types import ReplyKeyboardMarkup, InputFile
photo_map = InputFile("map.PNG")
easter_egg = InputFile("pins.png")


from tok import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def begin(message: types.Message):
    await bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}!\n"
                                            "Это бот-помощник для абитуриентов и ты можешь задать "
                                            "мне вопросы, выбрав из существующих или написав "
                                            "свой! "+ emoji.emojize("🤓"))

    kb1 = [
        [
            types.KeyboardButton(text="Выбрать вопрос " + emoji.emojize("👀")),
            types.KeyboardButton(text="Написать свой вопрос " + emoji.emojize("✍🏻"))
        ],
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb1,
        resize_keyboard=True,one_time_keyboard=True,
        input_field_placeholder="Напишешь 443?"
    )
    await message.answer("Как тебе помочь?", reply_markup=keyboard)

@dp.message_handler(text = '443')
async def little_secret(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=easter_egg)
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker=r'CAACAgIAAxkBAAEIlhpkOjBzAWCGrnZNzM7ONAj4Su0twAACIhAAAldhyUtXvemnZLvemS8E')


@dp.message_handler()
async def kb1_ans(message: types.Message):
    if message.text == "Выбрать вопрос " + emoji.emojize("👀"):

        kb2 = [
            [
                types.KeyboardButton(text="Где найти расписание?"),
                types.KeyboardButton(text="Как расположены корпуса?")
            ],
            [
                types.KeyboardButton(text="Где найти зачетку?"),
                types.KeyboardButton(text="Как найти медиацентр?")
            ],
            [
                types.KeyboardButton(text="Что такое ППОС ОмГТУ?"),
                types.KeyboardButton(text="Где знаменитая беляшка?")
            ],
            [
                types.KeyboardButton(text="Вернуться назад" + emoji.emojize("↩️"))
            ]

        ]
        keyboard2 = types.ReplyKeyboardMarkup(
            keyboard=kb2,
            resize_keyboard=True,
            input_field_placeholder="или тут..."
        )
        await message.answer("Самые популярные вопросы", reply_markup=keyboard2)

    #ответы на вопросы из менюшки два
    elif message.text == "Где найти расписание?":
        await message.answer(f"1 вариант: можно зайти на сайт РУЗ, выбрать свою группу и посмотреть расписание за "
                             f"выбранный период\n"
                             f'https://rasp.omgtu.ru/ruz/main')
        await message.answer("2 вариант: выполнив вход в личный кабинет на сайте ОмГТУ, перейти на студенческий портал"
                             "и посмотреть расписание на ближайшие два дня\n"
                             f'https://omgtu.ru/ecab/')
        await bot.send_sticker(chat_id=message.from_user.id,
                               sticker=r'CAACAgIAAxkBAAEIliFkOjDV6LiFLfVwhc2ouRIiqVpezgAC1xMAApJf4Evh4OWfxsrEgy8E')

    elif message.text == "Как расположены корпуса?":
        await message.answer(f"Схему расположения корпусов и адреса можно посмотреть тут: \n"
                             f'https://www.omgtu.ru/general_information/arrangement_of_buildings.php')

    elif message.text == "Где найти зачетку?":
        await message.answer(f"Зачетные книжки теперь в электронном формате и посмотреть свои баллы можно на "
                             f"студенческом портале в разделе 'зачетная книжка'")

    elif message.text == "Как найти медиацентр?":
        await message.answer(f"Медиацентр находится в 6 корпусе в кабинете 250 (нужно спуститься по лестнице)")

    elif message.text == "Что такое ППОС ОмГТУ?":
        await message.answer(f"Первичная профсоюзная организация студентов ОмГТУ, подробнее тут: \n"
                             f'https://vk.com/omgtuprof')

    elif message.text == "Где знаменитая беляшка?":
        await message.answer(f"Беляшка - это киоск с горячим питанием вблизи остановки общественного транспорта "
                             f"у главного корпуса.")
        await bot.send_photo(chat_id=message.chat.id, photo=photo_map)
        await bot.send_sticker(chat_id=message.from_user.id,
                               sticker=r'CAACAgIAAxkBAAEIliVkOjFZL7TH06fMA9Qegvk8-JZ1MQACLhYAAnkzeEk2e_4YaZfzPi8E')
    elif message.text == "Вернуться назад" + emoji.emojize("↩️"):
        await message.answer('Нажми ' + emoji.emojize("➡️") + ' /start')


    elif message.text == "Написать свой вопрос " + emoji.emojize("✍🏻"):
        await message.answer('Ты можешь присоедениться к чату единомышленников и попробовать задать вопрос там!\n'
                             'Помни о правилах поведения и не нарушай их!')
        await message.answer(f'https://t.me/+y8ihKE_oox45YTFi')
        await bot.send_sticker(chat_id=message.from_user.id,
                               sticker=r'CAACAgIAAxkBAAEIlitkOjK2X5HeeoPQX7Dz5eSIe9oM6gACIhoAAnbOYUspZwWlehPEsC8E')



    else:
       await message.answer(f"что-то не так")

