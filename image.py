import cv2
import numpy as np

class avion_image_tools:
    """ 
    [Summary]: 
        This is the class where we'll utilize 
        image functions.
    """

    def __init__(self):
        pass

    def enhance_image_gamma(self,image,gamma,demo=1,invert=0):
        '''
        image enhancing with gamma correction, set demo to 1 to see result in different window, set invert 1 to process inverted image
        '''
        invGamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
        if invert:
            image=cv2.bitwise_not(image)
        enhanced=cv2.LUT(image, table)
        if demo:
            cv2.imshow("gama={}".format(gamma),np.hstack([image,enhanced]))
            cv2.waitKey()
        return enhanced


    def enhance_image_clahe(self,image,limit,demo=1,invert=0):
        '''
        image enhancing with CLAHE method, set demo to 1 to see result in different window, set invert 1 to process inverted image
        '''
        if invert:
            image=cv2.bitwise_not(image)
        image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(clipLimit=limit,tileGridSize=(32,32))
        enhanced = clahe.apply(image_bw)
        if demo:
            cv2.imshow("CLAHE",np.concatenate((image_bw,enhanced),axis=0))
            cv2.waitKey()
        return enhanced

    def cropper(self, test_img, demonstration = True):
        pass


