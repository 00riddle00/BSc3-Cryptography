

# Kolio turinys (ką dėstytojas sakė per paskaitą, užrašai iš sąsiuvino)

## Reference
... - 3 taškai reiškia, kad užsirašiau, bet nelabai supratau kas apie tai ten buvo, arba nespėjau užsirašyti,
arba dar kažkas, kas neaišku liko (nes greitai kalbėjo dėstytojas).

## Teorija

* Teoremų įrodymų nebus

* Parašyti būtinas ir pakankamas minimumo sąlygos

* Aprašyti algoritmą
	
	** Pavyzdys: Aprašykite Niutono metodą

		Niutono metodas - realiai viena formulė tik iteratyvi.
		(Pradedame nuo 1 taško, ir kartojame, kol sąlygas tenkins (kai "norma" bus mažesnė už kažką ar kitkas kas nors))

		Kokios būtinosios/pakankamosios minimumo sąlygos?

		Kaip jas rasti (sąlygas ar tenkina?) -> Darom žingsnį, aproksimuojame, ...
			Pvz. Jei tikslo f-ja kvadratinė, jos išvestinė - tiesinė, tai tik 1 žingsnį atliekame (arba kartojame tą žingsnį)

			Galima kita interpretacija - išvestinė, ...globaliai..., tada žengiame į kvadratinę funkciją, ..., jei ne, kartotumėme, ...

	** Pavyzdys: Gradientinis nusileidimas

		Ne tik parašyti formulę, bet ir kodėl, paaiškinti. T.y. judame ta kryptimi, kurlink f-ja mažėja. Ir daugiklis yra formulėje, tai paaiškinti, ką jis reiškia, kad reikia jį įsistatyti, ir vis kartoti.

* Palyginti algoritmus
	
	** Pvz. panašūs algoritmai - Gradientinis nusileidimas (GD) ir Greičiausias nusileidimas (SD)

		Panašumai: Jų žingsnis yra gradiento kryptimi.

		Skirtumai: GD pastovų daugiklį turi, o SD - prisiderina daugiklį. Parašyti, kad SD mažiau iteracijų atlieka, tačiau tas prisiderinimas (t.y. daugiklio radimas minimizuojant vienmatę tikslo f-ją pasirinktu algoritmu iš 1-ojo laboro) kiekvieną iteraciją taip pat reikalauja resursų.

* Globalusis optimizavimas (bet neaišku ar bus kažkas iš jo, nebet labai general teorija, nes labai trumpai jį užkabinome per teoriją)

## Uždaviniai

* Analitiškai išspręsti optimizavimo uždavinį (naudojant Būtinas ir Pakankamas minimumo sąlgyas)

* Kelis žingsnius kokio nors algoritmo padaryti 

	Dauguma tų algoritmų - tiesiog viena formulė, tai užduotis "nesudėtinga"

	1 kintamasis - Auksinis Pjūvis, Dalijimas Pusiau, Niutono Metodas
	>1 kintamasis - GD, SD, Deformuojamas Simplexas (ir paprastas turbūt Simpleksas?), taip pat
	Niutono metodas daugiamatei funkcijai (šito nedarėme per pratybas, bet reikia žinoti kaip suprantu, čia biškį hardcore turbūt)
	