


name = input("Vad heter du? ")

svar = input(f"Hej, {name} Om du vill köra en frågeposert klicka ENTER om du inte vill köra klicka x: ").lower()

scoore = 0


gameover = True 



while gameover:


    if svar == "":
        print("OKej då kör vi")
    elif svar == "x":
        gameover = False

    fråga1 = input("Vad blir en kickflip + 360 shuv?\n").lower()
    if fråga1 == "treflip":
        scoore += 1
        print(f"Rätt svar! Du har nu {scoore} poäng")
        break
        
    else:
        köraigen = input(f"Fel svar du har {scoore} poäng.\n Vill du testa frågan igen?\n ").lower()
        
        if köraigen == "ja":
            continue
        else:
            fråga1 == "treflip"
            break    
        

    
while gameover:
    
    fråga2 = input("Vad blir en kickflip + shuv?\n").lower()
    if fråga2 == "varialflip":
        scoore += 1
        print(f"Rätt svar! Du har nu {scoore} poäng")
        break
        
    else:
        köraigen = input(f"Fel svar du har {scoore} poäng.\n Vill du testa frågan igen? \n").lower()
        
        if köraigen == "ja":
            continue
        else:
            fråga1 == "varialflip"
            break    
        
            
        
        
while gameover:
    
    fråga3 = input("Vad blir hellflip + 360 shuv?\n").lower()
    if fråga3 == "laserflip":
        scoore += 1
        print(f"Rätt svar! Du har nu {scoore} poäng")
        break
        
    else:
        köraigen = input(f"Fel svar du har {scoore} poäng.\n Vill du testa frågan igen? \n").lower()
        
        if köraigen == "ja":
            continue
        else:
            fråga3 == "laserflip"
            
        
            break
        

while gameover:
        
    fråga4 = input("Vad blir en kickflip + frontshuv?\n").lower()
    if fråga4 == "hardflip":
        scoore += 1
        print(f"Rätt svar! Du har nu {scoore} poäng")
        break
        
    else:
        köraigen = input(f"Fel svar du har {scoore} poäng.\n Vill du testa frågan igen? \n").lower()
        
        if köraigen == "ja":
            continue
        else:
            fråga4 == "hardflip"
            
        
            break

print(f"Du fick {scoore} av 4 poäng")