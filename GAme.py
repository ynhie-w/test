def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    print(f"Think of a number between 1 and {x} (inclusive), and I will try to guess it!")
    
    while feedback != 'c':
        if low != high:
            guess = (low + high) // 2
        else:
            guess = low  # low and high are equal
            
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f"Yay! I guessed your number, {guess}, correctly!")

# Bắt đầu trò chơi
computer_guess(100)
