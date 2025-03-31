import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Mot de passe admin (à changer selon ton besoin)
ADMIN_PASSWORD = "admin123"

# Fonction pour vérifier le mot de passe
def verifier_connexion():
    password = entry_password.get()
    
    if password == ADMIN_PASSWORD:
        window_login.destroy()  # Ferme la fenêtre de connexion
        ouvrir_application()    # Ouvre l'application
    else:
        messagebox.showerror("Erreur", "Mot de passe incorrect.")

# Fonction pour afficher l'application après connexion
def ouvrir_application():
    global root  # Utilisation de la variable root dans toute l'application
    root = tk.Tk()
    root.title("Inscription des élèves")
    root.geometry("600x550")
    root.configure(bg="#1e1e1e")

    # Création de la base de données
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
            afficher_eleves()
        else:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs correctement.")

    # Fonction pour afficher les élèves
    def afficher_eleves():
        for row in tree.get_children():
            tree.delete(row)
        cursor.execute("SELECT * FROM eleves")
        for row in cursor.fetchall():
            tree.insert("", tk.END, values=row)

    # Interface graphique principale
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

    # Tableau des élèves
    tree_frame = tk.Frame(root, bg="#1e1e1e")
    tree_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

    columns = ("ID", "Nom", "Prénom", "Âge", "Classe")
    tree = ttk.Treeview(tree_frame, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=tk.CENTER, width=100)

    tree.pack(fill=tk.BOTH, expand=True)

    afficher_eleves()

    root.mainloop()

    # Fermeture de la connexion à la base de données
    conn.close()

# Création de la fenêtre de connexion
window_login = tk.Tk()
window_login.title("Page de Connexion")
window_login.geometry("400x200")
window_login.configure(bg="#1e1e1e")

login_frame = tk.Frame(window_login, bg="#2e2e2e", bd=5, relief=tk.RIDGE)
login_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

# Champ de mot de passe
label_password = tk.Label(login_frame, text="Mot de passe", bg="#2e2e2e", fg="white", font=("Arial", 12, "bold"))
label_password.pack(pady=5)

entry_password = tk.Entry(login_frame, font=("Arial", 12), bg="#3e3e3e", fg="white", insertbackground="white", relief=tk.GROOVE, bd=3, show="*")
entry_password.pack(pady=10, ipadx=5, ipady=5, fill=tk.X)

# Bouton de connexion
btn_connexion = tk.Button(login_frame, text="Se connecter", command=verifier_connexion, font=("Arial", 12, "bold"), bg="#2196F3", fg="white", relief=tk.RAISED, bd=3)
btn_connexion.pack(pady=10)

window_login.mainloop()
