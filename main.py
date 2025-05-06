import random
class Surviver:
     def __init__ (self, name, age, health, mental_health):
        self.name = name
        self.age = age
        self.health = health
        self.mental_health = mental_health
mainSurvival = Surviver("Masha", 17, 1000)
print(mainSurvival.name)


def mysteryBox(Surviver):
    vastus = input("Te leidsite kasti, Kas teha seda lahti?")
    if vastus == "jah":
        Surviver.health -= 200
        print("kastis oli suur ämblik, -200hp.  teie tervis - ", Surviver.health)
    else:
        print("midagi ei toimunud, aga kastis oli ämblik")

def VoorasPerson(Surviver):
    vastus = input("Võõras mees koputab teie uksele, kas peaksite selle avama?")
    if vastus == "jah":
        Surviver.health += 200
        print("mees oli lahke ja andis sulle süüa.  teie terbvis -", Surviver.health)
    else: 
        print("mees kõndis mööda, tundub, et tahtis sulle midagi süüa anda")
def BreakWindow(Surviver):
    print("keegi üritab teie akent lõhkuda")
    vastus = input("1 - karjuge ja proovige inimest hirmutada \n 2 - joosta tänavale ja ajada inimene minema 1\n 3 - -proovida rääkida \n")
    if vastus == "1":
        print("mees ehmus kisa peale ja jooksis minema")
    elif vastus == "2":
        Surviver.health -= 400
        print("mees peksis sind - 400hp", "\n sinu tervis - Surviver.health")    
    else:
        print("mees ei rääkinud sinuga ja lõhkus edukalt su akna")

def kohtumineElusüüdiga(Surviver):
    print("Sa kohtasid teist ellujäänut, kes näeb välja väsinud ja kartlik.")
    vastus = input("1 - Mine tema juurde ja räägi temaga. \n2 - Mine mööda, mitte kontakti otsimata. \n3 - Proovi teda aidata.")
    if vastus == "1":
        print("Sa rääkisid temaga ja ta pakkus vahetada toitu turvalise koha kohta.")
        Surviver.health += 30
        Surviver.mental_health += 15 
        print("Teie suhted paranesid. Ta aitas sind.")
    elif vastus == "2":
        print("Sa läksid mööda, teda vältides. Võib-olla oli see turvalisem.")
        Surviver.mental_health -= 10  
        print("Sa tunned end üksildasena, kuid oled turvaline.")
    elif vastus == "3":
        print("Sa pakkusid abi, kuid ta kartis ja ründas sind.")
        Surviver.health -= 150
        Surviver.mental_health -= 30  
        print("Kahjuks ei ole kõik ellujääjad valmis koostööd tegema. Sa kannatasid.")

def imelikTaim(Surviver):
    print("Sa märkad kummalist taime. See näeb välja nagu ravimtaim, kuid pole kindel.")
    vastus = input("1 - Korja taim ja proovi seda kasutada. \n2 - Jäta taim rahule. \n3 - Uuri taime lähemalt.")
    if vastus == "1":
        print("Taim osutus mürgiseks! Sinu tervis on halvenenud.")
        Surviver.health -= 200
        Surviver.mental_health -= 40  
        print("Sa kaotad tervist ja tunned meeleheidet ebaõnnestumise tõttu.")
    elif vastus == "2":
        print("Sa otsustasid taime mitte riskida ja läksid mööda.")
        Surviver.mental_health += 10 
        print("Sa jätkad teed ilma kaotusteta.")
    elif vastus == "3":
        print("Sa otsustasid taime uurida ja avastasid, et see on ravitsev.")
        Surviver.health += 100
        Surviver.mental_health += 20 
        print("Sa kasutasid taime ja tundsid paranemist.")

def event(survivor):
    events = [mysteryBox, VoorasPerson, BreakWindow, kohtumineElusüüdiga, imelikTaim]
    random_event = random.choice(events)
    random_event(survivor)

event(mainSurvival)