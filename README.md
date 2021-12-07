# Rezolvare partea a II-a

**Parola echipei adverse: xt987wdfdvKc**

[**three haXORs** - echipa adversă](https://github.com/iuliali/xor-encryption)

---

### Partea II.1 (preluarea parolei pe baza inputului)
Am folosit un script de python prin care am extras parola folosindu-ne de input şi de faptul ca XOR este comutativă, generând primele 30 de caractere din parolă, ştiind că dimensiunea maximă a parolei poate fi de 15 caractere, pentru verificarea corectitudinii.
```
input_byte ^ password_byte = output_byte => password_byte = input_file_byte ^ output_byte
```
Scriptul utilizat se găseşte în cadrul acestui repository şi se numeşte **cracker_with_input.py**.

---

### Partea II.2 (preluarea parolei doar pe baza outputului)
**Trust-Factor heuristic algorithm**

Pentru a eficientiza algoritmul de brute-force echipa noastră a propus sa se creeze cate un thread nou pentru fiecare lungime de parola de la 10-15 (în total 6 fire de execuţie). Fiecare thread porneşte cu o metodă care oferă o parolă pentru lungimea propusă **(!) Metoda folosită este una ESTIMATIVĂ, întrucât se bazează pe faptul că principalele caractere (sau cele majoritare) sunt litere mici şi bineînţeles anumite semne ortografice şi de punctuaţie**. Datorită faptului că ştim componenţa parolei (este formată din A-Za-z0-9 vom itera prin caracterele textului encriptat si prin **posibilele caractere** din parolă, la fiecare pas obţinându-se un **caracter pseudo-input**).

Acest **caracter pseudo-input** trebuie să se regăsească printre cele mai utilizate caractere. Dacă este cazul, atunci se incrementează într-o "frecvenţă" (care reţine pentru fiecare poziţie (caracter) din parolă şi fiecare caractere posibile trust factor-ul asociat pe criteriul menţionat anterior). La final pentru fiecare poziţie (caracter) din parolă se aleg cheile (caracterele) corespunzătoare maximelor locale din frecvenţa anterioară.

Scriptul utilizat se găseşte în cadrul acestui repository şi se numeşte **cracker_without_input.py**.

---

# Introducere
**Cerința proiectului:** Scrieți scripturi python encrypt.py/decrypt.py care iau ca parametru în linia de comandă o cheie și un
fișier și realizează criptarea/decriptarea XOR folosind cheia dată. Programul va folosi cheia pentru a
cripta conținutul fișierului.

---

### Membrii echipei
**Florea George (grupa 142)** - responsabil pentru documentaţie, contribuţii pe partea II.1

**Stanciu Sergiu-Nicolas (grupa 142)** - responsabil de testarea funcţionalităţii, contribuţii pe partea II.1

**Teleagă Dragoş (grupa 142)** - responsabil pentru găsirea articolelor ce se regăsesc in partea dedicată a acestei documentaţii, contribuţii pe partea II.2 (conceptul de trust-factor)

**Vrînceanu Radu-Tudor (grupa 142)** - responsabil pentru git şi partea de cod, contribuţii pe partea II.2 (ideea de paralelizare a algoritmului)

---

# Cum se utilizează
### Mediul de lucru
- Python 3.10.0
### Metode de rulare
Există două metode de rulare, prima şi cea mai colocvială ar fi rularea directă cu interpretorul de python
```
python3 project.py <parola> <nume_fisier_input> <nume_fisier_output>
```
Sau a doua metodă ce propune convertirea scriptului project.py într-un executabil
```
cp project.py project
chomd a+x project
./project <parola> <nume_fisier_input> <nume_fisier_output>
```
**ATENŢIE!** A doua metodă poate fi nefuncţională în funcţie de amplasarea interpretorului de python, întrucât am oferit o cale la începutul scriptului
```
#!/usr/bin/python3
```
Această linie trebuie editată conform cu output-ul comenzii
```
which python3
```

---

# Articole utilizate / alte documentaţii
- [Violent Python: XOR Encrypt](https://samsclass.info/124/proj14/VPxor.htm)
- [stackoverflow File Decryption with XOR](https://stackoverflow.com/questions/43025170/python-3-6-file-decryption-with-xor)
