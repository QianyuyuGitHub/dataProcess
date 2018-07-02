import imageio
filenames = []
for i in range(10):
    filenames.append(str(i)+".png")
images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('result.gif', images)