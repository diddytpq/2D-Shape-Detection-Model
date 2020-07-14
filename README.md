# handwriting_shape_detect
손으로 쓴 글씨를 학습 및 실행까지 실습

#### 학습데이터
-------------
  학습 시간을 단축 시키기 위해 그레이 스케일 이미지를 사용
  학습 이미지(100x100x1)(20장씩 손으로 그린 후 이미지 변환을 통해 추가적으로 이미지를 생성함)
    - 원: 550장
    - 사각형: 550장
    - 삼각형: 550장

#### 신경망 구성
----------------
<img width="911" alt="스크린샷 2020-07-14 오후 3 52 38" src="https://user-images.githubusercontent.com/67572161/87394009-0c716a80-c5ea-11ea-9c7f-9efca55f267d.png">

#### 학습방법(epoch=100, steps per epoch=10)
-------------------
1. model_v1.0= loss: 0.0929 - accuracy: 0.9700
2. model_v1.2= loss: 1.4065e-04 - accuracy: 1.000


#### 실행 결과

<img width="1085" alt="result_1" src="https://user-images.githubusercontent.com/67572161/87394707-18116100-c5eb-11ea-8e70-ed1a1e79c0dc.png">
<img width="1085" alt="result_2" src="https://user-images.githubusercontent.com/67572161/87394759-2a8b9a80-c5eb-11ea-8a79-dccab4d21909.png">

보편화 된 모양은 잘 잡지만 예측할수 없는 부분의 모양까지 인식하기 위해선 조금더 많은 데이터와 학습이 필요함
