# Segmentation and Edge Detection for Ionogram Automatic Scaling
by Yijie Zheng, Xiaoqing Wang, Yefei Luo, Hao Tian, Ziwei Chen 

Code for paper 'Segmentation and Edge Detection for Ionogram Automatic Scaling'.
## Trained Model
The trained models have been uploaded to google drive.
1. mTPR=0.9021: [link](https://drive.google.com/file/d/1-0__f4pK5-wvBfFB0XFOB0d13N9Gyh2k/view?usp=sharing)
2. mTPR=0.9256: [link](https://drive.google.com/file/d/1-BF3YO9QeT1SmhDjHjvWOmyNnLP-hKDL/view?usp=sharing)
3. mTPR=0.8713: [link](https://drive.google.com/file/d/1-4Dgu8Ff5CijDMJFwRf89c2XAEfukTlp/view?usp=sharing)
## Prerequisites
[mmsegmentation](https://github.com/open-mmlab/mmsegmentation) , [colab](https://colab.research.google.com/) , and [opencv-python 4.5.3.56](https://opencv.org) 
## Dataset
The Dataset we use is shared on google drive: [Iono4311.rar](https://drive.google.com/file/d/1MZUonB6E0o7lq_NndI-F3PEVkQH3C8pz/view?usp=sharing)
## Config
The configuration of PSPNet is saved in pspnet_ce.py
## Train
Train a model by running Train.ipynb
## Evaluate
Evaluate by running the notebook Evaluate.ipynb
## APIs
The onnxruntime model is shared on google drive: [Ionogram.onnx](https://drive.google.com/file/d/1FHzDqeDSI2w9hBmtRwL9NKWW9ciFXtQM/view?usp=sharing)
### **Do_segementation (model_path, deploy_path, input_img, work_dir, show)**  
  Do the Ionogram Segmentation.  
  Before using this API, make sure you have install [mmsegmentation](https://github.com/open-mmlab/mmsegmentation) and [mmdeploy](https://github.com/open-mmlab/mmdeploy/).  
  #### Parameters  
  **· model_path**(str): The path of the onnx model.  
  **· deploy_path**(str): The path of MMDeploy.  
  **· input_img**(str): The path of the Ionogram to be scaled.  
  **· work_dir**(str): The path of work directory that used to save the result.  
  **· show**(int): 1 for show the result of segmentation, 0 for not.  
#### Returns
The segmentation result.
```
import onnxruntime

ort_session = onnxruntime.InferenceSession("srcnn.onnx")
ort_inputs = {'input': input_img}
ort_output = ort_session.run(['output'], ort_inputs)[0]
```
## Contact
Should you have any questions, please send email to 19211416@bjtu.edu.cn
