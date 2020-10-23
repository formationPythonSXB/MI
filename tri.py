def plus_petit(tab):

    petit = None

    for i in range(len(tab)):
        if i == 0 or tab[i] < petit:
            petit = tab[i]

    return petit


def tri(liste):
    listeTriee = []

    for i in range(len(liste)):
        petit = plus_petit(liste)
        listeTriee.append(petit)
        liste.remove(petit)

    return listeTriee


print(tri([5, -21, 22, 0, -5, 98, 77, 4]))
