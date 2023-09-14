from data import load
import pandas as pd
from PIL import Image
import numpy as np
from tensorflow.keras.applications import vgg16
from tensorflow.keras.models import Model



def save_file_tolist(folder_path):
    # VGG16 모델 로드
    vgg_model = vgg16.VGG16(weights='imagenet')
    extract_model = Model(inputs=vgg_model.input, outputs=vgg_model.get_layer("fc1").output)

    # 이미지 파일에서 특성을 추출하고 리스트에 저장
    feature_list = []

    # 이미지 경로와 파일이름을 담은 리스트 호출
    image_info_list = load.file_load(folder_path)

    # 각 이미지에 대한 특성을 추출하고 출력
    for image_path, image_name in image_info_list:
        # 이미지를 PIL Image 객체로 불러오기
        image = Image.open(image_path)
        image = image.resize((224, 224))
        image = image.convert("RGB")

        # PIL Image를 NumPy 배열로 변환
        x = np.array(image)
        x = np.expand_dims(x, axis=0)

        # 이미지 전처리
        x = vgg16.preprocess_input(x)

        # 특성 추출
        feature = extract_model.predict(x)[0]

        # 튜플 형태로 이미지 경로와 이름을 묶어 리스트에 추가
        feature_list.append((image_path, image_name, feature))

    return feature_list

