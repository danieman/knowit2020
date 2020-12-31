from PIL import Image

file = [list(line.strip("\n")) for line in open("cleaned_kart.txt").readlines()]
width, height = len(file[0]), len(file)
im = Image.new("L", (width, height), color=64)

for x in range(width):
    for y in range(height):
        if file[y][x] == "x":
            im.putpixel((x, y), 0)
        elif file[y][x] == ".":
            im.putpixel((x, y), 255)

im.save("cleaned_kart.png")