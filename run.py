import manage
class main_runner:
    def __init__(self):
        self.mange_class = manage.managent()
    def main_run(self):
        print(open("help.txt").read())
        input("\npress enter to continue: ")
        self.mange_class.runner()
if __name__ == "__main__":
    o = main_runner()
    o.main_run()