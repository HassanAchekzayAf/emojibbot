import telebot

BOT_TOKEN = "8626392285:AAHMbGfXTaGMluZFC9bMYPJLsFSkoBu23aI"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def get_emoji_id(message):
    # اگر پیام شامل ایموجی باشد
    if message.entities:
        for entity in message.entities:
            if entity.type == 'custom_emoji':
                emoji_id = entity.custom_emoji_id
                # ربات ID را به شما می‌دهد
                bot.reply_to(message, f"✅ ID این ایموجی پریمیوم:\n`{emoji_id}`", parse_mode='Markdown')
                return
    bot.reply_to(message, "این یک ایموجی معمولی است یا پریمیوم نیست.")

print("ربات روشن شد. لطفا با اکانت پریمیوم ایموجی بفرستید تا ID بگیرید.")
bot.infinity_polling()