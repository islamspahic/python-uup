import collections

Student = collections.namedtuple("Student", "ime, prezime, indeks, prosek")

s1 = Student("Milan", "Tait", 2008213514, 9.5)
s4 = Student("Kerim", "Nezic", 2010213514, 9.4)

print( s1.indeks )

s2 = {
    "ime": "Milan",
    "prezime": "Tair",
    "indeks": 2008213514,
    "prosek": 9.5
}


s3 = {
    "ime": "Kerim",
    "prezime": "Nezic",
    "index": 2021213514,
    "prosek": 9.5
}
print( s4.indeks)
