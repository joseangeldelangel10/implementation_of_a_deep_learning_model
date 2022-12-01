import cv2 as cv

full_image = cv.imread("C:\\Users\\super\\Pictures\\my_math_symbols.png")
cv.imshow("full image", full_image)
cv.waitKey(0)

cols = 8
rows = 2
row_height = int(full_image.shape[0]/rows)
col_width = int(full_image.shape[1]/cols)

for r in range(rows):
    row_image = full_image[r*row_height:(r+1)*row_height,:]
    for c in range(cols):
        cell_image = row_image[:,c*col_width:(c+1)*col_width]        
        cell_image = cv.resize(cell_image, (45,45), interpolation=cv.INTER_LINEAR)
        cv.imshow("cell", cell_image)
        cv.waitKey(0)
        cv.imwrite("C:\\Users\\super\\Documents\\7mo_semestre\\deep_lerning\\my_math_symbols\\cell_{r}_{c}.jpg".format(r=r, c=c), cell_image)
