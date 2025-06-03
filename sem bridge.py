class SamsungTV:
    def ligar(self):
        print("Samsung TV ligada.")

    def desligar(self):
        print("Samsung TV desligada.")

    def trocar_canal(self, canal):
        print(f"Samsung TV trocando para o canal {canal}.")


class LGTV:
    def ligar(self):
        print("LG TV ligada.")

    def desligar(self):
        print("LG TV desligada.")

    def trocar_canal(self, canal):
        print(f"LG TV trocando para o canal {canal}.")


class SonyTV:
    def ligar(self):
        print("Sony TV ligada.")

    def desligar(self):
        print("Sony TV desligada.")

    def trocar_canal(self, canal):
        print(f"Sony TV trocando para o canal {canal}.")


class PhilipsTV:
    def ligar(self):
        print("Philips TV ligada.")

    def desligar(self):
        print("Philips TV desligada.")

    def trocar_canal(self, canal):
        print(f"Philips TV trocando para o canal {canal}.")


class PanasonicTV:
    def ligar(self):
        print("Panasonic TV ligada.")

    def desligar(self):
        print("Panasonic TV desligada.")

    def trocar_canal(self, canal):
        print(f"Panasonic TV trocando para o canal {canal}.")


class ControleSamsung:
    def __init__(self):
        self.tv = SamsungTV()

    def ligar(self):
        self.tv.ligar()

    def desligar(self):
        self.tv.desligar()

    def trocar_canal(self, canal):
        self.tv.trocar_canal(canal)


class ControleLG:
    def __init__(self):
        self.tv = LGTV()

    def ligar(self):
        self.tv.ligar()

    def desligar(self):
        self.tv.desligar()

    def trocar_canal(self, canal):
        self.tv.trocar_canal(canal)


class ControleSony:
    def __init__(self):
        self.tv = SonyTV()

    def ligar(self):
        self.tv.ligar()

    def desligar(self):
        self.tv.desligar()

    def trocar_canal(self, canal):
        self.tv.trocar_canal(canal)


class ControlePhilips:
    def __init__(self):
        self.tv = PhilipsTV()

    def ligar(self):
        self.tv.ligar()

    def desligar(self):
        self.tv.desligar()

    def trocar_canal(self, canal):
        self.tv.trocar_canal(canal)


class ControlePanasonic:
    def __init__(self):
        self.tv = PanasonicTV()

    def ligar(self):
        self.tv.ligar()

    def desligar(self):
        self.tv.desligar()

    def trocar_canal(self, canal):
        self.tv.trocar_canal(canal)


print("=== Controle Samsung ===")
controle_samsung = ControleSamsung()
controle_samsung.ligar()
controle_samsung.trocar_canal(10)
controle_samsung.desligar()

print("\n=== Controle LG ===")
controle_lg = ControleLG()
controle_lg.ligar()
controle_lg.trocar_canal(20)
controle_lg.desligar()

print("\n=== Controle Sony ===")
controle_sony = ControleSony()
controle_sony.ligar()
controle_sony.trocar_canal(7)
controle_sony.desligar()

print("\n=== Controle Philips ===")
controle_philips = ControlePhilips()
controle_philips.ligar()
controle_philips.trocar_canal(15)
controle_philips.desligar()

print("\n=== Controle Panasonic ===")
controle_panasonic = ControlePanasonic()
controle_panasonic.ligar()
controle_panasonic.trocar_canal(5)
controle_panasonic.desligar()
