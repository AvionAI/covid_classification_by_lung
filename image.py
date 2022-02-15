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
        image_bw = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY).astype('uint8')
        image_bw=image_bw*255
        clahe = cv2.createCLAHE(clipLimit=limit,tileGridSize=(8,8))
        enhanced = clahe.apply(image_bw)
        if demo:
            cv2.imshow("CLAHE",np.concatenate((image_bw,enhanced),axis=0))
            cv2.waitKey()
        return enhanced

    def cropper(org_img,return_size=299,convert_to_gray=1):
        '''
        crops the given image, returns bounding box coordinates with cropped and resized image
        if given image is not-grayscale, set convert_to_gray to 1
        '''

        test_img=org_img

        #if not grayscale
        if convert_to_gray:
            test_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
        

        #convert to binary
        blurred = cv2.GaussianBlur(test_img, (7, 7), 0)
        thresh = cv2.adaptiveThreshold(blurred, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 4)
        
        #erode and dilate to join blobs together
        kernel=np.ones((1,3),np.uint8)
        kernel2=np.ones((4,1),np.uint8)

        eroded=cv2.erode(thresh,kernel,iterations=10)
        dilated=cv2.dilate(eroded,kernel2,iterations=10)
        dilated[0:20,:]=0
        dilated[:,0:15]=0
        dilated[:,275:]=0
        

        #find contours(lungs)
        contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        big_contours=list(contours)

        #choose 10 contours with the most area 
        big_contours.sort(key=cv2.contourArea,reverse=True)
        big_contours=big_contours[:10]
        
        
        all_contours=[item for c in big_contours for thing in c for item in thing]
        all_contours=np.array(all_contours)
        
        #find extreme values for bounding box
        max_x=all_contours[:,0].max()
        min_x=all_contours[:,0].min()
        max_y=all_contours[:,1].max()
        min_y=all_contours[:,1].min()
        
        bbox=(min_x,min_y,max_x,max_y)

        #crop and resize original image
        cropped=org_img[min_y:max_y+1,min_x:max_x+1]
        cropped=cv2.resize(cropped,(return_size,return_size))

        return bbox, cropped, return_size