from flask import Flask
from flask import jsonify
from flask import request
import const 
import requests

app = Flask(__name__)

print("Servidor do Chat está pronto para uso...")

count = 0

@app.route('/chat',methods=['POST'])
def createEmp():
    global count
    count +=1
    
    dados = {
    'dest':request.json['dest'],
    'name':request.json['name'],
    'msg':request.json['msg'],
    'id':request.json['id'],
    'count':count,
    }
    ip = const.registry[request.json['dest']][0]
    port = const.registry[request.json['dest']][1]

    print(str(count) + " - Respondendo mensagem: " + request.json['msg'] + " - De: " +  request.json['name'] + " - Para: " +  request.json['dest'] + '\n')
    resposta = requests.post(ip+":"+str(port)+'/chat', json = dados) #2
    return "ACK"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)