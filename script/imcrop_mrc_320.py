#from  EMAN2 import *
import sys,os,getopt
#from matplotlib import pyplot as plt
import cv2
#from skimage import io
#from mpi4py  import MPI
import mrcfile

import numpy as np

def norm(img):
    imax=np.max(img);
    imin=np.min(img);
    a=float(1)/(imax-imin);
    b=(-1)*a*imin;

    sizex=img.shape[0];
    sizey=img.shape[1];
    arr=np.zeros([sizex,sizey]);
    arr=a*img+b
#    arr=1.0-a*img+b

    return arr

def getId(fname):
    lines=fname.split('/');
    fname=lines[-1];
    lines=fname.split('.');
    stop=-1*(len(lines[-1])+1)
    fid=fname[:stop];
    print(fid)
    return fid;

def cutImg(fin,img,size,step,dout):
    #sizex,sizey,sizez=img.shape;
    sizex,sizey=img.shape;
    f0=getId(fin);
    if sizex<size:
        size=sizex;
    oldx=-1000;
    oldy=-1000;
    start=0;
    for x in range(start,sizex,step):
        for y in range(start,sizey,step):
            startx=x;
            starty=y;
            if startx+size>sizex:
                startx=sizex-size;
            if starty+size>sizey:
                starty=sizey-size;
            #if startx+size>sizex-200 and starty+size>sizey-200:
            #    continue;
            if oldx !=startx or oldy!=starty:
                arr=img[startx:startx+size,starty:starty+size];
                arr=norm(arr)
                fname=f0+'.'+str(startx)+'.'+str(starty)+'.'+str(size)+'.mrc';
                fout=os.path.join(dout,fname);
                print(fout)
                mrc_out=mrcfile.new(fout,overwrite=True)
                mrc_out.set_data(arr)
                print(mrc_out.data)
                #cv2.imwrite(fout, arr);
                #name=dout.split('/');
                #name=name[-1];
               # line=fname+'\n';
            #    flist.write(line);
                oldx=startx;
                oldy=starty;


def preProcess(fin,fout_norm,fout_noNorm):
    img=norm(fin,fout_norm);
#    img=toPng(fin,fout_noNorm)
    #cutImg(fin,img,size,step,dout,flist)


din=sys.argv[1]
#dout_noNorm=sys.argv[2]
dout_cut=sys.argv[2]
#flist=open(flist,'w');
list = os.listdir(din)
#mrcs=mrcfile.open()

step=160
size=256
#size=640
for i in range(0,len(list)):
        path = os.path.join(din,list[i])
        if os.path.isfile(path):
            #fout=getId(path)+'.png';
            #fout_cut=os.path.join(dout_cut,fout);
            #print(fout_cut)
            #preProcess(path,fout_norm,fout_noNorm)
            #img=cv2.imread(path)
            em=mrcfile.open(path,permissive=True)
            img=em.data
            print(img.shape)
            cutImg(path,img,size,step,dout_cut);
