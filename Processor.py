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


        
