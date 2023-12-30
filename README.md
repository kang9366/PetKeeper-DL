# PetKeeper_DeepLearning
## 안구 질환 식별 프로세스
<img width="1278" alt="image" src="https://github.com/kang9366/PetKeeper_DeepLearning/assets/63611804/4055abe3-e64e-48c3-abb6-beca8e3aa8a0">

<br>

### 1. 안구 식별 모델
* 사용 모델 : YOLOv5
* 학습 데이터 : DOG-EYES_ver.4 ([Robofow](https://universe.roboflow.com/dog-eyes/dog-eyes_ver.4))
* mAP50 : 0.95
<img width="876" alt="images-nellholic108-post-4aec7c3c-a0ec-4899-8c85-b0c176823d6e-Screen Shot 2021-12-28 at 10 52 59 AM" src="https://github.com/kang9366/PetKeeper_DeepLearning/assets/63611804/a15b12a7-3574-46f9-ab4b-04f2140b5af2">

<br>

### 2. 이미지 흐림 정도 식별 알고리즘
Laplacian Transform의 분산을 사용하여 이미지의 흐림 정도를 식별하는 알고리즘으로 이미지가 흐린 경우, 경계가 덜 뚜렷하게 나타나므로 Laplacian Transform의 결과도 덜 뚜렷하게 나타난다.
<br>따라서 이미지가 흐릴수록 Laplacian Transform의 분산이 낮아진다.
<br>분산이 300 이하인 경우에 흐린 이미지로 판별하여 식별 불가 판정을 내린다.
<br>

![image](https://github.com/kang9366/PetKeeper_DeepLearning/assets/63611804/b3f2f2db-0e98-4358-ae82-f8212d11443f)

<br>

### 3. 안구 질환 식별 모델
* 모델 : pytorch 프레임워크를 사용하여 pre-trained된 GoogleNet, DenseNet, VGG, MobileNet, ResNet 모델들에 대해 trasfer-learning을 수행하여 ensemble로 구성
* 학습 데이터 : 반려동물 안구 질환 데이터 ([AI Hub](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=562))
  * 사용된 데이터는 강아지의 눈 질환에 대한 이미지로, 정상, 결막염, 각막염, 유루증, 백내장의 5개 클래스로 구성되어 있으며, 클래스당 3000장의 이미지를 사용
  * Training 70%, Validation 20%, Test 10%의 비율로 나누어 학습을 진행
  <br>
  
  <img width="80%" height="80%" src="https://github.com/kang9366/PetKeeper_DeepLearning/assets/63611804/30fa2624-d3c4-47b0-84b0-cc7a19772978"/>
  <img width="80%" height="80%" src="https://github.com/kang9366/PetKeeper_DeepLearning/assets/63611804/18c8477f-eccd-4c79-8445-16377345fadc"/>
  
#### 1. GoogleNet ((best validation accuracy: 0.768)
<img width="893" alt="image" src="https://github.com/kang9366/PetKeeper-DL/assets/63611804/1f754ee3-ba27-4a9f-97ce-67c61fbae4ac">

<br>

#### 2. DenseNet (best validation accuracy: 0.69)
<img width="894" alt="image" src="https://github.com/kang9366/PetKeeper-DL/assets/63611804/db89f110-f5ad-4ce4-8c77-344a661e4fba">

#### 3. ResNet (best validation accuracy: 0.766)
<img width="893" alt="image" src="https://github.com/kang9366/PetKeeper-DL/assets/63611804/6eb2e7a4-3547-4ea4-a85e-79725d4268a1">

#### 4. VGG (best validation accuracy: 0.763)
<img width="893" alt="image" src="https://github.com/kang9366/PetKeeper-DL/assets/63611804/d9b430c2-8e51-424c-b2c1-78376fedd21b">

#### 5. MobileNet (best validation accuracy: 0.768)
<img width="893" alt="image" src="https://github.com/kang9366/PetKeeper-DL/assets/63611804/ee7817ad-d41d-4762-a96c-0ca9ac8e9761">

<br>

#### Ensemble Model (best validation accuracy: 0.79)

<br>

### 2. 피부질환 식별 모델
* 사용 알고리즘 : CNN
* 모델 : Custom CNN, AlexNet, ResNet 등의 여러 CNN 모델을 Ensemble로 적용



