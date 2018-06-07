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
        response = requests.get(self.apiURL + 'getUpdates', data=params)
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
        response = requests.post(self.apiURL + 'sendMessage', data=params)
        return response

def main():
    Ginge_420_bot = botHandler(glob_token)
    now = datetime.datetime.now()
    last = now
    offsetNext = None
    Ginge_420_bot.getUpdates(offsetNext)
    lastUpdateID = Ginge_420_bot.getLastUpdate()
    lastChatID = lastUpdateID['message']['chat']['id']
    Ginge_420_bot.sendMessage(lastChatID, 'Hello world!')
    while True:
        Ginge_420_bot.getUpdates(offset=offsetNext)
        lastUpdateID = Ginge_420_bot.getLastUpdate()
        lastChatID = lastUpdateID['message']['chat']['id']
        now = datetime.datetime.now()
        if now.second != last.second:
            Ginge_420_bot.sendMessage(lastChatID, 'Time: {0}:{1}:{2}'.format(now.hour,now.minute,now.second))
        last = now
        offsetNext = lastUpdateID + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
