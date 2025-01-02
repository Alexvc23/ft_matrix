from ex00.vector import Vector
from ex00.matrix import Matrix
from colorama import Fore, init

def main():
    """
    Demonstrates the usage of the Vector and Matrix classes by performing
    various operations such as addition, subtraction, and scaling.
    """
    # Initialize colorama
    init()

    # Example usage of Vector class
    print(f"{Fore.BLUE}Starting Vector operations demonstration...{Fore.RESET}")

    # Initialize two Objects Vector
    u = Vector([2.0, 3.0])
    v = Vector([5.0, 7.0])
    print(f"{Fore.GREEN}Initialized vectors:\n"
          f"u = {u.data}\n"
          f"v = {v.data}{Fore.RESET}")

    # Add two vectors
    print(f"\n{Fore.YELLOW}Adding vectors u + v:{Fore.RESET}")
    u.add(v)
    print(f"{Fore.CYAN}Result: {u.data}{Fore.RESET}")

    # Reset vector u and subtract vectors
    print(f"\n{Fore.YELLOW}Subtracting vectors u - v:{Fore.RESET}")
    u = Vector([2.0, 3.0])
    print(f"{Fore.MAGENTA}Reset u to: {u.data}{Fore.RESET}")
    u.sub(v)
    print(f"{Fore.CYAN}Result: {u.data}{Fore.RESET}")

    # Scale Vector u by 2
    print(f"\n{Fore.YELLOW}Scaling vector u by 2:{Fore.RESET}")
    u = Vector([2.0, 3.0])
    print(f"{Fore.MAGENTA}Reset u to: {u.data}{Fore.RESET}")
    u.scl(2)
    print(f"{Fore.CYAN}Result: {u.data}{Fore.RESET}")


    # -------------------------------------------------------------------------------------------------------

    # Example usage of Matrix class
    print(f"\n{Fore.BLUE}Starting Matrix operations demonstration...{Fore.RESET}")
    
    # Initialize two Matrices
    A = Matrix([[1.0, 2.0, 3.0], 
                [4.0, 5.0, 6.0], 
                [7.0, 8.0, 9.0]])

    B = Matrix([[2.0, -1.0, 4.0], 
                [0.0, 3.0, -2.0], 
                [1.0, 5.0, -3.0]])
    print(f"{Fore.GREEN}Initialized matrices:")
    print("A =")
    for row in A.data:
        print([f"{x:6.1f}" for x in row])
    print("\nB =")
    for row in B.data:
        print([f"{x:6.1f}" for x in row])
    print(f"{Fore.RESET}")

    # ?Add two matrices
    print(f"\n{Fore.YELLOW}Adding matrices A + B:{Fore.RESET}")
    A.add(B)
    print(f"{Fore.CYAN}Result:")
    for row in A.data:
        print([f"{x:6.1f}" for x in row])
    print(f"{Fore.RESET}")

    # ?subtract matrices
    print(f"\n{Fore.YELLOW}Subtracting matrices A - B:{Fore.RESET}")
    A = Matrix([[1.0, 2.0, 3.0], 
                [4.0, 5.0, 6.0], 
                [7.0, 8.0, 9.0]])
    print(f"{Fore.MAGENTA}Reset A to:")
    for row in A.data:
        print([f"{x:6.1f}" for x in row])
    print(f"{Fore.RESET}")
    print(f"{Fore.GREEN}\nB =")
    for row in B.data:
        print([f"{x:6.1f}" for x in row])
    print(f"{Fore.RESET}")
    A.sub(B)
    print(f"{Fore.CYAN}Result:")
    for row in A.data:
        print([f"{x:6.1f}" for x in row])
    print(f"{Fore.RESET}")

    # ?Scale Matrix A by 2
    print(f"\n{Fore.YELLOW}Scaling matrix A by 2:{Fore.RESET}")
    A = Matrix([[1.0, 2.0, 3.0], 
                [4.0, 5.0, 6.0], 
                [7.0, 8.0, 9.0]])
    print(f"{Fore.MAGENTA}Reset A to:")
    for row in A.data:
        print([f"{x:6.1f}" for x in row])
    print(f"{Fore.RESET}")
    A.scl(2)
    print(f"{Fore.CYAN}Result:")
    for row in A.data:
        print([f"{x:6.1f}" for x in row])
    print(f"{Fore.RESET}")


if __name__ == "__main__":
    main()
