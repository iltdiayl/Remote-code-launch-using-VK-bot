import vk_api, json
from vk_api.longpoll import VkLongPoll, VkEventType
import pyautogui 
import pyautogui as pg
import time

t = time.strftime("%X")

vk_session = vk_api.VkApi(token = "your token")
vk = vk_session.get_api()
longpol = VkLongPoll(vk_session)
pyautogui.FAILSAFE= False 

def get_but(text, color):
    return {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"" + "1" + "\"}",
                    "label": f"{text}"
                },
                "color": f"{color}"
            }

keyboard = {
    "one_time" : False,
    "buttons" : [
        [get_but('Видео 1' , 'primary'), get_but('Видео 2', 'primary')],
        [get_but("Минус курсор", "negative"), get_but('Минус вкладка', 'negative')],
        [get_but("Гифка", "secondary"), get_but('Далее', 'positive')]
    ]
}
keyboard2 = {
    "one_time" : False,
    "buttons" : [
        [get_but('Профиль' , 'primary'), get_but('Win', 'primary')],
        [get_but('Свернуть вкладки' , 'positive'), get_but('Язык', 'positive')],
        [get_but("Назад", "negative"), get_but('Прячь', 'secondary')]
    ]
}
keyboard = json.dumps(keyboard, ensure_ascii = False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

keyboard2 = json.dumps(keyboard2, ensure_ascii = False).encode('utf-8')
keyboard2 = str(keyboard2.decode('utf-8'))

def sender(id, text, key):
    vk_session.method('messages.send', {'user_id' : id, 'message' : text, 'random_id' : 0, 'keyboard' : key})
 
def main():
    
    a = "Пользователь"
    for event in longpol.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                id = event.user_id
                msg = event.text.lower()
                 

                if msg == "видео 1":
                    sender(id, "Код с видео был успешно запущен",keyboard) 
                    pg.hotkey("winleft")
                    time.sleep(1)
                    pg.typewrite("opera")
                    time.sleep (2)
                    pg.press("Enter")
                    time.sleep(10)
                    pg.typewrite("https://www.youtube.com/watch?v=NPe2rwUZbR0") # гимн казахстана
                    pg.press("Enter")
                    time.sleep(6)
                    pg.press("f")
                    sender(id, "Код с видео был завершён",keyboard)
                
                if msg == "видео 2":
                    sender(id, "Код с видео был успешно запущен",keyboard) 
                    pg.hotkey("winleft")
                    time.sleep(1)
                    pg.typewrite("opera")
                    time.sleep (2)
                    pg.press("Enter")
                    time.sleep(10)
                    pg.typewrite("https://www.youtube.com/watch?v=Ob5FyMJX2zk") # 
                    pg.press("Enter")
                    time.sleep(6)
                    pg.press("f")
                    sender(id, "Код с видео был завершён",keyboard)

                
                if msg == "минус курсор":
                    sender(id, "Курсор затерен на 10сек",keyboard)
                    for i in range(100):
                        pyautogui.moveTo(0, 0)
                    
                if msg == "прячь" and a == "admin":
                    sender(id, "Сервер был успешно убит",keyboard2)
                    pyautogui.FAILSAFE= True
                    while True:
                        pyautogui.moveTo(0, 0)
                        pyautogui.moveTo(100, 200)
                        pyautogui.moveTo(400, 300)
                        pyautogui.moveTo(200, 200)
                if msg == "прячь" and a == "Пользователь":
                    sender(id, "Ты не админ",keyboard2)
                
                if msg == "гифка":
                    sender(id, "Код с гифкой был успешно запущен", keyboard) 
                    pg.hotkey("winleft")
                    time.sleep(1)
                    pg.typewrite("opera")
                    time.sleep (2)
                    pg.press("Enter")
                    time.sleep(10)
                    pg.typewrite("https://i.gifer.com/7Rez.mp4") # гифка гуля
                    pg.press("Enter")
                    time.sleep(6)
                    pg.press("F11")
                    sender(id, "Код с гифкой был завершён", keyboard)
                
                if msg == "минус вкладка":
                    sender(id, "Вкладка закрыта",keyboard)
                    pg.hotkey("ctrl", "F4")
                
                if msg == "свернуть вкладки":
                    sender(id, "Вкладки скрыты",keyboard2)
                    pg.hotkey("winleft", "d")

                if msg == "язык":
                    sender(id, "Язык был сменён", keyboard2)
                    pg.hotkey("shift", "alt")
                
                if msg == "обновить":
                    sender(id, "Бот обновлён", keyboard)
                
                if msg == "win" or msg == "Вин":
                    sender(id, "Кнопка win нажата",keyboard2)
                    pg.hotkey("winleft")
              
                
                if msg == "далее":
                    sender(id,"а", keyboard2)
                if msg == "назад":
                    sender(id,"а", keyboard)
                if msg == "admin228":
                    a = "admin"
                    sender(id,"Вы теперь админ", keyboard2)
                if msg == "профиль":
                    sender(id,f"Вы: {a} \nСервер был подключён в: {t} \nВремя у сервера: " + time.strftime("%X") , keyboard2)
                    
                    
 
while True:
    main()
                                                     
