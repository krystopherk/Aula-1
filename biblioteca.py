# 1. Uma biblioteca tem diversos livros que podem ser emprestados para leitores. 
# Cada livro tem um título, um autor e um número de páginas. 
# Alguns livros estão emprestados e outros disponíveis. 
# Para realizar um empréstimo, um leitor precisa fornecer seu nome e 
# devolver o livro em até 15 dias. Caso o livro seja devolvido atrasado, há uma multa.

class Leitor:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

    def realizar_emprestimo(self, livro):
        if not livro.emprestado:
            self.livros_emprestados.append(livro)
            return livro.emprestar()

        return f"O livro {livro.titulo} não está disponível"
    
    def devolver_livro(self, livro, dias_atrasado):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            multa = max(0, (dias_atrasado - 15) * 2)
            
            return livro.devolver() + f"Multa: R${multa}"

        return f"O leitor {self.nome} não possui o livro {livro.titulo}"

class Livro:
    def __init__(self, titulo, autor, numero_pagina):
        self.titulo = titulo
        self.autor = autor
        self.paginas = numero_pagina
        self.emprestado = False

    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True
            return f"O livro {self.titulo} foi emprestado com sucesso"
        
        return f"O livro {self.titulo} já está emprestado"

    def devolver(self):
        if self.emprestado:
            self.emprestado = False
            return f"O livro {self.titulo} foi devolvido"
        
        return f"O livro {self.titulo} não está emprestado"

class Biblioteca:

    def __init__(self):
        self.livro = []
        self.leitor = []

    def adicionar_livro(self, livro):
        self.livro.append(livro)
        return f"O livro {livro.titulo} foi adicionado a biblioteca"
    
    def adicionar_leitor(self, leitor):
        self.leitor.append(leitor)
        return f"O leitor {leitor.nome} foi adicionado com sucesso"
    
    def remover_livro(self, livro):
        if livro in self.livro:
            self.livro.remove(livro)
            return f"O livro {livro.titulo} foi removido da biblioteca"
        
        return f"O livro {livro.titulo} não está cadastrado"
    
    def emprestar_livro(self, leitor, livro):
        if livro in self.livro and not livro.emprestado:
            return leitor.realizar_emprestimo(livro)
        
        return f"O {livro.titulo} não está disponível para empréstimo"
    
livro1 = Livro("Fundamentos de POO", "Larissa", 500)
livro2 = Livro("Academia em junho amem", "Krystopher", 122)
livro3 = Livro("Eu irritando um psicopata", "Kamilly", 1000)

larissa = Leitor("Larissa")
andre = Leitor("André")
nicolas = Leitor("Nicolas")

bib = Biblioteca()
print(bib.adicionar_livro(livro1))
print(bib.adicionar_livro(livro2))
print(bib.adicionar_livro(livro3))

print(bib.adicionar_leitor(larissa))
print(bib.adicionar_leitor(andre))
print(bib.adicionar_leitor(nicolas))

print(bib.emprestar_livro(nicolas, livro2))
print(nicolas.devolver_livro(livro2, 20))