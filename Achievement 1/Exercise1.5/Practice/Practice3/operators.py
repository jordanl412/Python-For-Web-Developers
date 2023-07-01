class Height:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        output = f'{self.feet} feet and {self.inches} inches'
        return output

    def __gt__(self, other):
        #Converting both objects' heights into inches
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches
        #Checking if height A is greater than height B
        return height_A_inches > height_B_inches

    def __ge__(self, other):
        #Converting both objects' heights into inches
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches
        #Checking if height A is greater than or equal to height B
        return height_A_inches >= height_B_inches

    def __ne__(self, other):
        #Converting both objects' heights into inches
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches
        #Checking if height A is NOT equal to height B
        return height_A_inches != height_B_inches


