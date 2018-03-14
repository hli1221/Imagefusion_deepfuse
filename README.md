# Imagefusion_deepfuse

This code is based on [K. Ram Prabhakar, V Sai Srikar, R. Venkatesh Babu. DeepFuse: A Deep Unsupervised Approach for Exposure Fusion with Extreme
Exposure Image Pairs. ICCV2017, pp. 4714-4722](http://openaccess.thecvf.com/content_iccv_2017/html/Prabhakar_DeepFuse_A_Deep_ICCV_2017_paper.html)

In this code, for all conv layers, the filter size is 3\*3.

We train this network using [Microsoft COCO dataset](http://msvocds.blob.core.windows.net/coco2014/train2014.zip)(T.-Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona, D. Ramanan, P. Dollar, and C. L. Zitnick. Microsoft coco: Common objects in context. In ECCV, 2014. 3-5.) as input images which contains 80000 images and all resize to 256×256 and RGB to gray.

# Citation
```
@misc{li2017deepfuse,
    author = {Hui Li},
    title = {CODE: Image Fusion based on Deepfuse},
    year = {2018},
    publisher = {GitHub},
    journal = {GitHub repository},
    howpublished = {\url{https://github.com/exceptionLi/Imagefusion_deepfuse}}
  }
```
