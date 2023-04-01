import cmath

def calc_koofisien_korelasi(x,y,x2,y2,xy):
    print()
    
    pg = (7*xy) - (x*y)
    py = (7*x2) - (x*x) * (7*y2) - (y*y)
    r = pg/cmath.sqrt(py)

    print("Koofisien Korelasi R: {}".format(r))

def find_koofisien_ab(x,y,x2,y2,xy):
    a_pg = (y*x2) - (x*xy)
    a_py = (7*x2) - (x*x)
    a = a_pg/a_py

    b_pg = (7*xy) - (x*y)
    b_py = (7*x2) - (x*x)
    b = b_pg/b_py

    return a,b

def regresi_linear(a,b,x):
    y = a + (b*x)

    return y

if __name__ == "__main__":
    data_x = [25468, 25465, 25954, 25932, 21252, 17441, 14198]
    data_y = [306, 305, 321, 327, 291, 272, 251]
    data_x2 = []
    data_y2 = []
    data_xy = []
    
    print("No\tX\tY\tX^2\t\tY^2\tXY")
    for i in range(7):
        data_x2.append(data_x[i] * data_x[i])
        data_y2.append(data_y[i] * data_y[i])
        data_xy.append(data_x[i] * data_y[i])
        print("{}\t{}\t{}\t{}\t{}\t{}".format(i+1, data_x[i], data_y[i], data_x2[i], data_y2[i], data_xy[i]))
    
    data_x_sum = sum(data_x)
    data_y_sum = sum(data_y)
    data_x2_sum = sum(data_x2)
    data_y2_sum = sum(data_y2)
    data_xy_sum = sum(data_xy)

    print("Jumlah\t{}\t{}\t{}\t{}\t{}".format(data_x_sum, data_y_sum, data_x2_sum, data_y2_sum, data_xy_sum))
    calc_koofisien_korelasi(data_x_sum, data_y_sum, data_x2_sum, data_y2_sum, data_xy_sum)
    a, b = find_koofisien_ab(data_x_sum, data_y_sum, data_x2_sum, data_y2_sum, data_xy_sum)

    print("A: ", a)
    print("B: ", b)
    x=int(input("Masukkan Variabel bebas x:"))
    y = regresi_linear(a,b,x)
    print(y)

