import math


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print("Współrzędna x : ", self.x, " y :", self.y)

    def set_position_zero(self):
        self.x = 0
        self.y = 0


class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def print_point_3d(self):
        print("Współrzedna x: ", self.x, " y: ", self.y, "z :", self.z)

    def set_zero_point_position_3_d(self):
        super().set_position_zero()
        self.z = 0


class LengthLine(Point2D):

    def __init__(self, x, y, x1, y1):
        super().__init__(x, y)
        self.x1 = x1
        self.y1 = y1

    def print_two_point(self):
        print("A -> x1=", self.x, "y1=", self.y, "B-> x2=", self.x1, "y2+",
              self.y1)

    def calculate_length_line(self):
        sub_x2_x1 = (self.x1 - self.x)
        sub_y2_y1 = (self.y1 - self.y)
        pow_x = pow(sub_x2_x1, 2)
        pow_y = pow(sub_y2_y1, 2)
        sum_pow_x_and_y = pow_x + pow_y
        length = math.sqrt(sum_pow_x_and_y)
        return length
