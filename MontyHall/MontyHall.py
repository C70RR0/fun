# Monty Hall Problem
# https://en.wikipedia.org/wiki/Monty_Hall_problem
# I wanto to verify the assumption with a great number of tests, and Yes, it works!

import random

NUM_SIMULAZIONI = 100000
successi = 0

for _ in range(NUM_SIMULAZIONI):
    # Posizione della macchina
    auto = random.randint(0, 2)

    # Scelta iniziale dell'utente
    scelta_iniziale = random.randint(0, 2)

    # Il sistema apre una porta con una capra:
    # deve essere diversa dalla scelta iniziale e non contenere l'auto.
    porte = [0, 1, 2]
    porte_possibili_da_mostrare = [
        p for p in porte if p != scelta_iniziale and p != auto
    ]
    porta_mostrata = random.choice(porte_possibili_da_mostrare)

    # L'utente cambia sempre scelta → prende l'unica porta rimasta
    porte_rimanenti = [
        p for p in porte if p != scelta_iniziale and p != porta_mostrata
    ]
    nuova_scelta = porte_rimanenti[0]

    # Verifica se ha vinto
    if nuova_scelta == auto:
        successi += 1

percentuale = (successi / NUM_SIMULAZIONI) * 100

print(f"Simulazioni eseguite: {NUM_SIMULAZIONI}")
print(f"Successi cambiando sempre scelta: {percentuale:.2f}%")
