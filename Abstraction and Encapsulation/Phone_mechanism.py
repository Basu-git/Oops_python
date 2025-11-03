#2. **Abstraction**:
# Design a `Phone` class with methods to `call_contact` and `take_picture`. Abstract away any internal processing details and focus on creating a user-friendly interface.
class phone:
    def __init__(self):
        pass
    def call_contact(self,name):
        print(f"Calling to {name}")
    def click_picture(self):
        print("SHutter Sound!!!!!! Clicked Successfully")

user=phone()
user.call_contact("You")
user.click_picture()