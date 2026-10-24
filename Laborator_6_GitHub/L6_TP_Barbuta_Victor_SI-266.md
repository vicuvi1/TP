<div align="center">

MINISTERUL EDUCAȚIEI ȘI CERCETĂRII AL REPUBLICII MOLDOVA

UNIVERSITATEA TEHNICĂ A MOLDOVEI

Facultatea Calculatoare, Informatică și Microelectronică

<br>

**Raport la Lucrarea de laborator Nr. 6**

Disciplina: Tehnici de programare

Tema: **GitHub, pas cu pas**

<br>

</div>

**A efectuat:** st. gr. SI-266 Bărbuță Victor

**A verificat:** asistent universitar Cristian Gonceari

<div align="center">

<br>

Chișinău – 2026

</div>

---

## CUPRINS

- [DATE DE IDENTIFICARE](#date-de-identificare)
- [SCOPUL LUCRĂRII](#scopul-lucrarii)
- [MEDIUL DE LUCRU](#mediul-de-lucru)
- [ACTIVITĂȚILE REALIZATE](#activitatile-realizate)
- [REZULTATELE OBȚINUTE](#rezultatele-obtinute)
- [COMENZILE FOLOSITE](#comenzile-folosite)
- [GREȘELI ÎNTÂLNITE ȘI CE AM ÎNVĂȚAT](#greseli-intalnite)
- [CONCLUZII](#concluzii)
- [BIBLIOGRAFIE ȘI SURSE](#bibliografie-si-surse)

---

<a id="date-de-identificare"></a>

## DATE DE IDENTIFICARE

Datele mele și linkurile depozitelor sunt prezentate în tabelul 1.

**Tabelul 1 – Date de identificare și linkuri**

| Câmp | Valoare |
|---|---|
| Nume, prenume | Bărbuță Victor |
| Grupa | SI-266 |
| Username GitHub | vicuvi1 |
| Depozitul public 1 | https://github.com/vicuvi1/exercitiu-git |
| Depozitul public 2 | https://github.com/vicuvi1/exercitiu-2 |

---

<a id="scopul-lucrarii"></a>

## SCOPUL LUCRĂRII

Scopul lucrării a fost să învăț să lucrez cu git și GitHub de la zero. Am configurat git pe calculatorul meu și am creat două depozite publice de exercițiu, exercitiu-git și exercitiu-2. Am exersat cum salvez schimbările (commit), cum le trimit pe GitHub (push), cum aduc schimbările de pe GitHub (pull) și cum citesc istoria unui proiect (log, diff).

---

<a id="mediul-de-lucru"></a>

## MEDIUL DE LUCRU

Am lucrat individual, pe calculatorul meu. Am folosit:

- sistemul de operare Windows și terminalul PowerShell;
- programul git, versiunea 2.55.0.windows.5;
- GitHub CLI (gh), pe care git îl folosește pentru autentificarea la GitHub;
- editorul Visual Studio Code;
- limbajul Python, pentru fișierul salut.py și mediul virtual .venv;
- browserul, pentru contul GitHub și paginile depozitelor.

---

<a id="activitatile-realizate"></a>

## ACTIVITĂȚILE REALIZATE

Am făcut pașii A1–A10 în ordine, fără să sar peste vreunul. După fiecare comandă am comparat rezultatul din terminal cu ce cerea fișa. Ce am exersat la fiecare pas este prezentat în tabelul 2.

**Tabelul 2 – Ce am exersat la fiecare pas**

| Pas | Ce am exersat |
|---|---|
| A1 | Aveam deja cont GitHub cu numele de utilizator vicuvi1, așa că m-am autentificat în el și am trecut la pasul următor. |
| A2 | Am verificat că git este instalat cu `git --version` și m-am prezentat lui git cu `git config --global` (nume, e-mail, ramura implicită main și `pull.rebase false`), apoi am verificat setările cu `git config --global --list`. |
| A3 | Am creat pe GitHub depozitul public exercitiu-git, cu descrierea „Exercitii de git pentru Tehnici de programare” și cu fișierul README.md. |
| A4 | Am descărcat depozitul pe calculator cu `git clone` și am intrat în folderul exercitiu-git, de unde am dat toate comenzile git următoare. |
| A5 | Am creat fișierul salut.py din editor, am văzut cu `git status` că este „untracked”, l-am pregătit cu `git add` și am făcut primul meu commit, „Adaug salut.py”; rularea cu `python salut.py` a mers abia după ce am rezolvat eroarea „Python was not found”, descrisă în capitolul despre greșeli. |
| A6 | Am trimis commit-ul pe GitHub cu `git push`; nu mi s-a cerut autentificarea, fiindcă pe calculator aveam deja GitHub CLI autentificat, setat ca credential helper (se vede în `git config --global --list`), iar pe pagina depozitului a apărut salut.py. |
| A7 | Am modificat README.md direct pe GitHub, apoi am adus schimbarea pe calculator cu `git pull` și am verificat conținutul fișierului cu `type README.md`. |
| A8 | Am creat fișierul .gitignore cu regulile `.venv/` și `__pycache__/`, ca git să nu urce aceste foldere, și am trimis regula cu commit-ul „Ignor mediul virtual”; mediul virtual .venv l-am creat după ce am rezolvat problema cu Python, iar `git status` nu l-a mai arătat, fiindcă era ignorat. |
| A9 | Am citit istoria cu `git log --oneline`, am văzut o schimbare necomisă cu `git diff` și am întors fișierul salut.py la ultimul commit cu `git restore`, după care `git status` a afișat „nothing to commit, working tree clean”. |
| A10 | Am creat local depozitul exercitiu-2 cu `git init`, am făcut commit-ul „primul commit”, apoi l-am legat de un depozit nou de pe GitHub cu `git remote add origin` și l-am trimis cu `git push -u origin main`. |

---

<a id="rezultatele-obtinute"></a>

## REZULTATELE OBȚINUTE

La verificarea finală (pasul A11) am deschis ambele depozite în browser. Conținutul lor este prezentat în tabelul 3.

**Tabelul 3 – Conținutul depozitelor publice**

| Depozit | Vizibilitate | Fișiere | Commit-uri |
|---|---|---|---|
| exercitiu-git | Public | README.md, salut.py, .gitignore | 4 |
| exercitiu-2 | Public | README.md | 1 |

Istoria depozitelor, așa cum o afișează `git log --oneline`, este prezentată în tabelul 4.

**Tabelul 4 – Istoria commit-urilor**

| Depozit | Cod commit | Mesaj | Pasul |
|---|---|---|---|
| exercitiu-git | fa82d7d | Initial commit | A3 |
| exercitiu-git | ec215f4 | Adaug salut.py | A5–A6 |
| exercitiu-git | 463f5f7 | Add description to README.md | A7 |
| exercitiu-git | be0d7b9 | Ignor mediul virtual | A8 |
| exercitiu-2 | cadbef6 | primul commit | A10 |

Commit-ul „Initial commit” l-a creat GitHub când am bifat Add a README file. Commit-ul „Add description to README.md” l-am făcut din browser, la pasul A7, când am adăugat în README.md rândul „Aici exersez git.”. Rândul `print("al doilea")` de la pasul A9 nu apare în istorie, fiindcă l-am anulat cu `git restore` înainte de commit.

---

<a id="comenzile-folosite"></a>

## COMENZILE FOLOSITE

Comenzile git pe care le-am folosit și ce face fiecare sunt prezentate în tabelul 5.

**Tabelul 5 – Comenzile git folosite**

| Comanda | Ce face |
|---|---|
| `git --version` | afișează versiunea git instalată |
| `git config --global ...` | salvează numele, e-mailul și setările mele pentru toate depozitele |
| `git clone <adresă>` | descarcă prima dată un depozit de pe GitHub |
| `git status` | arată ce fișiere sunt noi, modificate sau pregătite pentru commit |
| `git add <fișier>` | pune fișierul în „fotografia” următoare (staging) |
| `git commit -m "mesaj"` | salvează o fotografie a proiectului, cu un mesaj |
| `git push` | trimite commit-urile de pe calculator pe GitHub |
| `git pull` | aduce pe calculator ce s-a schimbat pe GitHub |
| `git log --oneline` | arată istoria commit-urilor, câte unul pe rând |
| `git diff` | arată ce s-a schimbat față de ultimul commit |
| `git restore <fișier>` | întoarce fișierul la ultimul commit |
| `git init` | transformă un folder obișnuit într-un depozit git |
| `git remote add origin <adresă>` | leagă depozitul local de cel de pe GitHub |
| `git push -u origin main` | trimite ramura main prima dată și o leagă de origin/main |

---

<a id="greseli-intalnite"></a>

## GREȘELI ÎNTÂLNITE ȘI CE AM ÎNVĂȚAT

**Python nu pornea din terminal.** La pașii A5 și A8, comenzile `python salut.py` și `python -m venv .venv` au afișat „Python was not found; run without arguments to install from the Microsoft Store”. Am înțeles că în Windows comanda `python` ducea la o scurtătură spre Microsoft Store, nu la un Python instalat. Am instalat Python cu `winget install Python.Python.3.13`, am redeschis terminalul și am rulat din nou cele două comenzi. Programul a afișat „Salut, GitHub!”, iar .venv a fost creat. Fișierul salut.py era deja în commit, așa că nu a fost nevoie de un commit nou. Am învățat că git urmărește fișierele indiferent dacă programul rulează sau nu, iar un commit nu verifică dacă codul funcționează.

**Rândul „șters” din git diff.** La pasul A9, `git diff` mi-a arătat primul rând atât cu minus, cât și cu plus, deși eu doar adăugasem un rând. Mesajul „\ No newline at end of file” mi-a explicat cauza: primul rând nu avea Enter la sfârșit. Când am adăugat al doilea rând, rândul întâi a primit și el un sfârșit de rând, iar git l-a considerat schimbat.

---

<a id="concluzii"></a>

## CONCLUZII

În această lucrare am configurat git pe calculatorul meu și am creat două depozite publice. Primul, exercitiu-git, l-am pornit de pe GitHub și l-am clonat. Al doilea, exercitiu-2, l-am pornit de pe calculator cu `git init` și l-am urcat apoi pe GitHub.

Am înțeles că git ține istoria proiectului pe calculator, iar GitHub ține o copie a ei pe internet. Am învățat ciclul de bază: `git pull` înainte de lucru, apoi `git add`, `git commit` și `git push` după lucru. Am învățat și să citesc istoria cu `git log` și `git diff`, să anulez o schimbare cu `git restore` și să opresc fișierele inutile cu `.gitignore`.

Ca viitor specialist în securitate, am reținut că într-un depozit public nu se urcă niciodată parole, token-uri sau chei, iar .gitignore ajută și la asta.

---

<a id="bibliografie-si-surse"></a>

## BIBLIOGRAFIE ȘI SURSE

1. Fișa de laborator „Laboratorul 6. GitHub, pas cu pas”, Tehnici de programare, UTM, FCIM, 2026.
2. Git – Documentație oficială. Disponibil: https://git-scm.com/docs
3. GitHub Docs – Hello World / Getting started. Disponibil: https://docs.github.com/en/get-started
4. Pro Git, Scott Chacon și Ben Straub. Disponibil: https://git-scm.com/book/en/v2

Ajutor primit: am folosit asistentul AI Claude pentru a verifica pașii și pentru redactarea acestui raport. Toate comenzile le-am rulat eu, pe calculatorul meu.
