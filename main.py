from model import model, similarity
import os

# 파일 경로 설정  ╰(*°▽°*)╯ ╰(*°▽°*)╯ ╰(*°▽°*)╯
folder_path = "./pokemon/images/images"

# 파일 경로를 확인해 주세요!
print("파일 경로가 올바르게 입력되었나요?")
if input('[y/n]: ') == 'y':
    
    print("포켓몬 사진을 읽고 있습니다! 잠시만 기다려주세요 ㅎㅎ")
    feature_list = model.save_file_tolist(folder_path)
    print("오래 기다리셨습니다~ (●'◡'●)")

    while 1:
        message = """
                    원하는 옵션을 숫자로 입력하세요 ╰(*°▽°*)╯
                    1번: 두 포켓몬 사이 코사인 유사도 비교하기!
                    2번: 각 포켓몬 간 유사도 출력하기!
                    
                    10번: 종료
                    """
        print(message)
        command = int(input())
        if command == 1:
            # 첫번째와 두번째 매개변수에 원하는 포켓몬의 이름(영어)을 넣어주세요!
            similarity.print_similarity('bidoof.png', 'bibarel.png', feature_list)
        elif command == 2:
            cosine_similarity_df = similarity.make_pokemon_DataFrame(feature_list)
            if input('매트릭스를 csv파일로 다운받으시겠습니까? [y/n]: ') == 'y':
                similarity.make_csv(cosine_similarity_df)
                print("파일이 생성되었습니다. 폴더를 확인해주세요. (～￣▽￣)～ ")
            else:
                continue
        elif command == 10:
            print("종료! ☆*: .｡. o(≧▽≦)o .｡.:*☆ ")
            break
        else:
            print("올바르지 않은 입력값입니다. 다시 입력해 주세요.")
else:
    print("프로그램을 종료하겠습니다. folder_path 변수에 있는 파일 경로를 확인해 주세요!")