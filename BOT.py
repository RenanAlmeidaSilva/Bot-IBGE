import logging
import json

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1739674397:AAEvt9_ta6ghkEJpPW1pfl_mKU7MOGY4odI'

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
with open('full.json', 'r') as f:
    full = json.load(f)


@dp.message_handler(commands=['info'])
async def send_welcome(message: types.Message):
    await message.reply("Hi! I'm Bot IBGE!\nPowered by:\nDev. Renan Almeida. (Estagiário Developer)\n")


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    with open('user.txt') as file:
        userList = file.read()
    user = userList.split('\n')
    textomsg1 = ''
    if message['chat']['username']:
        textomsg1 += message["chat"]["username"]
        with open('logs.log', 'a') as arquivo:
            arquivo.write('\n' + message["chat"]["username"] + '\n\n')
        if textomsg1 in user:
            await message.answer('Olá ' + message['chat'][
                'first_name'] + ', eu sou o Bot IBGE, criado para encontrar as informações do seu nome ou de outra pessoa.\n'
                                'Você deve me fornecer um valor para pesquisa.')
        else:
            await message.answer("Olá, eu sou o Bot IBGE, criado para encontrar as informações do seu nome ou de outra pessoa.\n"
                                 "No momento você não possui permissão para acessar as informações internas.\n"
                                 "Entre em contato com os desenvolvedores.\n"
                                 "Para mais informações do meu criador digite '/info'")
    else:
        await message.answer('Olá ' + message['chat'][
            'first_name'] + ', no momento não encontrei seu username. Você deve verifica-lo nas configurações do Telegram.')


@dp.message_handler()
async def echo(message: types.Message):

    segundos = message['date']
    with open('logs.log', 'a') as arquivo:
        arquivo.write(segundos.__str__())

    with open('user.txt') as file:
        userList = file.read()
    #print(userList)

    user = userList.split('\n')
    #print(user)
    textomsg = ''
    if message["chat"]["username"]:
        textomsg += message["chat"]["username"]
        with open('logs.log', 'a') as arquivo:
            arquivo.write('\n'+message["chat"]["username"]+'\n\n')
    else:
        await message.answer("Você não possui um Username. Logo, deverá ir em suas configurações e nomea-lo.")

    if textomsg in user:
        entradas = ['oi', 'olá', 'ola', 'oie', 'roi', 'hey', 'eai', 'eae', 'salve', 'hello', 'ei', 'hi', 'oii', 'oiee']
        txt = ''
        full
        for teste in full:
            if message.text.upper() in teste['nome']:
                if teste['genero']:
                    txt += f'Gênero: {teste["genero"]}\n'
                if teste['frequnciaF']:
                    txt += f'\nFrequência Feminina:\n{teste["frequnciaF"]}\n'
                if teste['frequnciaM']:
                    txt += f'\nFrequência Masculina:\n{teste["frequnciaM"]}\n'
                if teste['frequnciaT']:
                    txt += f'\nFrequência Total:\n{teste["frequnciaT"]}\n'
        if txt != '':
            await message.answer(txt)
        elif message.text.lower() in (entradas):
            await message.answer('Olá ' + message['chat']['first_name'] + ', eu sou o Bot para o alarme 828D, criado para encontrar as informações do seu erro.\n'
                                 'Você deve me fornecer um valor para pesquisa.')
        else:
            erro = "Você deve fornecer um valor válido."
            await message.answer(erro)
    else:
        await message.answer("Olá, eu sou o Bot para o alarme 828D, criado para encontrar as informações do seu erro.\n"
                             "No momento você não possui permissão para acessar as informações internas.\n"
                             "Entre em contato com os desenvolvedores.\n"
                             "Para mais informações dos meu criadores digite '/info'")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)