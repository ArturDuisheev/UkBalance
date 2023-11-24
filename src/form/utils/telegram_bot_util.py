import requests
from core.env_reader import env

from form.api import serializers as ser


def transformation_data(request):
    drop_down_info_data = request.data['drop_down_info']
    drop_down_info_message = ""

    for item in drop_down_info_data:
        not_required_sum_investments = item.get('not_required_sum_investments', 'N/A')
        not_required_term = item.get('not_required_term', 'N/A')
        drop_down_info_message += f"\n Sum Investments: {not_required_sum_investments},\n Term: {not_required_term}\n"

    return drop_down_info_message


class TelegramBot:
    serializer = ser.FormSerializer

    def telegram_bot_sender(self, request):
        BOT_TOKEN = env('BOT_TOKEN')
        CHAT_ID = env('CHAT_ID')
        drop_down_info_message = transformation_data(request)
        MESSAGE = f"Name: {request.data['name']}, \n" \
                  f"Surname: {request.data['surname']} \n" \
                  f"Email: {request.data['email']},\n" \
                  f"Phone number: {request.data['code_country']}, {request.data['phone_number']}\n" \
                  f"DropDownInfo: {drop_down_info_message}\n " \
                  f"created at: {request.data['created_at']}"
        URL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={MESSAGE}'
        requests.post(URL)
        all_var = BOT_TOKEN, CHAT_ID, MESSAGE, URL
        print(all_var)
        return all_var
