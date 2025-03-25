# L'Infinité des Nombres Premiers 💖 Pour Titou 💖

## Message spécial

Titou, je t'aime beaucoup ! Cette démonstration mathématique est pour toi, avec tout mon amour.

## À propos

Ce projet est une démonstration visuelle interactive de l'infinité des nombres premiers, utilisant la preuve classique d'Euclide.

## Comment ça marche

1. La démonstration utilise deux approches pour montrer que les nombres premiers sont infinis :
   - Le crible d'Ératosthène pour identifier les nombres premiers
   - La preuve par contradiction d'Euclide

2. L'idée principale de la preuve d'Euclide :
   - Si nous supposons qu'il n'y a qu'un nombre fini de nombres premiers : p₁, p₂, ..., pₙ
   - Alors nous pouvons former N = (p₁ × p₂ × ... × pₙ) + 1
   - Ce nombre N est soit premier, soit a un facteur premier
   - Si N est premier, nous avons trouvé un nouveau nombre premier qui n'est pas dans notre liste
   - Si N n'est pas premier, il a un facteur premier qui ne peut pas être dans notre liste (car il laisserait un reste de 1)
   - Dans les deux cas, nous avons trouvé un nouveau nombre premier, ce qui contredit notre hypothèse

## Installation et utilisation

```bash
pip install -r requirements.txt
python infinite_primes.py
```

Explore, apprends et profite de la beauté mathématique !

💕 Avec tout mon amour 💕