import numpy as np 


class ImageProcessor:

    def __init__(self):
        
        self.image=None
    @staticmethod #Babalar bu sınıfla uğraşmadan çağırmak için 
    def turn_gray(image):

        R=image[:,:,0]
        G=image[:,:,1]
        B=image[:,:,2]

        gray=R*0.299+G*0.587+B*0.114 #Ağırlıklı ortalama ile çarptık 
        gray=gray.astype(np.uint8) #Çıkan sayıyı tek matrise çevir

        return gray

    @staticmethod
    def turn_binary(image): #OPSİYONEL Arayüzde eşik değeri değişmek için bir argüman daha eklenebilir fonksiyona 
        threshold=127 #Eşik değeri belirle
        
        if image.ndim==3: #Önce graye çevir
            image=ImageProcessor.turn_gray(image)
        
        binary = (image > threshold).astype(np.uint8) * 255 #True False değerlerini 255 ile çarp Matriste elde et

        return binary    


    #Arayüze not : Ömer kanka bu her çağrıldığında 90 derece dönüyor gösterebilir bunu sunumda
    @staticmethod
    def rotation_image(image):
        if image.ndim==3: 
            transposed=image.transpose(1,0,2) #Transpose alarak sadece eksenlerin yerlerini değiştiriyoruz

        else : transposed=image.T #Binary ve gray için transpose

        rotated=transposed[:,::-1, ...] #YÜKSEKLİK :OLDUĞU GİBİ , GENİŞLİK: terse çevir  , Kanal : oldıuğu gibi kalsın
        return rotated
    
    @staticmethod
    def crop_image(image,x,y,width,height):
        result_image=image.copy()

        max_crop_x=result_image.shape[1] #Maks kırıpılacak genişlik
        max_crop_y=result_image.shape[0] #Maks yükseklik

        if x+width<=max_crop_x and y+height<=max_crop_y: #yükseklik ve genişlik aşıldı mı kontrol
            
            if image.ndim==3: # Boyut kontrol

                result_image[y:y+height,x:x+width,:]=0

            else:    
                result_image[y:y+height,x:x+width,]=0

        return result_image



    

