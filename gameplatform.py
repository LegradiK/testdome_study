def calculate_final_speed(initial_speed, inclinations):
    life = 3
    speed = initial_speed
    for i in inclinations:
        speed = speed - i
        if 0 >= speed:
            life -= 1
            speed = 0
            break
    return speed



print(calculate_final_speed(60, [0, 30, 0, -45, 0]))