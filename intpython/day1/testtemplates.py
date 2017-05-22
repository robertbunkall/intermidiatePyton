import math
class Point:

    """
    Represents a point in a 2-D geometric space
    """
    def __init__(self, x=0, y=0):
        """
        Intializes the position of a new point.
        If they are not specified, the point default to the origin
        :param x: x coordinate
        :param y: y coordinate
        """
        self.x = x
        self.y = y

    def reset(self):

          """
          Resert the point to the origin in 2D space,
          :return:
          """



    def move(self, x, y):
        """
        Move a point to new location in 2D space
        :param x: x-coordinate
        :param y: y-coordinate
        :return:
        """

        self.x = x
        self.y = y

    def calculate_distance(self, other_point):
        """
        Calculate the distance from this point to a second point passed
        as a parameter.
        This funcdtion used pythagorean therorum
        :param other_point: secpmd [pomt tp ca;ci;ate distance
        :return: The distance bertween two points (float)
        """


        return math.sqrt(
            (self.x - other_point.x)**2 +
             (self.y-other_point.y)**2)



def main():
    p1 = Point()
    print(p1.x, p1.y)
    p2 = Point(5,8)
    print(p2.x, p2.y)
    p2.reset()
    print(p2)




if __name__ == '__main__':
    main()
    exit(0)
