ZADANIE 3
scenariusz:
stowrzenie użytownika, 
zalogowanie,
usunięcie użytkownika. 

RAPORT testów . Generowany automatycznie. 
stowrzenie uzytkownika: createUser.py 
odpalenie testów:  pytest -v -s testHTML.py  
generowanie raportu z opisem błędów: pytest -v -s --capture sys -rP --capture sys -rF --html=report.html --self-contained-html testHTML.py
raport: raport.html

