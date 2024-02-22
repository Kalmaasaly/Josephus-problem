import math

def highest_power_of_2(n: int) -> int:
    """
    Returns the highest power of 2 less than or equal to the given number 'n'.
    
    Parameters:
    - n (int): The input integer for which the highest power of 2 needs to be calculated.
    
    Returns:
    - int: The highest power of 2 less than or equal to 'n'.
    """
    power = math.floor(math.log2(n))
    result = 2 ** power
    return result

def get_number_soldiers(prompt: str) -> int:
    """
    Takes user input for the number of soldiers in Joseph's Cave, ensuring it's a non-negative integer.
    
    Parameters:
    - prompt (str): The prompt to be displayed to the user.
    
    Returns:
    - int: The number of soldiers entered by the user.
    """
    while True:
        try:
            soldiers = int(input(prompt))
            if soldiers >= 0:
                return soldiers
        except ValueError:
            print("Invalid input: Please enter a valid integer.")

def get_safe_place(number_soldiers: int, power_of_2: int)->int:
    difference = number_soldiers - power_of_2
    joseph_site = 2 * difference + 1
    return joseph_site

def main() -> None:
    """
    The main function that calculates Joseph's survival position based on the number of soldiers in the cave.
    """
    number_soldiers = get_number_soldiers("How many soldiers are in Joseph's Cave? ")
    power_of_2 = highest_power_of_2(number_soldiers)
    joseph_site = get_safe_place(number_soldiers, power_of_2)
    print(f"Joseph's survival relies on being situated at {joseph_site}")



if __name__ == "__main__":
    main()
