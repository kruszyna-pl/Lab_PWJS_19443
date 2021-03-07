import mojeklasy


def testy():
    print("Zadanie 1")
    print("Wydruk ustawionego punktu 2D")
    point2_d = mojeklasy.Point2D(7, 19)
    point2_d.print_point()
    print("Wydruk wyzerowanego punktu 2D")
    point2_d.set_position_zero()
    point2_d.print_point()
    print("Zadanie 2 ")
    print("Wydruk punktu 3D")
    point = mojeklasy.Point3D(100, 150, 200)
    point.print_point_3d()
    print("Wyzerowanie punktu 3D")
    point.set_zero_point_position_3_d()
    point.print_point_3d()
    print("Zadanie 3")
    point_to_calculate_length = mojeklasy.LengthLine(5, 2, 1, 6)
    point_to_calculate_length.print_two_point()
    print("Wydruk długości odcinka")
    print(point_to_calculate_length.calculate_length_line())


if __name__ == "__main__":
    testy()
