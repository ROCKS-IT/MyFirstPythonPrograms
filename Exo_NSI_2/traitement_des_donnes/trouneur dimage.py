#rotation basique
from PIL import Image

im1 = Image.open("image.png")
L, H = im1.size
print("dimension de l'image",im1.size)

pix1 = im1.load()
pix2 = im2.load()

for x in range(L):
    for y in range(L):
        pix2[x,y] = pix1[y,...]

im2.save("rotation.png")

# rotation en utilisant "diviser pour régner"
from PIL import Image

im1 = Image.open("image.png")
L,H = im1.size
print("dimension de l'image", im1.size)
im2 = Image.new("RGB",im1.size)
pix1 = im1.load()

def rotation_aux(pix,x,y,t):
    t//=2
    if t>1:
        rotation_aux(pix,x,y,t)
        rotation_aux(pix,x+t,y,t)
        rotation_aux(pix,x,y+t,t)
        rotation_aux(pix,x+t,y+t,t)
    for h in range(x,x+t):
        for k in range(y,y+t):
            p0 = pix[h,k]
            pix[h,k] = pix[h+t,k]
            pix[h+t,k] = pix[h+t,k+t]
            pix[h+t,k+t] = pix[h,k+t]
            pix[h,k+t] = p0

rotation_aux(pix1,0,0,L)
im1.save("rotation2.png")
            pix[h, k+t] = p0
