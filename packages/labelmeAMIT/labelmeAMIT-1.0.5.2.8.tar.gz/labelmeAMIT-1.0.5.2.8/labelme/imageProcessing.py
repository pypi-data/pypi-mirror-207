import cv2
import numpy as np
class imageProcessing():
    def thresholdProcess(grayImage,min,max,mean,stddv):
        # ret,thresh3=cv2.threshold(grayImage,30,250,cv2.THRESH_TRUNC)
        
        
        # ret,thresh1=cv2.threshold(grayImage,127,255,cv2.THRESH_BINARY)
        # ret,thresh2=cv2.threshold(grayImage,127,255,cv2.THRESH_BINARY_INV)
        # # ret,thresh3=cv2.threshold(grayImage,127,255,cv2.THRESH_TRUNC)
        # ret,thresh4=cv2.threshold(grayImage,127,255,cv2.THRESH_TOZERO)
        # ret,thresh5=cv2.threshold(grayImage,127,255,cv2.THRESH_TOZERO_INV)
        
        # ret,thresh3=cv2.threshold(grayImage,int(stddv)-5,max,cv2.THRESH_TRUNC)
        ret,thresh3=cv2.threshold(grayImage,min+37,max,cv2.THRESH_TRUNC)
        ret,thresh1=cv2.threshold(grayImage,min+32,max,cv2.THRESH_BINARY)
        ret,thresh2=cv2.threshold(grayImage,min+20,max,cv2.THRESH_BINARY_INV)
        # ret,thresh3=cv2.threshold(grayImage,127,255,cv2.THRESH_TRUNC)
        ret,thresh4=cv2.threshold(grayImage,min+20,max,cv2.THRESH_TOZERO)
        ret,thresh5=cv2.threshold(grayImage,min+20,max,cv2.THRESH_TOZERO_INV)
        
        
        # cv2.imwrite("thresh1.jpg",thresh1)
        # cv2.imwrite("thresh2.jpg",thresh2)
        # cv2.imwrite("thresh3.jpg",thresh3)
        # cv2.imwrite("thresh4.jpg",thresh4)
        # cv2.imwrite("thresh5.jpg",thresh5)
        
        
        return thresh3

    def sobelProcess(grayImage):
        #Sobel 算子
        x=cv2.Sobel(grayImage,cv2.CV_16S,1,0)#对 x 求一阶导数
        y=cv2.Sobel(grayImage,cv2.CV_16S,0,1)#对 y 求一阶导数
        absX=cv2.convertScaleAbs(x)
        absY=cv2.convertScaleAbs(y)
        Sobel=cv2.addWeighted(absX,0.5,absY,0.5,0)
        return Sobel
        
    def prewittProcess(grayImage):
        #Prewitt 算子
        kernelx=np.array([[1,1,1],[0,0,0],[-1,-1,-1]],dtype=int)
        kernely=np.array([[-1,0,1],[-1,0,1],[-1,0,1]],dtype=int)
        x=cv2.filter2D(grayImage,cv2.CV_16S,kernelx)
        y=cv2.filter2D(grayImage,cv2.CV_16S,kernely)
        #转 uint8
        absX=cv2.convertScaleAbs(x)
        absY=cv2.convertScaleAbs(y)
        Prewitt=cv2.addWeighted(absX,0.5,absY,0.5,0)   
        return Prewitt 

    def cannyProcess(grayImage):
        #高斯滤波降噪
        gaussian=cv2.GaussianBlur(grayImage,(3,3),0)
        #Canny 算子
        Canny=cv2.Canny(gaussian,50,150)
        return Canny

    def getContour(grayImage):
        # contours,hierarchy=cv2.findContours(grayImage,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        contours,hierarchy=cv2.findContours(grayImage,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        return contours

        #include
        #include "cxcore.h"
        #pragma comment(lib, "cxcore.lib")

    

