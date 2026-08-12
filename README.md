# hj202608m1

Python & Git 기초 미션 저장소입니다.

## 프로젝트 개요

본 프로젝트는 Python과 Git의 기본 사용법을 익히는 미션으로, 환경 설정, Git 사용자 정보 설정, Python 실행 검증, 그리고 콘솔 기반 프롬프트 관리 프로그램 구현을 수행했습니다.

## 진행 상황

- 1단계: 개발 환경 설정 및 검증 완료
  - Python 3.14.6 확인
  - Git 2.55.0.windows.3 확인
  - 전역 Git 사용자 정보 설정 완료
  - 기본 브랜치 `main` 설정 완료
  - `hello.py` 실행 검증 완료
- 2단계: 건너뛰고 3단계로 진행
- 3단계: Python 콘솔 프로그램 구현 완료
  - 프롬프트 목록 관리 기능 구현
  - 카테고리별 조회, 검색, 상세 보기, 즐겨찾기, 추가 기능 구현
  - 구현 결과 보고서 작성 완료

## 프로젝트 구조

- `.gitignore`: Python 임시 파일 및 가상환경 제외 설정
- `hello.py`: Python 실행 확인용 샘플 코드
- `prompt_manager.py`: 프롬프트 관리 콘솔 프로그램
- `구현결과보고서.md`: 3단계 구현 내용 및 검증 결과 정리

## 실행 방법

1. Python 환경 확인

```bash
python --version
```

2. 프로그램 실행

```bash
python prompt_manager.py
```

3. 메뉴에서 번호를 선택하여 기능을 사용합니다.

- 1: 전체 목록 보기
- 2: 카테고리별 보기
- 3: 검색
- 4: 상세 보기
- 5: 즐겨찾기 토글
- 6: 즐겨찾기 목록
- 7: 새 프롬프트 추가
- 0: 종료

## 주요 기능

- 기본 반려견 관련 프롬프트 3개 제공
- 사용자 입력 기반 메뉴 선택
- 제목/내용 검색
- 상세 정보 출력
- 즐겨찾기 추가/제거
- 새로운 프롬프트 등록

## Git 설정 내용

```bash
git config --global user.name "haru2014"
git config --global user.email "mickey1008@naver.com"
git config --global init.defaultBranch main
```

## 참고

- 구현 결과 보고서: [구현결과보고서.md](구현결과보고서.md)
- 메인 프로그램: [prompt_manager.py](prompt_manager.py)
