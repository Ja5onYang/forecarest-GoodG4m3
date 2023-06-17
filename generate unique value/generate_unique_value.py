import time
import random
import hashlib
from PIL import Image, ImageDraw, ImageFont

def generate_nickname(adj, name):
    nickname= adj+name
    return nickname

def generate_id():
    timestamp = int(time.time() * 1000) 
    random_num = random.randint(1, 100000) 
    unique_id = str(timestamp) + str(random_num) 
    return unique_id

def generate_image(input_string):
    hash_value = hashlib.sha256(input_string.encode('utf-8')).hexdigest()
    random_seed = int(hash_value, 16) % (10 ** 16)  
    random_generator = random.Random(random_seed)

    # create an indexed color mode image
    image_size = (300, 300)
    background_color = (255, 255, 255)
    image = Image.new('RGB', image_size, background_color)
    quantized_image = image.quantize(colors=16)

    
    #(just for demo)
    # draw the tree 
    draw = ImageDraw.Draw(quantized_image)
    tree_trunk_width = 20
    tree_trunk_height = 70
    tree_canopy_width = 60
    tree_canopy_height = 60
    tree_trunk_x = 120
    tree_trunk_y = 200
    # draw the tree trunk 
    draw.rectangle((tree_trunk_x, tree_trunk_y, tree_trunk_x + tree_trunk_width, tree_trunk_y + tree_trunk_height), fill=(139, 69, 19))
    # draw the tree canopy 
    tree_color = (random_generator.randint(0, 255), random_generator.randint(0, 255), random_generator.randint(0, 255))
    canopy_x1 = tree_trunk_x - (tree_canopy_width - tree_trunk_width) / 2
    canopy_y1 = tree_trunk_y - tree_canopy_height
    canopy_x2 = canopy_x1 + tree_canopy_width
    canopy_y2 = tree_trunk_y
    draw.ellipse((canopy_x1, canopy_y1, canopy_x2, canopy_y2), fill=tree_color)

    # add random yellow pixels to the canopy
    for i in range(tree_canopy_width):
        for j in range(tree_canopy_height):
            rand_num = random_generator.random()
            if rand_num < 0.05:
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)

                draw.point((canopy_x1 + i, canopy_y1 + j), fill=(r, g, b))
    
    #add name to the image，the sets could be very large
    adj = random.choice(["confused", "energetic", "gentle", "loveable", "naughty", "cheerful", "ambitious", "reliable", "honest", "hardworking",
                        "confident", "humorous"])
    name = random.choice(["Mike", "Kelen", "Jacob", "Thomas", "Mia", "Sophia" , "Charlotte", "Daniel", "Ashley", "Emily"])
    nickname = generate_nickname(adj, name)
    font = ImageFont.truetype('arial.ttf', size=20)
    draw.text((10, 10), nickname, fill=(0, 0, 0), font=font)
    
    # # resize the image to get pixelated effect
    # enlarged_image = quantized_image.resize(image_size, Image.NEAREST)

    return quantized_image, nickname

uniqueID = generate_id()
image, name = generate_image(uniqueID)
image.show()

# save the image to disk
image.save(uniqueID + ".png")

# save id and nickname to a text file
with open(uniqueID+".txt", "w") as f:
    f.write("ID: "+uniqueID+"\n")
    f.write("Nickname: "+name)
