import colorgram
extracted = colorgram.extract('image.jpg', 20)
colors = []
for i in extracted:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    rgb = (r, g, b)
    colors.append(rgb)

print(colors)
