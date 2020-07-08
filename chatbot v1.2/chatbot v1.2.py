from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os


def setup():
    chatbot = ChatBot('Bot',storage_adapter='chatterbot.storage.SQLStorageAdapter',trainer='chatterbot.trainers.ListTrainer')
    for file in os.listdir('E:\chatbot v1.0\chatbot v1.2\data/'):
        convData = open(r'E:\chatbot v1.0\chatbot v1.2\data/' + file, encoding='latin-1').readlines()
        chatbot.set_trainer(ListTrainer)
        chatbot.train(convData)
        print("Training completed")
        #E:\chatbot v1.0\chatbot v1.2\data


setup()
