import random


ssp = ["sten", "sax", "påse"]

while True:
    val = random.choice(ssp)

    print("sten, sax eller påse?")
    mit_val = input()

    if mit_val not in ssp:
        print("Välj sten, sax eller påse!")

    while True:


        if val == mit_val:
            print(F"Du tog {mit_val} och datorn tog {val} så det blir lika")

        elif mit_val == "sten":
            if val == "sax":
                print("Du van!")
            else:
                print("Du förlorade")

        elif mit_val == "påse":
            if val == "sten":
                print("Du van!")
            else:
                print("Du förlorade")
            
        elif mit_val == "sax":
            if val == "påse":
                print("Du van!")
            else:
                print("Du förlorade!")



        break




