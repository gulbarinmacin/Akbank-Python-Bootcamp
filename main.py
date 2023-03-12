import csv
from datetime import datetime

class Pizza:
    def __init__(self):
        self.description = "Pizza"
        self.cost = 0.0
        
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost
    
class KlasikPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Klasik Pizza"
        self.cost = 120.0
        
    def get_cost(self):
        return self.cost
        
class MargaritaPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margarita Pizza"
        self.cost = 90.0
        
    def get_cost(self):
        return self.cost
    
class TurkPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Turk Pizza"
        self.cost = 150.0
        
    def get_cost(self):
        return self.cost
    
class SadePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Sade Pizza"
        self.cost = 100.0
        
    def get_cost(self):
        return self.cost
    

class Decorator(Pizza):
    def __init__(self, component):
        super().__init__()
        self.component = component
        
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)
    

class Zeytin(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Zeytin"
        self.cost = 5
        
    def get_cost(self):
        return self.component.get_cost() + self.cost
    
class Mantar(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Mantar"
        self.cost = 7
        
    def get_cost(self):
        return self.component.get_cost() + self.cost
    
class KeciPeyniri(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Keçi Peyniri"
        self.cost = 10
        
    def get_cost(self):
        return self.component.get_cost() + self.cost
    
class Et(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Et"
        self.cost = 15
        
    def get_cost(self):
        return self.component.get_cost() + self.cost
    
class Sogan(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Sogan"
        self.cost = 5
        
    def get_cost(self):
        return self.component.get_cost() + self.cost
    
class Mısır(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Mısır"
        self.cost = 8
        
    def get_cost(self):
        return self.component.get_cost() + self.cost

def main():
    # Menüyü dosyadan oku ve ekrana yazdır
    with open("Menu.txt", "r") as f:
        menu = f.read()
    print(menu)

    # Pizza ve sos seçimlerini al
    pizza_secim = int(input("Lütfen bir pizza seçin (1-4): "))
    while (pizza_secim  < 1  or pizza_secim  > 4 ):
      print("Lütfen 1-4 arası bir sayı seçiniz!")
      pizza_secim = int(input("Lütfen bir pizza seçin (1-4): "))
 
    
    sos_secim = int(input("Lütfen bir sos seçin (11-16): "))
    while (sos_secim  < 11 or pizza_secim  > 16 ):
      print("Lütfen 11-16 arası bir sayı seçiniz!")
      sos_secim = int(input("Lütfen bir sos seçin (11-16): "))

    # Pizza ve sos nesnelerini oluştur
    pizza = None
    sos = None
    if pizza_secim == 1:
        pizza = KlasikPizza()
    elif pizza_secim == 2:
        pizza = MargaritaPizza()
    elif pizza_secim == 3:
        pizza = TurkPizza()
    elif pizza_secim == 4:
        pizza = SadePizza()

    if sos_secim == 11:
        sos = Zeytin(pizza)
    elif sos_secim == 12:
        sos = Mantar(pizza)
    elif sos_secim == 13:
        sos = KeciPeyniri(pizza)
    elif sos_secim == 14:
        sos = Et(pizza)
    elif sos_secim == 15:
        sos = Sogan(pizza)
    elif sos_secim == 16:
        sos = Mısır(pizza)

    # Toplam fiyatı hesapla
    total_cost = sos.get_cost()

    # Kullanıcı bilgilerini al
    isim = input("Adınız Soyadınız: ")
    tc = int(input("TC Kimlik Numaranız: "))
    kredi_kart_no = int(input("Kredi Kartı Numaranız: "))
    kredi_kart_sifre = int(input("Kredi Kartı Sifreniz: "))

    # Veritabanına sipariş bilgilerini yaz
    with open("Orders_Database.csv", "a") as f:
        f.write(f"{isim}, {tc}, {kredi_kart_no}, {sos.get_description()}, {datetime.now(),}, {kredi_kart_sifre}\n")

    # Sipariş onayı
    print(f"\nSiparişiniz alınmıştır.\n\n{total_cost} TL ödeme yapılacaktır.\n\nTeşekkürler!")

main()