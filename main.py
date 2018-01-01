# Demo - train the style transfer network & use it to generate an image

from __future__ import print_function

import time

from train_recons import train_recons
from generate import generate
from utils import list_images
import os

# os.environ["CUDA_VISIBLE_DEVICES"] = "1"

# IS_TRAINING = True
IS_TRAINING = False

BATCH_SIZE = 2
EPOCHES = 2

MODEL_SAVE_PATH = './models/deepfuse_models/deepfuse_model_batch_size_2.ckpt'

# model_pre_path  = './models/style_weight_1e0_pre0/style_weight_1e0.ckpt'
model_pre_path  = None

def main():

    if IS_TRAINING:

        original_imgs_path = list_images('D:/ImageDatabase/Image_fusion_MSCOCO/original/')

        print('\nBegin to train the network ...\n')
        train_recons(original_imgs_path, MODEL_SAVE_PATH, model_pre_path, EPOCHES, BATCH_SIZE, debug=True)

        print('\nSuccessfully! Done training...\n')
    else:
        # output_save_path = 'outputs/fused'
        output_save_path = 'outputs'
        sourceA_name = 'VIS'
        sourceB_name = 'IR'
        print('\nBegin to generate pictures ...\n')

        content_name = 'images/IV_images/' + sourceA_name
        style_name   = 'images/IV_images/' + sourceB_name

        # content_path = 'images/IV/' + sourceB_name
        # style_path = 'images/IV/' + sourceA_name

        for i in range(1):
            index = i + 1
            content_path = content_name + str(index) + '.png'
            style_path = style_name + str(index) + '.png'
            generate(content_path, style_path, MODEL_SAVE_PATH, model_pre_path, index, output_path=output_save_path)

        # print('\ntype(generated_images):', type(generated_images))
        # print('\nlen(generated_images):', len(generated_images), '\n')


if __name__ == '__main__':
    main()

