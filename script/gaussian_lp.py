import sys,os
import mrcfile
import cv2
import skimage
import numpy as np
#mg_original=cv2.imread('E:\ShannonT\\notebook workspace\\images\\4.23.6.jpg')


def gaussian_lp(img_noisy):
    img_blur=cv2.GaussianBlur(img_noisy,(5,5),9)
    return img_blur

#img_noisy=mrcfile.open('/data/lihongjia/denoise/empiar/10077/sim/noisy1_crop640/MicrographNr9_size4096x4096_pixsize134_partnr675_dose20_cf0_mb0_df3504_PP0.640.0.640.mrc')
#img_noisy=img_noisy.data
#img_noisy=(img_noisy-np.min(img_noisy))/(np.max(img_noisy)-np.min(img_noisy))
#img_original_standard=img_original/255
#高斯滤波
#img_blur=cv2.GaussianBlur(img_noisy,(5,5),9)
#with mrcfile.new('img_gaussian_denoised.mrc') as img_denoised:
#    img_denoised.set_data(img_blur)


def getId(fname):
    lines=fname.split('/');
    fname=lines[-1];
    lines=fname.split('.');
    stop=-1*(len(lines[-1])+1)
    fid=fname[:stop];
    print(fid)
    return fid;



if __name__ == '__main__':
    dir_in=sys.argv[1]
    dir_out=sys.argv[2]
    list= os.listdir(dir_in)
    for i in range(0,len(list)):
        path = os.path.join(dir_in,list[i])
        img=mrcfile.open(path,permissive=True)
        img=img.data
        img=(img-np.min(img))/(np.max(img)-np.min(img))
        lp_img=gaussian_lp(img)
        lp_img=lp_img.astype(np.float32)
        fout=getId(path)+'.mrc';
        fout_norm=os.path.join(dir_out,fout);
        with mrcfile.new(fout_norm,overwrite=True) as lp:
            lp.set_data(lp_img)

