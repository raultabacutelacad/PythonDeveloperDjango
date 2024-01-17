# PythonDeveloperDjango

Un lista de carti virtuala. 

Avem posibilitatea sa adaugam o carte in lista

Avem posibilitatea sa stergem o carte din lista

Avem posibilitatea sa editam o carte - o data ce a fost adaugate

Avem posibilitatea sa marcam o carte ca fiind citita 

Avem posibilitatea sa dam o nota pentru carte 

O carte are urmatoarele campuri: 
* titlu
* autor
* descriere
* citit - Boolean 
* rating - (0-5)
* imagini adaugate pentru o carte (extensie)

## Taskuri

## Sprint 1

1. Adaugarea modelului pentru Carte - Emanuela ✔️
   * Aici putem folosi structura Django - adaugarea in models, crearea unei migratii etc 
2. Template pe homepage pentru lista de carti- Alex
    * Construiti o lista de detalii fake pentru carti si afisati informatiile respective pe pagina radacina (homepage - / - root)
3. Template pentru adaugarea unei carti. - Dan
   * disponibil la /add/<id>
   * Ar trebui sa fie un formular ce contine urmatoarele campuri
     * titlu - input
     * autor - input
     * descriere - textarea
   * datele captate din formular sunt afisate la consola. 
4. Template pentru stergerea unei carti - Ioana
   * Sunt doua rute 
     * /delete/<id> - Afiseaza un mesaj de confirmare "Sunteti sigur ca vreti sa stergeti <x>"
       * Pentru "Nu" se intoarce inapoi la homepage
       * Pentru "Da" se redirecteaza catre /delete/confirm/<id>
     * /delete/confirm/<id>
       * Afiseaza un mesaj la consola
       * Redirecteaza catre homepage. 
5. Template pentru rating - Aura
   * Disponibil la /rate/<id>
     * Afiseaza un formular cu un dropdown
     * Dropdown contine 5 valori de la 1 la 5 stelute - se pot folosi emoji
     * Valoarea va fi un numar de la 1 la 5
     * La submit, valoarea este afisata la consola.
6. Template pentru marcarea unei carti ca fiind citita - Alexandu
   * Disponibil la /read/<id>
     * Doua butoane, Yes / No
     * No - > redirect catre homepage
     * Yes -> redirect catre /mark-as-read/<id>
   * mark-as-read/<id>
     * Afiseaza un mesaj la consola si face redirect catre homepage
7. Fisiere statice - Dana
  * Configurati Django sa poata folosi fisiere statice 
  * Urmati exemplul de configurare din curs. 
  * Fisierele statice vor fi disponbile la /static/<nume-fisier>

### Sprint 2
2. Template pe homepage pentru lista de carti- Alex
    * Construiti o lista de detalii fake pentru carti si afisati informatiile respective pe pagina radacina (homepage - / - root)
3. Template pentru adaugarea unei carti. - Dan
   * disponibil la /add/<id>
   * Ar trebui sa fie un formular ce contine urmatoarele campuri
     * titlu - input
     * autor - input
     * descriere - textarea
   * datele captate din formular sunt afisate la consola.
4. Template pentru stergerea unei carti - Ioana
   * Sunt doua rute 
     * /delete/<id> - Afiseaza un mesaj de confirmare "Sunteti sigur ca vreti sa stergeti <x>"
       * Pentru "Nu" se intoarce inapoi la homepage
       * Pentru "Da" se redirecteaza catre /delete/confirm/<id>
     * /delete/confirm/<id>
       * Afiseaza un mesaj la consola
       * Redirecteaza catre homepage.

5. Template pentru rating - Aura
   * Disponibil la /rate/<id>
     * Afiseaza un formular cu un dropdown
     * Dropdown contine 5 valori de la 1 la 5 stelute - se pot folosi emoji
     * Valoarea va fi un numar de la 1 la 5
     * La submit, valoarea este afisata la consola.
6. Template pentru marcarea unei carti ca fiind citita - Alexandu
   * Disponibil la /read/<id>
     * Doua butoane, Yes / No
     * No - > redirect catre homepage
     * Yes -> redirect catre /mark-as-read/<id>
   * mark-as-read/<id>
     * Afiseaza un mesaj la consola si face redirect catre homepage
7. Fisiere statice - Dana
  * Configurati Django sa poata folosi fisiere statice 
  * Urmati exemplul de configurare din curs. 
  * Fisierele statice vor fi disponbile la /static/<nume-fisier>
