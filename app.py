from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os


tot = ChatBot('Bot')
tot.set_trainer(ListTrainer)

for files in os.listdir('E:/Chat Bot\Chatbot_Project-master\data/'):
        data = open('E:/Chat Bot\Chatbot_Project-master\data/' + files , 'r').readlines()
        tot.train(data)
while True:
        message = input('you:')
        if message.strip() != 'Bye':
                reply = tot.get_response(message)
                print('JOB :',reply)
        if message.strip() == 'Bye':
                print('JOB : Bye')
                break
