from item_biblioteca import ItemBiblioteca

class Livro(ItemBiblioteca):
    def __init__(self, codigo, titulo, ano, autor, num_paginas):
        super().__init__(codigo, titulo, ano)
        self.set_autor(autor)
        self.set_num_paginas(num_paginas)

    def get_autor(self):
        return self.__autor

    def get_num_paginas(self):
        return self.__num_paginas

    def set_autor(self, autor):
        if autor.strip() != "":
            self.__autor = autor
        else:
            raise ValueError("Autor inválido.")

    def set_num_paginas(self, num_paginas):
        if num_paginas > 0:
            self.__num_paginas = num_paginas
        else:
            raise ValueError("Número de páginas inválido.")

    def exibir_detalhes(self):
        status = "Disponível" if self.get_disponivel() else "Emprestado"
        print(f"[LIVRO] Código: {self.get_codigo()} | "
              f"Título: {self.get_titulo()} | "
              f"Autor: {self.__autor} | "
              f"Páginas: {self.__num_paginas} | "
              f"Ano: {self.get_ano()} | "
              f"Status: {status}")