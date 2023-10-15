import random

location = ["start"] #shipwreck, stone_circle, fishing_hut, watch_tower, ware_houses, lighthouse, plane, air_drop, villa_front, generators, obervatory, meeting_point_A, meeting_point_B, meeting_point_C
inventory = [""] #night_vision, fishing_rod, fuse, plane_steering_wheel, plane_wheel, revolver, double_barrel_shotgun, flashlight

night_rng = random.randint(0, 1)
airdrop_rng = 2
ship_rng = random.randint(0, 1)
fishing_rng = random.randint(0, 2)

shipwreck_loot = []
if ship_rng == 1:
    shipwreck_loot.append("flashlight")

guard_loot = ["medkit"]

villa_front_loot = ["torch"]

stone_circle_loot = ["torch"]
stone_circle_secret_loot = ["revolver"]

generator_loot = ["fuse"]
generator_warehouse = []
generator_observatory = []
generators_visit = []

observatory_door = []
observatory_loot = ["night_vision"]

lighthouse_visit = []

airdrop_loot = []
if airdrop_rng == random.randint(0, 2):
    airdrop_loot.append("revolver")

fishing_hut_loot = ["fishing_rod"]
fishing_loot = []
if fishing_rng == 1:
    fishing_loot.append("ammo_crate")


while True:
    if "start" in location:
        print("Probouzíš se na ostrově. Ohlédneš se kolem sebe a vidíš pár mrtvol a za sebou ztrozkotanou loď.")
        print("Po chvíli se ti do hlavy vrací vzpomínky o tom jak si plul po moři, když v tu najednou přišla velká bouře a slyšel si výbuch. Po té už si pamatuješ jen na své probuzení zde na ostrově.")
        print("Po pár minutách co se zpamatuješ ze šoku, si uvědomíš že bude lepší začít něco dělat. Třeba aspoň prozkoumat kde si to vlastně skončil.")
        print("")
        while True:
            okoli = str(input("Chceš prozkoumat své okolí než se vidáš hlouběji do ostrova? [ano, ne]: "))
            if okoli == "ano":
                location.remove("start")
                location.append("shipwreck")
                print("")
                break
            elif okoli == "ne":
                location.remove("start")
                location.append("meeting_point_A")
                print("")
                break
            else:
                print("Zadal si špatnou odpověď. Správné odpovědi jsou [ano, ne].")
                print("")
    
    
    if "shipwreck" in location:
        print("Porozhlédneš se kolem a po větším zkoumání svého okolí vidíš dvě místa kam se můžeš vydat.")
        print("Můžeš se porozhlédnout po vraku lodi na které si připlul nebo jít prohlédnout a prohledat dvě mrtvá těla lidí opodál po tvé pravici, kteří s tebou pravděpodobně byli na lodi.")
        print("")
        while True:
            vrak = int(input("Kam se chceš vydat? [1 - vrak lodi, 2 - těla lidí, 3 - odejít]: "))
            if vrak == 1:
                location.remove("shipwreck")
                location.append("shipwreck_close")
                print("")
                break
            elif vrak == 2:
                location.remove("shipwreck")
                location.append("guard_bodies")
                print("")
                break
            elif vrak == 3:
                location.remove("shipwreck")
                location.append("meeting_point_A")
                print("")
                break
            else:
                print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - vrak lodi, 2 - těla lidí, 3 - odejít].")
                print("")
    if "shipwreck_close" in location:
        print("Po chvíli hledání způsobu jak se dostat na loď, si všimneš části která je víc zabořená do písku.")
        print("Vylezeš tedy na palubu. Vidíš že vnitřek lodi je v plamenech, pravděpodobně kvůli dřívějšímu výbuchu. Rozhodneš se tedy prohledat aspoň palubu.")
        print("Po chvíli hledání si...")
        print("")
        if "flashlight" in shipwreck_loot:
            print("Našel svítilnu. Schováš si ji k sobě pro další využití.")
            shipwreck_loot.remove("flashlight")
            inventory.append("flashlight")
            print("Po-té jsi slezl z paluby a vrátil se zpátky.")
            print("")
            while True:
                pokracovani = input("Stiskni Enter pro pokračování: ")
                if pokracovani.strip() == "":
                    location.remove("shipwreck_close")
                    location.append("shipwreck")
                    print("")
                    break
                if pokracovani.strip() != "":
                    print("Zkus to znovu.")
        elif "flashlight" not in shipwreck_loot:
            print("Bohužel nic nenašel. Slezeš z paluby a vrátíš se zpátky.")
            print("")
            while True:
                pokracovani = input("Stiskni Enter pro pokračování: ")
                if pokracovani.strip() == "":
                    location.remove("shipwreck_close")
                    location.append("shipwreck")
                    print("")
                    break
                if pokracovani.strip() != "":
                    print("Zkus to znovu.")
    if "guard_bodies" in location:
        print("Jakmile dojdeš k tělům, tak zjistíš že tyhle lidi s tebou na lodi nebyli. Vypadají jako nějací strážní.")
        print("Jejich těla mají v okolí torsa obří drápance, jak od nějakého zvířete.")
        print("Znepokojí tě myšlenka že těla vypadají čerstvě. Takže ten kdo je zabil nebo to co je zabilo bude asi ještě někde poblíž na ostrově...")
        print("")
        while True:
            tela = str(input("Chceš těla prohledat? [ano, ne]: "))
            if tela == "ano":
                location.remove("guard_bodies")
                location.append("guard_bodies_inspection")
                print("")
                break
            elif tela == "ne":
                print("")
                print("Vrátíš se zpátky.")
                print("")
                while True:
                    pokracovani = input("Stiskni Enter pro pokračování: ")
                    if pokracovani.strip() == "":
                        location.remove("guard_bodies")
                        location.append("shipwreck")
                        print("")
                        break
                    if pokracovani.strip() != "":
                        print("Zkus to znovu.")
                break
            else:
                print("Zadal si špatnou odpověď. Správné odpovědi jsou [ano, ne].")
                print("")
    if "guard_bodies_inspection" in location:
        print("Po bližším prohledání si...")
        if "medkit" in guard_loot:
            print("Našel MedKit. Schoval sis ho pro budoucí použití.")
            guard_loot.remove("medkit")
            inventory.append("medkit")
            print("Zvedl ses a pokračuješ v prohledávání.")
            print("")
            while True:
                pokracovani = input("Stiskni Enter pro pokračování: ")
                if pokracovani.strip() == "":
                    location.remove("guard_bodies_inspection")
                    location.append("guard_bodies_inspection_final")
                    print("")
                    break
                if pokracovani.strip() != "":
                    print("Zkus to znovu.")
        elif "medkit" not in guard_loot:
            print("Bohužel nic nenašel.")
            print("Zvedl ses a pokračuješ v prohledávání.")
            print("")
            while True:
                pokracovani = input("Stiskni Enter pro pokračování: ")
                if pokracovani.strip() == "":
                    location.remove("guard_bodies_inspection")
                    location.append("guard_bodies_inspection_final")
                    print("")
                    break
                if pokracovani.strip() != "":
                    print("Zkus to znovu.")
    if "guard_bodies_inspection_final" in location:
        print("Pak si našel nějakou nahrávku. S největší pravděpodobností patřila tomu strážnému.")
        print("Ještě byla od krve jak jí pevně držel, když se mu to asi přihodilo...")
        print("")
        while True:
            tela = str(input("Chceš si nahrávku přehrát? [ano, ne]: "))
            if tela == "ano":
                location.remove("guard_bodies_inspection_final")
                location.append("guard_bodies_inspection_final_tape")
                print("")
                break
            elif tela == "ne":
                print("")
                print("Vrátíš se zpátky.")
                print("")
                while True:
                    pokracovani = input("Stiskni Enter pro pokračování: ")
                    if pokracovani.strip() == "":
                        location.remove("guard_bodies_inspection_final")
                        location.append("shipwreck")
                        print("")
                        break
                    if pokracovani.strip() != "":
                        print("Zkus to znovu.")
                break
            else:
                print("Zadal si špatnou odpověď. Správné odpovědi jsou [ano, ne].")
                print("")
    if "guard_bodies_inspection_final_tape" in location:
        print("Nahrávka se po pár sekundách začne přehrávat.")
        print("")
        print("[Hlas 1]: UTÍKEJ RYCHLEJI!")
        print("[Hlas 2]: Ale.. já už.. nemůžu...")
        print("[Hlas 1]: Ještě chvíli, už budeme venku z lesa, víš že to nemá rádo sluneční svit.")
        print("[Hlas 1]: Zvládli jsme to! Jo! Jsme venku.. huf")
        print("[Hlas 2]: JO! Pane bože! huf.. huf.. *slabé zvuky deště*")
        print("[Hlas 1]: KURVA! Proč musí začít pršet zrovna teď!? Potřebujeme sluneční svit.")
        print("[Hlas 2]: Myslím.. že nás to dohnalo.")
        print("[Hlas 1]: Do prdele! Nejdu dolů bez boje! *zvuky střelby*")
        print("[Hlas 1]: AAAAAA *zvuky seknutí* eaa..")
        print("[Hlas 2]: Je konec... *zvuky seknutí* *zvuk kašlání*")
        print("[]: beep beep beep...")
        print("")
        print("Po pár minutách ticha a přemýšlení se rozhodneš zvednout a vydat se na dál. Než čekat na konec jaký měli oni.")
        print("")
        while True:
            pokracovani = input("Stiskni Enter pro pokračování: ")
            if pokracovani.strip() == "":
                location.remove("guard_bodies_inspection_final_tape")
                location.append("shipwreck")
                print("")
                break
            if pokracovani.strip() != "":
                print("Zkus to znovu.")


    if "meeting_point_A" in location:
        print("Ujdeš pár metrů a začneš se rozlížet kolem.")
        print("Před tebou stojí hustý listnatý les. Napravo vidíš pokračovat pláž kolem moře a ve stromech nějakou bednu. Když se podíváš nalevo tak spatříš maják. Který se vyjímá na útesu u pobřeží.")
        print("")
        while True:
            rozhodnuti = int(input("Kam se chceš vydat? [1 - maják, 2 - les, 3 - bedna]: "))
            if rozhodnuti == 1:
                location.remove("meeting_point_A")
                location.append("lighthouse")
                print("")
                break
            elif rozhodnuti == 2:
                location.remove("meeting_point_A")
                location.append("stone_circle")
                print("")
                break
            elif rozhodnuti == 3:
                location.remove("meeting_point_A")
                location.append("air_drop")
                print("")
                break
            else:
                print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - maják, 2 - les, 3 - bedna].")
                print("")


    if "air_drop" in location:
        print("Po chvíli chůze se přiblížíš k záhadné krabici. Všimneš si že je zaseknutá ve větvých i se svým padákem. Dojde ti že to je airdrop.")
        print("Také si všimneš že krabice je ze spodu poškozená a je v ní díra, pravděpodobně kvůli nárazu na strom, takže věci co v ní byli museli vypadnout pod ní.")
        print("")
        while True:
            tela = str(input("Chceš airdrop prozkoumat? [ano, ne]: "))
            print("")
            if tela == "ano":
                location.remove("air_drop")
                location.append("air_drop_close")
                break
            elif tela == "ne":
                while True:
                    nevim = int(input("Kam se tedy chceš vydat? [1 - vrak lodi, 2 - pláž]: "))
                    print("")
                    if nevim == 1:
                        print("Vydáš se k vraku lodi.")
                        print("")
                        location.remove("air_drop")
                        location.append("shipwreck")
                        break
                    elif nevim == 2:
                        print("Vydáš se na pláž.")
                        print("")
                        location.remove("air_drop")
                        location.append("villa_front")
                        break
                    else:
                        print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - vrak lodi, 2 - pláž].")
                        print("")
                break
            else:
                print("Zadal si špatnou odpověď. Správné odpovědi jsou [ano, ne].")
                print("")
    if "air_drop_close" in location:
        print("Přiblížíš se k airdropu, podíváš se pod něj. Po pečlivém hledání si...")
        if "revolver" in airdrop_loot:
            print("Našel revolver. Schováš si ho k sobě pro další využití.")
            airdrop_loot.remove("revolver")
            inventory.append("revolver")
            print("")
            while True:
                nevim = int(input("Kam se chceš vydat teď? [1 - vrak lodi, 2 - pláž]: "))
                print("")
                if nevim == 1:
                    print("Vydáš se k vraku lodi.")
                    print("")
                    location.remove("air_drop_close")
                    location.append("shipwreck")
                    break
                elif nevim == 2:
                    print("Vydáš se na pláž.")
                    print("")
                    location.remove("air_drop_close")
                    location.append("villa_front")
                    break
                else:
                    print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - vrak lodi, 2 - pláž].")
                    print("")
        elif "revolver" not in airdrop_loot:
            print("Bohužel nic nenašel.")
            print("")
            while True:
                nevim = int(input("Kam se chceš vydat teď? [1 - vrak lodi, 2 - pláž]: "))
                print("")
                if nevim == 1:
                    print("Vydáš se k vraku lodi.")
                    print("")
                    location.remove("air_drop_close")
                    location.append("shipwreck")
                    break
                elif nevim == 2:
                    print("Vydáš se na pláž.")
                    print("")
                    location.remove("air_drop_close")
                    location.append("villa_front")
                    break
                else:
                    print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - vrak lodi, 2 - pláž].")
                    print("")
    
    
    if "villa_front" in location:
        print("Procházíš se po pláží, sleduješ vlny na moři, když v tu najednou si všimneš že na levé straně pláže jsou jakési chatky.")
        print("Je jich tak pět, nachází se po celé pláži a nad nimi jde vidět les co se na ostrově nachází")
        print("")
        while True:
            tela = str(input("Chceš chatky prozkoumat? [ano, ne]: "))
            print("")
            if tela == "ano":
                location.remove("villa_front")
                location.append("villa_front_close")
                break
            elif tela == "ne":
                while True:
                    nevim = int(input("Kam se tedy chceš vydat? [1 - bedna, 2 - ke generátorům]: "))
                    print("")
                    if nevim == 1:
                        print("Vydáš se k záhadné bedně.")
                        print("")
                        location.remove("villa_front")
                        location.append("air_drop")
                        break
                    elif nevim == 2:
                        print("Vydáš se ke generátorům.")
                        print("")
                        location.remove("villa_front")
                        location.append("meeting_point_B")
                        break
                    else:
                        print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - bedna, 2 - ke generátorům].")
                        print("")
                break
            else:
                print("Zadal si špatnou odpověď. Správné odpovědi jsou [ano, ne].")
                print("")
    if "villa_front_close" in location:
        print("Začneš prohledávat chatky. Prohledáš první, pak druhou, třetí a čtvrtou chatku, ale nic.")
        print("Pak něco ale zahlédneš v páté poslední chatce. Po bližším prozkoumání si...")
        if "torch" in villa_front_loot and "torch" not in inventory:
            print("Našel pochodeň. Schováš si ho k sobě pro další využití.")
            villa_front_loot.remove("torch")
            inventory.append("torch")
            print("")
            while True:
                nevim = int(input("Kam se chceš vydat teď? [1 - bedna, 2 - ke generátorům]: "))
                print("")
                if nevim == 1:
                    print("Vydáš se k záhadné bedně.")
                    print("")
                    location.remove("villa_front_close")
                    location.append("air_drop")
                    break
                elif nevim == 2:
                    print("Vydáš se ke generátorům.")
                    print("")
                    location.remove("villa_front_close")
                    location.append("meeting_point_B")
                    break
                else:
                    print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - bedna, 2 - ke generátorům].")
                    print("")
        elif "torch" not in villa_front_loot:
            print("Bohužel nic nenašel.")
            print("")
            while True:
                nevim = int(input("Kam se chceš vydat teď? [1 - bedna, 2 - ke generátorům]: "))
                print("")
                if nevim == 1:
                    print("Vydáš se k záhadné bedně.")
                    print("")
                    location.remove("villa_front_close")
                    location.append("air_drop")
                    break
                elif nevim == 2:
                    print("Vydáš se ke generátorům.")
                    print("")
                    location.remove("villa_front_close")
                    location.append("meeting_point_B")
                    break
                else:
                    print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - bedna, 2 - ke generátorům].")
                    print("")
        elif "torch" in villa_front_loot and "torch" in inventory:
            print("Našel pochodeň. Jelikož už ale jednu máš, tak ti přijde nepotřebné mít dvě. Necháš ji v chatce, kde si ji našel.")
            print("")
            while True:
                nevim = int(input("Kam se chceš vydat teď? [1 - bedna, 2 - ke generátorům]: "))
                print("")
                if nevim == 1:
                    print("Vydáš se k záhadné bedně.")
                    print("")
                    location.remove("villa_front_close")
                    location.append("air_drop")
                    break
                elif nevim == 2:
                    print("Vydáš se ke generátorům.")
                    print("")
                    location.remove("villa_front_close")
                    location.append("meeting_point_B")
                    break
                else:
                    print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - bedna, 2 - ke generátorům].")
                    print("")


    if "meeting_point_B" in location:
        print("Po pár minutách chůze zahlédneš kovový drátěný plot. Za ním si všimneš že je hodně nějakých žlutých přístrojů. Vypadá to, že tohle bude zdroj energie pro celý ostrov.")
        print("Pak se podíváš nahoru a všimneš si velké budovy s kopulovitou střechou na skále za generátory. Po bližším pozorování ti dojde že je to observatoř.")
        print("Když se podíváš doleva tak vidíš velké jezero, když sleduješ jeho břeh tak zanedloho si všimneš malého mola s budkou.")
        print("Na druhé straně jezera také spatříš jakousi dřevěnou hlídací věž. A vedle ní nějaké dvě větší budovy. Nedokážeš ale rozeznat co je to za budovu z důvodu velké vzdálenosti.")
        print("Když se podíváš za sebe, tak uvidíš dlouhou pláž, která vede kolem moře. Také spatříš jakousi chatku.")
        print("")
        while True:
            rozhodnuti = int(input("Kam se chceš vydat? [1 - generátory, 2 - observatoř, 3 - rybářská chatka, 4 - pláž]: "))
            if rozhodnuti == 1:
                location.remove("meeting_point_B")
                location.append("generators")
                print("")
                break
            elif rozhodnuti == 2:
                location.remove("meeting_point_B")
                location.append("observatory")
                print("")
                break
            elif rozhodnuti == 3:
                location.remove("meeting_point_B")
                location.append("fishing_hut")
                print("")
                break
            elif rozhodnuti == 4:
                location.remove("meeting_point_B")
                location.append("villa_front")
                print("")
                break
            else:
                print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - generátory, 2 - observatoř, 3 - rybářská chatka, 4 - pláž].")
                print("")


    if "generators" in location:
        print("Dojdeš ke plotu. Všimneš si že na levo se nachází díra v plotě, tak ní projdeš. Nyní se nacházíš uvnitř plotu a před tebou je několik generátorů.")
        print("Na pravo ale uvidíš jakousi bezpečností budku. Opodál spatříš jediný otevřený generátor.")
        print("")
        while True:
            rozhodnuti = int(input("Co chceš prozkoumat nebo kam se vydat? [1 - bezpečnostní budka, 2 - otevřený generátor, 3 - odejít]: "))
            if rozhodnuti == 1:
                location.remove("generators")
                location.append("generators_security")
                print("")
                break
            elif rozhodnuti == 2:
                location.remove("generators")
                location.append("generators_fuses")
                print("")
                break
            elif rozhodnuti == 3:
                location.remove("generators")
                location.append("meeting_point_B")
                print("")
                break
            else:
                print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - bezpečnostní budka, 2 - otevřený generátor, 3 - odejít].")
                print("")
    if "generators_security" in location:
        print("Vejdeš dovnitř budky. Po následném hledání si...")
        if "fuse" in generator_loot:
            print("Našel pojistku. Schováš si ho k sobě pro další využití.")
            generator_loot.remove("fuse")
            inventory.append("fuse")
            print("")
            print("Vydáš se zpátky.")
            print("")
            while True:
                pokracovani = input("Stiskni Enter pro pokračování: ")
                if pokracovani.strip() == "":
                    location.remove("generators_security")
                    location.append("generators")
                    print("")
                    break
                if pokracovani.strip() != "":
                    print("Zkus to znovu.")
        elif "fuse" not in generator_loot:
            print("Bohužel nic nenašel.")
            print("")
            print("Vydáš se zpátky.")
            print("")
            while True:
                pokracovani = input("Stiskni Enter pro pokračování: ")
                if pokracovani.strip() == "":
                    location.remove("generators_security")
                    location.append("generators")
                    print("")
                    break
                if pokracovani.strip() != "":
                    print("Zkus to znovu.")
    if "generators_fuses" in location:
        print("Dojdeš k otevřenému generátoru. Po následném zkoumání zjistíš že se jedná o jakýsi hlavní generátor.")
        print("Nachází se v něm deska, kam se dá vložit pojistka. Každý otvor má u sebe popisek lokace, která se s největší pravděpodobností spustí a dostane elektřinu.")
        print("")
        if "fuse" in inventory:
            print("Vytáhneš dřívě získanou pojistku z kapsy. Vidíš dva volné otvory kam by mohla pasovat.")
            print("U prvního otvoru stojí: SKLADY. U druhého stojí: OBSERVATOŘ.")
            print("")
            while True:
                gens = int(input("Co chceš udělat? [1 - zapnout sklady, 2 - zapnout observatoř, 3 - odejít]: "))
                print("")
                if gens == 1:
                    print("Vložíš pojistku do otvoru. Rozsvítí se kontrolní dioda u SKLADY. Následně uslyšíš jak některé generátory začly dělat hluk.")
                    print("")
                    inventory.remove("fuse")
                    generator_warehouse.append("fuse")
                    while True:
                        pokracovani = input("Stiskni Enter pro pokračování: ")
                        if pokracovani.strip() == "":
                            print("")
                            break
                        if pokracovani.strip() != "":
                            print("Zkus to znovu.")
                    break
                elif gens == 2:
                    print("Vložíš pojistku do otvoru. Rozsvítí se kontrolní dioda u OBSERVATOŘ. Následně uslyšíš jak některé generátory začly dělat hluk.")
                    print("")
                    inventory.remove("fuse")
                    generator_observatory.append("fuse")
                    while True:
                        pokracovani = input("Stiskni Enter pro pokračování: ")
                        if pokracovani.strip() == "":
                            print("")
                            break
                        if pokracovani.strip() != "":
                            print("Zkus to znovu.")
                    break
                elif gens == 3:
                    print("Odstoupíš od generátoru.")
                    print("")
                    while True:
                        pokracovani = input("Stiskni Enter pro pokračování: ")
                        if pokracovani.strip() == "":
                            location.remove("generators_fuses")
                            location.append("generators")
                            print("")
                            break
                        if pokracovani.strip() != "":
                            print("Zkus to znovu.")
                    break
                else:
                    print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - zapnout sklady, 2 - zapnout observatoř, 3 - odejít].")
                    print("")
        if "fuse" not in inventory and "fuse" not in generator_warehouse and "fuse" not in generator_observatory:
            print("Bohužel si ještě nenašel žádnou pojistku. Tím pádem nemáš čím zapnout generátory.")
            print("")
            print("Odstoupíš od generátoru.")
            print("")
            while True:
                pokracovani = input("Stiskni Enter pro pokračování: ")
                if pokracovani.strip() == "":
                    location.remove("generators_fuses")
                    location.append("generators")
                    print("")
                    break
                if pokracovani.strip() != "":
                    print("Zkus to znovu.")
        if "fuse" in generator_warehouse:
            otaz = str(input("Chceš pojistku umístiť jinam? [ano, ne]: "))
            print("")
            if otaz == "ano": 
                print("Přijdeš k desce a vytáhneš dříve umístěnou pojistku.")
                print("")
                generator_warehouse.remove("fuse")
                while True:
                    gens = int(input("Kam chceš pojistku umístit teď? [1 - SKLADY, 2 - OBSERVATOŘ]"))
                    print("")
                    if gens == 1:
                        generator_warehouse.append("fuse")
                        print("Vložíš pojistku do otvoru. Rozsvítí se kontrolní dioda u SKLADY. Následně uslyšíš jak některé generátory začly dělat hluk.")
                        print("")
                        while True:
                            pokracovani = input("Stiskni Enter pro pokračování: ")
                            if pokracovani.strip() == "":
                                print("")
                                break
                            if pokracovani.strip() != "":
                                print("Zkus to znovu.")
                        break
                    elif gens == 2:
                        generator_observatory.append("fuse")
                        print("Vložíš pojistku do otvoru. Rozsvítí se kontrolní dioda u OBSERVATOŘ. Následně uslyšíš jak některé generátory začly dělat hluk.")
                        print("")
                        while True:
                            pokracovani = input("Stiskni Enter pro pokračování: ")
                            if pokracovani.strip() == "":
                                print("")
                                break
                            if pokracovani.strip() != "":
                                print("Zkus to znovu.")
                        break
                    else:
                        print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - SKLADY, 2 - OBSERVATOŘ].")
                        print("")
            elif otaz == "ne":
                print("")
                print("Odstoupíš od generátoru.")
                print("")
                while True:
                    pokracovani = input("Stiskni Enter pro pokračování: ")
                    if pokracovani.strip() == "":
                        location.remove("generators_fuses")
                        location.append("generators")
                        print("")
                        break
                    if pokracovani.strip() != "":
                        print("Zkus to znovu.")
            else:
                print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - SKLADY, 2 - OBSERVATOŘ].")
                print("")
        if "fuse" in generator_observatory:
            otaz = str(input("Chceš pojistku umístiť jinam? [ano, ne]: "))
            print("")
            if otaz == "ano":
                print("Přijdeš k desce a vytáhneš dříve umístěnou pojistku.")
                print("")
                generator_observatory.remove("fuse")
                while True:
                    gens = int(input("Kam chceš pojistku umístit teď? [1 - SKLADY, 2 - OBSERVATOŘ]"))
                    print("")
                    if gens == 1:
                        generator_warehouse.append("fuse")
                        print("Vložíš pojistku do otvoru. Rozsvítí se kontrolní dioda u SKLADY. Následně uslyšíš jak některé generátory začly dělat hluk.")
                        print("")
                        while True:
                            pokracovani = input("Stiskni Enter pro pokračování: ")
                            if pokracovani.strip() == "":
                                location.remove("generators_fuses")
                                location.append("generators")
                                print("")
                                break
                            if pokracovani.strip() != "":
                                print("Zkus to znovu.")
                        break
                    elif gens == 2:
                        generator_observatory.append("fuse")
                        print("Vložíš pojistku do otvoru. Rozsvítí se kontrolní dioda u OBSERVATOŘ. Následně uslyšíš jak některé generátory začly dělat hluk.")
                        print("")
                        while True:
                            pokracovani = input("Stiskni Enter pro pokračování: ")
                            if pokracovani.strip() == "":
                                location.remove("generators_fuses")
                                location.append("generators")
                                print("")
                                break
                            if pokracovani.strip() != "":
                                print("Zkus to znovu.")
                        break
                    else:
                        print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - SKLADY, 2 - OBSERVATOŘ].")
                        print("")
            elif otaz == "ne":
                print("")
                print("Odstoupíš od generátoru.")
                print("")
                while True:
                    pokracovani = input("Stiskni Enter pro pokračování: ")
                    if pokracovani.strip() == "":
                        location.remove("generators_fuses")
                        location.append("generators")
                        print("")
                        break
                    if pokracovani.strip() != "":
                        print("Zkus to znovu.")
            else:
                print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - SKLADY, 2 - OBSERVATOŘ].")
                print("")
        
    
    if "observatory" in location and "cleared" not in observatory_door:
        print("Začneš vylézat zdejší kopec. Po pár minutách se konečně dostáváš k observatoři.")
        print("Párkrát obervatoř obejdeš, jelikož hledáš vchod. Jenže ho nemůžeš najít.")
        print("Po bližsím zkoumaní ho konečně najdeš. Je tu ale problém. Je zarostlý nějakou ostnatou kapradinou. Nikdy si ji neviděl, asi pochází z tohoto ostrova.")
        print("")
        print("Teď by se hodila pochodeň.")
        print("")
        if "torch" in inventory:
            print("Naštěstí už pochodeň máš. Silně ji vezmeš do ruk a přiložíš ke kapradině.")
            print("Kapradina ihned vzplane. Po pár minutách po kapradině zbyl jen popel a vchod se uvolnil.")
            observatory_door.append("cleared")
            print("")
            while True:
                tela = str(input("Chceš jít dovnitř observatoře? [ano, ne]: "))
                print("")
                if tela == "ano":
                    location.remove("observatory")
                    location.append("observatory_inside")
                    break
                if tela == "ne":
                    print("Slezeš kopec zpátky dolů.")
                    print("")
                    location.remove("observatory")
                    location.append("meeting_point_B")
                    break
                else:
                    print("Zadal si špatnou odpověď. Správné odpovědi jsou [ano, ne].")
                    print("")
        elif "torch" not in inventory:
            print("Bohužel si pochodeň ještě nenašel. Slezeš kopec zpátky dolů a plánuješ jít jinam, dokud ji nedajdeš.")
            print("")
            while True:
                pokracovani = input("Stiskni Enter pro pokračování: ")
                if pokracovani.strip() == "":
                    location.remove("observatory")
                    location.append("meeting_point_B")
                    print("")
                    break
                if pokracovani.strip() != "":
                    print("Zkus to znovu.")
    if "observatory" in location and "cleared" in observatory_door:
        print("Začneš vylézat zdejší kopec. Po pár minutách se konečně dostáváš k observatoři.")
        print("")
        while True:
            tela = str(input("Chceš jít dovnitř observatoře? [ano, ne]: "))
            print("")
            if tela == "ano":
                location.remove("observatory")
                location.append("observatory_inside")
                break
            if tela == "ne":
                print("Slezeš kopec zpátky dolů.")
                print("")
                location.remove("observatory")
                location.append("meeting_point_B")
                break
            else:
                print("Zadal si špatnou odpověď. Správné odpovědi jsou [ano, ne].")
                print("")
    if "observatory_inside" in location:
        print("Vejdeš do observatoře. Většina zdí i uvnitř je porostlá divnou kapradinou. Už ale neblokuje tvou cestu.")
        print("Na levo si všimneš žebříku. Vylezeš po něm, pak následuje pár schodů a dorazil si na to co vypadá jako hlavní podlaží.")
        print("Když se porozhlédneš uvidíš pár stolů s počítači. Které vypadají stále funkčně.")
        print("")
        while True:
            tela = str(input("Chceš počítače prozkoumat víc? [ano, ne]: "))
            print("")
            if tela == "ano":
                location.remove("observatory_inside")
                location.append("observatory_computers")
                break
            if tela == "ne":
                print("Vyjdeš z obervatoře a slezeš kopec zpátky dolů.")
                print("")
                location.remove("observatory_inside")
                location.append("meeting_point_B")
                break
            else:
                print("Zadal si špatnou odpověď. Správné odpovědi jsou [ano, ne].")
                print("")
    if "observatory_computers" in location and "fuse" in generator_observatory:
        print("Zkusíš počítač zapnout. Po pár sekundách se počítač začne načítat.")
        print("Počítač se načtě a naštěstí nepotřebuje heslo.")
        print("Začneš tedy projíždět počítač a hledat jakékoli užitečné informace.")
        print("")
        print("Když v tu najednou jeden ze souborů upoutá tvou pozornost.")
        print("Její název je ZÁZNAMY ANOMÁLIE.")
        print("")
        while True:
            pokracovani = input("Stiskni Enter pro pokračování: ")
            if pokracovani.strip() == "":
                location.remove("observatory_computers")
                location.append("observatory_records")
                print("")
                break
            if pokracovani.strip() != "":
                print("Zkus to znovu.")
    if "observatory_computers" in location and "fuse" not in generator_observatory:
        print("Zkusíš počítač zapnout. Po pár sekundách čekání ti dojde že se nic nestane.")
        print("Blíže si prohlédneš počítač a zjistíš že mu chybí elektřina.")
        print("")
        print("Bohužel tak vycházíš s prázdnou z observatoře a slézáš kopec zpátky dolů")
        print("")
        while True:
            pokracovani = input("Stiskni Enter pro pokračování: ")
            if pokracovani.strip() == "":
                location.remove("observatory_computers")
                location.append("meeting_point_B")
                print("")
                break
            if pokracovani.strip() != "":
                print("Zkus to znovu.")
    if "observatory_records" in location:
        print("[ZÁZNAM ZE DNE 16.1#.2### 16:04]: Anomálie je v klidovém stavu. Zítra mají proběhnout finální testy. Celý výzkumný tým na tento okamžik čeká.")
        print("[ZÁZNAM ZE DNE 17.1#.2### 06:19]: Za tři hodiny přijede velení. Chtějí také vidět finální testy.")
        print("[ZÁZNAM ZE DNE 17.1#.2### 09:38]: Za dvacet minut začnou finální testy. Většina lidí ze všech oddělení už je na místě a netrpělivé čeká.")
        print("[ZÁZNAM ZE DNE 17.1#.2### 10:21]: Něco se děje. Anomálie po celých pěti letech není v klidovém stavu. Možná se nám to podaří!")
        print("[ZÁZNAM ZE DNE 17.1#.2### 10:33]: ZADRŽOVACÍ PROSTOR BYL PROLOMEN *intenzivní střelba* *hlasitý křik* ZADRŽOVACÍ PROSTOR BYL PROLOMEN *sirény* ZADRŽOVACÍ PROSTO#.##..")
        print("")
        print("V tichu tam dalších pět minut sedíš na židli před počítačem a srovnáváš si myšlenky. Na další soubory už se radši podívat nechceš.")
        print("")
        while True:
            pokracovani = input("Stiskni Enter pro pokračování: ")
            if pokracovani.strip() == "":
                location.remove("observatory_records")
                location.append("observatory_drawer")
                print("")
                break
            if pokracovani.strip() != "":
                print("Zkus to znovu.")
    if "observatory_drawer" in location:
        print("Zkusíš aspoň ještě otevřít šuplíky u stolu u kterého sedíš.")
        print("Po otevření šuplíku si...")
        if "night_vision" in observatory_loot:
            print("Našel brýle nočního vidění. Schováš si je k sobě pro další využití.")
            observatory_loot.remove("night_vision")
            inventory.append("night_vision")
            print("")
            print("Odejdeš z observatoře a slezeš kopec zpátky dolů.")
            print("")
            while True:
                pokracovani = input("Stiskni Enter pro pokračování: ")
                if pokracovani.strip() == "":
                    location.remove("observatory_drawer")
                    location.append("meeting_point_B")
                    print("")
                    break
                if pokracovani.strip() != "":
                    print("Zkus to znovu.")
        elif "night_vision" not in observatory_loot:
            print("Bohužel nic nenašel.")
            print("")
            print("Odejdeš z observatoře a slezeš kopec zpátky dolů.")
            print("")
            while True:
                pokracovani = input("Stiskni Enter pro pokračování: ")
                if pokracovani.strip() == "":
                    location.remove("observatory_drawer")
                    location.append("meeting_point_B")
                    print("")
                    break
                if pokracovani.strip() != "":
                    print("Zkus to znovu.")
    

    if "stone_circle" in location and "night_vision" not in inventory:
        print("Vydáš se do lesa. Po pár minutách chůze si začneš všímat že les je celkem hustý a že moc slunečního svitu neproniká skrze stromy. Je tu celkem tmavo.")
        print("Je to ale zvládnutelné, takže se vydáváš dál.")
        print("")
        while True:
            pokracovani = input("Stiskni Enter pro pokračování: ")
            if pokracovani.strip() == "":
                location.remove("stone_circle")
                location.append("stone_circle_second")
                print("")
                break
            if pokracovani.strip() != "":
                print("Zkus to znovu.")
    if "stone_circle" in location and "night_vision" in inventory:
        print("Vydáš se do lesa. Po pár minutách chůze si začneš všímat že les je celkem hustý a že moc slunečního svitu neproniká skrze stromy. Je tu celkem tmavo.")
        print("Zapneš tedy své brýle nočního vidění.")
        print("")
        while True:
            pokracovani = input("Stiskni Enter pro pokračování: ")
            if pokracovani.strip() == "":
                location.remove("stone_circle")
                location.append("stone_circle_secret")
                print("")
                break
            if pokracovani.strip() != "":
                print("Zkus to znovu.")
    if "stone_circle_secret" in location:
        print("Najednou se tvoje vidění zbarví do zelena. I tak ale vidíš lépe než předtím.")
        print("Po chvíli chůze si všimneš něčeho ve stromě. Po přiblížení si...")
        if "revolver" in stone_circle_secret_loot:
            print("Našel revolver. Schováš si ho k sobě pro další využití.")
            stone_circle_secret_loot.remove("revolver")
            inventory.append("revolver")
            print("")
            while True:
                pokracovani = input("Stiskni Enter pro pokračování: ")
                if pokracovani.strip() == "":
                    location.remove("stone_circle_secret")
                    location.append("stone_circle_second")
                    print("")
                    break
                if pokracovani.strip() != "":
                    print("Zkus to znovu.")
        elif "revolver" not in stone_circle_secret_loot:
            print("Bohužel nic nenašel.")
            print("")
            while True:
                pokracovani = input("Stiskni Enter pro pokračování: ")
                if pokracovani.strip() == "":
                    location.remove("stone_circle_secret")
                    location.append("stone_circle_second")
                    print("")
                    break
                if pokracovani.strip() != "":
                    print("Zkus to znovu.")    
    if "stone_circle_second" in location:
        print("po chvíli chůze si všimneš v dálce nějakých velkých kamenů.")
        print("")
        while True:
            tela = str(input("Chceš kameny prozkoumat více? [ano, ne]: "))
            print("")
            if tela == "ano":
                location.remove("stone_circle_second")
                location.append("stone_circle_close")
                break
            elif tela == "ne":
                while True:
                    nevim = int(input("Projdeš tedy kolem kamenů a pokračuješ ve své cestě. Kam se chceš vydat teď? [1 - vrak lodi, 2 - rybářská chatka]: "))
                    print("")
                    if nevim == 1:
                        print("Vydáš se k vraku lodi.")
                        print("")
                        location.remove("stone_circle_second")
                        location.append("shipwreck")
                        break
                    elif nevim == 2:
                        print("Vydáš se k rybářské chatce.")
                        print("")
                        location.remove("stone_circle_second")
                        location.append("fishing_hut")
                        break
                    else:
                        print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - vrak lodi, 2 - rybářská chatka].")
                        print("")
                break
    if "stone_circle_close" in location:
        print("Začneš se přibližovat k záhadným kamenům. Kameny vypadají že jsou ve tvaru kruhu. Odhaduješ jejich výšku asi na tři metry.")
        print("Radši nezkoumáš jejich využití. Začneš se dívat kolem nich jestli nenajdeš něco užitečného.")
        print("")
        while True:
            pokracovani = input("Stiskni Enter pro pokračování: ")
            if pokracovani.strip() == "":
                location.remove("stone_circle_close")
                location.append("stone_circle_final")
                print("")
                break
            if pokracovani.strip() != "":
                print("Zkus to znovu.")
    if "stone_circle_final" in location:
        print("Začneš obcházet kameny. Něco zahlédneš u čtvrtého kamenu. Po bližsím proukoumání si...")
        if "torch" in stone_circle_loot and "torch" not in inventory:
            print("Našel pochodeň. Schováš si ji k sobě pro další využití.")
            stone_circle_loot.remove("torch")
            inventory.append("torch")
            print("")
            while True:
                nevim = int(input("Kam se chceš vydat teď? [1 - vrak lodi, 2 - rybářská chatka]: "))
                print("")
                if nevim == 1:
                    print("Vydáš se k vraku lodi.")
                    print("")
                    location.remove("stone_circle_final")
                    location.append("shipwreck")
                    break
                elif nevim == 2:
                    print("Vydáš se k rybářské chatce.")
                    print("")
                    location.remove("stone_circle_final")
                    location.append("fishing_hut")
                    break
                else:
                    print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - vrak lodi, 2 - rybářská chatka].")
                    print("")
        elif "torch" not in stone_circle_loot:
            print("Bohužel nic nenašel.")
            print("")
            while True:
                nevim = int(input("Kam se chceš vydat teď? [1 - vrak lodi, 2 - rybářská chatka]: "))
                print("")
                if nevim == 1:
                    print("Vydáš se k vraku lodi.")
                    print("")
                    location.remove("stone_circle_final")
                    location.append("shipwreck")
                    break
                elif nevim == 2:
                    print("Vydáš se k rybářské chatce.")
                    print("")
                    location.remove("stone_circle_final")
                    location.append("fishing_hut")
                    break
                else:
                    print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - vrak lodi, 2 - rybářská chatka].")
                    print("")
        elif "torch" in stone_circle_loot and "torch" in inventory:
            print("Našel pochodeň. Jelikož už ale jednu máš, tak ti přijde nepotřebné mít dvě. Necháš ji u kamene kde si ji našel.")
            while True:
                nevim = int(input("Kam se chceš vydat teď? [1 - vrak lodi, 2 - rybářská chatka]: "))
                print("")
                if nevim == 1:
                    print("Vydáš se k vraku lodi.")
                    print("")
                    location.remove("stone_circle_final")
                    location.append("shipwreck")
                    break
                elif nevim == 2:
                    print("Vydáš se k rybářské chatce.")
                    print("")
                    location.remove("stone_circle_final")
                    location.append("fishing_hut")
                    break
                else:
                    print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - vrak lodi, 2 - rybářská chatka].")
                    print("")

    
    if "fishing_hut" in location:
        print("Po chvíli chůze vidíš obrovské jezero. Voda čirá jako křišťál a na jejím břehu malé molo s chatkou. Uvnitř zahlédneš rybářské náčiní.")
        print("po své pravici zahlédneš něco žlutého, za velkým kovovým plotem. Vypadá to jako nějaký generátor.")
        print("Za zmíněným generátorem zahlédneš na kopci budovu s kopulitou střechou. Pak si všimneš velkého teleskopu a dojde ti že je to observatoř.")
        print("Na levo na hoře nad jezerem si všimneš nějaké dřevěnné hlídací věže. A za tebou velkého lesa, co se na ostrově nachází.")
        print("")
        while True:
            rozhodnuti = int(input("Kam se chceš vydat? [1 - dovnitř rybářské chatky, 2 - ke generátorům, 3 - hlídací věž, 4 - do lesa]: "))
            if rozhodnuti == 1:
                location.remove("fishing_hut")
                location.append("fishing_hut_inside")
                print("")
                break
            elif rozhodnuti == 2:
                location.remove("fishing_hut")
                location.append("meeting_point_B")
                print("")
                break
            elif rozhodnuti == 3:
                location.remove("fishing_hut")
                location.append("watch_tower")
                print("")
                break
            elif rozhodnuti == 4:
                location.remove("fishing_hut")
                location.append("stone_circle")
                print("")
                break
            else:
                print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - dovnitř rybářské chatky, 2 - ke generátorům, 3 - hlídací věž, 4 - do lesa].")
                print("")
    if "fishing_hut_inside" in location and "fishing_rod" in fishing_hut_loot:
        print("Vejdeš do rybářské chatky. Na zdech uvidíš různé rybářské náčiní. Pak uvidíš vzadu funkčně vypadající rybářský prut.")
        print("")
        while True:
            tela = str(input("Chceš si zarybařit? [ano, ne]: "))
            print("")
            if tela == "ano":
                location.remove("fishing_hut_inside")
                location.append("fishing_hut_pier")
                fishing_hut_loot.remove("fishing_rod")
                break
            elif tela == "ne":
                while True:
                    nevim = int(input("Vyjdeš z chatky. Kam se chceš vydat teď? [1 - ke generátorům, 2 - hlídací věž, 3 - do lesa]: "))
                    print("")
                    if nevim == 1:
                        location.remove("fishing_hut_inside")
                        location.append("meeting_point_B")
                        print("")
                        break
                    elif nevim == 2:
                        location.remove("fishing_hut_inside")
                        location.append("watch_tower")
                        print("")
                        break
                    elif nevim == 3:
                        location.remove("fishing_hut_inside")
                        location.append("stone_circle")
                        print("")
                        break
                    else:
                        print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - ke generátorům, 2 - hlídací věž, 3 - do lesa].")
                        print("")
                break
    if "fishing_hut_inside" in location and "fishing_rod" not in fishing_hut_loot:
        print("Vejdeš do rybářské chatky. Na zdech uvidíš různé rybářské náčiní. Už si ale využil jediný funkční rybářský prut.")
        print("")
        while True:
            nevim = int(input("Tak vyjdeš z chatky. Kam se chceš vydat teď? [1 - ke generátorům, 2 - hlídací věž, 3 - do lesa]: "))
            print("")
            if nevim == 1:
                location.remove("fishing_hut_inside")
                location.append("meeting_point_B")
                print("")
                break
            elif nevim == 2:
                location.remove("fishing_hut_inside")
                location.append("watch_tower")
                print("")
                break
            elif nevim == 3:
                location.remove("fishing_hut_inside")
                location.append("stone_circle")
                print("")
                break
            else:
                print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - ke generátorům, 2 - hlídací věž, 3 - do lesa].")
                print("")
    if "fishing_hut_pier" in location:
        print("Uchopíš rybářský prut do svých rukou a vydáš se na molo vedle chatky.")
        print("Nahodíš návnadu do vody a čekáš. Po chvíli se něco začne dít. Silně chytíš prut a začneš tahat. Podařilo se...")
        if "ammo_crate" in fishing_loot:
            print("Vylovit bednu s municí. Schováš si je k sobě pro další využití.")
            print("Prut bohužel následně praskl a stal se nepoužitelným.")
            fishing_loot.remove("ammo_crate")
            inventory.append("ammo_crate")
            print("")
            print("Po-té vyjdeš z chatky.")
            print("")
            while True:
                nevim = int(input("Tak vyjdeš z chatky. Kam se chceš vydat teď? [1 - ke generátorům, 2 - hlídací věž, 3 - do lesa]: "))
                print("")
                if nevim == 1:
                    location.remove("fishing_hut_pier")
                    location.append("meeting_point_B")
                    print("")
                    break
                elif nevim == 2:
                    location.remove("fishing_hut_pier")
                    location.append("watch_tower")
                    print("")
                    break
                elif nevim == 3:
                    location.remove("fishing_hut_pier")
                    location.append("stone_circle")
                    print("")
                    break
                else:
                    print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - ke generátorům, 2 - hlídací věž, 3 - do lesa].")
                    print("")
        elif "ammo_crate" not in fishing_loot:
            print("Vylovit bohužel nic.")
            print("Prut bohužel následně praskl a stal se nepoužitelným.")
            print("")
            print("Po-té vyjdeš z chatky.")
            print("")
            while True:
                nevim = int(input("Tak vyjdeš z chatky. Kam se chceš vydat teď? [1 - ke generátorům, 2 - hlídací věž, 3 - do lesa]: "))
                print("")
                if nevim == 1:
                    location.remove("fishing_hut_pier")
                    location.append("meeting_point_B")
                    print("")
                    break
                elif nevim == 2:
                    location.remove("fishing_hut_pier")
                    location.append("watch_tower")
                    print("")
                    break
                elif nevim == 3:
                    location.remove("fishing_hut_pier")
                    location.append("stone_circle")
                    print("")
                    break
                else:
                    print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - ke generátorům, 2 - hlídací věž, 3 - do lesa].")
                    print("")


    if "lighthouse" in location:
        print("Vydáš se k majáku. Než se k němu přiblížíš tak už obdivuješ útes na kterém je a jak pod ním zuří vlny moře.")
        print("Jakmile dojdeš k majáku tak se podíváš nahoru, jak vysoký vlastně je.")
        print("Podíváš se kolem a v dáli na pravo zahlédneš jakousi dřevěnou hlídací věž a za ní dvě nerozpoznatelné budovy.")
        print("")
        while True:
            tela = str(input("Chceš vylézt nahoru majáku? [ano, ne]: "))
            print("")
            if tela == "ano":
                location.remove("lighthouse")
                location.append("lighthouse_top")
                break
            elif tela == "ne":
                if "check" in lighthouse_visit:
                    while True:
                        nevim = int(input("Kam se chceš vydat? [1 - vrak lodi, 2 - hlídací věž, 3 - letadlo]: "))
                        print("")
                        if nevim == 1:
                            location.remove("lighthouse")
                            location.append("shipwreck")
                            print("")
                            break
                        elif nevim == 2:
                            location.remove("lighthouse")
                            location.append("watch_tower")
                            print("")
                            break
                        elif nevim == 3:
                            location.remove("lighthouse")
                            location.append("plane")
                            print("")
                            break
                        else:
                            print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - vrak lodi, 2 - hlídací věž, 3 - letadlo].")
                            print("")
                    break
                if "check" not in lighthouse_visit:
                    while True:
                        nevim = int(input("Kam se chceš vydat? [1 - vrak lodi, 2 - hlídací věž]: "))
                        print("")
                        if nevim == 1:
                            location.remove("lighthouse")
                            location.append("shipwreck")
                            print("")
                            break
                        elif nevim == 2:
                            location.remove("lighthouse")
                            location.append("watch_tower")
                            print("")
                            break
                        else:
                            print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - vrak lodi, 2 - hlídací věž].")
                            print("")
                    break
    if "lighthouse_top" in location:
        print("Vkročíš dovnitř majáku. Pohlédneš nahoru a uvidíš desítky schodů a dojde ti do čeho ses to vlastně dostal.")
        print("Po ani nevíš kolika schodech a jednom finálním žebříku ses konečně vyhrabal nahoru.")
        print("Rozehlédneš se po ostrově a začneš obdivovat výhlet. Pak si ale nalevo něčeho všimneš.")
        print("Kromě hlídací věže a dvou budov zahlédneš něco co vypadá jako letadlo. Na útesu dál za majákem")
        print("Možná to bude moje cesta ven, pomyslíš si...")
        print("")
        lighthouse_visit.append("check")
        print("Následné slezeš dolů a začneš přemýšlět kam dál jít.")
        print("")
        while True:
            pokracovani = input("Stiskni Enter pro pokračování: ")
            if pokracovani.strip() == "":
                location.remove("lighthouse_top")
                location.append("lighthouse_down")
                print("")
                break
            if pokracovani.strip() != "":
                print("Zkus to znovu.")
    if "lighthouse_down" in location:
        while True:
            nevim = int(input("Kam se chceš vydat? [1 - vrak lodi, 2 - hlídací věž, 3 - letadlo]: "))
            print("")
            if nevim == 1:
                location.remove("lighthouse_down")
                location.append("shipwreck")
                print("")
                break
            elif nevim == 2:
                location.remove("lighthouse_down")
                location.append("watch_tower")
                print("")
                break
            elif nevim == 3:
                location.remove("lighthouse_down")
                location.append("plane")
                print("")
                break
            else:
                print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - vrak lodi, 2 - hlídací věž, 3 - letadlo].")
                print("")


    if "plane" in location:
        print("Po pár minutách chůze ve směru dřívě spatřeného letadla z m")
        break


    if "watch_tower" in location:
        print("není heheha")
        break