import os
try:
    import commands, time, threading
except:
    os.system('pip install threading')
    os.system('pip install time')

class managent:
    def __init__(self):
        self.main_token = open("token.txt").read() # telegram bot token
        self.file = "data.json" # json data file
        self.clients = "clients.txt" # channels ids.
        self.commands = commands.bot_commands()
    def runner(self):
        while True:
            athkar = self.commands.get_athkar(self.file) #generate athkar from the json file
            file = open(self.clients, "r") # getting channels ids
            clients = file.read().splitlines()
            for channel_id in clients: # handel channels.
                if os.path.isfile(f"{channel_id}.txt") == False:
                    file = open(f"{channel_id}.txt", "w+") #create a text file for the channel.
                    file.close()
                threading.Thread(target=managent.handle, args=[self, f"{channel_id}.txt", channel_id, athkar]).start()
            time.sleep(60)
    def handle(self, messages_id_file, channel_id, athkar):
                res = self.commands.share_text(self.main_token, channel_id, str(athkar)) # send's athkar to channels.
                if res['ok'] == True: print(f"athkar sent to {channel_id}") # if athkar status is ok it'll print.
                else:print(res) # if there was an error in the status it'll print.
                message_id = self.commands.get_message_id(res) #getting extracting the message id from the res.
                save = self.commands.save_message_id(messages_id_file, message_id) # saves the message id.
                print(save)
                message_state = self.commands.delete_message(messages_id_file, self.main_token, channel_id) # delete old message
                print(f"delete message state: {message_state}")


if __name__ == "__main__":
    o = managent()
    o.runner()