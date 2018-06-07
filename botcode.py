import requests
import datetime

glob_token = "610511246:AAGlbLe__skR2sn4GpoIzc-NtVkJgrgU_Vs"
glob_timeout = 30

class botHandler:
    def __init__(self, token = glob_token):
        self.token = token
        self.apiURL = "https://api.telegram.org/bot{}/".format(token)

    def getUpdates(self, offset = None, timeout = glob_timeout):
        params = {'timeout':timeout, 'offset':offset}
        method = 'getUpdates'
        response = requests.get(self.apiURL + method, data=params)
        respJson = response.json()['result']
        return respJson

    def getLastUpdate(self):
        result = self.getUpdates()
        if len(result) > 0:
            updateLast = result[-1]
        else:
            updateLast = result[len(result)]
        return updateLast

    def getChatID(update):
        chatID = update['message']['chat']['id']
        return chatID

    def sendMessage(self, chatID, text):
        params = {'chat_id': chatID, 'text': text}
        method = 'sendMessage'
        response = requests.post(self.apiURL + method, data=params)
        return response

def main():
    Ginge_420_bot = botHandler(glob_token)
    offsetNext = None
    Ginge_420_bot.getUpdates(offsetNext)
    lastUpdate = Ginge_420_bot.getLastUpdate()
    lastUpdateID = lastUpdate['update_id']
    lastChatID = lastUpdateID['message']['chat']['id']
    Ginge_420_bot.sendMessage(lastChatID, 'Hello world!')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
