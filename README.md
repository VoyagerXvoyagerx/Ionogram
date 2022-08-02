# Segmentation and Edge Detection for Ionogram Automatic Scaling
by Yijie Zheng, Xiaoqing Wang, Yefei Luo, Hao Tian, Ziwei Chen 

Code for paper 'Segmentation and Edge Detection for Ionogram Automatic Scaling'.

## Abstract
Ionograms, recorded by ionosondes, include cru- cial information about the ionosphere. Scaling ionograms is the fundamental step for analyzing ionospheric weather. With the fast growth in data collecting in recent years, human specialists are unable to manually scale a large number of ionograms in a reasonable amount of time. To acquire exact ionospheric parameters of E, F1, and F2 layers, a 3-stage technique based on semantic segmentation networks, an edge detection module, and a feature fusing module is proposed in this research. 3448 ionograms from the Chinese Academy of Sciences Digital Ionosonde located in Hainan, Huailai, and Wuhan are used to train the segmentation networks. The test results over 863 images show that 99.1% of autoscaled critical frequency foF2 has an error within 0.2 MHz, while 98.7% of autoscaled minimum virtual height h’F2 has an error within 10 km, indicating that the performance of our method is close to that by human experts. Therefore, our work may make a great contribution to ionospheric research.


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
## Models and results

| Method        | Background Weight | Download | mTPR   | DH   | DF    | dfoF2 $\le$ 0.2MHz | dhF2 $\le$ 10km |
|---------------|-------------------|----------|--------|------|-------|--------------|----------|
| PSPNet        | 0.10| [model](https://drive.google.com/file/d/1-4Dgu8Ff5CijDMJFwRf89c2XAEfukTlp/view?usp=sharing)     | 0.8713 | 4.38 | 0.12  | 98.6 | 97.0 |
| PSPNet        | 0.15   | [model](https://drive.google.com/file/d/10qGjK_RCBv5J0OEBBqNFSmi0V5Q4yJ_S/view?usp=sharing)     | 0.8814 | 4.63 | 0.112 | 98.3 | 97.0 |
| PSPNet        | 0.20| [model](https://drive.google.com/file/d/15GxkUFSU4WzGD123GhpWVjE7YsIY9cIg/view?usp=sharing)     | 0.8070  | 4.69 | 0.100   | 98.5 | 97.8 |
| PSPNNet+Canny | 0.08   | [model](https://drive.google.com/file/d/1-P8oreRabOPzO__NX2Ng6NUDKbGgOLW4/view?usp=sharing) | 0.9415 | 3.05 | 0.100  | 97.7 | 98.6 |
| PSPNNet+Canny | 0.02   | [model](https://drive.google.com/file/d/1-BF3YO9QeT1SmhDjHjvWOmyNnLP-hKDL/view?usp=sharing)    | 0.9256 | 2.88 | 0.091 | 98.4 | **98.8** |
| PSPNNet+Canny | 0.05   | [model](https://drive.google.com/file/d/1-0__f4pK5-wvBfFB0XFOB0d13N9Gyh2k/view?usp=sharing)    | 0.9021 | **2.82** | 0.084 | **99.1** | 98.7 |
| PSPNNet+Canny | 0.10| [model](https://drive.google.com/file/d/1-4Dgu8Ff5CijDMJFwRf89c2XAEfukTlp/view?usp=sharing)    | 0.8713 | 3.01 | **0.08**  | 99.0 | 98.5 |
| PSPNNet+Canny | 0.15   | [model](https://drive.google.com/file/d/10qGjK_RCBv5J0OEBBqNFSmi0V5Q4yJ_S/view?usp=sharing)     | 0.8814 |4.63 |0.096      |97.9|98.3    |
| PSPNNet+Canny | 0.20| [model](https://drive.google.com/file/d/15GxkUFSU4WzGD123GhpWVjE7YsIY9cIg/view?usp=sharing)     | 0.8070  | 4.05 | 0.093 | 98.3 | 97.1 |
## Contact
Should you have any questions, please send email to 19211416@bjtu.edu.cn
