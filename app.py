from flask import Flask, request
from wa_automate import WAProtocol, WAConnection
from wa_automate.whatsapp import WhatsApp

app = Flask(__name__)
wa = WhatsApp()

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    message = data['message']
    if ".gn" in message.lower():
        wa.send_message(data['chat_id'], "good night")
    return '', 200

if __name__ == '__main__':
    wa.connect()
    wa.wait_for_login()
    app.run()
  
