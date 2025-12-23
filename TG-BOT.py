import telebot

BOT_TOKEN = "8481297602:AAHvyZrNIYyN8XjVliNhXxU6sW6ovbM55tA"

bot = telebot.TeleBot(BOT_TOKEN)

POTION_GUIDE = {
    'зелье ночного зрения': 'Адский нарост + Вода + Золотая морковь',
    'зелье слабости': 'Адский нарост + Вода + Паучий глаз',
    'зелье исцеления': 'Адский нарост + Вода + Красный гриб',
    'зелье исцеления II': 'Зелье исцеления + Красный гриб',
    'зелье прыгучести': 'Адский нарост + Вода + Лапка кролика',
    'зелье прыгучести II': 'Зелье прыгучести + Красная пыль',
    'зелье силы': 'Адский нарост + Вода + Огненный порошок',
    'зелье силы II': 'Зелье силы + Красная пыль',
    'зелье скорости': 'Адский нарост + Вода + Сахар',
    'зелье скорости II': 'Зелье скорости + Красная пыль',
    'зелье дыхания под водой': 'Адский нарост + Вода + Рыба фугу',
    'зелье невидимости': 'Адский нарост + Вода + Золотая морковь + Приготовленный паучий глаз',
    'зелье регенерации': 'Адский нарост + Вода + Красный гриб + Паучий глаз',
    'зелье регенерации II': 'Зелье регенерации + Красная пыль',
    'зелье сопротивления огню': 'Адский нарост + Вода + Сгусток магмы',
    'зелье замедленного падения': 'Адский нарост + Вода + Мембрана фантома',
    'зелье замедленного падения II': 'Зелье падения + Красная пыль',
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "🌿 Привет, варитель Это гайд по зельеварению в Minecraft+\n\n"
        "Доступные команды:\n"
        "/potion [название зелья] — получить рецепт\n"
        "/brewing — основы зельеварения\n"
        "/potions — список обычных зелий\n"
        "/help — помощь"
    )
    bot.reply_to(message, welcome_text)

@bot.message_handler(commands=['brewing'])
def brewing_info(message):
    text = (
        "🔮 Основы зельеварения Minecraft:\n\n"
        "1. Огненный порошок — топливо.\n"
        "2. Зелье-основа + ингредиент = новое зелье.\n"
        "3. Красная пыль — увеличивает уровень зелья.\n"
        "4. Порох — делает зелье взрывным.\n"
        "5. Приготовленный паучий глаз — инвертирует эффект зелья.\n"
    )

    bot.reply_to(message, text)

@bot.message_handler(commands=['potions'])
def list_potions(message):
    potions_list = '\n'.join(POTION_GUIDE.keys())
    bot.reply_to(message, f"Доступные обычные зелья:\n{potions_list}")

@bot.message_handler(commands=['potion'])
def get_potion_recipe(message):
    try:
        potion_name = ' '.join(message.text.split(' ')[1:]).lower()
        if not potion_name:
            bot.reply_to(message, "Укажите название зелья. Пример: /potion зелье силы")
            return

        recipe = POTION_GUIDE.get(potion_name, "Зелье не найдено. Попробуйте /potions для списка.")
        bot.reply_to(message, recipe)
    except Exception:
        bot.reply_to(message, "Ошибка. Попробуйте ещё раз.")

@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = (
        "/start — начать общение\n"
        "/brewing — как варить зелья\n"
        "/potions — список обычных зелий\n"
        "/potion [название] — рецепт зелья\n"
        "/help — эта справка"
    )
    bot.reply_to(message, help_text)

bot.polling()