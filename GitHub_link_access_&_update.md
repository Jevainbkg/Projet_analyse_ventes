_Commande servant à créer, lier et modfifier son repo github depuis son accès local_

🧠 1. git init

# > git init

👉 Tu as transformé ton dossier en projet Git

📌 Traduction :

“Commence à suivre les modifications de ce dossier”

📦 2. git add .

# > git add .

👉 Tu ajoutes tous les fichiers à la zone de préparation

📌 Traduction :

“Prépare ces fichiers pour être enregistrés”

💡 Important :

ça ne sauvegarde pas encore
ça prépare juste
📸 3. git commit -m "First commit"

# > git commit -m "First commit"

👉 Tu crées une version sauvegardée de ton projet

📌 Traduction :

“Enregistre l’état actuel du projet avec ce message”

💡 Un commit = une photo du projet

🌿 4. git branch -M main

# > git branch -M main

👉 Tu renommes ta branche en main

📌 Traduction :

“La branche principale s’appelle main”

💡 Aujourd’hui :

main = standard
master = ancien
🔗 5. git remote add origin ...

# > git remote add origin https://github.com/Jevainbkg/Projet_analyse_ventes.git

👉 Tu relies ton projet local à GitHub

📌 Traduction :

“Mon dépôt GitHub s’appelle origin”

💡 origin = nom du dépôt distant (par défaut)

🔍 6. git remote -v

# > git remote -v

👉 Tu vérifies les liens avec GitHub

📌 Traduction :

“Montre-moi où mon projet est connecté”

🔄 7. git remote set-url origin ...

# > git remote set-url origin https://github.com/Jevainbkg/Projet_analyse_ventes.git

👉 Tu corriges l’URL du dépôt

📌 Traduction :

“Change le lien vers GitHub”

🚀 8. git push -u origin main

# > git push -u origin main

👉 Tu envoies ton projet sur GitHub

📌 Traduction :

“Envoie ma branche main vers GitHub”

💡 -u :

lie ta branche locale à GitHub
ensuite tu peux juste faire git push
⛔ 9. Erreur rencontrée → rejected (fetch first)

👉 Git t’a dit :

“GitHub a déjà des fichiers que tu n’as pas”

🔄 10. git pull origin main --allow-unrelated-histories

# > git pull origin main --allow-unrelated-histories

👉 Tu récupères ce qu’il y a sur GitHub

📌 Traduction :

“Fusionne mon projet avec celui de GitHub”

💡 Pourquoi ?

deux projets séparés
Git refuse de fusionner sans autorisation
🔁 11. git push

# > git push

👉 Tu envoies les modifications

📌 Traduction :

“Met à jour GitHub avec mes changements”

📊 BONUS (très utiles que tu as utilisés ou devrais utiliser)
🔍 git status

# > git status

👉 Voir l’état du projet

🧾 git log --oneline

# > git log --oneline

👉 Voir l’historique des commits

📥 git pull

# > git pull

👉 Récupérer les modifications depuis GitHub

Et une fois ayant apporté des modifications en local, pour synchroniser il suffit de faire

# > git add .

# > git commit -m "comment commit"

# > git pull

# > git push
