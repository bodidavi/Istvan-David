nyertes = 45
nyertes1 = 32
nyertes2 = 16
nyertes3 = 76
nyertes4 = 57

elsolap = int(input("Adja meg az első részhez a tippjét."))

if nyertes == elsolap:
    print("Az első tipp sikeres.")
elif  elsolap > 90:
    print("A megadott szám helytelen.")
else:
    print("Az első tipp sikertelen.")
    
masodiklap = int(input("Adja meg a masodik részhez a tippjét."))

if nyertes1 == masodiklap:
    print("Az második tipp sikeres.")
elif  masodiklap > 90:
    print("A megadott szám helytelen.")
else:
    print("Az második tipp sikertelen.")
    
harmadiklap = int(input("Adja meg a harmadik részhez a tippjét."))

if nyertes2 == harmadiklap:
    print("A harmadik tipp sikeres.")
elif  harmadiklap > 90:
    print("A megadott szám helytelen.")
else:
    print("A harmadik tipp sikertelen.")

negyediklap = int(input("Adja meg a negyedik részhez a tippjét."))

if nyertes3 == negyediklap:
    print("A negyedik tipp sikeres.")
elif  negyediklap > 90:
    print("A megadott szám helytelen.")
else:
    print("A negyedik tipp sikertelen.")
    
otodiklap = int(input("Adja meg az ötödik részhez a tippjét."))

if nyertes4 == otodiklap:
    print("Az ötödik tipp sikeres.")
elif  otodiklap > 90:
    print("A megadott szám helytelen.")
else:
    print("Az ötödik tipp sikertelen.")
