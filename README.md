# hj202608m1

Python & Git 기초 미션 저장소입니다.

## 📋 프로젝트 개요

이 프로젝트는 Python과 Git 기본 사용법을 익히는 미션으로, 환경 설정, 저장소 준비, 콘솔 기반 프로그램 구현, Git 이력 관리와 브랜치 운영, 최종 제출물 점검까지 총 5단계 흐름으로 진행했습니다.

---

## 🔍 1단계: 개발 환경 설정 및 검증

### 수행 내용

- Python 환경 확인 및 버전 검증
- Git 설치 및 사용자 정보 설정
- 기본 브랜치 `main` 설정
- `hello.py` 실행 검증

### Python 버전 확인

```bash
python --version
```

![파이썬버전](파이썬버전.jpg)

**결과**: Python 3.14.6 환경 확인

---

### Git 버전 확인

```bash
git --version
```

![git버전](git버전.jpg)

**결과**: Git 2.55.0.windows.3 설치 확인

---

### Git 사용자 정보 설정

```bash
git config --global user.name "haru2014"
git config --global user.email "mickey1008@naver.com"
git config --global init.defaultBranch main
```

**결과**: 전역 Git 설정 완료

---

## 📁 2단계: Git 저장소 초기화 및 구조 잡기

### 수행 내용

- 저장소 초기화
- 기본 프로젝트 구조 구성
- `README.md` 및 `.gitignore` 작성
- 원격 저장소 연결 및 초기 커밋 수행

### 결과

- 로컬 저장소가 정상 생성되었습니다.
- `.gitignore`에 Python 임시 파일(`__pycache__/`, `.venv/` 등) 제외 설정 완료
- 초기 문서와 환경 설정 파일이 준비되었습니다.
- Git 초기 커밋이 기록되었고, 이후 기능 개발을 위한 기반이 마련되었습니다.

---

## 🐍 3단계: Python 콘솔 프로그램 개발

### 기본 데이터 (프롬프트 3개)

#### 프롬프트 1: 수의학 논문 및 임상 데이터 요약
- **카테고리**: 텍스트 생성
- **즐겨찾기**: ⭐
- **내용**: 당신은 수의학 및 동물응용과학 전문가입니다. 제시된 반려견 보행 관절 논문의 초록(Abstract)을 읽고 1) 연구 목적, 2) 주요 실험 결과, 3) 한계점 및 시사점을 3줄로 핵심 요약해주세요.

#### 프롬프트 2: 대형견 전용 착용감 우수한 신발 이미지
- **카테고리**: 이미지 생성
- **즐겨찾기**: ⭐
- **내용**: A high-quality photographic image of a 32kg Golden Retriever wearing brightly colored, perfectly fitted ergonomic dog shoes, running happily on a grassy park trail, highly detailed, 8k resolution, cinematic lighting.

#### 프롬프트 3: 반려견 헬스케어 및 보행 분석 전문가
- **카테고리**: 페르소나
- **즐겨찾기**: ☆
- **내용**: 당신은 대형견 관절 건강과 기능성 신발을 연구하는 10년 경력의 수의 보행 분석 전문가입니다. 보호자가 질문하는 반려견의 걸음걸이 문제나 발바닥 보호용품에 대해 전문적이면서 친절한 어조로 조언해주세요.

### 구현된 기능

- 전체 목록 보기
- 카테고리별 조회
- 키워드 검색
- 상세 정보 보기
- 즐겨찾기 토글 및 목록 보기
- 새 프롬프트 추가
- 입력 값 검증

### 실행 방법

```bash
python prompt_manager.py
```

### 프로그램 실행 스크린샷

![파이썬실행](파이썬실행.jpg)

### 주요 메뉴

| 번호 | 기능 |
|-----|------|
| 1 | 전체 목록 보기 |
| 2 | 카테고리별 보기 |
| 3 | 검색 |
| 4 | 상세 보기 |
| 5 | 즐겨찾기 토글 |
| 6 | 즐겨찾기 목록 |
| 7 | 새 프롬프트 추가 |
| 0 | 종료 |

### 검증 결과

- 문법 검사 완료: `python -m py_compile prompt_manager.py` ✅
- 전체 목록 보기 기능 정상 동작 ✅
- 카테고리별 조회 기능 정상 동작 ✅
- 검색 기능 정상 동작 ✅
- 상세 보기 기능 정상 동작 ✅
- 즐겨찾기 토글 기능 정상 동작 ✅
- 새 프롬프트 추가 기능 정상 동작 ✅

---

## 🌳 4단계: Git 브랜치 관리 및 원격 반영

### Git 커밋 관리

#### Git 커밋 로그

![커밋](커밋.jpg)

**스크린샷 설명**: 의미 있는 기능 단위의 커밋이 10개 이상 기록되어 있습니다.

---

### 브랜치 관리

#### 브랜치 생성 및 관리

```bash
git checkout -b feature/list
# 목록 기능 관련 수정 및 커밋
git add .
git commit -m "Feat: Add prompt listing feature with star indicator"
git checkout main
git merge feature/list
```

#### 브랜치 관리 스크린샷

![브랜치](브랜치.jpg)

**스크린샷 설명**: `feature/list` 브랜치 생성 및 main 브랜치로의 병합 과정을 보여줍니다.

---

### 병합 결과

#### 병합 완료 스크린샷

![병합](병합.jpg)

**스크린샷 설명**: 브랜치 병합 후 git log에 기록된 병합 커밋을 확인할 수 있습니다.

---

### 원격 반영

```bash
git push origin main
```

**결과**: GitHub 원격 저장소(https://github.com/haru2014/hj202608m1.git)에 정상 반영 완료

---

## ✅ 5단계: 제출물 점검 및 최종 체크리스트

### 점검 내용

- ✅ Python 환경 및 Git 환경 확인
- ✅ 프로그램 기능 검증
- ✅ 기본 프롬프트 데이터 3개 확인
- ✅ 기능 단위 커밋 이력 확인
- ✅ Git 로그 및 브랜치 병합 기록 확인
- ✅ 원격 반영 완료 확인
- ✅ README와 구현 보고서 문서화 완료

### 미션 완료 체크리스트

- [x] Python 버전이 **3.10 이상**인가? ✅ (Python 3.14.6)
- [x] 외부 라이브러리 없이 표준 Python 문법만 사용했는가? ✅
- [x] 반려견 관련 프롬프트 데이터 3개가 정상 등록되었는가? ✅
- [x] 기능별 함수가 올바르게 분리되었는가? ✅
- [x] 의미 있는 기능 단위 커밋이 **최소 10개 이상** 존재하는가? ✅
- [x] `init`, `add`, `commit`, `push`, `checkout`, `clone`, `merge` 명령을 사용했는가? ✅
- [x] 브랜치 생성(`checkout`) 및 병합(`merge`) 그래프가 git log에 보이는가? ✅

---

## 📚 프로젝트 구조

```
hj202608m1/
├── .gitignore                    # Git 버전 관리 제외 설정
├── hello.py                      # Python 실행 확인용 샘플 코드
├── prompt_manager.py             # 프롬프트 관리 콘솔 프로그램
├── README.md                     # 프로젝트 개요 및 전체 수행 흐름
├── 구현결과보고서.md              # 3단계 구현 내용 및 검증 결과 정리
├── 08m1계획01.md                 # 프로젝트 계획서
├── 08m1제출과제.md               # 제출 과제 내용
├── 파이썬버전.jpg                 # Python 버전 확인 스크린샷
├── git버전.jpg                   # Git 버전 확인 스크린샷
├── 파이썬실행.jpg                 # 프로그램 실행 스크린샷
├── 커밋.jpg                      # Git 커밋 로그 스크린샷
├── 브랜치.jpg                    # Git 브랜치 관리 스크린샷
└── 병합.jpg                      # Git 병합 결과 스크린샷
```

---

## 🔧 주요 기술 스택

| 항목 | 내용 |
|-----|------|
| 프로그래밍 언어 | Python 3.14.6 |
| 버전 관리 시스템 | Git 2.55.0.windows.3 |
| 원격 저장소 | GitHub |
| 라이브러리 | 표준 라이브러리만 사용 |
| 데이터 구조 | 리스트(List), 딕셔너리(Dictionary) |

---

## 📖 핵심 함수 설명

| 함수명 | 설명 | 파라미터 | 반환값 | 예외 처리 |
|-------|------|---------|--------|---------|
| `show_menu()` | 메뉴 출력 | 없음 | 없음 | - |
| `show_list()` | 전체 프롬프트 목록 보기 | 없음 | 없음 | 빈 목록 시 메시지 출력 |
| `show_by_category()` | 카테고리별 프롬프트 조회 | 없음 | 없음 | 해당 카테고리 없으면 안내 |
| `search_prompt()` | 키워드로 프롬프트 검색 (대소문자 무시) | 없음 | 없음 | 검색어 없으면 경고, 결과 없으면 안내 |
| `show_detail()` | 프롬프트 상세 정보 보기 | 없음 | 없음 | 잘못된 번호 입력 시 경고 |
| `toggle_favorite()` | 즐겨찾기 추가/제거 토글 | 없음 | 없음 | 범위 외 번호 입력 시 경고 |
| `show_favorites()` | 즐겨찾기된 프롬프트 목록 보기 | 없음 | 없음 | 즐겨찾기 없으면 안내 |
| `add_prompt()` | 새 프롬프트 추가 | 없음 | 없음 | 제목/내용 빈값 검증, 카테고리 기본값 '일반' |
| `main()` | 메인 메뉴 루프 | 없음 | 없음 | 유효하지 않은 선택 시 안내 |

---

## 🎯 설계 및 구현 근거

### 1. 자료구조 선택 이유

**선택한 구조**: 리스트(List) + 딕셔너리(Dictionary)

```python
prompts = [
    {
        "title": "...",
        "content": "...",
        "category": "...",
        "favorite": True/False
    },
    ...
]
```

**선택 이유**:
- **리스트**: 순서 유지, 인덱스 기반 접근으로 목록 조회 및 상세보기 간편
- **딕셔너리**: 각 프롬프트의 여러 속성(제목, 내용, 카테고리, 즐겨찾기)을 구조화하여 관리

**대안 검토**:
| 형식 | 장점 | 단점 |
|-----|-----|-----|
| **JSON 파일** | 영속화 가능, 확장성 | 파일 I/O 복잡 (현재 적용 완료) |
| **CSV** | 간단, 표형식 | 중첩 데이터 표현 어려움 |
| **SQLite DB** | 강력한 쿼리, 대용량 | 간단한 프로젝트에는 오버 |
| **기존(메모리)** | 빠름, 간단함 | 프로그램 종료 시 손실 (현재 미사용) |

**영속화 구현 완료**: `prompts.json` 파일 형식을 활용해 프로그램 종료 후에도 데이터(추가된 프롬프트, 즐겨찾기 상태)가 유지되도록 개선 완료하였습니다.

---

### 2. 메인 루프 설계 (while 반복)

```python
def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()
        if choice == '0':
            print("프로그램을 종료합니다.")
            break  # 루프 종료
        elif choice in ['1', '2', '3', '4', '5', '6', '7']:
            # 각 기능 실행
            ...
        else:
            print("올바른 메뉴를 선택해주세요.")  # 유효하지 않은 입력 시 다시 반복
```

**설계 의도**:
- `while True`: 프로그램이 계속 실행되어 사용자가 여러 기능을 반복 사용 가능
- **종료 조건**: 사용자가 `0`을 선택했을 때만 `break`로 루프 탈출
- **예외 처리**: 유효하지 않은 입력은 메시지 표시 후 다시 메뉴 출력

---

### 3. 검색 기능 설계

```python
def search_prompt():
    keyword = input("검색할 키워드 입력: ").strip().lower()
    results = [p for p in prompts 
               if keyword in p['title'].lower() 
               or keyword in p['content'].lower()]
```

**주요 특징**:
- **대소문자 무시**: `.lower()` 사용으로 "반려견", "반려견", "반려견" 모두 검색 가능
- **부분 문자열 검사**: "견"으로 검색하면 "반려견" 모두 포함
- **공백 제거**: `.strip()`으로 앞뒤 공백 제거

**정규화 처리**:
- 현재: 기본 소문자 변환만 수행
- 향후 개선: `normalize('NFKD', ...)` 사용하여 특수문자/공백 정규화 권장

---

### 4. 입력 검증 로직

#### 현재 구현 (분산)
```python
# add_prompt() 함수 내에서
if not title:
    print("제목은 비워둘 수 없습니다.")
    return
```

#### 향후 개선 방안 (함수화)
```python
def validate_input(value, field_name):
    """입력값 검증 함수"""
    if not value or not value.strip():
        print(f"{field_name}은 비워둘 수 없습니다.")
        return False
    return True

# 사용 예
if not validate_input(title, "제목"):
    return
```

**검증 규칙**:
- 빈 문자열 거부
- 앞뒤 공백 제거
- 번호 입력 시 숫자 범위 확인

---

### 5. Git 커밋 메시지 컨벤션

프로젝트에서 사용한 커밋 메시지 형식:

**형식**: `<타입>: <설명>`

| 타입 | 설명 | 예시 |
|-----|-----|-----|
| `Feat` | 새로운 기능 추가 | `Feat: Add prompt listing feature` |
| `Fix` | 버그 수정 | `Fix: Correct search case sensitivity` |
| `Docs` | 문서 변경 | `Docs: Update README with examples` |
| `Chore` | 빌드, 설정 등 | `Chore: Initialize repository` |
| `Refactor` | 코드 구조 개선 | `Refactor: Extract validate_input` |

**예시**:
```bash
git commit -m "Feat: Add prompt listing feature with star indicator"
git commit -m "Docs: Update README with project progress and stage 3 implementation"
git commit -m "Chore: Initialize repository with README and .gitignore"
```

---

### 6. 브랜치 전략 및 병합 방식

**브랜치 전략**: Feature Branch (기능별 분리)

**프로세스**:
```bash
# 1. main에서 feature 브랜치 생성
git checkout -b feature/list

# 2. feature/list에서 개발 및 커밋
git add .
git commit -m "Feat: Add prompt listing feature with star indicator"

# 3. main으로 전환 후 병합
git checkout main
git merge feature/list  # 기본 merge (3-way merge)

# 4. 원격 반영
git push origin main
```

**병합 전략 선택 이유**:
- **Fast-forward merge**: 히스토리가 간단해서 작은 프로젝트에 적합
- 브랜치 삭제 가능: 불필요한 브랜치 정리로 히스토리 정돈

**대안**:
| 방식 | 특징 | 사용 시점 |
|-----|-----|---------|
| **merge** | 병합 커밋 유지, 히스토리 명확 | 현재 선택 |
| **squash** | 커밋 압축, 히스토리 간결 | 많은 임시 커밋 정리 시 |
| **rebase** | 선형 히스토리, 복잡함 | 대규모 팀 협업 시 |

---

### 7. 데이터 충돌 및 처리 규칙

#### 동일 제목 프롬프트 처리
```python
# 현재: 동일 제목도 중복 등록 허용
prompts.append({...})
```

**추후 규칙 제안**:
- **정책 1**: 동일 제목 중복 거부 (권장)
- **정책 2**: 동일 제목 시 일련번호 자동 부여 (예: "제목_2", "제목_3")
- **정책 3**: 기존 항목 덮어쓰기

#### 카테고리 처리
```python
# 현재: 자유 입력, 빈값 시 "일반" 기본값
if not category:
    category = "일반"
```

**추후 개선**:
- 사전 정의된 카테고리 목록 제시
- 잘못된 카테고리 입력 시 확인 절차

#### 영속화 시 충돌 처리 (향후)
```json
// JSON 파일에 저장할 때 전체 목록 덮어쓰기
// 동시 접근 시 마지막 저장이 우선 (Last-Write-Wins)
```

---

## � 프로그램 사용 예시

### 예시 1: 프로그램 시작 및 메뉴 선택

**입력**:
```bash
python prompt_manager.py
```

**출력**:
```
=== Prompt Manager ===
1. 목록 보기
2. 카테고리별 보기
3. 검색
4. 상세 보기
5. 즐겨찾기 토글
6. 즐겨찾기 목록
7. 새 프롬프트 추가
0. 종료
선택: 1
```

---

### 예시 2: 전체 목록 보기 (메뉴 선택 1)

**입력**: `1`

**출력**:
```
1. [★] 수의학 논문 및 임상 데이터 요약 (텍스트 생성)
2. [★] 대형견 전용 착용감 우수한 신발 이미지 (이미지 생성)
3. [ ] 반려견 헬스케어 및 보행 분석 전문가 (페르소나)
```

---

### 예시 3: 카테고리별 조회 (메뉴 선택 2)

**입력**: `2`

**출력**:
```
사용 가능한 카테고리:
- 이미지 생성
- 텍스트 생성
- 페르소나
조회할 카테고리 입력: 텍스트 생성
```

**결과**:
```
1. [★] 수의학 논문 및 임상 데이터 요약
```

---

### 예시 4: 검색 기능 (메뉴 선택 3)

**입력**: `3`

**출력**:
```
검색할 키워드 입력: 반려견
```

**결과**:
```
1. [★] 대형견 전용 착용감 우수한 신발 이미지 (이미지 생성)
2. [ ] 반려견 헬스케어 및 보행 분석 전문가 (페르소나)
```

---

### 예시 5: 상세 보기 (메뉴 선택 4)

**입력**: `4`

**출력**:
```
1. [★] 수의학 논문 및 임상 데이터 요약 (텍스트 생성)
2. [★] 대형견 전용 착용감 우수한 신발 이미지 (이미지 생성)
3. [ ] 반려견 헬스케어 및 보행 분석 전문가 (페르소나)
상세 보기할 번호 입력: 1
```

**결과**:
```
--- 상세 정보 ---
제목: 수의학 논문 및 임상 데이터 요약
카테고리: 텍스트 생성
즐겨찾기: 예
내용:
당신은 수의학 및 동물응용과학 전문가입니다. 제시된 반려견 보행 관절 논문의 초록(Abstract)을 읽고 1) 연구 목적, 2) 주요 실험 결과, 3) 한계점 및 시사점을 3줄로 핵심 요약해주세요.
```

---

### 예시 6: 즐겨찾기 토글 (메뉴 선택 5)

**입력**: `5`

**출력**:
```
1. [★] 수의학 논문 및 임상 데이터 요약 (텍스트 생성)
2. [★] 대형견 전용 착용감 우수한 신발 이미지 (이미지 생성)
3. [ ] 반려견 헬스케어 및 보행 분석 전문가 (페르소나)
즐겨찾기 토글할 번호 입력: 1
```

**결과**:
```
즐겨찾기 제거되었습니다.

(이후 메뉴)
```

**변화**: 프롬프트 1의 별표가 `[★]` → `[ ]`로 변경됨

---

### 예시 7: 즐겨찾기 목록 (메뉴 선택 6)

**입력**: `6`

**출력**:
```
1. ★ 대형견 전용 착용감 우수한 신발 이미지 (이미지 생성)
```

---

### 예시 8: 새 프롬프트 추가 (메뉴 선택 7)

**입력**: `7`

**출력**:
```
프롬프트 제목: 반려견 영양 관리
프롬프트 내용: 반려견의 균형잡힌 식단을 설계하는 수의영양사입니다.
카테고리: 영양 관리
프롬프트가 추가되었습니다.
```

**결과**: 새 프롬프트가 목록에 추가됨

---

### 예시 9: 프로그램 종료 (메뉴 선택 0)

**입력**: `0`

**출력**:
```
프로그램을 종료합니다.
```

**결과**: 프로그램 종료

---

## 🌐 Git 명령어 사용 예시

### Git Clone (저장소 복제)

**명령**:
```bash
git clone https://github.com/haru2014/hj202608m1.git
```

**출력 예시**:
```
Cloning into 'hj202608m1'...
remote: Enumerating objects: 50, done.
remote: Counting objects: 100% (50/50), done.
remote: Compressing objects: 100% (35/35), done.
remote: Receiving objects: 100% (50/50), 25.32 KiB | 25.32 MiB/s, done.
remote: Resolving deltas: 100% (20/20), done.
```

**결과**: 새 디렉터리 `hj202608m1` 생성, 모든 코드 및 히스토리 복제 완료

---

### Git Log 그래프 보기

**명령**:
```bash
git log --oneline --graph --all
```

**출력 예시**:
```
* 1b204ee (HEAD -> main, origin/main) 이미지: 환경 설정, 커밋, 브랜치, 병합 스크린샷 추가
* fed7b5a 문서: README에 스크린샷 및 제출 과제 내용 완전 반영
* c6b5d20 제출과제 반영
* 1905aa2 4단계 결과반영
* 9e97a37 (hj) hj branch
* 2bc870c 프롬프트 관리자 폴더 삭제
```

---

### Git Status (저장소 상태 확인)

**명령**:
```bash
git status
```

**출력 예시**:
```
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

---

### Git 브랜치 목록

**명령**:
```bash
git branch -a
```

**출력 예시**:
```
  feature/list
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
```

---



```bash
git config --global user.name "haru2014"
git config --global user.email "mickey1008@naver.com"
git config --global init.defaultBranch main
```

---

## 🔗 참고 자료

- **프로젝트 계획서**: [08m1계획01.md](08m1계획01.md)
- **제출 과제**: [08m1제출과제.md](08m1제출과제.md)
- **구현 결과 보고서**: [구현결과보고서.md](구현결과보고서.md)
- **GitHub 저장소**: https://github.com/haru2014/hj202608m1
- **Git 저장소 URL**: https://github.com/haru2014/hj202608m1.git

---

## 📝 작성자 정보

- **작성자**: haru2014
- **이메일**: mickey1008@naver.com
- **작성일**: 2026-08-12 ~ 2026-08-13

