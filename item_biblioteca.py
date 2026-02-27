class ItemBiblioteca:
    def __init__(self, codigo, titulo, ano):
        self.set_codigo(codigo)
        self.set_titulo(titulo)
        self.set_ano(ano)
        self.__disponivel = True

    def get_codigo(self):
        return self.__codigo

    def get_titulo(self):
        return self.__titulo

    def get_ano(self):
        return self.__ano

    def get_disponivel(self):
        return self.__disponivel



    def set_codigo(self, codigo):
        if codigo:
            self.__codigo = codigo
        else:
            raise ValueError("Código inválido.")

    def set_titulo(self, titulo):
        if titulo.strip() != "":
            self.__titulo = titulo
        else:
            raise ValueError("Título não pode ser vazio.")
        
    def set_ano(self, ano):
        if ano > 0:
            self.__ano = ano
        else:
            raise ValueError("Ano deve ser maior que zero.")
        

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            print(f"Item '{self.__titulo}' emprestado com sucesso!")
        else:
            print(f"Item '{self.__titulo}' já está emprestado.")

    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
            print(f"Item '{self.__titulo}' devolvido com sucesso!")
        else:
            print(f"Item '{self.__titulo}' já está disponível.")

    def exibir_detalhes(self):
        print(f"Código: {self.__codigo} | Título: {self.__titulo} | Ano: {self.__ano}")