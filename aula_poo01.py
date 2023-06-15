class Pessoa:
    def __init__(self,nome,idade,):
        self.nome=nome
        self.idade=idade
    
        
        
        
    def apresentar(self):
        
        print('ola meu nome é:',self.nome)
        
    def envelhecer(self,anos):
        self.idade += anos
        print('A nova idade é:',self.idade)
            
        
        
   
pessoa1= Pessoa('paula',10)

pessoa1.apresentar()
pessoa1.envelhecer(2)                