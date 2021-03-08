

class car:
    def car_name(self):
        print("Car nme:",cn)

class model(car):
    def car_model(self):
        print("car model:",cm)
obj=model()
cn=input("erter car nme")
cm=input("erter car model")
obj.car_name()
obj.car_model()
