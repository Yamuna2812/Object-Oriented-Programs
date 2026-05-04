class classes:
    def __init__(self,room):
        self.room=room
    def permission(self):
        print(f"can i enter into {self.room}")    



rooms=classes("classroom")
rooms.permission()        