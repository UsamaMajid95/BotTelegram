import telebot
from telebot import types

token='5236575684:AAFEl03G24Sg-NSfIknFdn1WU04FC27v2vA'
bot=telebot.TeleBot(token)

def create_keyboard():
    keyboard=types.InlineKeyboardMarkup()
    drink_btn=types.InlineKeyboardButton(text="drink water",callback_data=1)
    eat_btn=types.InlineKeyboardButton(text="want eat",callback_data=2)
    sleep_btn=types.InlineKeyboardButton(text="want sleep",callback_data=3)
    walk_btn=types.InlineKeyboardButton(text="want walk",callback_data=4)
    joke_btn=types.InlineKeyboardButton(text="want joke",callback_data=5)
    keyboard.add(drink_btn)
    keyboard.add(eat_btn)
    keyboard.add(sleep_btn)
    keyboard.add(walk_btn)
    keyboard.add(joke_btn)

    return keyboard



@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard=create_keyboard()
    bot.send_message(message.chat.id,"Добрый день! Выберите, что Вы хотите",reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call:True)
def call_back(call):
    keyboard = create_keyboard()
    if call.message:
        if call.data=='1':
           img = open('image1.jfif','rb')
           bot.send_photo(chat_id=call.message.chat.id,photo=img,caption= "water",reply_markup=keyboard)
           img.close()

        if call.data == '2':
           img = open("image2.jpg",'rb')
           bot.send_photo(chat_id=call.message.chat.id, photo=img, caption="food", reply_markup=keyboard)
           img.close()

        if call.data == '3':
           img = open("image7.jfif", 'rb')
           bot.send_photo(chat_id=call.message.chat.id, photo=img, caption="sleep", reply_markup=keyboard)
           img.close()

        if call.data == '4':
           img = open('image3.jpg','rb')
           bot.send_photo(chat_id=call.message.chat.id, photo=img, caption="walk", reply_markup=keyboard)
           img.close()

        if call.data == '5':
           img = open('image5.jpg', 'rb')
           bot.send_photo(chat_id=call.message.chat.id, photo=img, caption="joke", reply_markup=keyboard)
           img.close()

if __name__ == '__main__':
    bot.polling(none_stop=True)