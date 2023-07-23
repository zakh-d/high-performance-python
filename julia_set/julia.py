"""Julia set generator without optional PIL-based image drawing """

# area of complex space to investigate
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -0.42193


def calculate_z_serial_purepython(max_iter, zs, cs):
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while n < max_iter and abs(z) < 2:
            z = z * z + c
            n += 1
        output[i] = n
    return output


def calc_pure_python(desired_width, max_iterations):
    """"Create a list of complex coordinates (zs) and complex parameters (cs),
     build Julia set"""
    x_step = (x2 - x1) / desired_width
    y_step = (y1 - y2) / desired_width
    x = []
    y = []

    y_coord = y2
    while y_coord > y1:
        y.append(y_coord)
        y_coord += y_step

    x_coord = x1
    while x_coord < x2:
        x.append(x_coord)
        x_coord += x_step
    # build a list of coordinates and the initial condition for each cell.
    # Note that our initial condition is a constant and could easily be removed
    # we use it to simulate a real-world scenario with several inputs to our
    # function
    zs = []
    cs = []
    for y_coord in y:
        for x_coord in x:
            zs.append(complex(x_coord, y_coord))
            cs.append(complex(c_real, c_imag))

    print("Length of x:", len(x))
    print("Total elements:", len(zs))
    output = calculate_z_serial_purepython(max_iterations, zs, cs)

    return zs, output


if __name__ == '__main__':
    calc_pure_python(1000, 300)
