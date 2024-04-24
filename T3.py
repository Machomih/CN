import tkinter as tk
from tkinter import simpledialog, messagebox

import numpy as np


# Exercițiul 1
def calculeaza_vector_b_cu_precizie(A, s, epsilon):
    b = np.dot(A, s)
    numar_zecimale = abs(int(np.floor(np.log10(epsilon))))
    b = np.around(b, decimals=numar_zecimale)
    return b


def executa_exercitiul_1():
    try:
        n = simpledialog.askinteger("Input", "Dimensiunea n a sistemului:", parent=root)
        if n is None:
            return
        A = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                A[i, j] = simpledialog.askfloat("Input", f"Elementul A[{i + 1}][{j + 1}]:", parent=root)
                if A[i, j] is None:
                    return
        s = np.zeros(n)
        for i in range(n):
            s[i] = simpledialog.askfloat("Input", f"Elementul s[{i + 1}]:", parent=root)
            if s[i] is None:
                return
        epsilon = simpledialog.askfloat("Input", "Precizia ε:", parent=root)
        if epsilon is None:
            return
        vector_b_precis = calculeaza_vector_b_cu_precizie(A, s, epsilon)
        messagebox.showinfo("Rezultat", f"Vectorul b este: {vector_b_precis}")
    except Exception as e:
        messagebox.showerror("Eroare", str(e))


# Exercițiul 2
def descompunere_qr_householder(A):
    (m, n) = np.shape(A)
    Q = np.eye(m)
    R = A.copy()
    for k in range(n - (m == n)):
        x = R[k:m, k]
        e = np.zeros_like(x)
        e[0] = np.copysign(np.linalg.norm(x), -A[k, k])
        u = x + e
        u = u / np.linalg.norm(u)
        R[k:m, k:n] -= 2.0 * np.outer(u, np.dot(u.T, R[k:m, k:n]))
        Q[:, k:m] -= 2.0 * np.outer(Q[:, k:m].dot(u), u)
    return Q, R


def executa_exercitiul_2():
    try:
        n = simpledialog.askinteger("Input", "Dimensiunea n a sistemului:", parent=root)
        if n is None:
            return
        A = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                A[i, j] = simpledialog.askfloat("Input", f"Elementul A[{i + 1}][{j + 1}]:", parent=root)
                if A[i, j] is None:
                    return
        Q, R = descompunere_qr_householder(A)
        messagebox.showinfo("Rezultat Q", f"Matricea Q este:\n{np.array_str(Q, precision=3)}")
        messagebox.showinfo("Rezultat R", f"Matricea R este:\n{np.array_str(R, precision=3)}")
    except Exception as e:
        messagebox.showerror("Eroare", str(e))


# Exercitiul 3


def rezolva_sistem_qr(A, b):
    Q, R = descompunere_qr_householder(A)
    Q_trans_b = np.dot(Q.T, b)
    x = np.linalg.solve(R, Q_trans_b)
    return x


# Cod pentru Exercițiul 3
def executa_exercitiul_3():
    try:
        n = simpledialog.askinteger("Input", "Dimensiunea n a sistemului:", parent=root)
        if n is None:
            return
        A = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                A[i, j] = simpledialog.askfloat("Input", f"Elementul A[{i + 1}][{j + 1}]:", parent=root)
                if A[i, j] is None:
                    return

        b = np.zeros(n)
        for i in range(n):
            b[i] = simpledialog.askfloat("Input", f"Elementul b[{i + 1}]:", parent=root)
            if b[i] is None:
                return

        x_qr = rezolva_sistem_qr(A, b)

        messagebox.showinfo("Rezultat x", f"Soluția x este:\n{x_qr}")

        Q_np, R_np = np.linalg.qr(A)
        x_householder = np.linalg.solve(R_np, np.dot(Q_np.T, b))
        eroare = np.linalg.norm(x_qr - x_householder)

        messagebox.showinfo("Eroare", f"Eroarea ||x_QR - x_Householder||₂ este: {eroare}")

    except Exception as e:
        messagebox.showerror("Eroare", str(e))


def executa_exercitiul_4():
    try:
        n = simpledialog.askinteger("Input", "Dimensiunea n a sistemului:", parent=root)
        if n is None:
            return

        A_init = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                A_init[i, j] = simpledialog.askfloat("Input", f"Elementul A[{i + 1}][{j + 1}]:", parent=root)
                if A_init[i, j] is None:
                    return

        b_init = np.zeros(n)
        for i in range(n):
            b_init[i] = simpledialog.askfloat("Input", f"Elementul b[{i + 1}]:", parent=root)
            if b_init[i] is None:
                return

        s = np.zeros(n)
        for i in range(n):
            s[i] = simpledialog.askfloat("Input", f"Elementul s[{i + 1}]:", parent=root)
            if s[i] is None:
                return

        Q_householder, R_householder = descompunere_qr_householder(A_init)
        x_householder = np.linalg.solve(R_householder, Q_householder.T @ b_init)

        Q_np, R_np = np.linalg.qr(A_init)
        x_qr = np.linalg.solve(R_np, Q_np.T @ b_init)

        eroare_Ax_minus_b_householder = np.linalg.norm(A_init @ x_householder - b_init, 2)
        eroare_Ax_minus_b_qr = np.linalg.norm(A_init @ x_qr - b_init, 2)
        eroare_xhouse_minus_s = np.linalg.norm(x_householder - s, 2) / np.linalg.norm(s, 2)
        eroare_xqr_minus_s = np.linalg.norm(x_qr - s, 2) / np.linalg.norm(s, 2)

        messagebox.showinfo("Erori Exercițiul 4",
                            f"Eroarea ||A^init * x_Householder - b^init||₂ este: {eroare_Ax_minus_b_householder:e}\n"
                            f"Eroarea ||A^init * x_QR - b^init||₂ este: {eroare_Ax_minus_b_qr:e}\n"
                            f"Eroarea ||x_Householder - s||₂ / ||s||₂ este: {eroare_xhouse_minus_s:e}\n"
                            f"Eroarea ||x_QR - s||₂ / ||s||₂ este: {eroare_xqr_minus_s:e}")

        if any(eroare > 1e-6 for eroare in
               [eroare_Ax_minus_b_householder, eroare_Ax_minus_b_qr, eroare_xhouse_minus_s, eroare_xqr_minus_s]):
            messagebox.showwarning("Avertizare", "Una sau mai multe erori nu sunt sub pragul de 10^-6.")

    except Exception as e:
        messagebox.showerror("Eroare", str(e))


# Exercițiul 5
def calculeaza_inversa_qr(A):
    # Calculăm descompunerea QR a lui A
    Q, R = descompunere_qr_householder(A)
    # Inițializăm inversa cu o matrice zero
    A_inv = np.zeros_like(A)
    # Rezolvăm sistemele liniare pentru fiecare coloană a identității
    for i in range(A.shape[0]):
        e = np.zeros(A.shape[0])
        e[i] = 1
        A_inv[:, i] = np.linalg.solve(R, Q.T @ e)
    return A_inv


def executa_exercitiul_5():
    try:
        n = simpledialog.askinteger("Input", "Dimensiunea n a sistemului:", parent=root)
        if n is None:
            return
        A = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                A[i, j] = simpledialog.askfloat("Input", f"Elementul A[{i + 1}][{j + 1}]:", parent=root)
                if A[i, j] is None:
                    return

        # Calculăm inversa folosind descompunerea QR
        A_inv_qr = calculeaza_inversa_qr(A)

        # Calculăm inversa folosind numpy
        A_inv_np = np.linalg.inv(A)

        # Calculăm și afișăm norma diferentței dintre cele două inverse
        norma_diferenta = np.linalg.norm(A_inv_qr - A_inv_np)

        messagebox.showinfo("Inversa matricei A",
                            f"Norma diferentței dintre inversa calculată cu QR și cea din NumPy este: {norma_diferenta:e}")
    except Exception as e:
        messagebox.showerror("Eroare", str(e))


def executa_exercitiul_6():
    n = simpledialog.askinteger("Input", "Introduceți dimensiunea n a sistemului:", parent=root)
    if n is None:  # Dacă utilizatorul anulează
        return

    # Inițializăm matricea A și vectorul b aleatoriu
    A = np.random.rand(n, n)
    b = np.random.rand(n)

    # Utilizăm funcțiile definite anterior pentru a calcula soluția și a afișa rezultatele
    try:
        # Calculăm soluția sistemului folosind metoda Householder
        x_householder = rezolva_sistem_qr(A, b)

        # Calculăm inversa matricei A folosind descompunerea QR
        A_inv = calculeaza_inversa_qr(A)

        # Calculăm inversa matricei A folosind NumPy
        A_inv_np = np.linalg.inv(A)

        # Calculăm norma diferenței dintre cele două inverse
        eroare_inversa = np.linalg.norm(A_inv - A_inv_np)

        messagebox.showinfo("Rezultat Exercițiul 6", f"Inversa matricei A folosind Householder:\n{A_inv}\n"
                                                     f"Inversa matricei A folosind numpy.linalg.inv:\n{A_inv_np}\n"
                                                     f"Norma diferenței între cele două inverse este: {eroare_inversa}")

    except np.linalg.LinAlgError as e:
        messagebox.showerror("Eroare", "A apărut o problemă la calculul inversei: " + str(e))


root = tk.Tk()
root.title("Exerciții Numerice")
root.geometry("400x300")

btn_ex1 = tk.Button(root, text="Exercițiul 1", command=executa_exercitiul_1)
btn_ex1.pack(pady=5)

btn_ex2 = tk.Button(root, text="Exercițiul 2", command=executa_exercitiul_2)
btn_ex2.pack(pady=5)

btn_ex3 = tk.Button(root, text="Exercițiul 3", command=executa_exercitiul_3)
btn_ex3.pack(pady=5)

btn_ex4 = tk.Button(root, text="Exercițiul 4", command=executa_exercitiul_4)
btn_ex4.pack(pady=5)

btn_ex5 = tk.Button(root, text="Exercițiul 5", command=executa_exercitiul_5)
btn_ex5.pack(pady=5)

btn_ex6 = tk.Button(root, text="Exercițiul 6", command=executa_exercitiul_6)
btn_ex6.pack(pady=5)

root.mainloop()
