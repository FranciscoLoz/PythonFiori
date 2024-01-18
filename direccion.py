#Declaramos el constructor y los atributos
class direccion:
    def __init__(self, street:str, number:int, pcode:int, country:str, city:str):
        self._street= street
        self._number= number
        self._pcode= pcode
        self._country= country
        self._city= city

#Getters y setters
    
    #GetterSetter de la calle
    def get_street(self):
        return self._street
        
    def set_street(self, street):
        self._street=street
    
    #GetterSetter del numero
    def get_number(self):
        return self._number
    
    def set_number(self, number):
        self._number=number

    #GetterSetter del codigo postal
    def get_pcode(self):
        return self._pcode
    
    def set_pcode(self, pcode):
        self._pcode=pcode

    #GetterSetter del poblado
    def get_country(self):
        return self._country
    
    def set_country(self, country):
        self._country=country

    #GetterSetter de la ciudad
    def get_city(self):
        return self._city
    
    def set_city(self, city):
        self._city=city