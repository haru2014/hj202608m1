# hj202608m1

Python & Git 기초 미션 저장소입니다.

## 프로젝트 개요

이 프로젝트는 Python과 Git 기본 사용법을 연습하는 미션으로, 개발 환경 설정, Git 저장소 관리, 콘솔 기반 데이터 관리 프로그램 구현, 그리고 Git 커밋을 기능 단위로 쪼개어 기록하는 과정을 수행했습니다.

## 구현 내용

- 반려견 관련 프롬프트 3개를 기본 데이터로 구성
- 콘솔 메뉴 기반 프로그램 구현
- 전체 목록, 카테고리별 조회, 검색, 상세 보기, 즐겨찾기 토글, 즐겨찾기 목록, 새 프롬프트 추가 기능 제공
- 목록 기능은 별표 여부와 카테고리 정보를 함께 표시하여 사용자가 빠르게 확인할 수 있도록 구성
- 기능 단위 커밋을 활용한 Git 이력 관리

## 프로젝트 구조

- `hello.py`: Python 실행 검증용 샘플 파일
- `prompt_manager.py`: 프롬프트 관리 프로그램
- `README.md`: 프로젝트 소개 및 사용 방법
- `구현결과보고서.md`: 구현 및 검증 결과 문서
- `.gitignore`: Python 임시 파일 제외 설정

## 실행 방법

```bash
python prompt_manager.py
```

메뉴에서 아래 항목을 선택합니다.

- 1: 전체 목록 보기
- 2: 카테고리별 보기
- 3: 검색
- 4: 상세 보기
- 5: 즐겨찾기 토글
- 6: 즐겨찾기 목록
- 7: 새 프롬프트 추가
- 0: 종료

## 주요 기능

- 기본 반려견 프롬프트 데이터 제공
- 제목/내용 기반 키워드 검색
- 카테고리 분류
- 상세 정보 조회
- 즐겨찾기 추가/제거
- 사용자 입력 검증 및 예외 처리

## Git 설정

```bash
git config --global user.name "haru2014"
git config --global user.email "mickey1008@naver.com"
git config --global init.defaultBranch main
```

## 4단계: 브랜치 관리 및 원격 반영

다음 절차를 수행하여 Git 브랜치 흐름과 원격 반영을 검증했습니다.

- `feature/list` 브랜치 생성
- 목록 기능 관련 수정 사항을 별도 브랜치에서 커밋
- `main` 브랜치로 병합 (`git merge --no-ff feature/list`)
- 원격 저장소로 푸시 (`git push origin main`)

이 과정을 통해 브랜치 분기, 병합, 로그 확인, 원격 반영까지 실제 Git workflow를 수행했습니다.

## 참고 자료

- 구현 결과 보고서: 구현결과보고서.md
- 메인 프로그램: prompt_manager.py
- GitHub 원격 저장소: https://github.com/haru2014/hj202608m1.git
