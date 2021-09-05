import os
try:
    import json
except:
    os.system('pip install json')
class main_admin:
    def __init__(self):
        self.file = "data.json"
    def append_athkar(self, day, text):
        json_file = open(self.file, "r")
        data = json.load(json_file)
        new_data = {"data":{"day_time": str(day), "athkar": text}}
        data.append(new_data)
        json_file.close()
        file = open(self.file, "w")
        json.dump(data, file, indent=4)
        file.close()
        print("added")
    def main(self):
        while True:
            print("[1]Add athkar")
            mood = int(input("Mood: "))
            if int(mood) == 1:
                day = input("PM/AM/null: ")
                athkar = input("athkar: ")
                main_admin.append_athkar(self, day, athkar)
if __name__ == "__main__":
    o = main_admin()
    o.main()