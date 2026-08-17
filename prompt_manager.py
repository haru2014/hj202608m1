# json 파일을 다루기 위한 파이썬 내장 라이브러리입니다.
import json
# 파일이나 디렉토리(폴더)가 존재하는지 확인하는 등 운영체제 기능을 쓰기 위한 라이브러리입니다.
import os

# 프롬프트 데이터를 저장할 JSON 파일의 이름입니다.
DATA_FILE = "prompts.json"

# 프로그램이 처음 실행되거나 저장된 데이터 파일이 없을 때 사용할 기본 프롬프트 목록(데이터베이스)입니다.
# 리스트 안의 각 항목은 하나의 프롬프트 정보를 담고 있는 사전(Dictionary, 딕셔너리) 형식입니다.
DEFAULT_PROMPTS = [
    {
        "title": "수의학 논문 및 임상 데이터 요약",
        "content": "당신은 수의학 및 동물응용과학 전문가입니다. 제시된 반려견 보행 관절 논문의 초록(Abstract)을 읽고 1) 연구 목적, 2) 주요 실험 결과, 3) 한계점 및 시사점을 3줄로 핵심 요약해주세요.",
        "category": "텍스트 생성",
        "favorite": True, # True는 이 프롬프트가 즐겨찾기(보관함)에 등록되어 있음을 의미합니다.
    },
    {
        "title": "대형견 전용 착용감 우수한 신발 이미지",
        "content": "A high-quality photographic image of a 32kg Golden Retriever wearing brightly colored, perfectly fitted ergonomic dog shoes, running happily on a grassy park trail, highly detailed, 8k resolution, cinematic lighting.",
        "category": "이미지 생성",
        "favorite": True,
    },
    {
        "title": "반려견 헬스케어 및 보행 분석 전문가",
        "content": "당신은 대형견 관절 건강과 기능성 신발을 연구하는 10년 경력의 수의 보행 분석 전문가입니다. 보호자가 질문하는 반려견의 걸음걸이 문제나 발바닥 보호용품에 대해 전문적이면서 친절한 어조로 조언해주세요.",
        "category": "페르소나",
        "favorite": False, # False는 즐겨찾기에 등록되지 않았음을 의미합니다.
    },
]


# 저장된 JSON 파일에서 프롬프트 목록을 불러오는 함수입니다.
def load_prompts():
    # 데이터 파일이 존재하지 않는 경우
    if not os.path.exists(DATA_FILE):
        try:
            # 파일을 쓰기("w") 모드로 열고 한글이 깨지지 않게 utf-8 인코딩을 지정합니다.
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                # DEFAULT_PROMPTS 데이터를 JSON 포맷으로 변환하여 파일에 저장합니다.
                # ensure_ascii=False는 한글이 아스키 코드로 변환되지 않고 그대로 저장되게 해줍니다.
                # indent=4는 가독성을 위해 들여쓰기를 4칸씩 적용합니다.
                json.dump(DEFAULT_PROMPTS, f, ensure_ascii=False, indent=4)
        except Exception as e:
            # 오류가 발생한 경우 오류 메시지를 출력합니다.
            print(f"기본 데이터 파일 생성 실패: {e}")
        # 기본 데이터의 복사본(값 복사)을 만들어 리스트로 돌려줍니다.
        return [dict(p) for p in DEFAULT_PROMPTS]
    
    # 데이터 파일이 이미 존재하는 경우 파일을 읽어옵니다.
    try:
        # 파일을 읽기("r") 모드로 엽니다.
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            # 파일 안에 적힌 JSON 데이터를 파이썬의 리스트/딕셔너리 구조로 변환하여 돌려줍니다.
            return json.load(f)
    except Exception as e:
        # 파일을 읽는 중 오류(파일 손상 등)가 발생하면 오류를 알리고 기본 데이터를 대신 반환합니다.
        print(f"데이터 로드 실패: {e}. 기본 데이터로 시작합니다.")
        return [dict(p) for p in DEFAULT_PROMPTS]


# 현재 메모리(prompts 변수)에 있는 프롬프트 목록을 JSON 파일에 저장하는 함수입니다.
def save_prompts():
    try:
        # 파일을 쓰기("w") 모드로 열어 최신 데이터를 덮어씁니다.
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(prompts, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"데이터 저장 실패: {e}")


# 프로그램을 실행하자마자 파일로부터 프롬프트 데이터를 불러와 prompts 전역 변수에 저장합니다.
prompts = load_prompts()


# 사용자에게 보여줄 콘솔 메뉴 화면을 출력하는 함수입니다.
def show_menu():
    print("\n=== Prompt Manager ===")
    print("1. 목록 보기")
    print("2. 카테고리별 보기")
    print("3. 검색")
    print("4. 상세 보기")
    print("5. 즐겨찾기 토글")
    print("6. 즐겨찾기 목록")
    print("7. 새 프롬프트 추가")
    print("0. 종료")


# 하나의 프롬프트 딕셔너리를 받아서 목록 화면에 표시할 예쁜 라벨 형식으로 만드는 함수입니다.
# 예: 즐겨찾기된 경우 "[★] 제목 (카테고리)", 즐겨찾기가 아니면 "[ ] 제목 (카테고리)"
def get_prompt_label(prompt):
    # favorite 키의 값이 True이면 꽉 찬 별(★)을, False이거나 키가 없으면 빈 칸(" ")을 사용합니다.
    star = "★" if prompt.get("favorite") else " "
    return f"[{star}] {prompt['title']} ({prompt['category']})"


# 전체 프롬프트 목록을 콘솔에 보여주는 함수입니다.
def show_list():
    # 저장된 프롬프트가 없을 때 안내 메시지를 출력하고 함수를 종료합니다.
    if not prompts:
        print("저장된 프롬프트가 없습니다.")
        return
    # enumerate(리스트, start=1)을 사용해 1번부터 시작하는 번호(idx)와 항목(prompt)을 하나씩 가져옵니다.
    for idx, prompt in enumerate(prompts, start=1):
        print(f"{idx}. {get_prompt_label(prompt)}")


# 카테고리별로 필터링하여 목록을 조회하는 함수입니다.
def show_by_category():
    # 모든 프롬프트의 카테고리를 모은 뒤, set(집합)을 통해 중복을 제거하고 정렬(sorted)합니다.
    categories = sorted({prompt["category"] for prompt in prompts})
    # 카테고리가 하나도 없는 경우
    if not categories:
        print("카테고리가 없습니다.")
        return
    
    # 사용 가능한 모든 카테고리를 화면에 나열합니다.
    print("사용 가능한 카테고리:")
    for category in categories:
        print(f"- {category}")
        
    # 사용자로부터 조회하고 싶은 카테고리 이름을 입력받습니다. .strip()은 좌우 공백을 제거해줍니다.
    choice = input("조회할 카테고리 입력: ").strip()
    
    # 리스트 컴프리헨션을 사용해 입력된 카테고리와 일치하는 프롬프트만 골라 filtered 리스트를 만듭니다.
    filtered = [p for p in prompts if p["category"] == choice]
    
    # 필터링 결과가 비어있는 경우
    if not filtered:
        print("해당 카테고리의 프롬프트가 없습니다.")
        return
    
    # 검색된 프롬프트 목록을 순서대로 출력합니다.
    for idx, prompt in enumerate(filtered, start=1):
        print(f"{idx}. {get_prompt_label(prompt)}")


# 제목이나 내용에 특정 키워드가 포함된 프롬프트를 검색하는 함수입니다.
def search_prompt():
    # 검색어를 입력받고, .lower()를 통해 소문자로 변환해 둡니다(대소문자 구분 없이 검색하기 위함).
    keyword = input("검색할 키워드 입력: ").strip().lower()
    # 검색어가 빈 문자열인 경우 예외 처리합니다.
    if not keyword:
        print("키워드를 입력해주세요.")
        return
    
    # 제목(title) 또는 내용(content)에 키워드가 포함된 프롬프트만 필터링합니다.
    results = [
        p for p in prompts if keyword in p["title"].lower() or keyword in p["content"].lower()
    ]
    
    # 검색 결과가 없는 경우
    if not results:
        print("검색 결과가 없습니다.")
        return
    
    # 검색 결과를 번호와 함께 출력합니다.
    for idx, prompt in enumerate(results, start=1):
        print(f"{idx}. {get_prompt_label(prompt)}")


# 특정 프롬프트의 상세 내용을 보여주는 함수입니다.
def show_detail():
    # 먼저 전체 목록을 출력하여 사용자가 번호를 선택하기 편하게 돕습니다.
    show_list()
    if not prompts:
        return
    
    # 사용자로부터 상세조회할 번호를 숫자로 입력받습니다.
    try:
        choice = int(input("상세 보기할 번호 입력: ").strip())
    except ValueError:
        # 사용자가 숫자가 아닌 문자(예: "abc")를 입력했을 때 예외 처리를 수행합니다.
        print("숫자를 입력해주세요.")
        return
        
    # 입력한 번호가 목록의 범위를 벗어나는지 검사합니다.
    if choice < 1 or choice > len(prompts):
        print("유효하지 않은 번호입니다.")
        return
        
    # 리스트는 0부터 시작하므로 입력값에서 1을 뺀 인덱스로 프롬프트 정보를 가져옵니다.
    prompt = prompts[choice - 1]
    print("\n--- 상세 정보 ---")
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {'예' if prompt.get('favorite') else '아니요'}")
    print("내용:")
    print(prompt['content'])


# 특정 프롬프트의 즐겨찾기(favorite) 상태를 설정하거나 해제(토글)하는 함수입니다.
def toggle_favorite():
    # 전체 프롬프트 목록을 먼저 보여줍니다.
    show_list()
    if not prompts:
        return
        
    try:
        choice = int(input("즐겨찾기 토글할 번호 입력: ").strip())
    except ValueError:
        print("숫자를 입력해주세요.")
        return
        
    # 번호의 유효성을 검사합니다.
    if choice < 1 or choice > len(prompts):
        print("유효하지 않은 번호입니다.")
        return
        
    # 지정한 프롬프트의 'favorite' 값을 반전시킵니다. (True -> False, False -> True)
    # .get("favorite", False)는 키가 없을 때 기본값으로 False를 사용하라는 의미입니다.
    prompts[choice - 1]["favorite"] = not prompts[choice - 1].get("favorite", False)
    
    # 변경된 데이터를 JSON 파일에 영구 저장합니다.
    save_prompts()
    
    # 상태 메시지를 사용자에게 보여줍니다.
    status = "추가" if prompts[choice - 1]["favorite"] else "제거"
    print(f"즐겨찾기 {status}되었습니다.")


# 즐겨찾기(favorite=True)로 등록된 프롬프트 목록만 모아서 출력하는 함수입니다.
def show_favorites():
    # 즐겨찾기가 참(True)인 프롬프트만 리스트로 필터링합니다.
    favorites = [p for p in prompts if p.get("favorite")]
    # 즐겨찾기된 프롬프트가 하나도 없는 경우
    if not favorites:
        print("즐겨찾기된 프롬프트가 없습니다.")
        return
    # 즐겨찾기된 프롬프트들을 화면에 출력합니다.
    for idx, prompt in enumerate(favorites, start=1):
        print(f"{idx}. {get_prompt_label(prompt)}")


# 새로운 프롬프트를 추가하는 함수입니다.
def add_prompt():
    # 제목 입력받기 및 예외 처리
    title = input("프롬프트 제목: ").strip()
    if not title:
        print("제목은 비워둘 수 없습니다.")
        return
        
    # 내용 입력받기 및 예외 처리
    content = input("프롬프트 내용: ").strip()
    if not content:
        print("내용은 비워둘 수 없습니다.")
        return
        
    # 카테고리 입력받기 (미입력 시 기본적으로 "일반" 카테고리가 부여됩니다.)
    category = input("카테고리: ").strip()
    if not category:
        category = "일반"
        
    # 새 프롬프트 딕셔너리를 생성하여 prompts 리스트에 마지막 요소로 추가(append)합니다.
    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False, # 새로 생성된 프롬프트는 즐겨찾기가 되지 않은 상태(False)로 시작합니다.
    })
    
    # 추가된 최신 프롬프트 데이터를 파일에 저장합니다.
    save_prompts()
    print("프롬프트가 추가되었습니다.")


# 프로그램의 메인 실행 제어 함수입니다.
def main():
    # 사용자가 0번을 눌러 종료하기 전까지 메뉴를 무한히 띄웁니다.
    while True:
        show_menu()
        choice = input("선택: ").strip()
        
        # 입력받은 메뉴 번호가 올바른 선택지 목록에 있는지 확인합니다.
        valid_choices = {"0", "1", "2", "3", "4", "5", "6", "7"}
        if choice not in valid_choices:
            print("올바른 메뉴를 선택해주세요.")
            continue

        # 사용자의 선택에 맞춰 해당하는 기능 함수를 실행합니다.
        if choice == "1":
            show_list()
        elif choice == "2":
            show_by_category()
        elif choice == "3":
            search_prompt()
        elif choice == "4":
            show_detail()
        elif choice == "5":
            toggle_favorite()
        elif choice == "6":
            show_favorites()
        elif choice == "7":
            add_prompt()
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break # while 루프를 탈출하여 프로그램을 정상 종료시킵니다.


# 이 스크립트 파일이 직접 실행되었을 때(예: python prompt_manager.py)만 main() 함수가 작동하게 제어합니다.
# 다른 파일에서 이 파일을 모듈로서 import하여 사용할 경우에는 main()이 자동 실행되지 않습니다.
if __name__ == "__main__":
    main()

