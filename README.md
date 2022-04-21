# Segmentation and Edge Detection for Ionogram Automatic Scaling
by Yijie Zheng, Xiaoqing Wang, Yefei Luo, Hao Tian, Ziwei Chen 

Code for paper 'Segmentation and Edge Detection for Ionogram Automatic Scaling'.
## Trained Model
The trained models have been uploaded to google drive.
1. mTPR=0.9021: [link](https://drive.google.com/file/d/1-0__f4pK5-wvBfFB0XFOB0d13N9Gyh2k/view?usp=sharing)
2. mTPR=0.9256: [link](https://drive.google.com/file/d/1-BF3YO9QeT1SmhDjHjvWOmyNnLP-hKDL/view?usp=sharing)
3. mTPR=0.8713: [link](https://drive.google.com/file/d/1-4Dgu8Ff5CijDMJFwRf89c2XAEfukTlp/view?usp=sharing)
4. The onnxruntime model: [Ionogram.onnx](https://drive.google.com/file/d/1FHzDqeDSI2w9hBmtRwL9NKWW9ciFXtQM/view?usp=sharing)
## Prerequisites
[torch](https://pytorch.org/) 1.7, [mmsegmentation](https://github.com/open-mmlab/mmsegmentation) 0.20.0, [colab](https://colab.research.google.com/) , and [opencv-python 4.5.3.56](https://opencv.org) 
## Dataset
The Dataset we use is shared on google drive: [Iono4311.rar](https://drive.google.com/file/d/1MZUonB6E0o7lq_NndI-F3PEVkQH3C8pz/view?usp=sharing)
## Config
The configuration of PSPNet is saved in pspnet_ce.py
## Train
Train a model by running Train.ipynb
## Evaluate
Evaluate by running the notebook Evaluate.ipynb
## APIs

```Python
Do_segementation(model_path, deploy_path, input_img, work_dir, show) 
```
  Do the Ionogram Segmentation. Before using this API, make sure you have install [mmsegmentation](https://github.com/open-mmlab/mmsegmentation) and [mmdeploy](https://github.com/open-mmlab/mmdeploy/).  
> Parameters  
  - **model_path**(str) - The path of the onnx model.  
  - **deploy_path**(str) - The path of MMDeploy.  
  - **input_img**(str) - The path of the Ionogram to be scaled.  
  - **work_dir**(str) - The path of work directory that used to save the result.  
  - **show**(int) - 1 for show the result of segmentation, 0 for not.  
> Returns  
  - The output segmentation map.  
> Return type  
  - Tensor.  
 
  
```Python
onnxruntime.InferenceSession(model_path) 
```  
Get the onnx runtime inference session.  
> Parameters 
  - **model_path**(str) - The path of the onnx model. 
> Returns  
 - Ort_session.
> Return type  
 - onnxruntime.capi.onnxruntime_inference_collection.InferenceSession.  
  

```Python
  ort_session.run(['output'], ort_inputs)[0]
```
  Inferent on onnxruntime.  
> Parameters
  - **ort_inputs**(str) - The path of the onnx model.  
> Returns  
  - The output segmentation map.  
> Return type  
  - Tensor.  


```Python
  interpret(segmap)
```
  Obtain ionospheric parameters.   
> Parameters
  - **segmap**(str) - The path of the segmentation map.  
> Returns  
  - mh_pred, mf_pred, mhe_pred, mfe_pred, mhf1_pred, mff1_pred, fmin - The parameters. 
> Return type  
  - List.


```Python
  show_cha_pyplot(cimg, cmask, segmap, palette,
                                  mh_pred, mf_pred, mhe_pred, mfe_pred, mhf1_pred, mff1_pred, fmin_pred,
                                  mh_truth, mf_truth, mhe_truth, mfe_truth, mhf1_truth, mff1_truth, fmin_truth))
```
  Visualization of the ionogram, the manual scaling result, and autoscaling result.  
> Parameters
  - **cimg**(str) - The path of the image.  
  - **cmask**(list) - The mask of image.
  - **segmap**(str) - The path of the segmentation map.
  - **palette**(list) - The palette of image.
  - **mh_pred, ...**(list) - The parameters of the Ionogram.
  
## Contact
Should you have any questions, please send email to 19211416@bjtu.edu.cn
