prompts = [
    {
        "title": "수의학 논문 및 임상 데이터 요약",
        "content": "당신은 수의학 및 동물응용과학 전문가입니다. 제시된 반려견 보행 관절 논문의 초록(Abstract)을 읽고 1) 연구 목적, 2) 주요 실험 결과, 3) 한계점 및 시사점을 3줄로 핵심 요약해주세요.",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "대형견 전용 착용감 우수한 신발 이미지",
        "content": "A high-quality photographic image of a 32kg Golden Retriever wearing brightly colored, perfectly fitted ergonomic dog shoes, running happily on a grassy park trail, highly detailed, 8k resolution, cinematic lighting.",
        "category": "이미지 생성",
        "favorite": True
    },
    {
        "title": "반려견 헬스케어 및 보행 분석 전문가",
        "content": "당신은 대형견 관절 건강과 기능성 신발을 연구하는 10년 경력의 수의 보행 분석 전문가입니다. 보호자가 질문하는 반려견의 걸음걸이 문제나 발바닥 보호용품에 대해 전문적이면서 친절한 어조로 조언해주세요.",
        "category": "페르소나",
        "favorite": False
    }
]


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


prompts = [
    {
        "title": "수의학 논문 및 임상 데이터 요약",
        "content": "당신은 수의학 및 동물응용과학 전문가입니다. 제시된 반려견 보행 관절 논문의 초록(Abstract)을 읽고 1) 연구 목적, 2) 주요 실험 결과, 3) 한계점 및 시사점을 3줄로 핵심 요약해주세요.",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "대형견 전용 착용감 우수한 신발 이미지",
        "content": "A high-quality photographic image of a 32kg Golden Retriever wearing brightly colored, perfectly fitted ergonomic dog shoes, running happily on a grassy park trail, highly detailed, 8k resolution, cinematic lighting.",
        "category": "이미지 생성",
        "favorite": True
    },
    {
        "title": "반려견 헬스케어 및 보행 분석 전문가",
        "content": "당신은 대형견 관절 건강과 기능성 신발을 연구하는 10년 경력의 수의 보행 분석 전문가입니다. 보호자가 질문하는 반려견의 걸음걸이 문제나 발바닥 보호용품에 대해 전문적이면서 친절한 어조로 조언해주세요.",
        "category": "페르소나",
        "favorite": False
    }
]


def show_list():
    if not prompts:
        print("저장된 프롬프트가 없습니다.")
        return
    for idx, prompt in enumerate(prompts, start=1):
        star = "★" if prompt.get("favorite") else " "
        print(f"{idx}. [{star}] {prompt['title']} ({prompt['category']})")


def show_by_category():
    categories = sorted({prompt['category'] for prompt in prompts})
    if not categories:
        print("카테고리가 없습니다.")
        return
    print("사용 가능한 카테고리:")
    for category in categories:
        print(f"- {category}")
    choice = input("조회할 카테고리 입력: ").strip()
    filtered = [p for p in prompts if p['category'] == choice]
    if not filtered:
        print("해당 카테고리의 프롬프트가 없습니다.")
        return
    for idx, prompt in enumerate(filtered, start=1):
        star = "★" if prompt.get("favorite") else " "
        print(f"{idx}. [{star}] {prompt['title']}")


def search_prompt():
    keyword = input("검색할 키워드 입력: ").strip().lower()
    if not keyword:
        print("키워드를 입력해주세요.")
        return
    results = [p for p in prompts if keyword in p['title'].lower() or keyword in p['content'].lower()]
    if not results:
        print("검색 결과가 없습니다.")
        return
    for idx, prompt in enumerate(results, start=1):
        star = "★" if prompt.get("favorite") else " "
        print(f"{idx}. [{star}] {prompt['title']} ({prompt['category']})")


def show_detail():
    show_list()
    if not prompts:
        return
    try:
        choice = int(input("상세 보기할 번호 입력: ").strip())
    except ValueError:
        print("숫자를 입력해주세요.")
        return
    if choice < 1 or choice > len(prompts):
        print("유효하지 않은 번호입니다.")
        return
    prompt = prompts[choice - 1]
    print("\n--- 상세 정보 ---")
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {'예' if prompt.get('favorite') else '아니요'}")
    print("내용:")
    print(prompt['content'])


def toggle_favorite():
    show_list()
    if not prompts:
        return
    try:
        choice = int(input("즐겨찾기 토글할 번호 입력: ").strip())
    except ValueError:
        print("숫자를 입력해주세요.")
        return
    if choice < 1 or choice > len(prompts):
        print("유효하지 않은 번호입니다.")
        return
    prompts[choice - 1]['favorite'] = not prompts[choice - 1].get('favorite', False)
    status = '추가' if prompts[choice - 1]['favorite'] else '제거'
    print(f"즐겨찾기 {status}되었습니다.")


def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()
        if choice == '1':
            show_list()
        elif choice == '2':
            show_by_category()
        elif choice == '3':
            search_prompt()
        elif choice == '4':
            show_detail()
        elif choice == '5':
            toggle_favorite()
        elif choice == '0':
            print("프로그램을 종료합니다.")
            break
        else:
            print("기본 메뉴가 준비 중입니다.")


if __name__ == '__main__':
    main()
