from random import randint as rand
intrebari=[
    ['Matematica',
    'Dacă un triunghi are un unghi de 60 de grade şi un alt unghi de 90 de grade, câte grade are al treilea unghi?',
    'Cu cât este egal 90 : 10',
    'Rezolva ecuatia: x^2=4',
    'Daca tai un segment in 8 locuri, cate segmente obtii?',
    'Cate numere sunt de la 45 la 76?',
    'Cate numere cuprinse intre 10 si 30 se impart la 3?',
    'Daca intr-un cos am 12 mere si manac 4 dintre ele, iar lui Andrei ii ofer doua cadou. Cu cate mare raman?',
    'In curtea casei sunt 4 motani negri, 2 gaini, un porumbel si un caine. Cate picioare sunt in total?',
    'Care este formula ariei patratului?',
    'Continuați șirul de numere: 17, 9, 16, 10, 15, 11, ___, ___.'
    ],
    ['Biologie',
    'Care este cel mai mare organ al corpului uman?',
    'Ce parte a corpului uman este mandibula?',
    'Câte oase are un om adult?',
    'În ce an a fost clonat primul animal?',
    'Cine a descoperit penicilina?',
    'Câte vertebre ale gâtului au girafele, în comparație cu cele șapte ale unui om?',
    'Care este numele celei mai mari părți a creierului uman?',
    'Boala Hansen este mai frecvent cunoscută sub ce nume?',
    'Când a fost finalizat proiectul genomului uman?',
    'Câte specii se estimează că trăiesc pe Pământ?',
    ],
    ['Geografie',
    'Care este cel mai lung fluviu din Europa?',
    'Câte continente există pe Pământ?',
    'Cine a realizat prima călătorie în jurul lumii?',
    'Spune trei țări prin care trece Ecuatorul?',
    'Câte state are Statele Unite ale Americii?',
    'În ce capitală europeană poți vizita Colosseum?',
    'Care este cel mai înalt munte de pe Glob?',
    'Care este capitale Moldovei?',
    'Cu ce state se invecineaza Moldova?',
    'De unde izvoraste Dunarea?',
    ],
    ['Istoria',
    'Ce grad de rudenie este între Carol al II-lea și Ferdinand I?',
    'În ce țară s-a născut Adolf Hitler? ',
    'În ce oraș au fost executați soții Ceaușescu? ',
    'În ce an a reușit Mihai Viteazul unirea celor trei mari țări medievale?',
    'Cand s-a inceput primul razboi mondial?',
    'Ce naționalitate are Papa Francisc I?',
    'În ce an a murit Prințesa Diana? ',
    'În ce an a intrat România în Uniunea Europeana? ',
    'Când a avut loc al doilea Război Mondial? ', 
    'În ce an s-a proclamat independența de stat a Moldovei',
    ],
    ['Limba romana',
    'Câte strofe are poezia “Luceafărul” de Mihai Eminescu?',
    'Cine a scris romanul “Ion”?',
    'Unde s-a născut Ion Creangă?',
    'Cine a scris poezia “Repetabila povară”? ',
    'Cine a scris “Enigma Otilei”?',
    'Cine a scris versurile imnului nostru?',
    'Ce poet a ocupat funcția de Ministru al Culturii? ',
    'Ce poet avea profesia de medic?',
    'Cine poet a scris poezia “Plumb”? ',
    'În ce oraș a murit Nichita Stănescu?',
    ]
    
    ]
raspunsuri=[['','30','9','2','9','29','6','6','26','a^2','14 12'],
            ['','Piele','Jawbone inferior','206','1996','Alexander Fleming','7','Cerebrul','Lepră','2003','8,7 milioane',],
            ['','Volga','7','Feredenando Magelan','Ecuador, Brazilia, Kenya','50','Roma','Everest','Chisinau','Romania Ucraina','Germania'],
            ['','tata si fiu','Ausria','Targoviste','1600','1914','argentinian','1997','2007','1939','1992'],
            ['','98','Liviu Rebreanu','Humulesti','Adrian Paunescu','George Calinescu','Alexe Mateevici','Marin Sorescu','Vasile Voiculescu','George Bacovia','Bucuresti'],]

def vrea_sa_fiu_milionar():
    i=0
    categoria=rand(0,4)
    intrebare=rand(1,10)
    intreb_asked=[]
    print('Categoria: ',intrebari[categoria][0])  
    while i<10:
        i=i+1
        while intrebare in intreb_asked:
            intrebare=rand(1,10)
        intreb_asked.append(intrebare)
        print(intrebari[categoria][intrebare]) 
        answer = input('Raspunsul: ')
        if answer in raspunsuri[categoria][intrebare]:
            print('Raspunsul e correct.')
        else:
            print('Gresiiitt!!!! Raspunsul corect este: ',raspunsuri[categoria][intrebare],'\n')
    return print('Felicitari, ati finalizat joaca!')
vrea_sa_fiu_milionar()