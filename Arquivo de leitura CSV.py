import json

nomes = ''
with open('grupos.csv', 'rb') as m:
    nomes = m.read().decode()



full = []
txt = ''
nomesList = nomes.split('\n')
for linha in nomesList:
    if linha not in ['name,classification,frequency_female,frequency_male,frequency_total,ratio,names\r']:
        if len(linha) > 0:
            ll = linha.split(',')
            if ll[1] != 'F':
                if ll[6].split('|') != '':
                    dicionario = dict(
                        nome=(ll[0]) and ll[6].split('|')[1:-1],
                        genero=ll[1],
                        frequnciaF=ll[2],
                        frequnciaM=ll[3],
                        frequnciaT=ll[4],
                        )
                    full.append(dicionario)


'''for teste in dicionario:
    if teste['nome'] == 'RENAN':
        print(dicionario)
'''
'''
txt = ''
full
compara = 'RENAN'
for teste in full:
    if compara in teste['nome']:
        if teste['genero']:
            txt += f'genero: {teste["genero"]}\n'
        if teste['frequnciaF']:
            txt += f'\nfrequnciaF:\n{teste["frequnciaF"]}\n'
        if teste['frequnciaM']:
            txt += f'\nfrequnciaM:\n{teste["frequnciaM"]}\n'
        if teste['frequnciaT']:
            txt += f'\nfrequnciaT:\n{teste["frequnciaT"]}\n'

print(txt)

'''




#print([x for x in alarmes if x['numero'] == '2001'][0]['titulo'])


#print([linha for linha in dicionario if linha['nome'])










'''
full = json.dumps(full, sort_keys=True, indent=4, ensure_ascii=True)
with open('leitura.json', 'w') as file:
    file.write(full)
'''

'''
full = json.dumps(full, sort_keys=True, indent=4, ensure_ascii=True)
with open('leitura.json', 'w') as file:
    file.write(full)
    '''

testejson = json.dumps(full, sort_keys=True, indent=4, ensure_ascii=True)
with open('full.json', 'w+') as file:
    file.write(testejson)