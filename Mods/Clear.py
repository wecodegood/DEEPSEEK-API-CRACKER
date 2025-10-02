def clean():
    import os
    """
    this function runs the optimized command to clean the terminal
    """
    os.system('cls') if os.name == 'nt' else os.system('clean')
