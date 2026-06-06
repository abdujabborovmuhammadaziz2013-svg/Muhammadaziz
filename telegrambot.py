import telebot 

API_TOKEN='8891443647:AAGn3NAeBXcwINAob72oO0GqZ4oPgpYcwRk'
bot = telebot.Telebot(API_TOKEN)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id=message.from_user.id
    with open('users.txt','r') as f:
        users = f.read()
        if str(user_id) not in users:
            with open('users.txt', 'a') as f:
                f.write(f'(user_id)\n')

    name = message.from_user.first_name
    bot.reply_to(message, text=f"""Assalomu aleykum {name}\n Mening aqllilar uchun botimga xush kelibsiz!""")

@bot.message_handler(commands=['count'])
def send_count(message):
    with open('users.txt', 'r') as f:
        users = f.readlines()
        all_users = len(users)

    bot.reply_to(message, text:f"""Assalomu aleykum sizning foydalanuvchilar soni{all_users} nafar""")


@bot.message_handler(commands=['ads'])
def send_ads(message):
    user_id=message.from_user.id
    
    if user_id == 92473435:
        print(user.id)

    with open('users.txt', 'r') as f:
        users =list(map(int, f.readlines()))
    for user in users:
                    bot.reply_to(message, text:f"""Bu xabar test sifatida yujborilmoqda""")
    else:
        bot.reply_to(message, text:"Bu command sizga tegishli emas")

@bot.message_handler(commands=['help'])
def help_func(message):
    bot.reply_to(message, text:f"""Yordam menyusi""")