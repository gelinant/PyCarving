# -*- coding: utf-8 -*-
from PIL import Image
import sys
import seam
import gradient_prewitt
import dual_gradient
import seam_treatment
import seam_carving

def main():
    '''
    Fonction principale
    
    Paramètres : 
        - Chemin d'accès à l'image                  (string)

        - Choix 
                Rapetissement :                     0
                Agrandissement :                    1
                Elargissement :                     2

        - Nombre de seam carving horizontaux (k)    (int)

        - Nombre seam carving verticaux (kp)        (int)
    


    Cette fonction récupère l'image grâce au chemin passé en
    paramètre, calcul de son gradient et applique un seam carving horizontal k fois
    et un seam carving vertical kp fois (avec k et kp passés en paramètre) en 
    plusieurs étapes : 
        - Calcul d'une matrice de coût de l'image à partir de son gradient
        - Detection de la seam optimale à partir de la pmatrice de coût
        - Suppression de la seam déterminée
    en affichant l'image à chaque fin de boucle pour suivre l'évolution
    '''

    
    chemin = str(sys.argv[1])
    choix = int(sys.argv[2])
    k = int(sys.argv[3])
    kp = int(sys.argv[4])
    if(choix>2 or choix<0):
        print("Votre deuxième argument est invalide : ")
        print("     0 : Rapetissement")
        print("     1 : Agrandissement")
        print("     2 : Elargissement")
        quit()
    if(k < 0):
        print("Votre troisième argument est invalide : argument négatif")
        quit()
    if(kp < 0):
        print("Votre quatrième argument est invalide : argument négatif")
        quit()
    
    im = Image.open(chemin)

    if(k > im.size[1] and choix != 1):
        print("Votre troisième argument est invalide : dépassement de la taille de l'image")
        quit()
    if(k > im.size[0] and choix != 1):
        print("Votre quatrième argument est invalide : dépassement de la taille de l'image")
        quit()
    
    #image = im.load()
    img = dual_gradient.gradient(im)
    print("grad fini")
    
    compteur = k
    while compteur>0:
        im, img = seam_carving.horizontal_carving(im,img)
        im.save("gif/h"+str(k-compteur)+".bmp")
        compteur-=1
    compteur = kp
    while compteur>0:
        im, img = seam_carving.vertical_carving(im,img)
        im.save("gif/v"+str(kp-compteur)+".bmp")
        compteur-=1
    im.show()
    #img.show()
if __name__ == "__main__":
    main()