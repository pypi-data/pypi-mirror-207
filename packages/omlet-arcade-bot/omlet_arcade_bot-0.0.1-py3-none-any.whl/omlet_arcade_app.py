import requests
from bs4 import BeautifulSoup

class Auth:
    def __init__(self, api_key):
        self.api_key = api_key

    def api(self):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get("https://api.omlet.gg/v1/user", headers=headers)
        return response.json()

class Bot:
    def __init__(self, stream_link, interaction, role, nickname):
        self.stream_link = stream_link
        self.interaction = interaction
        self.role = role
        self.nickname = nickname

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
            # реакция на слово "ban" для модератора
            pass
        elif self.nickname == self.author and word == "subscribe":
            # реакция на слово "subscribe" для автора
            pass
