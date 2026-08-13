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


def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()
        if choice == '0':
            print("프로그램을 종료합니다.")
            break
        else:
            print("기본 메뉴가 준비 중입니다.")


if __name__ == '__main__':
    main()
