import random

location = ["start"] #shipwreck, stone_circle, fishing_hut, watch_tower, ware_houses, lighthouse, plane, air_drop, villa_front, generators, obervatory, meeting_point_A, meeting_point_B, meeting_point_C
inventory = [""] #night_vision, fishing_rod, fuse, plane_steering_wheel, plane_wheel, revolver, double_barrel_shotgun, flashlight


night_rng = random.randint(0, 1)
airdrop_rng = 2
ship_rng = random.randint(0, 1)


shipwreck_loot = []
if ship_rng == 1:
    shipwreck_loot.append("flashlight")

guard_loot = ["medkit"]

airdrop_loot = []
if airdrop_rng == random.randint(0, 2):
    airdrop_loot.append("revolver")


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
            vrak = int(input("Chceš prozkoumat své okolí než se vidáš hlouběji do ostrova? [1 - vrak lodi, 2 - těla lidí, 3 - odejít]: "))
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


    if "lighthouse" in location:
        print("Smula pičo ještě není1")
        break
    if "stone_circle" in location:
        print("Smula pičo ještě není2")
        break


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
                        while True:
                            pokracovani = input("Stiskni Enter pro pokračování: ")
                            if pokracovani.strip() == "":
                                location.remove("air_drop")
                                location.append("shipwreck")
                                print("")
                                break
                            if pokracovani.strip() != "":
                                print("Zkus to znovu.")
                        break
                    elif nevim == 2:
                        print("Vydáš se na pláž.")
                        print("")
                        while True:
                            pokracovani = input("Stiskni Enter pro pokračování: ")
                            if pokracovani.strip() == "":
                                location.remove("air_drop")
                                location.append("villa_front")
                                print("")
                                break
                            if pokracovani.strip() != "":
                                print("Zkus to znovu.")
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
                    while True:
                        pokracovani = input("Stiskni Enter pro pokračování: ")
                        if pokracovani.strip() == "":
                            location.remove("air_drop_close")
                            location.append("shipwreck")
                            print("")
                            break
                        if pokracovani.strip() != "":
                            print("Zkus to znovu.")
                    break
                elif nevim == 2:
                    print("Vydáš se na pláž.")
                    print("")
                    while True:
                        pokracovani = input("Stiskni Enter pro pokračování: ")
                        if pokracovani.strip() == "":
                            location.remove("air_drop_close")
                            location.append("villa_front")
                            print("")
                            break
                        if pokracovani.strip() != "":
                            print("Zkus to znovu.")
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
                    while True:
                        pokracovani = input("Stiskni Enter pro pokračování: ")
                        if pokracovani.strip() == "":
                            location.remove("air_drop_close")
                            location.append("shipwreck")
                            print("")
                            break
                        if pokracovani.strip() != "":
                            print("Zkus to znovu.")
                    break
                elif nevim == 2:
                    print("Vydáš se na pláž.")
                    print("")
                    while True:
                        pokracovani = input("Stiskni Enter pro pokračování: ")
                        if pokracovani.strip() == "":
                            location.remove("air_drop_close")
                            location.append("villa_front")
                            print("")
                            break
                        if pokracovani.strip() != "":
                            print("Zkus to znovu.")
                    break
                else:
                    print("Zadal si špatnou odpověď. Správné odpovědi jsou [1 - vrak lodi, 2 - pláž].")
                    print("")
    
    
    if "villa_front" in location:
        print("test2")
        break