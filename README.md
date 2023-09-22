# PetKeeper_DeepLearning


## 안구 질환 식별 프로세스
<img width="1278" alt="image" src="https://github.com/kang9366/PetKeeper_DeepLearning/assets/63611804/4055abe3-e64e-48c3-abb6-beca8e3aa8a0">


### 1. 안구 식별 모델
* 사용 모델 : YOLOv5
* 학습 데이터 : DOG-EYES_ver.4 ([Robofow](https://universe.roboflow.com/dog-eyes/dog-eyes_ver.4))
* map50 : 0.95
<img width="876" alt="images-nellholic108-post-4aec7c3c-a0ec-4899-8c85-b0c176823d6e-Screen Shot 2021-12-28 at 10 52 59 AM" src="https://github.com/kang9366/PetKeeper_DeepLearning/assets/63611804/a15b12a7-3574-46f9-ab4b-04f2140b5af2">

### 2. 이미지 흐림 정도 식별 알고리즘
Laplacian Transform의 분산을 사용하여 이미지의 흐림 정도를 식별하는 알고리즘으로 이미지가 흐린 경우, 경계가 덜 뚜렷하게 나타나므로 Laplacian Transform의 결과도 덜 뚜렷하게 나타난다.
<br>따라서 이미지가 흐릴수록 Laplacian Transform의 분산이 낮아진다.
<br>분산이 300 이하인 경우에 흐린 이미지로 판별하여 식별 불가 판정을 내린다.
![image](https://github.com/kang9366/PetKeeper_DeepLearning/assets/63611804/b3f2f2db-0e98-4358-ae82-f8212d11443f)

<br>

### 3. 안구질환 식별 모델
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
