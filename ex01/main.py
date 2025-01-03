from .vector import Vector
from colorama import Fore, init

def main():
    # Example 1: Basic linear combination
    init()  # Initialize colorama
    print(f"{Fore.CYAN}Example 1: Basic linear combination{Fore.RESET}")
    vectors1 = [[1, 2, 3], [4, 5, 6]]
    scalars1 = [2, 1]
    print(f"{Fore.YELLOW}Vectors: {vectors1}{Fore.RESET}")
    print(f"{Fore.GREEN}Scalars: {scalars1}{Fore.RESET}")
    try:
        result1 = Vector.linear_combination(vectors1, scalars1)
        print(f"{Fore.MAGENTA}Result: {result1}{Fore.RESET}")
    except ValueError as e:
        print(f"{Fore.RED}{e}{Fore.RESET}")

    # Example 2: Linear combination with more vectors
    print(f"\n{Fore.CYAN}Example 2: Linear combination with three vectors{Fore.RESET}")
    vectors2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    scalars2 = [2, -1, 3]
    print(f"{Fore.YELLOW}Vectors: {vectors2}{Fore.RESET}")
    print(f"{Fore.GREEN}Scalars: {scalars2}{Fore.RESET}")
    try:
        result2 = Vector.linear_combination(vectors2, scalars2)
        print(f"{Fore.MAGENTA}Result: {result2}{Fore.RESET}")
    except ValueError as e:
        print(f"{Fore.RED}{e}{Fore.RESET}")

    # Example 3: Error case - mismatched vectors and scalars
    print(f"\n{Fore.CYAN}Example 3: Error case{Fore.RESET}")
    vectors3 = [[1, 1], [2, 2], [3, 3]]
    scalars3 = [1, 2]
    print(f"{Fore.YELLOW}Vectors: {vectors3}{Fore.RESET}")
    print(f"{Fore.GREEN}Scalars: {scalars3}{Fore.RESET}")
    try:
        result3 = Vector.linear_combination(vectors3, scalars3)
        print(f"{Fore.MAGENTA}Result: {result3}{Fore.RESET}")
    except ValueError as e:
        print(f"{Fore.RED}{e}{Fore.RESET}")
    
if __name__ == "__main__":
    main()
