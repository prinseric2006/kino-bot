import os
from telebot import TeleBot, types

# Render Environment Variables bo'limidagi BOT_TOKEN nomli kalitdan tokenni oladi
TOKEN = os.environ.get('BOT_TOKEN')
bot = TeleBot(TOKEN)

# 1. Maxfiy kanallaringiz ID-si va ularning Taklif havolalari (Join Request link)
CHANNELS = [
    {
        "id": -1003920903568,
        "link": "https://t.me/+TK5aA-Vv1zI4Njc6",
        "name": "1-Kanal"
    },
    {
        "id": -1004397640907,
        "link": "https://t.me/+DVwzomTsLS05Y2My",
        "name": "2-Kanal"
    },
    {
        "id": -1004398516177,
        "link": "https://t.me/+TcdO4ASzsiBhNTBi",
        "name": "3-Kanal"
    },
    {
        "id": -1004442275540,
        "link": "https://t.me/+ZXtkEoJCBEljM2Zi",
        "name": "4-Kanal"
    },
    {
        "id": -1003753617217,
        "link": "https://t.me/+U7E9evjCvTozMGIy",
        "name": "5-Kanal"
    }
]

# Kinolar bazasi: "Kino kodi": Kanaldagi post ID-si
MOVIES = {
    "1200": 3,
    "1201": 4,
    "1202": 5,
}

MAIN_MOVIE_CHANNEL = -1004407760150  # Kinolar joylangan asosiy kanal ID-si

# Zayavka yuborgan foydalanuvchilarni saqlash xotirasi
PENDING_REQUESTS = {}

# Foydalanuvchi kanallarga a'zo yoki zayavka yuborganini tekshirish
def check_subscriptions(user_id):
    unsubscribed_channels = []
    user_requests = PENDING_REQUESTS.get(user_id, set())

    for ch in CHANNELS:
        ch_id = ch["id"]
        # 1-tekshiruv: Agar foydalanuvchi zayavka yuborgan bo'lsa
        if ch_id in user_requests:
            continue
            
        # 2-tekshiruv: Telegram kanaldagi statusini tekshirish
        try:
            member = bot.get_chat_member(chat_id=ch_id, user_id=user_id)
            if member.status in ['left', 'kicked']:
                unsubscribed_channels.append(ch)
        except Exception:
            unsubscribed_channels.append(ch)
            
    return unsubscribed_channels

# Obuna tugmalarini yaratish
def get_subscription_keyboard(unsubscribed_channels):
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    for idx, ch in enumerate(unsubscribed_channels, start=1):
        btn = types.InlineKeyboardButton(text=f"➕ {idx}-Kanalga a'zo bo'lish (Zayavka)", url=ch["link"])
        markup.add(btn)
        
    check_btn = types.InlineKeyboardButton(text="✅ Obunani / Zayavkani tekshirish", callback_data="check_sub")
    markup.add(check_btn)
    return markup

# FOYDALANUVCHI KANALGA ZAYAVKA TASHAGANDA SHU HANDLER ISHLAYDI
@bot.chat_join_request_handler()
def handle_join_request(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    
    if user_id not in PENDING_REQUESTS:
        PENDING_REQUESTS[user_id] = set()
    
    PENDING_REQUESTS[user_id].add(chat_id)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    unsubscribed = check_subscriptions(user_id)
    
    if unsubscribed:
        text = "⚠️ Botdan foydalanish uchun quyidagi kanallarga zayavka yuboring (ulaning):"
        bot.send_message(message.chat.id, text, reply_markup=get_subscription_keyboard(unsubscribed))
    else:
        text = (
            f"👋 Salom, {message.from_user.first_name}!\n\n"
            "🎬 Kino kodini kiriting (masalan: `69`):"
        )
        bot.send_message(message.chat.id, text, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == "check_sub")
def callback_check(call):
    user_id = call.from_user.id
    unsubscribed = check_subscriptions(user_id)
    
    if unsubscribed:
        bot.answer_callback_query(call.id, "❌ Hali barcha kanallarga zayavka yubormadingiz!", show_alert=True)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="⚠️ Botdan foydalanish uchun barcha kanallarga zayavka yuborishingiz kerak:",
            reply_markup=get_subscription_keyboard(unsubscribed)
        )
    else:
        bot.answer_callback_query(call.id, "✅ Obuna / Zayavka tasdiqlandi!")
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="🎉 Barcha kanallarga zayavka yuborildi!\n\n🎬 Endi kino kodini yuborishingiz mumkin (masalan: `69`):"
        )

@bot.message_handler(func=lambda message: True)
def handle_movie_code(message):
    user_id = message.from_user.id
    unsubscribed = check_subscriptions(user_id)
    
    if unsubscribed:
        text = "⚠️ Siz kanallarga zayavka yubormagansiz. Botdan foydalanish uchun qayta obuna bo'ling:"
        bot.send_message(message.chat.id, text, reply_markup=get_subscription_keyboard(unsubscribed))
        return

    code = message.text.strip()
    if code in MOVIES:
        msg_id = MOVIES[code]
        try:
            bot.copy_message(
                chat_id=message.chat.id,
                from_chat_id=MAIN_MOVIE_CHANNEL,
                message_id=msg_id
            )
        except Exception as e:
            bot.reply_to(message, "⚠️ Kinoni yuborishda xatolik yuz berdi. Bot kanalda admin ekanligini tekshiring.")
    else:
        bot.reply_to(message, "❌ Bunday kodli kino topilmadi.")

if __name__ == '__main__':
    bot.infinity_polling()
    
