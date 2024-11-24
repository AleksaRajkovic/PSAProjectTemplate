import cv2
import os
dir = r'C:\Users\strelok\Desktop\PSA_Project_MVC\V2\assets\GALLERY\EN'
files = os.listdir(dir)
height = []
width = []
difs = []
#avoid = [1,7,10,5,4,3,0,2]
for f in files:
    # if files.index(f) in avoid:
    #     continue
    path = os.path.join(dir,f)
    im = cv2.imread(path)
    h, w, _ = im.shape
    print(f'{h} x {w}')
    height.append(h)
    width.append(w)
    difs.append(abs(w-h))
l = len(difs)
ordered = {}
for i in range(l):
    index = difs.index(min(difs))
    print(f"{difs[index]}   {files[index]}")
    ordered.update({index:difs.pop(index)})

for k,v in ordered:
    print(f"{v} {files[k]}")




# print('-'*118)
# print(min(width))
# print(min(height))
# print(files[height.index(min(height))])
# print(files[width.index(min(width))])
# print('-'*118)
# print(max(width))
# print(max(height))
# print(files[height.index(max(height))])
# print(files[width.index(max(width))])
# print('-'*118)
