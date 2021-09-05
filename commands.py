import os
try:
    import datetime, pytz, requests, json, random
except:
    os.system('pip install random')
    os.system('pip install datetime')
    os.system('pip install pytz')
    os.system('pip install json')
    os.system('pip install requests')
class bot_commands:
    def get_athkar(self, file):
        count = 0
        lis = [""]
        json_file = open(file, "r")
        data = json.load(json_file)
        vaild = False
        while vaild == False:
            for datta in data:
                count += 1
                lis.append(datta)
            if count == 0:
                return "out of range count is 0"
            random_data = random.randint(1, count)
            athkar = lis[random_data]
            day = bot_commands.get_day(self)
            if bot_commands.get_day(self) == athkar["data"]["day_time"]:break
            elif athkar["data"]["day_time"] == "null":break
        return athkar['data']['athkar']
    def save_message_id(self, file_name, message_id):
        try:
            file = open(file_name, "a")
            file.write(f"{str(message_id)}\n")
            file.flush()
            file.close()
            return f"saved Message Id [{message_id}]"
        except Exception as e:
            return f"Save message id error {e}"
    def get_message_id(self, json_data):
        try:
            idd = json_data["result"]["message_id"]
            return idd
        except Exception as e:
            return f"returning id error {e}"
    def get_idd(self, file_name):
        count = 0
        idd_list = []
        file = open(file_name, "r")
        for idd in file.read().splitlines():
            count += 1
            idd_list.append(idd)
        if count > 4:
            o = count - 5
            return idd_list[o]
        else:
            return None
    def delete_message(self, file_name, token, chat_id):
        idd = bot_commands.get_idd(self, file_name)
        if idd != None:
            url = f'https://api.telegram.org/bot{token}/deleteMessage?chat_id=@{chat_id}&message_id={idd}'
            try:
                r = requests.get(url)
                return r.json()
            except Exception as e:
                return f"delete message ERROR {e}"
    def get_day(self):
            tz = pytz.timezone('Asia/Dubai')
            date = datetime.datetime.now(tz)
            return date.strftime('%p')
    def share_text(self, token, chat_id, text):
        try:
            url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id=@{chat_id}&text={text}'
            request = requests.get(url)

            return request.json()
        except Exception as e:
            return f"SHARE TEXT ERROR \n ERROR: {e}"
