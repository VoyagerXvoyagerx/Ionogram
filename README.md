# Segmentation and Edge Detection for Ionogram Automatic Scaling
by Yijie Zheng, Xiaoqing Wang, Yefei Luo, Hao Tian, Ziwei Chen.

Code for paper [_Segmentation and Edge Detection for Ionogram Automatic Scaling_](https://ieeexplore.ieee.org/document/9955166).

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
## Citation
If you find our work useful for your research, please consider citing:
```
@INPROCEEDINGS{9955166,
  author={Zheng, Yijie and Wang, Xiaoqing and Luo, Yefei and Tian, Hao and Chen, Ziwei},
  booktitle={2022 International Conference on Machine Learning, Cloud Computing and Intelligent Mining (MLCCIM)},
  title={Segmentation and Edge Detection for Ionogram Automatic Scaling},
  year={2022},
  pages={115-120},
  doi={10.1109/MLCCIM55934.2022.00026}
}
```
## Contact
Should you have any questions, please send email to 19211416@bjtu.edu.cn
