# Interface do dispositivo
class Dispositivo:
    def ligar(self):
        pass

    def desligar(self):
        pass

    def trocar_canal(self, canal):
        pass

# Implementações concretas (TVs de diferentes marcas)
class SamsungTV(Dispositivo):
    def ligar(self):
        print("Samsung TV ligada.")

    def desligar(self):
        print("Samsung TV desligada.")

    def trocar_canal(self, canal):
        print(f"Samsung TV trocando para o canal {canal}.")


class LGTV(Dispositivo):
    def ligar(self):
        print("LG TV ligada.")

    def desligar(self):
        print("LG TV desligada.")

    def trocar_canal(self, canal):
        print(f"LG TV trocando para o canal {canal}.")


# Abstração: Controle remoto genérico
class ControleRemoto:
    def __init__(self, dispositivo: Dispositivo):
        self.dispositivo = dispositivo

    def ligar(self):
        self.dispositivo.ligar()

    def desligar(self):
        self.dispositivo.desligar()

    def trocar_canal(self, canal):
        self.dispositivo.trocar_canal(canal)


# Abstração estendida: Controle com funções extras
class ControleRemotoAvancado(ControleRemoto):
    def abrir_netflix(self):
        print("Abrindo Netflix no dispositivo...")

# Samsung com controle básico
samsung = SamsungTV()
controle_samsung = ControleRemoto(samsung)
controle_samsung.ligar()
controle_samsung.trocar_canal(5)
controle_samsung.desligar()

print("\n---\n")

# LG com controle avançado
lg = LGTV()
controle_lg = ControleRemotoAvancado(lg)
controle_lg.ligar()
controle_lg.trocar_canal(12)
controle_lg.abrir_netflix()
controle_lg.desligar()
