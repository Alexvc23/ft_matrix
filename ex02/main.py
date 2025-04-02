from vector import Vector
from matrix import Matrix
from colorama import Fore, Style, init

def main():
    # Initialize colorama
    init()
    
    print(Fore.CYAN + "Linear Interpolation Demo for ex02" + Style.RESET_ALL)
    
    # Vector interpolation demonstration
    print(Fore.GREEN + "\nVector Interpolation:" + Style.RESET_ALL)
    v1 = Vector([2.0, 1.0])
    v2 = Vector([4.0, 2.0])
    t_v = 0.3
    interpolated_vector = Vector.lerp(v1, v2, t_v)
    print(f"{Fore.YELLOW}v1: {v1}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}v2: {v2}{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}Interpolated vector (t = {t_v}): {interpolated_vector}{Style.RESET_ALL}")
    
    # Matrix interpolation demonstration
    print(Fore.GREEN + "\nMatrix Interpolation:" + Style.RESET_ALL)
    m1 = Matrix([[2.0, 1.0], [3.0, 4.0]])
    m2 = Matrix([[20.0, 10.0], [30.0, 40.0]])
    t_m = 0.5
    interpolated_matrix = Matrix.lerp(m1, m2, t_m)
    print(f"{Fore.YELLOW}Matrix 1:{Style.RESET_ALL}")
    print(f"{Fore.BLUE}{m1}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Matrix 2:{Style.RESET_ALL}")
    print(f"{Fore.BLUE}{m2}{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}Interpolated matrix (t = {t_m}):{Style.RESET_ALL}")
    print(f"{Fore.BLUE}{interpolated_matrix}{Style.RESET_ALL}")

if __name__ == '__main__':
    main()
