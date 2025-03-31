import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import re

# Mot de passe admin
ADMIN_PASSWORD = "admin123"

def verifier_connexion():
    if entry_password.get() == ADMIN_PASSWORD:
        fenetre_connexion.destroy()
        lancer_application()
    else:
        messagebox.showerror("Erreur", "Mot de passe incorrect")

def afficher_fenetre_connexion():
    global fenetre_connexion, entry_password
    fenetre_connexion = tk.Tk()
    fenetre_connexion.title("Connexion Admin")
    fenetre_connexion.geometry("400x200")
    fenetre_connexion.configure(bg="#2e2e2e")
    
    label = tk.Label(fenetre_connexion, text="Mot de passe Admin", bg="#2e2e2e", fg="white", font=("Arial", 12, "bold"))
    label.pack(pady=20)
    
    entry_password = tk.Entry(fenetre_connexion, show="*", font=("Arial", 12), bg="#3e3e3e", fg="white", insertbackground="white")
    entry_password.pack(pady=10, ipadx=5, ipady=5)
    
    btn_login = tk.Button(fenetre_connexion, text="Connexion", command=verifier_connexion, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white")
    btn_login.pack(pady=10)
    
    fenetre_connexion.mainloop()

def lancer_application():
    global root, tree, conn, cursor, entry_nom, entry_prenom, entry_age, entry_date_naissance, entry_adresse, entry_sexe, entry_nom_parents, entry_classe
    
    conn = sqlite3.connect("eleves.db")
    cursor = conn.cursor()

    # Vérification des colonnes existantes et ajout de colonnes si nécessaire
    cursor.execute("PRAGMA table_info(eleves)")
    columns = [column[1] for column in cursor.fetchall()]
    
    # Ajout des colonnes manquantes
    if 'date_naissance' not in columns:
        cursor.execute('ALTER TABLE eleves ADD COLUMN date_naissance TEXT')
    if 'adresse' not in columns:
        cursor.execute('ALTER TABLE eleves ADD COLUMN adresse TEXT')
    if 'sexe' not in columns:
        cursor.execute('ALTER TABLE eleves ADD COLUMN sexe TEXT')
    if 'nom_parents' not in columns:
        cursor.execute('ALTER TABLE eleves ADD COLUMN nom_parents TEXT')
    if 'classe' not in columns:
        cursor.execute('ALTER TABLE eleves ADD COLUMN classe TEXT')

    conn.commit()

    root = tk.Tk()
    root.title("Inscription des élèves")
    root.geometry("900x600")
    root.configure(bg="#1e1e1e")

    frame = tk.Frame(root, bg="#2e2e2e", bd=5, relief=tk.RIDGE)
    frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

    title_label = tk.Label(frame, text="Inscription des Élèves", bg="#2e2e2e", fg="white", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    form_frame = tk.Frame(frame, bg="#2e2e2e")
    form_frame.pack(pady=10, padx=20)

    labels = ["Nom", "Prénom", "Âge", "Date de Naissance", "Adresse", "Sexe", "Nom des Parents", "Classe"]
    entries = []
    for i, label in enumerate(labels):
        tk.Label(form_frame, text=label, bg="#2e2e2e", fg="white").grid(row=i, column=0, pady=5, padx=5, sticky=tk.W)
        entry = tk.Entry(form_frame, bg="#3e3e3e", fg="white")
        entry.grid(row=i, column=1, pady=5, padx=5)
        entries.append(entry)

    entry_nom, entry_prenom, entry_age, entry_date_naissance, entry_adresse, entry_sexe, entry_nom_parents, entry_classe = entries

    btn_frame = tk.Frame(frame, bg="#2e2e2e")
    btn_frame.pack(pady=10, fill=tk.X)

    tree_frame = tk.Frame(frame, bg="#1e1e1e")
    tree_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

    columns = ("ID", "Nom", "Prénom", "Âge", "Date de Naissance", "Adresse", "Sexe", "Nom des parents", "Classe")
    tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=tk.CENTER, width=80)

    scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    tree.pack(fill=tk.BOTH, expand=True)

    def valider_date(date_naissance):
        # Vérifie si la date est au format YYYY-MM-DD
        pattern = r"^\d{4}-\d{2}-\d{2}$"
        if re.match(pattern, date_naissance):
            return True
        return False

    def ajouter_eleve():
        try:
            nom = entry_nom.get()
            prenom = entry_prenom.get()
            age = entry_age.get()
            date_naissance = entry_date_naissance.get()
            adresse = entry_adresse.get()
            sexe = entry_sexe.get()
            nom_parents = entry_nom_parents.get()
            classe = entry_classe.get()
            
            if nom and prenom and age.isdigit() and date_naissance and valider_date(date_naissance) and adresse and sexe and nom_parents and classe:
                cursor.execute("INSERT INTO eleves (nom, prenom, age, date_naissance, adresse, sexe, nom_parents, classe) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                               (nom, prenom, int(age), date_naissance, adresse, sexe, nom_parents, classe))
                conn.commit()
                messagebox.showinfo("Succès", "Élève ajouté avec succès !")
                afficher_eleves()
            else:
                messagebox.showerror("Erreur", "Veuillez remplir tous les champs correctement.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue : {str(e)}")

    def afficher_eleves():
        for row in tree.get_children():
            tree.delete(row)
        cursor.execute("SELECT * FROM eleves")
        for row in cursor.fetchall():
            tree.insert("", tk.END, values=row)

    def deconnexion():
        root.destroy()
        afficher_fenetre_connexion()

    btn_ajouter = tk.Button(btn_frame, text="Ajouter", command=ajouter_eleve, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white")
    btn_ajouter.pack(side=tk.LEFT, padx=10, ipadx=10, ipady=5)

    btn_afficher = tk.Button(btn_frame, text="Afficher", command=afficher_eleves, font=("Arial", 12, "bold"), bg="#2196F3", fg="white")
    btn_afficher.pack(side=tk.LEFT, padx=10, ipadx=10, ipady=5)

    btn_deconnexion = tk.Button(btn_frame, text="Déconnexion", command=deconnexion, font=("Arial", 12, "bold"), bg="#f44336", fg="white")
    btn_deconnexion.pack(side=tk.LEFT, padx=10, ipadx=10, ipady=5)

    afficher_eleves()
    root.mainloop()
    conn.close()

# Lancer la page de connexion
afficher_fenetre_connexion()
