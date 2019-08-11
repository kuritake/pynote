class human:
     
    def __init__(self, name,):
    # With one underbar(_),this val is considered private.
    # There is no binding effect if they use "instanceName_val".
        self.name = name
        self.age = None
        
    #Setter and getter are hardly used in python coding.
    #Cause python can't keep members secret own private variables.
    #First of all,you easily get/set them useing "." (ex:instanceName.age = 19)
    
    def get_name(self):
        return self.name
        
    def set_name(self, name):
        self.name = name
 
    def get_age(self):
        return self.age
 
    def set_age(self, age):
        self.age = age 
        
        
    #These methods are more popular you use decorator.
    #You can restrict access and check parameter.
    #@property and gettermetohd have almost same function.  
    
    @property
    def age(self):
        return self.age
 
    @age.setter
    def age(self, age):
        if type(age) == int:
            if age > 0:
                self.age = age
                return
        raise ValuError('年齢は0以上の整数を指定してください')
