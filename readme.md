# Mon Projet

**projet de pipeline de traitement de video :**

 **Objectif** : Le projet a pour but de creer un pipeline de traitement video.Les videos sont stockes en local et sont traitees par un ensemble de conteneurs,notamment un conteneur qui va compresser la video,detecter la langue,sous-titrer, et enfin detecter si il y'a des animaux dans la video.Les metadonnees seront aggreges par des VMs heberge dans AWS, et le resultat sera affichee sur une page web publique.


    
   # a- conteneur de la compression

     la commande qui permet de l'executer est: docker run -d mycompression

   # b- conteneur des sous-titres
       
       commande a executer: docker run -d subtitle

       # Nous avons cree deux dockerfile pour la langue et les animaux et les commandes respectives permettant de les executer sont: 
       docker build -t langue . et docker build -t myanimaux .


    # c- on a lance les deux conteneurs au meme moment grace a docker-compose: docker-compose up -d


    # d- sur aws, on a aggrege la video compresse et les soustitres grace a une instance qu'on a cree et ensuite on a fait communiquer cette instance avec s3


    # e- sur s3 on a stocke la video compressee, le fichier de soustitres, et la video aggregee dans le bucket aggregation


    # f- et enfin on a affiche notre video aggregee sur la page web: pageweb.html




 
