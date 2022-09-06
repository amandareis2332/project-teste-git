class Pessoa:
    def __init__(self, document, name):
        self.document = document
        self.name = name
    

class PessoaJuridica(Pessoa):
    def __init__(self, document, name, ie):      
      self.ie = ie
      super.__init__(self, document, name)

class PessoaFisica(Pessoa):
    def __init__(self, document, name, sexo, raca):      
      self.sexo = sexo
      self.raca = raca
      super.__init__(self, document, name)


pessoa = PessoaFisica("311131313", "Amanda", "F", "Branca")
pessoa2 = PessoaJuridica("979879878", "Saguam", "12312312")

print(pessoa.name)
