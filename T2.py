import numpy as np


def descompunere_LU(matrice, eps=1e-10):
    n = matrice.shape[0]  # dimensiunea matricei
    for k in range(n):
        if abs(matrice[k, k]) < eps:  # verifică dacă pivotul este suficient de mare
            raise ValueError("Pivotul prea mic => descompunerea LU nu poate fi realizată adecvat.")
        for i in range(k + 1, n):
            matrice[i, k] /= matrice[k, k]  # actualizează elementele L
            for j in range(k + 1, n):
                matrice[i, j] -= matrice[i, k] * matrice[k, j]  # actualizează elementele U

    print("\nMatricea L:")
    print(np.tril(matrice))
    print("\nMatricea U:")
    print(np.triu(matrice))
    return matrice  # A devine o matrice combinată L și U


# rezolvă sistemul Ax = b folosind descompunerea LU. Aici, A este deja descompusă în L și U.
def rezolva_sistem(matrice, b):
    n = b.size
    y = np.zeros(n)
    x = np.zeros(n)
    # rezolvare Ly = b pentru y folosind substitutie directa.
    for i in range(n):
        y[i] = b[i] - np.dot(matrice[i, :i], y[:i])
    # rezolvare Ux = y pentru x folosind substitutie inversa.
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(matrice[i, i + 1:], x[i + 1:])) / matrice[i, i]
    return x


# calculeaza determinantul matricei A folosind descompunerea LU. Aici, A este descompusa in L si U.
def calculeaza_determinant(matrice):
    n = matrice.shape[0]
    det = 1
    for i in range(n):  # produsul elementelor diagonale din L
        det *= matrice[i, i]
    return det


# calculează norma Euclidiană a diferentei dintre Ainit*x și binit.
def norma(Ainit, x, binit):
    return np.linalg.norm(np.dot(Ainit, x) - binit)


# functie pentru interfata grafica care preia inputurile, calculeaza descompunerea LU,
# rezolvă sistemul, si afisează rezultatele.
def realizare_descompunere():
    try:
        # transformare input in matrice si  array
        A = np.array(entry_A, dtype=float)
        b = np.array(entry_b, dtype=float)
        Ainit = np.copy(A)  # copie a matricei A pentru a pastra datele initiale
        binit = np.copy(b)  # copie a vectorului b pentru a pastra datele initiale
        A_LU = descompunere_LU(A)  # efectueaza descompunerea LU
        x = rezolva_sistem(A_LU, b)  # rezolva sistemul
        norma_sol = norma(Ainit, x, binit)  # calculeaza norma solutiei
        det_A = calculeaza_determinant(A_LU)  # calculeaza determinantul

        x_lib = np.linalg.solve(Ainit, binit)
        norma_comparata1 = np.linalg.norm(x - x_lib)
        Ainv_lib = np.linalg.inv(Ainit)
        norma_comparata2 = np.linalg.norm(x - np.dot(Ainv_lib, binit))

        print("Rezultat:",
          f"Soluția x: {x}\nDeterminantul A: {det_A}\nNorma soluției: {norma_sol}\nNorma diferenței xLU și xlib: {norma_comparata1}\nNorma diferenței xLU și A^-1*b: {norma_comparata2}")
    except Exception as e:
        print("Eroare", str(e))


entry_A = [[2.5, 2, 2], [5, 6, 5], [5, 6, 6.5]]
entry_b = [2, 2, 2]

realizare_descompunere()
