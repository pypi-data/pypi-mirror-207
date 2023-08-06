import requests
from bs4 import BeautifulSoup

class Auth:
    def __init__(self, api_key):
        self.api_key = api_key

    def api(self):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get("https://api.omlet.gg/v1/user", headers=headers)
        return response.json()

class Power:
    def __init__(self, bot):
        self.bot = bot

    def ban(self, user):
        if self.bot.role != "moderator":
            print("Error: check bot role, he does not have permission to ban users.")
            return
        # бан пользователя
        pass

    def delete_message(self, message_id):
        if self.bot.role != "moderator" and self.bot.nickname != self.bot.author:
            print("Error: check bot role, he does not have permission to delete messages.")
            return
        # удаление сообщения
        pass

class Bot:
    def __init__(self, stream_link, interaction, role, nickname):
        self.stream_link = stream_link
        self.interaction = interaction
        self.role = role
        self.nickname = nickname
        self.author = None
        self.power = Power(self)

    def interaction(self):
        if self.interaction == "command":
            # реакция на команды
            pass
        elif self.interaction == "moderator":
            # реакция на действия модератора
            if self.role == "moderator":
                # реакция на действия для модератора
                pass
        elif self.interaction == "author":
            # реакция на действия автора стрима
            if self.nickname == self.author:
                # реакция на действия для автора
                pass

    def get_stream_info(self):
        response = requests.get(self.stream_link)
        soup = BeautifulSoup(response.content, "html.parser")
        # парсинг информации о стриме
        pass

    def message_context(self, word):
        if self.role == "moderator" and word == "ban":
            self.power.ban("user_to_ban")
        elif self.nickname == self.author and word == "delete":
            self.power.delete_message("message_id_to_delete")

