#running command

CUDA_VISIBLE_DEVICES=2 python3 main_savemrc_128.py --dataset custom --batch_size 64 --model WGAN-GP --dataroot /data/lihongjia/denoise/empiar/10077/denoised/noise_128/ --cuda True