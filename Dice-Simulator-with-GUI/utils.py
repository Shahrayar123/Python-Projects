
def generate_circle_points(dice_location: int, dice_number: int):
    '''
    Shifts the x-coordinate of the dice dot by
    a unit of 50. This generates the number of 
    dice "dots" to display based on the value of 
    dice_number
    '''
    points = []
    for _ in range(dice_number):
        dice_location += 50
        points.append(dice_location)
    return points 
 
