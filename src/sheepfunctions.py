import re
from typing import List, Union
from pathlib import Path
from word2number import w2n

def eval_int_exp(exp: str) -> int:
    """
    Safely evaluates a mathematical expression, numeric words, or strings representing numbers as an integer.
    Converts strings like "zero", "two thousand twenty three", etc., to their integer form.
    
    Args:
        exp (str): A string representing a mathematical expression or number in words.
    
    Returns:
        int: The evaluated integer, or None if it's not valid.
    """
    try:
        exp = exp.strip()
        
        # Step 1: If the expression is wrapped in quotes, remove them and check if it's numeric
        if exp.startswith('"') and exp.endswith('"'):
            exp = exp[1:-1]  # Remove the quotes
            if exp.isdigit():
                return int(exp)

        # Step 2: Check if it's a valid integer or mathematical expression (e.g., "10**29", "2*50-100")
        if re.match(r'^[0-9\+\-\*\/\(\)\s]+$', exp):
            return eval(exp)  # Evaluate safe arithmetic expressions
        
        # Step 3: Convert a number written in words (e.g., "two thousand twenty three")
        elif re.match(r'^[a-zA-Z\s\-]+$', exp):
            return w2n.word_to_num(exp)  # Convert words to numbers
        
        return None
    except Exception:
        return None

def read_input(input_file: Union[str, Path]) -> List[int]:
    """
    Reads the input file and returns a list of integers representing test cases.
    Ignores invalid inputs (non-integers or malformed expressions).
    
    Args:
        input_file (Union[str, Path]): The path to the input file.
    
    Returns:
        List[int]: A list of valid integers from the input file.
    """
    cases = []
    with open(input_file, 'r') as file:
        T = int(file.readline().strip())  # Number of test cases
        for _ in range(T):
            exp = file.readline().strip()
            N = eval_int_exp(exp)  # Evaluate and validate the input expression
            if N is not None and 0 <= N < 10**30:  # Ensure N is within the valid range
                cases.append(N)
    return cases

def process_case(n: int) -> Union[int, str]:
    """
    Processes a single test case and determines the last multiple of N before Bleatrix falls asleep.
    
    Args:
        n (int): The number chosen by Bleatrix.
    
    Returns:
        Union[int, str]: The last number counted before Bleatrix falls asleep, or 'INSOMNIA' if she never sees all digits.
    """
    if n == 0:
        return "INSOMNIA"
    
    seen_digits = set()
    current_multiple = 0
    multiplier = 1
    
    while len(seen_digits) < 10:
        current_multiple = n * multiplier
        seen_digits.update(str(current_multiple))  # Add digits to the set
        multiplier += 1
        
    return current_multiple

def generate_output(input_file: Union[str, Path], output_file: Union[str, Path]) -> str:
    """
    Processes all test cases and writes the results to an output file in the expected format.
    
    Args:
        input_file (Union[str, Path]): The path to the input file containing test cases.
        output_file (Union[str, Path]): The path to the output file where results will be saved.
    
    Returns:
        str: A string representation of the output file content.
    """
    cases = read_input(input_file)
    results = []
    
    for i, case in enumerate(cases, start=1):
        result = process_case(case)
        results.append(f"Case #{i}: {result}")
    
    with open(output_file, 'w') as file:
        file.write("\n".join(results) + "\n")  # Ensure correct format with final newline
    
    return "\n".join(results) + "\n"
