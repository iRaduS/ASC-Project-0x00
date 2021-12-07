# Rezolvare partea a II-a
**Parola echipei adverse: xt987wdfdvKc**

[Repository echipa adversa](https://github.com/iuliali/xor-encryption)

# Introducere
**Cerința proiectului:** Scrieți scripturi python encrypt.py/decrypt.py care iau ca parametru în linia de comandă o cheie și un
fișier și realizează criptarea/decriptarea XOR folosind cheia dată. Programul va folosi cheia pentru a
cripta conținutul fișierului.

---

### Membrii echipei
**Florea George (grupa 142)** - responsabil pentru documentaţie

**Stanciu Sergiu-Nicolas (grupa 142)** - responsabil de testarea funcţionalităţii

**Teleagă Dragoş (grupa 142)** - responsabil pentru găsirea articolelor ce se regăsesc in partea dedicată a acestei documentaţii

**Vrînceanu Radu-Tudor (grupa 142)** - responsabil pentru git şi partea de cod

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
