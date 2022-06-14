
# return img, nested list
def read_ppm_file(f):
    fp = open(f)
    fp.readline()  # reads P3 (assume it is P3 file)
    lst = fp.read().split()
    n = 0
    n_cols = int(lst[n])
    n += 1
    n_rows = int(lst[n])
    n += 1
    max_color_value = int(lst[n])
    n += 1
    img = []
    for r in range(n_rows):
        img_row = []
        for c in range(n_cols):
            pixel_col = []
            for i in range(3):
                pixel_col.append(int(lst[n]))
                n += 1
            img_row.append(pixel_col)
        img.append(img_row)
    fp.close()
    return img, max_color_value


# Works
def img_printer(img):
    row = len(img)
    col = len(img[0])
    cha = len(img[0][0])
    for i in range(row):
        for j in range(col):
            for k in range(cha):
                print(img[i][j][k], end=" ")
            print("\t|", end=" ")
        print()


filename = input()
operation = int(input())


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE


if operation == 1:
    min = int(input())
    max = int(input())
    newlist = []

    image, maxcolor = read_ppm_file(filename)
    for i in range(len(image)): #changing the board
        for j in range(len(image[i])):
            for k in range(len(image[i][j])):
                x = float("{0:.4f}".format((image[i][j][k]/maxcolor)*(max-min)+min))
                image[i][j][k] = x
    img_printer(image)

if operation == 2:
    image, maxcolor = read_ppm_file(filename)
    elem = 0
    sumred = 0
    sumgreen = 0
    sumblue = 0
    for i in range(len(image)): #calculating sum of the colors to calculate mean of them
        for j in range(len(image[i])):
            elem = elem + 1
            sumred = sumred + image[i][j][0]
            sumgreen = sumgreen + image[i][j][1]
            sumblue = sumblue + image[i][j][2]
    meanred = sumred/elem
    meangreen = sumgreen/elem
    meanblue = sumblue/elem

    deviationredsum = 0
    deviationgreensum = 0
    deviationbluesum = 0
    for i in range(len(image)): #calculating deviation of colors
        for j in range(len(image[i])):
            deviationredsum = deviationredsum + (image[i][j][0] - meanred)**2
            deviationgreensum = deviationgreensum + (image[i][j][1] - meangreen)**2
            deviationbluesum = deviationbluesum + (image[i][j][2] - meanblue)**2
    deviationred = ((deviationredsum/elem)**(1/2)) + 1e-6
    deviationgreen = ((deviationgreensum/elem)**(1/2)) + 1e-6
    deviationblue = ((deviationbluesum/elem)**(1/2)) + 1e-6

    for i in range(len(image)): #changing the board
        for j in range(len(image[i])):
            image[i][j][0] = float("{0:.4f}".format((image[i][j][0]-meanred)/deviationred))
            image[i][j][1] = float("{0:.4f}".format((image[i][j][1]-meangreen)/deviationgreen))
            image[i][j][2] = float("{0:.4f}".format((image[i][j][2]-meanblue)/deviationblue))
    img_printer(image)

if operation == 3:
    image, maxcolor = read_ppm_file(filename)
    for i in range(len(image)): #changing the board
        for j in range(len(image[i])):
            mean = 0
            mean = int((image[i][j][0] + image[i][j][1] + image[i][j][2]) / 3) #calculating mean
            image[i][j][0] = mean
            image[i][j][1] = mean
            image[i][j][2] = mean
    img_printer(image)

if operation == 4:
    image, maxcolor = read_ppm_file(filename)
    dosya = open(input())
    stride = int(input())
    liste = dosya.read().split()
    n = int(len(liste)**(1/2))
    listeboard = []
    for i in range(n): #creating board of the given filter
        listeboard.append([])
        if i == n-1:
            listeboard[i] = liste
        else:
            listeboard[i] = liste[:n]
            liste = liste[n:]
    x = int((int(len(liste))-1)/2) #it is the number of lost pixels because of the filter
    imagenew = []
    for i in range(x,len(image)-x,stride):
        for j in range(x,len(image[i])-x,stride):
            for k in range(len(image[i][j])):
                sumoffilter = 0
                for line in range(len(listeboard)): #applying filter to the picture
                    for row in range(len(listeboard[line])):
                        sumoffilter = sumoffilter + float(int(image[i-x+line][j-x+row][k]) * float(listeboard[line][row]))
                if sumoffilter < 0:
                    sumoffilter = 0
                if sumoffilter > int(maxcolor):
                    sumoffilter = int(maxcolor)
                imagenew.append(int(sumoffilter)) #saving data to convert it to the board
                sumoffilter = 0
    imagelast = []
    newlistlinenumber = int((len(imagenew)/3) ** (1 / 2))
    for i in range(newlistlinenumber):#creating board
        imagelast.append([])
        for j in range(newlistlinenumber):
            imagelast[i].append([])
            for k in range(3):
                imagelast[i][j].append(imagenew[0])
                imagenew.remove(imagenew[0])
    img_printer(imagelast)

    def write_image(img, name):
        image_file = open(name, 'w')
        for i in range(len(img)):
            for j in range(len(img[0])):
                for k in range(3):
                    image_file.write(str(img[i][j][k]) + ' ')
                image_file.write("\t|" + " ")
            image_file.write('\n')

        image_file.close()
    write_image(imagelast,"deneme1.txt")

if operation == 5:
    image, maxcolor = read_ppm_file(filename)
    dosya = open(input())
    stride = int(input())
    liste = dosya.read().split()
    n = int(len(liste) ** (1 / 2))
    listeboard = []
    for i in range(n): #creating board of the given filter
        listeboard.append([])
        if i == n - 1:
            listeboard[i] = liste
        else:
            listeboard[i] = liste[:n]
            liste = liste[n:]
    x = int((int(len(liste))-1)/2)

    pad = []
    for i in range(len(image) + (2*x)): #creating a pad based on filter size
        pad.append([0,0,0])
    for i in range(int(len(image))): #padding
        for j in range(x):
            image[i].insert(0,[0,0,0])
            image[i].append([0,0,0])
    for i in range(x):
        image.insert(0,pad)
        image.append(pad)

    imagenew = []
    for i in range(x, len(image) - x, stride): #same as operation 4
        for j in range(x, len(image[i]) - x, stride):
            for k in range(len(image[i][j])):
                sumoffilter = 0
                for line in range(len(listeboard)):
                    for row in range(len(listeboard[line])):
                        sumoffilter = sumoffilter + float(int(image[i - x + line][j - x + row][k]) * float(listeboard[line][row]))
                if sumoffilter < 0:
                    sumoffilter = 0
                if sumoffilter > maxcolor:
                    sumoffilter = maxcolor
                imagenew.append(int(sumoffilter))
                sumoffilter = 0

    imagelast = []
    newlistlinenumber = int((len(imagenew)/3) ** (1 / 2))
    for i in range(newlistlinenumber):
        imagelast.append([])
        for j in range(newlistlinenumber):
            imagelast[i].append([])
            for k in range(3):
                imagelast[i][j].append(imagenew[0])
                imagenew.remove(imagenew[0])
    img_printer(imagelast)


    def write_image(img, name):
        image_file = open(name, 'w')
        for i in range(len(img)):
            for j in range(len(img[0])):
                for k in range(3):
                    image_file.write(str(img[i][j][k]) + ' ')
                image_file.write("\t|" + " ")
            image_file.write('\n')

        image_file.close()
    write_image(imagelast,"deneme1.txt")

if operation == 6:
    image, maxcolor = read_ppm_file(filename)
    range_number = int(input())
    def operationsix(image, rangenumber, k = 0, x = 0, y = 0, temporaryk = 0):
        if k == 0: # k is the variable to decide the direction of the iterating
            if x == 0 and y == len(image)-1 and int(len(image)) % 2 == 0:
                return img_printer(image)
            if temporaryk == 1:# temporaryk is the second variable to change the movement to the horizontal mode
                flag = True
                for c in range(3): #changing board
                    if (int(image[x][y][c]) - int(image[x][y+1][c])) >= rangenumber or (int(image[x][y][c]) - int(image[x][y+1][c])) <= -rangenumber:
                        flag = False
                    if flag == False:
                        break
                if flag == True:
                    for c in range(3):
                        image[x][y+1][c] = int(image[x][y][c])
                temporaryk = 0
                return operationsix(image, rangenumber, k, x, y+1, temporaryk)
            else:
                flag = True
                for c in range(3):#changing board
                    if (int(image[x][y][c]) - int(image[x+1][y][c])) >= rangenumber or (int(image[x][y][c]) - int(image[x+1][y][c])) <= -rangenumber:
                        flag = False
                    if flag == False:
                        break
                if flag == True:
                    for c in range(3):
                        image[x+1][y][c] = int(image[x][y][c])
                if (x+1) == int(len(image))-1:#this part tells us that it is the last pixel of the column
                    k = 1
                    temporaryk = 1
                    return operationsix(image, rangenumber, k, x+1, y, temporaryk)
                else:
                    return operationsix(image, rangenumber, k, x+1, y, temporaryk)


        if k == 1: #same as k=0
            if x == int(len(image))-1 and y == int(len(image))-1 and int(len(image)) % 2 == 1:
                return img_printer(image)
            if temporaryk == 1:
                flag = True
                for c in range(3):
                    if (int(image[x][y][c]) - int(image[x][y+1][c])) >= rangenumber or (int(image[x][y][c]) - int(image[x][y+1][c])) <= -rangenumber:
                        flag = False
                    if flag == False:
                        break
                if flag == True:
                    for c in range(3):
                        image[x][y+1][c] = int(image[x][y][c])
                temporaryk = 0
                return operationsix(image, rangenumber, k, x, y+1, temporaryk)

            else:
                flag = True
                for c in range(3):
                    if (int(image[x-1][y][c]) - int(image[x][y][c])) >= rangenumber or (int(image[x-1][y][c]) - int(image[x][y][c])) <= -rangenumber:
                        flag = False
                    if flag == False:
                        break
                if flag == True:
                    for c in range(3):
                        image[x - 1][y][c] = int(image[x][y][c])
                if (x-1) == 0:
                    k = 0
                    temporaryk = 1
                    return operationsix(image, rangenumber, k, x-1, y, temporaryk)
                else:
                    return operationsix(image, rangenumber, k, x - 1, y, temporaryk)

    operationsix(image, range_number)

if operation == 7:
    image, maxcolor = read_ppm_file(filename)
    range_number = int(input())
    def operationseven(image, rangenumber, k=0, x=0, y=0, temporaryk=0, c=0):
        if k == 0 and c != 1: #same as operation 6 but this time there is one more variable which represents the color
            if x == 0 and y == len(image) - 1 and int(len(image)) % 2 == 0:
                if c == 2:
                    return img_printer(image)
                else:
                    c += 1
                    k = 0
                    temporaryk = 0
                    flag = True
                    if (int(image[x][y][c-1]) - int(image[x][y][c])) >= rangenumber or (int(image[x][y][c-1]) - int(image[x][y][c])) <= -rangenumber:
                        flag = False
                    if flag == True:
                        image[x][y][c] = int(image[x][y][c-1])
                    return operationseven(image, rangenumber, k, x, y, temporaryk, c)
            if temporaryk == 1:
                flag = True
                if (int(image[x][y][c]) - int(image[x][y + 1][c])) >= rangenumber or (int(image[x][y][c]) - int(image[x][y + 1][c])) <= -rangenumber:
                    flag = False
                if flag == True:
                    image[x][y + 1][c] = int(image[x][y][c])
                temporaryk = 0
                return operationseven(image, rangenumber, k, x, y + 1, temporaryk, c)
            else:
                flag = True
                if (int(image[x][y][c]) - int(image[x + 1][y][c])) >= rangenumber or (int(image[x][y][c]) - int(image[x + 1][y][c])) <= -rangenumber:
                    flag = False
                if flag == True:
                    image[x + 1][y][c] = int(image[x][y][c])
                if (x + 1) == int(len(image)) - 1:
                    k = 1
                    temporaryk = 1
                    return operationseven(image, rangenumber, k, x + 1, y, temporaryk, c)
                else:
                    return operationseven(image, rangenumber, k, x + 1, y, temporaryk, c)

        if k == 1 and c != 1:
            if x == int(len(image)) - 1 and y == int(len(image)) - 1 and int(len(image)) % 2 == 1:
                if c == 2:
                    return img_printer(image)
                else:
                    c += 1
                    k = 1
                    flag = True
                    if (int(image[x][y][c - 1]) - int(image[x][y][c])) >= rangenumber or (int(image[x][y][c - 1]) - int(image[x][y][c])) <= -rangenumber:
                        flag = False
                    if flag == True:
                        image[x][y][c] = int(image[x][y][c - 1])
                    return operationseven(image, rangenumber, k, x, y, temporaryk, c)
            if temporaryk == 1:
                flag = True
                if (int(image[x][y][c]) - int(image[x][y + 1][c])) >= rangenumber or (int(image[x][y][c]) - int(image[x][y + 1][c])) <= -rangenumber:
                    flag = False
                if flag == True:
                    image[x][y + 1][c] = int(image[x][y][c])
                temporaryk = 0
                return operationseven(image, rangenumber, k, x, y + 1, temporaryk, c)

            else:
                flag = True
                if (int(image[x - 1][y][c]) - int(image[x][y][c])) >= rangenumber or (int(image[x - 1][y][c]) - int(image[x][y][c])) <= -rangenumber:
                    flag = False
                if flag == True:
                    image[x - 1][y][c] = int(image[x][y][c])
                if (x - 1) == 0:
                    k = 0
                    temporaryk = 1
                    return operationseven(image, rangenumber, k, x - 1, y, temporaryk, c)
                else:
                    return operationseven(image, rangenumber, k, x - 1, y, temporaryk, c)

        if c == 1:#this is the reverse direction part
            if k == 0:
                if x == 0 and y == 0 and int(len(image)) % 2 == 0:
                    c += 1
                    temporaryk = 0
                    flag = True
                    if (-int(image[x][y][c - 1]) + int(image[x][y][c])) >= rangenumber or (- int(image[x][y][c - 1]) + int(image[x][y][c])) <= -rangenumber:
                        flag = False
                    if flag == True:
                        image[x][y][c] = int(image[x][y][c - 1])
                    return operationseven(image, rangenumber, k, x, y, temporaryk, c)
                if temporaryk == 1:
                    flag = True
                    if (-int(image[x][y][c]) + int(image[x][y - 1][c])) >= rangenumber or (-int(image[x][y][c]) + int(image[x][y - 1][c])) <= -rangenumber:
                        flag = False
                    if flag == True:
                        image[x][y - 1][c] = int(image[x][y][c])
                    temporaryk = 0
                    return operationseven(image, rangenumber, k, x, y - 1, temporaryk, c)
                else:
                    flag = True
                    if (-int(image[x + 1][y][c]) + int(image[x][y][c])) >= rangenumber or (-int(image[x + 1][y][c]) + int(image[x][y][c])) <= -rangenumber:
                        flag = False
                    if flag == True:
                        image[x + 1][y][c] = int(image[x][y][c])

                    if (x + 1) == int(len(image)) - 1:
                        k = 1
                        temporaryk = 1
                        return operationseven(image, rangenumber, k, x + 1, y, temporaryk, c)
                    else:
                        return operationseven(image, rangenumber, k, x + 1, y, temporaryk, c)

            if k == 1:
                if x == 0 and y == 0 and int(len(image)) % 2 == 1:
                    c += 1
                    temporaryk = 0
                    flag = True
                    if (-int(image[x][y][c - 1]) + int(image[x][y][c])) >= rangenumber or (-int(image[x][y][c - 1]) + int(image[x][y][c])) <= -rangenumber:
                        flag = False
                    if flag == True:
                        image[x][y][c] = int(image[x][y][c - 1])
                    return operationseven(image, rangenumber, k, x, y, temporaryk, c)
                if temporaryk == 1:
                    flag = True
                    if (-int(image[x][y][c]) + int(image[x][y - 1][c])) >= rangenumber or (-int(image[x][y][c]) + int(image[x][y - 1][c])) <= -rangenumber:
                        flag = False
                    if flag == True:
                        image[x][y - 1][c] = int(image[x][y][c])
                    temporaryk = 0
                    return operationseven(image, rangenumber, k, x, y-1, temporaryk, c)
                else:
                    flag = True
                    if (-int(image[x - 1][y][c]) + int(image[x][y][c])) >= rangenumber or (-int(image[x - 1][y][c]) + int(image[x][y][c])) <= -rangenumber:
                        flag = False
                    if flag == True:
                        image[x - 1][y][c] = int(image[x][y][c])
                    if (x - 1) == 0:
                        k = 0
                        temporaryk = 1
                        return operationseven(image, rangenumber, k, x - 1, y, temporaryk, c)
                    else:
                        return operationseven(image, rangenumber, k, x - 1, y, temporaryk, c)

    operationseven(image, range_number)


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

