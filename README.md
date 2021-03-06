# Segmentation and Edge Detection for Ionogram Automatic Scaling
by Yijie Zheng, Xiaoqing Wang, Yefei Luo, Hao Tian, Ziwei Chen 

Code for paper 'Segmentation and Edge Detection for Ionogram Automatic Scaling'.
## Trained Model
The trained models have been uploaded to google drive.
1. mTPR=0.9021: [link](https://drive.google.com/file/d/1-0__f4pK5-wvBfFB0XFOB0d13N9Gyh2k/view?usp=sharing)
2. mTPR=0.9256: [link](https://drive.google.com/file/d/1-BF3YO9QeT1SmhDjHjvWOmyNnLP-hKDL/view?usp=sharing)
3. mTPR=0.8713: [link](https://drive.google.com/file/d/1-4Dgu8Ff5CijDMJFwRf89c2XAEfukTlp/view?usp=sharing)
## Prerequisites
[torch](https://pytorch.org/) 1.7, [mmsegmentation](https://github.com/open-mmlab/mmsegmentation) 0.20.0, [colab](https://colab.research.google.com/), and [opencv-python](https://opencv.org) 4.5.3.56.
## Dataset
The Dataset we use is shared on google drive: [Iono4311.rar](https://drive.google.com/file/d/1MZUonB6E0o7lq_NndI-F3PEVkQH3C8pz/view?usp=sharing)
## Config
The configuration of PSPNet is saved in pspnet_ce.py
## Train
Train a model by running Train.ipynb
## Evaluate
Evaluate by running the notebook Evaluate.ipynb
## Contact
Should you have any questions, please send email to 19211416@bjtu.edu.cn
