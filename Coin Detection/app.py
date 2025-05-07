def convert_to_grayscale(image):
grayscale = [ ]
for row in image:
gray_row = [ ]
for pixel in row:
R, G, B = pixel
gray = int(0.299 * R + 0.587 * G + 0.114 * B)
gray_row.append(gray)
grayscale.append(gray_row)
return grayscale
def threshold_image(grayscale, threshold=128):
binary = [ ]
for row in grayscale:
bin_row = [255 if pixel > threshold else 0 for pixel in row]
binary.append(bin_row)
return binary
def flood_fill(matrix, x, y, label):
stack = [(x, y)]
while stack:
i, j = stack.pop()
if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and matrix[i][j] == 255:
matrix[i][j] = label
stack.extend([(i+1,j), (i-1,j), (i,j+1), (i,j-1)])
def count_connected_components(binary):
label = 2
for i in range(len(binary)):
for j in range(len(binary[0])):
if binary[i][j] == 255:
flood_fill(binary, i, j, label)
label += 1
return label - 2 # Exclude background