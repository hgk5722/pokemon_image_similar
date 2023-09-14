import os

def file_load(_folder_path):
    folder_path = _folder_path

    # 폴더 내 파일 리스트 가져오기
    file_list = os.listdir(folder_path)

    # 이미지 파일 경로와 이름을 튜플로 묶어 리스트 초기화
    image_info_list = []

    # 모든 파일을 이미지 파일 경로와 이름을 튜플로 묶어 리스트에 추가
    for file_name in file_list:
        image_path = os.path.join(folder_path, file_name)
        image_info_list.append((image_path, file_name))

    return image_info_list