# Mirori_ACQ

### Programme d'acquisition - FR

## INSTALLATION
`sudo apt install libopencv-dev python3-opencv`<br>

`python3 pip install`<br>
ou<br>
`wget https://bootstrap.pypa.io/get-pip.py`
`sudo python3 get-pip.py && rm get-pip.py`<br>

`pip install face-recognition`<br>
`pip install python-dotenv`<br>
`pip install paramiko`<br>
`pip install scp`<br>
`pip install numpy`<br>

## LANCEMENT DE L'ACQUISITION :

Une fois dans le dossier du projet, vous pouvez executer les commandes suivantes:

`python3 index.py your@email.address`<br>
ou<br>
`python3 index.py #l'email vous seras demandé dans la console`


Une fois les librairies chargé par le script et une fois l'email renseigné, votre caméra devrait s'allumer, vous aurez 2 choix possibles ***"ESC"*** ou ***"SPACE BAR"*** pour la touche ***"échap"*** et ***"espace"*** de
votre clavier.

Si l'image de référence vous parait cadré correctement, vous pouvez appuyer sur la barre d'espace.

La touche échap sert à annuler et quitter le programme.

#### Attention aux problèmes de droit des dossiers, fichiers
### Si l'image de référence n'est pas "correcte" et que vous avez appuyé sur "espace" par inadvertance, relancé simplement le programme, la nouvelle photo écrasera la précédente
