Step 1. Follow the installation guide to mmDetect from their website. 

[mmDetect Installation Guide](https://mmdetection.readthedocs.io/en/latest/get_started.html)

Step 2. Put your dataset within the data folder. I have named my dataset ic_bin_omc_w.

![Alt text](image.png)

Step 3. Train a machine learning model with the following command:

``` python
python tools/train configs/blenderbin/instaboost.py
```