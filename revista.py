from item_biblioteca import ItemBiblioteca


class Revista(ItemBiblioteca):
    def __init__(self, codigo, titulo, ano, edicao, mes):
        super().__init__(codigo, titulo, ano)
        self.set_edicao(edicao)
        self.set_mes(mes)

    def get_edicao(self):
        return self.__edicao

    def get_mes(self):
        return self.__mes

    def set_edicao(self, edicao):
        if edicao > 0:
            self.__edicao = edicao
        else:
            raise ValueError("Edição inválida.")

    def set_mes(self, mes):
        if mes.strip() != "":
            self.__mes = mes
        else:
            raise ValueError("Mês inválido.")

    def exibir_detalhes(self):
        status = "Disponível" if self.get_disponivel() else "Emprestado"
        print(f"[REVISTA] Código: {self.get_codigo()} | "
              f"Título: {self.get_titulo()} | "
              f"Edição: {self.__edicao} | "
              f"Mês: {self.__mes} | "
              f"Ano: {self.get_ano()} | "
              f"Status: {status}")