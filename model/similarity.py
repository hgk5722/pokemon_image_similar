
import pandas as pd
from scipy.spatial.distance import cosine


# 두 포켓몬의 유사도를 측정
def print_similarity(pokemon_image1, pokemon_image2, feature_list):
    # image1, image2에 유사도를 측정하고 싶은 파일 이름을 넣어주세요!
    image1 = pokemon_image1
    image2 = pokemon_image2
    for image_path, image_name, feature in feature_list:
        if image_name == image1:
            tmp_image1 = feature
        elif image_name == image2:
            tmp_image2 = feature

    # image1와 image2 파일 간의 코사인 유사도 계산
    if tmp_image1 is not None and tmp_image2 is not None:
        similarity = 1 - cosine(tmp_image1, tmp_image2)
        print("두 이미지 사이 코사인 유사도:", round(similarity, 3))
    else:
        print("사진을 찾을 수 없습니다.")

def make_pokemon_DataFrame(feature_list):
    print("포켓몬 간 유사도를 매트릭스로 만들고 있어요~~")

    # 빈 데이터 프레임 생성
    cosine_similarity_df = pd.DataFrame(index=[image_info[1] for image_info in feature_list], 
                                        columns=[image_info[1] for image_info in feature_list])
    
    # 이미지 간의 코사인 유사도 계산
    for i in range(len(feature_list)):
        for j in range(len(feature_list)):
            similarity = 1 - cosine(feature_list[i][2], feature_list[j][2])
            cosine_similarity_df.iloc[i, j] = similarity

    # 데이터 프레임 출력
    print(cosine_similarity_df)
    return cosine_similarity_df

def make_csv(cosine_similarity_df):
    cosine_similarity_df.to_csv("pokemon_similarity.csv")