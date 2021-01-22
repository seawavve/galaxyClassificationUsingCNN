#이미지 사이즈 변환
from PIL import Image
galaxyType=['edge','spiral','smooth']

for i in range(len(galaxyType)):
    for j in range(30):
        im=Image.open(galaxyType[i]+str(j)+'.jpg')
        im2=im.resize((50,50))
        im2.save(galaxyType[i]+'-re('+str(j)+').jpg')
#사이즈 확인
from PIL import Image
im=Image.open('smooth-re (3643).jpg')
print(im.size)
