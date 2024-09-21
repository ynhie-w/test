import random

def generate_funny_face():
    # Các phần của khuôn mặt
    eyes = ['o', 'O', '0', '-', 'x', 'X']
    noses = ['<', '-', '^', 'v', 'o']
    mouths = ['_', '.', 'o', 'O', 'w', 'W', 'v', 'u', 'U']
    
    # Tạo khuôn mặt ngẫu nhiên
    face = f" {random.choice(eyes)} {random.choice(noses)} {random.choice(eyes)} \n"
    face += f"   {random.choice(mouths)}   "
    
    print("Here's your funny face:")
    print(face)

# Tạo khuôn mặt ngộ nghĩnh
generate_funny_face()
