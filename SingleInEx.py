#CODE IMPLEMENTING SIMPLE INHERITANCE AND MULTI INHERITANCE

class Alarm:
    def Alarm_on(self):
        print("Someone is at the Gate")
    def Alarm_off(self):
        print("Gate remains Closed")

class Gate():
    def open(self):
        print("Open the Gate ")
    def close(self):
        print("close the Gate")

class Camera(Gate):
    def view(self):
        print("See who is at the Gate")

class Who_is_it(Alarm,Camera):
    def Know(self):
        print("Is it Someone I know")

#DEFINING AN OBJECT AND INSTANCE
Home= Who_is_it()
Home.Alarm_on()
Home.Alarm_off()
Home.open()
Home.close()
Home.view()
Home.Know()