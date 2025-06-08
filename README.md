# Uploader-de-Webshell-PHP-Automatis-

Uploader de Webshell PHP Automatisé

Script Python pour uploader une webshell PHP sur un serveur vulnérable via un gestionnaire de fichiers (File Manager).

Fonctionnalités
✔ Connexion automatique avec gestion de token CSRF
✔ Upload furtif d'une webshell simple (system($_GET['cmd']))
✔ Détection de réussite et affichage du lien d'accès
Utilisation
 1 Modifiez la cible (TARGET), identifiants (USERNAME/PASSWORD) et chemin (UPLOAD_PATH)
 2 Exécutez :
bash


python3 upload_shell_php.py


 3 La webshell sera disponible à l'URL indiquée (test via curl).
Cas d'usage
 • Tests de pénétration légitimes (avec autorisation)
 • Récupération d'accès sur un système compromis
⚠ À utiliser uniquement à des fins légales et éthiques.

Code optimisé : Gestion de session, détection d'erreurs et sortie claire.
🔗 Testé sur : File Manager PHP vulnérables (ex: TinyFileManager).

#Pentesting #WebSecurity #RedTeam
