prosjek_ocjena = 3.8
rezultat_testa = 66

if prosjek_ocjena >= 3.5:
    if rezultat_testa > 65:
        print("Ispunjavate uslove za punu stipendiju!")
    elif rezultat_testa >= 50:
        print("Ispunjavate uslove za djelomičnu stipendiju.")
    else:
        print("Ne ispunjavate uslove za stipendiju.")