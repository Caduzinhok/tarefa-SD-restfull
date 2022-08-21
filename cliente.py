from flask import Flask
from flask import jsonify
from flask import request
import sys
import const 
import requests
import threading
# Handle interactive loop

app = Flask(__name__)

@app.route('/chat',methods=['POST'])
def createEmp():

    dados = {
    'dest':request.json['dest'],
    'name':request.json['name'],
    'msg':request.json['msg'],
    'id':request.json['id'],
    }
    
    if(request.json['id'] == ''):
        print(str(request.json['count']) + " - Mensagem: " + request.json['msg'] + " - De: " +  request.json['name']) 
    else:
        print("Respondendo para: " + request.json['id'] +" - Mensagem: " + request.json['msg'] + " - De: " +  request.json['name']) 
    return "ACK"

me = str(sys.argv[1]) 

def sending():
    while True:
        dest = ''
        idmsg = ''
        reply = input("Responder? (s or n): \n")

        if (str(reply).lower == 's'):
            idmsg = input("Digite o ID da mensagem: \n")
        dest = input("Para quem deseja enviar a mensagem: \n")
        msg = input("Digite a mensagem: \n")

        data = {
            'dest':dest,
            'name':me,
            'msg':msg,
            'ip':const.registry[me][0],
            'id':idmsg,
        }

        resposta = requests.post(const.CHAT_SERVER_HOST+":"+str(const.CHAT_SERVER_PORT)+'/chat', json = data) #2
        if resposta.text != "ACK":
            print("Error: O servidor não aceitou a mensagem (o destino não existe?)")
        else:
            pass

def receiving():
    app.run(host="0.0.0.0",port=const.registry[me][1])

if __name__ == '__main__':
    
    send = threading.Thread(target=sending)
    send.start()
    
    receive = threading.Thread(target=receiving)
    receive.start()