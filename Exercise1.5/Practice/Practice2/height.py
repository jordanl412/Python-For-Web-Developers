class Height:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        output = f'{self.feet} feet and {self.inches} inches'
        return output

    def __sub__(self, other):
        #Converting both objects' heights into inches
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches

        #Subtracting
        difference_height_inches = height_A_inches - height_B_inches

        #Getting output in feet
        output_feet = difference_height_inches // 12

        #Getting output in inches
        output_inches = difference_height_inches - (output_feet * 12)

        #Returning final output as new Height object
        return Height(output_feet, output_inches)

person_A_height = Height(5, 10)
person_B_height = Height(3, 9)
height_difference = person_A_height - person_B_height

print('Total height: ', height_difference)
