import requests
import json

def cotacao(cot):
    print("############# COTACAO DO DIA!! #############")
    print('DOLAR: ',cot['valores']['USD']['valor'])
    print('EURO: ',cot['valores']['EUR']['valor'])
    print('BITCOIN: ',cot['valores']['BTC']['valor'])

requisicao = requests.get('http://api.promasters.net.br/cotacao/v1/valores')
cot = json.loads(requisicao.text)

cotacao(cot)