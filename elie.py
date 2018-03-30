from PIL import Image
import seam
import gradient_prewitt
import dual_gradient

def remove_seam(im,seam):
    image = im.load()
    for elm in seam: #pour chaque element du seam (de la forme (x,y))
        for x in range (elm[0],im.size[0]-1): #pour chaque x 
                image[x,elm[1]] = image[x+1,elm[1]]
    final =  resize(im,(im.size[0]-1,im.size[1]))    
    return final #l'image modifiée est retournée

def resize(im, dec):
    image2 = Image.new("RGB",(dec[0],dec[1]))
    image2_ = image2.load()
    image = im.load()
    for y in range (image2.size[1]):
        for x in range (image2.size[0]):
            image2_[x,y]=image[x*im.size[0]//image2.size[0],y*im.size[1]//image2.size[1]]
    return image2     

def main():
    im = Image.open('1.jpg')
    image_smc = Image.new("RGB",(im.size[0],im.size[1]))
    img = dual_gradient.gradient(im)
    image_smc = im
    # img = Image.open('1g.jpg')
    compteur = 10
    while compteur!=0:
        cm = seam.calculate_cost_matrix(img)
        sm = seam.detect_seam(cm)
        image_smc = remove_seam(image_smc,sm)
        #img = remove_seam(img,sm)
        compteur-=1
    image_smc.show()
    #img.show()
if __name__ == "__main__":
    main()