from image import Image
from astar import *
image = Image('./img/bigmaze.png')

start = (0, 3)
end = (40, 31)

image.serialize()
image.refresh()

image.solve(astar(image.img, start, end))

image.save()

