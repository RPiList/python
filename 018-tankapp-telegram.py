Chat_ID finden:

https://api.telegram.org/bot{API-KEY}/getUpdates

In Datei .env:
teletoken={API-TOKEN-Eintragen}


chat_id = {chat_id_eintragen}
message = sprit_schoen + ': ' + str(sprit_preis).replace('.',',')
TOKEN = os.getenv('teletoken')
telegramurl = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(telegramurl).json())
