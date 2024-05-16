from pathlib import Path
from typing import Union, List
from hashlib import sha256

def verify(ans_file, num_test):
    out = f"{ans_file}: FAILED"
    answers = {
        1: "26db825d95ae7d4e17d390da877d34dc0860f5b488b3edf43faa3a5219cba2f5",
        2: "03ad2675505e9dce6ad4947b180cf46f8973d2247e8c5f350acef14f240a4a8e",
        3: "90010567bc90a40ab638e6af16871dc1daef99358fa7b6046a5ecd69ef44d548",
    }
    ans = answers[num_test]
    with open(ans_file, "r") as f:
        if ans == sha256(f.read().encode("utf-8")).hexdigest():
            out = f"{ans_file}: SUCCEED"
    print(out)

def read_input(input_file: Union[str, Path]) -> List[Union[int, str]]:
    cases = []

    with open(input_file, "r") as f:
        T = int(f.readline().strip())
        for _ in range(T):
            line = f.readline().strip()
            try:
                N = eval(line)  
                if isinstance(N, int) and 0 <= N < 10**30:
                    cases.append(N)
                else:
                    raise ValueError("Invalid number or expression.")
            except (ValueError, SyntaxError):
                
                try:
                    N = int(line.strip('"'))  
                    if 0 <= N < 10**30:
                        cases.append(N)
                except ValueError:
                    pass  

    return cases

def process_case(n: Union[int, str]) -> Union[int, str]:
    if isinstance(n, int):
        if n == 0:
            return "INSOMNIA"
        
        digits_seen = set()
        i = 1
        while len(digits_seen) < 10:
            current_number = n * i
            digits_seen.update(str(current_number))
            i += 1
        
        return current_number
    else:
        return n  

def generate_output(test_file: Union[str, Path], save_to: Union[str, Path]) -> str:
    out = ""
    cases = read_input(test_file)
    with open(save_to, "w") as f:
        for idx, n in enumerate(cases, start=1):
            result = process_case(n)
            f.write(f"Case #{idx}: {result}\n")
            out += f"Case #{idx}: {result}\n"
    return out

out = generate_output(
    test_file="test1.in", 
    save_to="test1_resultado",
)
print(out)
verify(ans_file="test1_resultado", num_test=1)

out = generate_output(
    test_file="test2.in", 
    save_to="test2_resultado",
)
print(out)
verify(ans_file="test2_resultado", num_test=2)

out = generate_output(
    test_file="test3.in", 
    save_to="test3_resultado",
)
print(out)
verify(ans_file="test3_resultado", num_test=3)
