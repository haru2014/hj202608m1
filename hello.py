# os는 컴퓨터의 폴더를 만들거나 경로를 합치는 등 운영체제(OS)의 기능을 파이썬에서 쓸 수 있게 해주는 도구(라이브러리)입니다.
import os

# 화면에 출력하고 파일에 저장할 기본 문자열 "Hello"를 output 변수에 저장합니다.
output = "Hello"

# 결과를 폴더와 파일로 저장하는 함수를 정의합니다.
# text: 저장할 내용, folder: 저장할 폴더 이름 (기본값은 "result1"), filename: 저장할 파일 이름 (기본값은 "hello_output.txt")
def save_result(text, folder="result1", filename="hello_output.txt"):
    # 지정한 폴더가 없으면 새로 생성합니다. exist_ok=True는 폴더가 이미 있어도 에러를 내지 않고 넘어가라는 뜻입니다.
    os.makedirs(folder, exist_ok=True)
    
    # 폴더 경로와 파일 이름을 합쳐서 전체 경로(예: result1/hello_output.txt)를 만듭니다.
    path = os.path.join(folder, filename)
    
    # 파일을 쓰기 모드("w")로 열고, 한글이나 특수문자가 깨지지 않도록 utf-8 인코딩을 지정합니다.
    # with 블록을 사용하면 파일 처리가 끝난 후 자동으로 파일을 닫아줍니다(close).
    with open(path, "w", encoding="utf-8") as f:
        # 파일에 텍스트 내용을 씁니다.
        f.write(text)
        
    # 저장이 완료된 파일의 전체 경로를 반환(리턴)합니다.
    return path

# 콘솔 화면에 output 변수의 값("Hello")을 출력합니다.
print(output)

# save_result 함수를 호출하여 "Hello"를 파일에 저장하고, 저장된 경로를 output_path 변수에 받습니다.
output_path = save_result(output)

# 파일이 저장된 최종 경로를 화면에 출력합니다.
print(f"Saved result to: {output_path}")
