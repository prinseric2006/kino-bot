import os
from threading import Thread
from flask import Flask
from telebot import TeleBot, types

# ---------------------------------------------------
# 1. RENDER'DA BEPUL (WEB SERVICE) ISHLASHI UCHUN SOXTA WEB-SERVER
app = Flask('')

@app.route('/')
def home():
    return "Bot faol ishlamoqda!"

def run():
    # Render avtomatik ajratadigan portni oladi
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Web-serverni fonda ishga tushirish
keep_alive()

# ---------------------------------------------------
# 2. TELEGRAM BOT SOZLAMALARI

# Render Environment Variables bo'limidagi BOT_TOKEN nomli kalitdan tokenni oladi
TOKEN = os.environ.get('BOT_TOKEN')
bot = TeleBot(TOKEN)

# Maxfiy Telegram kanallaringiz ro'yxati
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
        "id": -1003753617217,
        "link": "https://t.me/+U7E9evjCvTozMGIy",
        "name": "4-Kanal"
    }
]

# YouTube kanal havolasi
YOUTUBE_LINK = "https://youtube.com/@cr1menal23?si=qzGTFp2N88-t4y_o"

# Kinolar bazasi: "Kino kodi": Kanaldagi post ID-si
MOVIES = {
    "1200": 11,
    "1201": 12,
    "1202": 13,
    "1203": 15,
    "1204": 18,
    "1205": 19,
    "1": 20,
    "2": 21,
    "3": 22,
    "4": 23,
    "5": 24,
    "6": 25,
    "7": 26,
    "8": 27,
    "9": 28,
    "10": 29,
    "11": 30,
    "12": 31,
    "13": 32,
    "14": 33,
    "15": 34,
    "16": 35,
    "17": 36,
    "18": 37,
    "19": 38,
    "20": 39,
    "21": 40,
    "22": 41,
    "23": 42,
    "24": 43,
    "25": 44,
    "26": 45,
    "27": 46,
    "28": 47,
    "29": 48,
    "30": 49,
    "31": 50,
    "32": 51,
    "33": 52,
    "34": 53,
    "35": 54,
    "36": 55,
    "37": 56,
    "38": 57,
    "39": 58,
    "40": 59,
    "41": 60,
    "42": 61,
    "43": 62,
    "44": 63,
    "45": 64,
    "46": 65,
    "47": 66,
    "48": 67,
    "49": 68,
    "50": 69,
    "51": 70,
    "52": 71,
    "53": 72,
    "54": 73,
    "55": 74,
    "56": 75,
    "57": 76,
    "58": 77,
    "59": 78,
    "60": 79,
    "61": 80,
    "62": 81,
    "63": 82,
    "64": 83,
    "65": 84,
    "66": 85,
    "67": 86,
    "68": 87,
    "69": 88,
    "70": 89,
    "71": 90,
    "72": 91,
    "73": 92,
    "74": 93,
    "75": 94,
    "76": 95,
    "77": 96,
    "78": 97,
    "79": 98,
    "80": 99,
    "81": 100,
    "82": 101,
    "83": 102,
    "84": 103,
    "85": 104,
    "86": 105,
    "87": 106,
    "88": 107,
    "89": 108,
    "90": 109,
    "91": 110,
    "92": 111,
    "93": 112,
    "94": 113,
    "95": 114,
    "96": 115,
    "97": 116,
    "98": 117,
    "99": 118,
    "100": 119,
    "101": 120,
    "102": 121,
    "103": 122,
    "104": 123,
    "105": 124,
    "106": 125,
    "107": 126,
    "108": 127,
    "109": 128,
    "110": 129,
    "111": 130,
    "112": 131,
    "113": 132,
    "114": 133,
    "115": 134,
    "116": 135,
    "117": 136,
    "118": 220,
    "119": 138,
    "120": 139,
    "121": 140,
    "122": 141,
    "123": 142,
    "124": 143,
    "125": 144,
    "126": 145,
    "127": 146,
    "128": 147,
    "129": 148,
    "130": 149,
    "131": 150,
    "132": 151,
    "133": 152,
    "134": 153,
    "135": 154,
    "136": 155,
    "137": 156,
    "138": 157,
    "139": 158,
    "140": 159,
    "141": 160,
    "142": 161,
    "143": 162,
    "144": 163,
    "145": 164,
    "146": 165,
    "147": 166,
    "148": 167,
    "149": 168,
    "150": 169,
    "151": 170,
    "152": 171,
    "153": 172,
    "154": 173,
    "155": 174,
    "156": 175,
    "157": 176,
    "158": 177,
    "159": 178,
    "160": 179,
    "161": 180,
    "162": 181,
    "163": 182,
    "164": 183,
    "165": 184,
    "166": 185,
    "167": 186,
    "168": 187,
    "169": 188,
    "170": 189,
    "171": 190,
    "172": 191,
    "173": 192,
    "174": 193,
    "175": 194,
    "176": 195,
    "177": 196,
    "178": 197,
    "179": 198,
    "180": 199,
    "181": 200,
    "182": 201,
    "183": 202,
    "184": 203,
    "185": 204,
    "186": 205,
    "187": 206,
    "188": 207,
    "189": 208,
    "190": 209,
    "191": 210,
    "192": 211,
    "193": 212,
    "194": 213,
    "195": 214,
    "196": 215,
    "197": 216,
    "198": 217,
    "199": 218,
    "200": 219,
    "201": 263,
    "202": 264,
    "203": 265,
    "204": 266,
    "205": 267,
    "206": 268,
    "207": 278,
    "208": 277,
    "209": 274,
    "210": 276,
    "211": 271,
    "212": 221,
    "213": 222,
    "214": 223,
    "215": 224,
    "216": 225,
    "217": 226,
    "218": 227,
    "219": 228,
    "220": 229,
    "221": 230,
    "222": 231,
    "223": 232,
    "224": 233,
    "225": 234,
    "226": 235,
    "227": 236,
    "228": 237,
    "229": 238,
    "230": 239,
    "231": 240,
    "232": 241,
    "233": 242,
    "234": 243,
    "235": 244,
    "236": 245,
    "237": 246,
    "238": 247,
    "239": 248,
    "240": 249,
    "241": 250,
    "242": 251,
    "243": 252,
    "244": 253,
    "245": 254,
    "246": 255,
    "247": 256,
    "248": 257,
    "249": 258,
    "250": 259,
    "251": 260,
    "252": 261,
    "253": 262,
    "254": 263,
    "255": 264,
    "256": 265,
    "257": 266,
    "258": 267,
    "259": 268,
    "260": 269,
    "261": 270,
    "262": 271,
    "263": 272,
    "264": 273,
    "265": 274,
    "266": 275,
    "267": 279,
    "268": 280,
    "269": 281,
    "270": 282,
    "271": 283,
    "272": 284,
    "273": 285,
    "274": 286,
    "275": 287,
    "276": 288,
    "277": 289,
    "278": 290,
    "279": 291,
    "280": 292,
    "281": 293,
    "282": 294,
    "283": 295,
    "284": 296,
    "285": 297,
    "286": 298,
    "287": 299,
    "288": 300,
    "289": 301,
    "290": 302,
    "291": 303,
    "292": 304,
    "293": 305,
    "294": 306,
    "295": 307,
    "296": 308,
    "297": 309,
    "298": 310,
    "299": 311,
    "300": 312,
    "301": 313,
    "302": 314,
    "303": 315,
    "304": 316,
    "305": 317,
    "306": 318,
    "307": 319,
    "308": 320,
    "309": 321,
    "310": 322,
    "311": 323,
    "312": 324,
    "313": 325,
    "314": 326,
    "315": 327,
    "316": 328,
    "317": 329,
    "318": 330,
    "319": 331,
    "320": 332,
    "321": 333,
    "322": 334,
    "323": 335,
    "324": 336,
    "325": 337,
    "326": 338,
    "327": 339,
    "328": 340,
    "329": 341,
    "330": 342,
    "331": 343,
    "332": 344,
    "333": 345,
    "334": 346,
    "335": 347,
    "336": 348,
    "337": 349,
    "338": 350,
    "339": 351,
    "340": 352,
    "341": 353,
    "342": 354,
    "343": 355,
    "344": 356,
    "345": 357,
    "346": 358,
    "347": 359,
    "348": 360,
    "349": 361,
    "350": 362,
    "351": 363,
    "352": 364,
    "353": 365,
    "354": 366,
    "355": 367,
    "356": 368,
    "357": 369,
    "358": 370,
    "359": 371,
    "360": 372,
    "361": 373,
    "362": 374,
    "363": 375,
    "364": 376,
    "365": 377,
    "366": 378,
    "367": 379,
    "368": 380,
    "369": 381,
    "370": 382,
    "371": 383,
    "372": 384,
    "373": 385,
    "374": 386,
    "375": 387,
    "376": 388,
    "377": 389,
    "378": 390,
    "379": 391,
    "380": 392,
    "381": 393,
    "382": 394,
    "383": 395,
    "384": 396,
    "385": 397,
    "386": 398,
    "387": 399,
    "388": 400,
    "389": 401,
    "390": 402,
    "391": 403,
    "392": 404,
    "393": 405,
    "394": 406,
    "395": 407,
    "396": 408,
    "397": 409,
    "398": 410,
    "399": 411,
    "400": 412,
    "401": 413,
    "402": 414,
    "403": 415,
    "404": 416,
    "405": 417,
    "406": 418,
    "407": 419,
    "408": 420,
    "409": 421,
    "410": 422,
    "411": 423,
    "412": 424,
    "413": 425,
    "414": 426,
    "415": 427,
    "416": 428,
    "417": 429,
    "418": 430,
    "419": 431,
    "420": 432,
    "421": 433,
    "422": 434,
    "423": 435,
    "424": 436,
    "425": 437,
    "426": 438,
    "427": 439,
    "428": 440,
    "429": 441,
    "430": 442,
    "431": 443,
    "432": 444,
    "433": 445,
    "434": 446,
    "435": 447,
    "436": 448,
    "437": 449,
    "438": 450,
    "439": 451,
    "440": 452,
    "441": 453,
    "442": 454,
    "443": 455,
    "444": 456,
    "445": 457,
    "446": 458,
    "447": 459,
    "448": 460,
    "449": 461,
    "450": 462,
    "451": 463,
    "452": 464,
    "453": 465,
    "454": 466,
    "455": 467,
    "456": 468,
    "457": 469,
    "458": 470,
    "459": 471,
    "460": 472,
    "461": 473,
    "462": 474,
    "463": 475,
    "464": 476,
    "465": 477,
    "466": 478,
    "467": 479,
    "468": 480,
    "469": 481,
    "470": 482,
    "471": 483,
    "472": 484,
    "473": 485,
    "474": 486,
    "475": 487,
    "476": 488,
    "477": 489,
    "478": 490,
    "479": 491,
    "480": 492,
    "481": 493,
    "482": 494,
    "483": 495,
    "484": 496,
    "485": 497,
    "486": 498,
    "487": 499,
    "488": 500,
    "489": 501,
    "490": 502,
    "491": 503,
    "492": 504,
    "493": 505,
    "494": 506,
    "495": 507,
    "496": 508,
    "497": 509,
    "498": 510,
    "499": 511,
    "500": 512,
    "501": 513,
    "502": 514,
    "503": 515,
    "504": 516,
    "505": 517,
    "506": 518,
    "507": 519,
    "508": 520,
    "509": 521,
    "510": 522,
    "511": 523,
    "512": 524,
    "513": 525,
    "514": 526,
    "515": 527,
    "516": 528,
    "517": 529,
    "518": 530,
    "519": 531,
    "520": 532,
    "521": 533,
    "522": 534,
    "523": 535,
    "524": 536,
    "525": 537,
    "526": 538,
    "527": 539,
    "528": 540,
    "529": 541,
    "530": 542,
    "531": 543,
    "532": 544,
    "533": 545,
    "534": 546,
    "535": 547,
    "536": 548,
    "537": 549,
    "538": 550,
    "539": 551,
    "540": 552,
    "541": 553,
    "542": 554,
    "543": 555,
    "544": 556,
    "545": 557,
    "546": 558,
    "547": 559,
    "548": 560,
    "549": 561,
}

MAIN_MOVIE_CHANNEL = -1004407760150  # Kinolar joylangan asosiy kanal ID-si

# Zayavka yuborgan foydalanuvchilarni saqlash xotirasi
PENDING_REQUESTS = {}

# ---------------------------------------------------
# 3. YORDAMCHI FUNKSIYALAR

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

def get_subscription_keyboard(unsubscribed_channels):
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    # YouTube kanal uchun maxsus tugma
    yt_btn = types.InlineKeyboardButton(text="➕Link orqali obuna boʻlish", url=YOUTUBE_LINK)
    markup.add(yt_btn)
    
    # Telegram kanallar uchun tugmalar
    for idx, ch in enumerate(unsubscribed_channels, start=1):
        btn = types.InlineKeyboardButton(text=f"➕ {idx}-Telegram kanalga a'zo bo'lish (Zayavka)", url=ch["link"])
        markup.add(btn)
        
    check_btn = types.InlineKeyboardButton(text="✅ Obunani / Zayavkani tekshirish", callback_data="check_sub")
    markup.add(check_btn)
    return markup

# ---------------------------------------------------
# 4. HANDLERLAR (BOT ISHLASH MANTIG'I)

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
        text = "⚠️ Botdan foydalanish uchun quyidagi kanallarga a'zo bo'ling/zayavka yuboring:"
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
        bot.answer_callback_query(call.id, "❌ Hali barcha Telegram kanallarga zayavka yubormadingiz!", show_alert=True)
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
            print(f"Xatolik: {e}")
    else:
        bot.reply_to(message, "❌ Bunday kodli kino topilmadi.")

# Botni ishga tushirish
if __name__ == '__main__':
    bot.infinity_polling()
