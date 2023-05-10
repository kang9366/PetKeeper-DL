# PetKeeper_DeepLearning

## 딥러닝 모델
### 1. 반려동물 감정 인식 모델
반려동물의 얼굴 사진을 찍으면 감정을 분류 하는 모델
* 사용 모델 : 
* class : happy, sad, angry, relaxed
* 사용 데이터 : 이미지 약 15,000장
* https://www.kaggle.com/datasets/devzohaib/dog-emotions-prediction

<br>

### 2. 반려동물의 안구질환을 식별할 수 있는 모델
#### 1. 결막염
* 사용 모델 : MobileNet
* 사용 데이터

<img width="400" alt="loss" src="https://github.com/kang9366/PetKeeper_DeepLearning/assets/63611804/7416066e-83ce-4174-bd34-44c3f24ead88">
<br>
<img width="600" alt="loss" src="https://github.com/kang9366/PetKeeper_DeepLearning/assets/63611804/64030430-1000-47ec-9799-3c6024052fcb">

<br>

* Accuracy : 96.7%
<div style="display: flex;">
<img width="400" alt="loss" src="https://github.com/kang9366/PetKeeper_DeepLearning/assets/63611804/616c3051-5369-404e-ba38-c22266c41f85">
<img width="400" alt="accuracy" src="https://github.com/kang9366/PetKeeper_DeepLearning/assets/63611804/daa06c45-7e27-4cb5-9f66-7e25cee19adc">
</div>

#### 2. 색소침착성 각막염
<br>

### 3. 반려동물의 피부질환을 식별할 수 있는 모델
* 사용 알고리즘 : CNN
* 모델 : Custom CNN, AlexNet, ResNet 등의 여러 CNN 모델을 Ensemble로 적용

<br>

### 4. 반려동물의 행동을 인식할 수 있는 모델
* 사용 알고리즘 : object-detection
* 모델 : yolov5
* 사용 데이터
![Unknown-3](https://github.com/kang9366/PetKeeper_DeepLearning/assets/63611804/64030430-1000-47ec-9799-3c6024052fcb)
