from profesor import profesor

class asignatura:
    def __init__(self, assignature_id: int, desc: str, credit: int, assigned_prof=None):
        self._assignature_id = assignature_id
        self._desc = desc
        self._credit = credit
        self._assigned_prof = assigned_prof

#Getters y setters
        
    #GetterSetters de los IDs
    def get_assignature_id(self):
        return self._assignature_id
    
    def set_id(self, assignature_id):
        self._assignature_id=assignature_id

    #GetterSetter de las descripciones
    def get_desc(self):
        return self._desc
    
    def set_desc(self, desc):
        self._desc=desc
    
    #GetterSetter de los créditos
    def get_credit(self):
        return self._credit
    
    def set_credit(self, credit):
        self._credit=credit
    
    #GetterSetter de los profesores asignados
    def get_assigned_prof(self):
        return self._assigned_prof
    
    def set_assigned_prof(self, assigned_prof):
        self._assigned_prof=assigned_prof