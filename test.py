import requests
url = "https://api.telegram.org/bot5164303840:AAFinWpqK_Nk3_6ZJscImsaL31zoCE0dsyo/"


data_tel = {
    'chat_id': 107814146,
    'text': 'Salam khobi?'
}
requests.post(url+'sendMessage', data_tel)
