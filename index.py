import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Création et connexion à la base de données
conn = sqlite3.connect("eleves.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS eleves (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT,
                    prenom TEXT,
                    age INTEGER,
                    classe TEXT)''')
conn.commit()

# Fonction pour ajouter un élève
def ajouter_eleve():
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    age = entry_age.get()
    classe = entry_classe.get()
    
    if nom and prenom and age.isdigit() and classe:
        cursor.execute("INSERT INTO eleves (nom, prenom, age, classe) VALUES (?, ?, ?, ?)",
                       (nom, prenom, int(age), classe))
        conn.commit()
        messagebox.showinfo("Succès", "Élève ajouté avec succès !")
        entry_nom.delete(0, tk.END)
        entry_prenom.delete(0, tk.END)
        entry_age.delete(0, tk.END)
        entry_classe.delete(0, tk.END)
    else:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs correctement.")

# Fonction pour afficher les élèves dans une nouvelle fenêtre
def afficher_eleves():
    fenetre_affichage = tk.Toplevel(root)
    fenetre_affichage.title("Liste des élèves")
    fenetre_affichage.geometry("500x300")
    
    tree_frame = tk.Frame(fenetre_affichage)
    tree_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
    
    columns = ("ID", "Nom", "Prénom", "Âge", "Classe")
    tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
    
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=tk.CENTER, width=100)
    
    tree.pack(fill=tk.BOTH, expand=True)
    
    cursor.execute("SELECT * FROM eleves")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)

# Interface graphique
root = tk.Tk()
root.title("Inscription des élèves")
root.geometry("600x550")
root.configure(bg="#1e1e1e")

# Style des widgets
frame = tk.Frame(root, bg="#2e2e2e", bd=5, relief=tk.RIDGE)
frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

def create_label(entry_frame, text):
    label = tk.Label(entry_frame, text=text, bg="#2e2e2e", fg="white", font=("Arial", 12, "bold"))
    label.pack(pady=5)
    return label

def create_entry(entry_frame):
    entry = tk.Entry(entry_frame, font=("Arial", 12), bg="#3e3e3e", fg="white", insertbackground="white", relief=tk.GROOVE, bd=3)
    entry.pack(pady=5, ipadx=5, ipady=5, fill=tk.X)
    return entry

title_label = tk.Label(frame, text="Inscription des Élèves", bg="#2e2e2e", fg="white", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

entry_frame = tk.Frame(frame, bg="#2e2e2e")
entry_frame.pack(pady=10)

create_label(entry_frame, "Nom:")
entry_nom = create_entry(entry_frame)

create_label(entry_frame, "Prénom:")
entry_prenom = create_entry(entry_frame)

create_label(entry_frame, "Âge:")
entry_age = create_entry(entry_frame)

create_label(entry_frame, "Classe:")
entry_classe = create_entry(entry_frame)

# Boutons
btn_frame = tk.Frame(frame, bg="#2e2e2e")
btn_frame.pack(pady=10)

btn_ajouter = tk.Button(btn_frame, text="Ajouter", command=ajouter_eleve, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief=tk.RAISED, bd=3)
btn_ajouter.grid(row=0, column=0, padx=5, ipadx=10, ipady=5)

btn_afficher = tk.Button(btn_frame, text="Afficher", command=afficher_eleves, font=("Arial", 12, "bold"), bg="#2196F3", fg="white", relief=tk.RAISED, bd=3)
btn_afficher.grid(row=0, column=1, padx=5, ipadx=10, ipady=5)

root.mainloop()

# Fermeture de la connexion à la base de données
conn.close()
