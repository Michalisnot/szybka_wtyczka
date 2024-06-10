	Wtyczka została stworzona w celu liczenia przewyższenia dwóch zaznaczonych punktów,
lub pola figury składającej się z 3 lub więcej zaznaczonych punktów.

	Wymagania systemowe:
- program QGIS wersja 3.22 lub wyższa
- program Python wersja 3.9
- biblioteka PyQt5
- biblioteka qgis.core
- biblioteka qgis.utilis
- biblioteka qgis.pyqt

	Program został napisany dla systemu operacyjnego Windows 10 i Windows 11


	Sposób korzystania z wtyczki:
- Najpierw należy wybrać warstę na której chcemy zaznaczyć punkty, przy czym 
  wybrana warstwa musi mieć geometrię typu points. 

- Następnie w QGiS na wybranej powyżej warstwie należy zaznaczyć punkty, 
  dla których chce się wykonać obliczenia: 2 w przypadku różnicy wysokości,
  3 lub więcej w przypadku obliczenia pola powierzchni.

- W celu obliczenia przewyższenia należy klikąć przycisk "Oblicz dh"

- W celu obliczenia pola powirzchni należy klikąć przycisk "Oblicz area"

- Po uruchomieniu programu pojawi się okno wynikowe
  wynik pojawi się też w komórce obok przycisku

- Obliczone przewyższenia podawane są w metrach [m]

- Obliczone pola powierzchni podawane są w metrach kwadratowych [m^2]

- W celu zakończenia programu lub wykonania obliczeń
  dla innych punktów należy kliknąć przycisk "wyczyść" i powtórzyć całą proedurę.

	Zaobserwowane błędy:
- W przypadku wprowadzenia niepoprawnej ilości punktów (zbyt dużej lub zbyt małej), program 
  nie zostanie uruchomiony i pojawi się okno z komunikatem: "Niepoprawna ilosc punktow"
  informujący o ilości brakujących/nadmiarowych punktów.


