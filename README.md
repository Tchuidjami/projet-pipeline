# projet pipeline
   Le projet a pour but de creer un pipeline de traitement video. Les videos sont stockees et sont traitees par un ensemble de conteneurs pour y extraire les metadonnees. les metadonnees et la video seront aggregees grace a des vms heberges dans aws et le resultat de la video doit etre accessible publiquement sur une page web.

# Notre pipeline
    - Nous avons crees deux conteneurs, le conteneur qui permet de compresser la video : docker run -d mycompression 
    et celui qui permet de sous titrer: docker run -d subtitle
    - Nous avons lances les deux conteneurs au meme moment grace a docker-compose en utilisant la commande ci: docker-compose -d
    - sur aws, nous avons envoyes les metadonnees generees par docker compose c'est a dire la video compressee, les soustitres egalement sur S3 disponible dans le bucket monaggregation
    - ensuite sur ec2, on a recuperer les metadonnees stockees sur s3 pour les aggreger (video_sous_titres.mp4)
    - on a stocke le resultat sur s3
    - on a cree une page qui permet d'afficher le resultat de la video, cette page c'est pageweb.html et sur cette page on a la video aggregee qu on a recupere dans s3 qui s'affiche.
  
# Comment tester notre pipeline sur votre machine
   - Nous avons commences par creer un conteneur qui compresse la video. pour tester sur votre machine vous allez mettre dans un meme dossier le dockerfile-c en renommant Dockerfile tout simplement,le code compression.py et la video souhaitee et vous allez executer les commandes suivantes: docker build -t macompression . et apres vous allez faire un docker run -d ma compression
   - conteneur qui permet de sous titrer, pour le tester c'est docker build -t monsubtitle . et docker run -d monsubtitle , mettre dockerfile-s tout en le renommant en dockerfile ,subtitle.py,et l'audio de la video souhaitee dans un meme dossier
   - lancer les deux conteneurs au meme moment en faisant un docker-compose -d
   - recuperer les donnees pour les aggreger.

# prerequis 
  Installer docker, docker compose sur votre machine
   
   

