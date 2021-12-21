import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import keyboards as kb
import config 
import time

bot = telebot.TeleBot(config.TOKEN)

final_dict = {}
user_info = {} 

@bot.message_handler(commands=['start'])
def start(msg):
    start_msg = 'Привіт, я бот для реєстрації на 5-ий щорічний Молодіжний форум Кельменеччини'
    bot.send_message(msg.chat.id, start_msg, reply_markup=kb.home())
    
    if msg.chat.id == 948240305 :
        bot.send_message(msg.chat.id, 'ку ку') 
    
@bot.message_handler(regexp='Інформація про форум')
def send_info(msg):
    info = f'На цю подію молодь Кельменеччини очікувала давно😎\n\n' \
            f'Молодіжному форуму Кельменеччини бути🤩\n\n' \
            f'📍грудня у смт. Кельменці представники влади, молодіжні працівники, представники молодіжних рад, громадських організацій, лідери думок та небайдужа молодь будуть шукати відповіді на запитання, «А яка ж участь молоді у розвитку громади»🤷🏼\n\n' \
            f'Учасники зможуть попрацювати у трьох напрямках:\n' \
            f'➖Розвиток молодіжної інфраструктури у нашій громаді\n' \
            f'➖Розвиток молодіжної ради\n' \
            f'➖Молодіжні ініціативи, які змінюють громади\n\n' \
            f'📌Організатори форуму: \n' \
            f'Кельменецька селищна рада, Активна молодь Кельменеччини'
    bot.send_message(msg.chat.id, info, reply_markup=kb.get_back())
    
@bot.message_handler(regexp='Назад')
def back(msg):
    bot.send_message(msg.chat.id,'Ви повернулися назад',reply_markup=kb.home())    


@bot.message_handler(regexp='Зареєструватися')
def start_reg(msg):
    bot.send_message(msg.chat.id, 'Ну що ж, почнемо?', reply_markup=kb.delete())
    time.sleep(1)
    bot.send_message(msg.chat.id, 'Як тебе звати?')
    bot.register_next_step_handler(msg, get_name)
    
def get_name(msg):    
    if not msg.chat.id in user_info:
            user_info[msg.chat.id] = []
            
    user_id = msg.chat.id
    user_info[msg.chat.id].append(user_id) # 0 - id
    
    user_name = msg.text
    user_info[msg.chat.id].append(user_name) # 1 - name
    
    bot.send_message(msg.chat.id, 'Напиши своє прізвище)')
    bot.register_next_step_handler(msg, get_surname)

def get_surname(msg):
    user_surname = msg.text
    user_info[msg.chat.id].append(user_surname) # 2 - surname
    
    bot.send_message(msg.chat.id, 'Ну і по-батькові')
    bot.register_next_step_handler(msg, get_fathername)
    
def get_fathername(msg):
    user_fathername = msg.text
    user_info[msg.chat.id].append(user_fathername) # 3 - fathername
    
    bot.send_message(msg.chat.id, 'Для звязку нам потрібен номер телефону (натисніть кнопку)', reply_markup=kb.get_contact())
    bot.register_next_step_handler(msg, get_contact)
    
def get_contact(msg):
    try :
        user_contact = msg.contact.phone_number
        user_info[msg.chat.id].append(user_contact) # 4 - number
        
    except AttributeError:
        user_contact = msg.text
        user_info[msg.chat.id].append(user_contact) # 4 - number
    
    user_username = msg.from_user.username
    user_info[msg.chat.id].append(msg.from_user.username) # 5 - username  
     
    bot.send_message(msg.chat.id, 'Молодець!', reply_markup=kb.delete())
    bot.send_message(msg.chat.id, 'Тепер скинь посилання на якусь соціальну мережу (інстаграм/фейсбук)')
    bot.register_next_step_handler(msg, get_username)

def get_username(msg):
    user_link = msg.text
    user_info[msg.chat.id].append(msg.text) # 6 - link
    
    bot.send_message(msg.chat.id, "Вау, гарні фото)")
    time.sleep(1)
    bot.send_message(msg.chat.id, "А з якого ти населеного пункту?")
    bot.register_next_step_handler(msg, get_location)
    
def get_location(msg):
    user_location = msg.text
    user_info[msg.chat.id].append(msg.text) # 7 - location
    
    bot.send_message(msg.chat.id, "Чекаємо запрошення у гості))")
    time.sleep(1)
    bot.send_message(msg.chat.id, "А скільки такій крутій персоні років?")
    bot.register_next_step_handler(msg, get_age)
    
def get_age(msg):
    user_info[msg.chat.id].append(msg.text) # 8 - age
    bot.send_message(msg.chat.id, "Начебто ще молодий))")
    time.sleep(1)
    bot.send_message(msg.chat.id, "Який статус представляєте? (молодіжна рада, ініціативна молодь, учнівське самоврядування тощо)")
    bot.register_next_step_handler(msg, get_type)
    
def get_type(msg):
    user_info[msg.chat.id].append(msg.text) # 9 - type   
    bot.send_message(msg.chat.id, "Чотко")
    time.sleep(1)    
    bot.send_message(msg.chat.id, "Ну і на кінець, напиши свої очікування від форуму)")
    bot.register_next_step_handler(msg, get_expectation)
    
def get_expectation(msg):
    user_info[msg.chat.id].append(msg.text) # 10 - expectation 
    bot.send_message(msg.chat.id, "Все, тепер чекай посилання до спільного чату, адже це буде запрошенням на форум", reply_markup=kb.home())
    print(user_info)
    
    bot.send_message(948240305, 'ку молодіжним гоблінам))')
    msg1 = f'ПІБ - {user_info[msg.chat.id][1]} {user_info[msg.chat.id][2]} {user_info[msg.chat.id][3]}\n\n' \
            f'Номер телефону - {user_info[msg.chat.id][4]}\n\n' \
            f'Нік у телеграмі - @{user_info[msg.chat.id][5]}\n\n' \
            f'Посилання на соцмережу - {user_info[msg.chat.id][6]}\n\n' \
            f'Місце проживання - {user_info[msg.chat.id][7]}\n\n' \
            f'Вік - {user_info[msg.chat.id][8]}\n\n' \
            f'Кого представляє - {user_info[msg.chat.id][9]}\n\n' \
            f'Очікування - {user_info[msg.chat.id][10]}\n' 

    bot.send_message(948240305, msg1)
    bot.send_message(707897264, 'ку молодіжним гоблінам))')
    bot.send_message(707897264, msg1)
    user_info[msg.chat.id].clear()


    


bot.polling(none_stop=True, interval=0)