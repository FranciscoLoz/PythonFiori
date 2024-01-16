#Declaramos el constructor y los atributos
class persona:
    def __init__(self, dni:str, name:str, gender:str, age:int):
        self._dni = dni
        self._name = name
        self._gender = gender
        self._age = age

#Getters y setters (GRACIAS FIORI, ESTO ERA SUPER NECESARIO)
        
    #GetterSetter de DNI
    def get_dni(self):
        return self._dni
    
    def set_dni(self, dni):
        self._dni=dni
    
    #GetterSetter del nombre
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name=name

    #GetterSetter del apellido
    def get_gender(self):
        return self._gender
    
    def set_gender(self, gender):
        self._gender=gender
    
    #GetterSetter de la edad
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        self._age=age