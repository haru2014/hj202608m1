import os

output = "Hello"

def save_result(text, folder="result1", filename="hello_output.txt"):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path

print(output)
output_path = save_result(output)
print(f"Saved result to: {output_path}")
