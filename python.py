
class Publicacao:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def exibir_info(self):
        return f"{self.titulo} — {self.autor} ({self.ano_publicacao})"


class Livro(Publicacao):
    def __init__(self, titulo, autor, ano_publicacao, isbn):
        super().__init__(titulo, autor, ano_publicacao)
        self.isbn = isbn

    def exibir_info(self):
        return f"[LIVRO] {super().exibir_info()} | ISBN: {self.isbn}"


class Revista(Publicacao):
    def __init__(self, titulo, autor, ano_publicacao, edicao):
        super().__init__(titulo, autor, ano_publicacao)
        self.edicao = edicao

    def exibir_info(self):
        return f"[REVISTA] {super().exibir_info()} | Edição: {self.edicao}"

class Quadrinho(Publicacao):
    def __init__(self, titulo, autor, ano_publicacao, ilustrador):
        super().__init__(titulo, autor, ano_publicacao)
        self.ilustrador = ilustrador

    def exibir_info(self):
        return f"[QUADRINHO] {super().exibir_info()} | Ilustrador: {self.ilustrador}"

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.publicacoes = []

    def adicionar_publicacao(self, pub):
        self.publicacoes.append(pub)

    def remover_publicacao_por_titulo(self, titulo):
        for pub in self.publicacoes:
            if pub.titulo == titulo:
                self.publicacoes.remove(pub)
                print(f"\n✔ Publicação removida: {titulo}")
                return
        print("\n⚠ Nenhuma publicação encontrada com esse título!")

    def listar_publicacoes(self):
        print(f"\n📚 Publicações na biblioteca '{self.nome}':")
        for pub in self.publicacoes:
            print(" -", pub.exibir_info())

    def buscar_por_autor(self, autor):
        print(f"\n🔎 Buscando publicações do autor '{autor}':")
        resultados = [pub for pub in self.publicacoes if pub.autor == autor]
        for r in resultados:
            print(" -", r.exibir_info())
        if not resultados:
            print("Nenhuma publicação encontrada.")


if __name__ == "__main__":
    p1 = Livro("Python Básico", "Fausto Silva", 2020, "123-ABC")
    p2 = Livro("Estruturas de Dados", "Maria Laura", 2018, "456-DEF")
    p3 = Livro("Machine Learning", "Ana Torres", 2022, "789-GHI")
    p4 = Revista("Tech News", "Ricardo Martins", 2023, 15)
    p5 = Revista("Ciência Hoje", "Carlos Lima", 2019, 42)
    p6 = Quadrinho("Homem-Aranha", "Stan Lee", 1963, "Steve Ditko")
    p7 = Quadrinho("Batman", "Bob Kane", 1940, "Bill Finger")
    p8 = Livro("Banco de Dados", "Paulo César", 2017, "321-CBA")
    p9 = Revista("National Geo", "Lara Nunes", 2021, 120)
    p10 = Quadrinho("X-Men", "Stan Lee", 1963, "Jack Kirby")

    biblioteca = Biblioteca("Biblioteca Central")

    todas = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
    for pub in todas:
        biblioteca.adicionar_publicacao(pub)
    biblioteca.listar_publicacoes()
    biblioteca.remover_publicacao_por_titulo("Batman")
    biblioteca.listar_publicacoes()
    biblioteca.buscar_por_autor("Fausto Silva")
