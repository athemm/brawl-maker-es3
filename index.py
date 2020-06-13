import sys
import json

import datetime
x = datetime.datetime.now()
file_thing = x.strftime("%Y%m%d%H%M%S")

b_list = []

bl = dict(
    no = "5",
    water = "17",
    brick = "6",
    brick2 = "8",
    crate = "7",
    barrel = "0",
    fence = "15",
    cactus = "9",
    bone = "10",
    indes = "11",
    y_bush = "4",
    g_bush = "3",
    sp_b = "1",
    sp_r = "2",
    sd_box = "16",
    heist_safe = "12"
)

gogo = 0
cnt = 1
bro = 0
indexc = 0
somec = 0

try:
    json_file_config = open("config.json", "r+")
except FileNotFoundError:
    print("cannot find config file")
    sys.exit()

conf = json.load(json_file_config) # load the json

# map size stuff
size = conf["mapSize"]

if size == "1":
    sizeId = "0"
    bro_number = 693
    somec_check = 32
    gogo_check = 21

elif size == "2":
    sizeId = "2"
    bro_number = 3600
    somec_check = 59
    gogo_check = 60

else:
    print("unsupported map size")
    sys.exit()
   
out = open(file_thing + ".es3", "w+")
save = open("saves.es3", "w+")
save.write('{"saves":{"__type":"System.Collections.Generic.List`1[[MapSave, Assembly-CSharp, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null]],mscorlib","value":[{"id":"' + file_thing + '","mapName":"' + conf["mapName"] + '","mapAuthor":"' + conf["mapAuthor"] + '","mapEvent":"Custom"}]}}')


out.write('{"IDs":{"__type":"System.Int32[,],mscorlib","value":[')


while bro < bro_number:
    try:
        f = open(conf["fileName"], "r+")
    except FileNotFoundError:
        print("Put your map in a file called 'sample.txt' or change that in config file")
        input()
        sys.exit()
    
    line = f.readline()
    while line:
        if line.strip()[indexc] == "W":
                b_list.append(bl["water"])

        elif line.strip()[indexc] == "M":
            b_list.append(bl["brick"])
        elif line.strip()[indexc] == "F":
            b_list.append(bl["y_bush"])
        elif line.strip()[indexc] == "R":
            b_list.append(bl["g_bush"])
        elif line.strip()[indexc] == "Y":
            b_list.append(bl["crate"])
        elif line.strip()[indexc] == "8":
            b_list.append(bl["heist_safe"])            
        elif line.strip()[indexc] == "C":
            b_list.append(bl["barrel"])
        elif line.strip()[indexc] == "1":
            b_list.append(bl["sp_b"])
        elif line.strip()[indexc] == "2":
            b_list.append(bl["sp_r"])
        elif line.strip()[indexc] == "B":
            b_list.append(bl["bone"])
        elif line.strip()[indexc] == "4":
            b_list.append(bl["sd_box"])            
        elif line.strip()[indexc] == "N":
            b_list.append(bl["fence"])            
        elif line.strip()[indexc] == "T":
            b_list.append(bl["cactus"])            
        elif line.strip()[indexc] == ".":
            b_list.append(bl["no"])
        else:
            b_list.append(bl["no"])
        bro += 1
        if somec == somec_check:
            indexc += 1
            somec = 0
            gogo += 1
            print(b_list)
            for i in range(0, len(b_list)): 
                b_list[i] = int(b_list[i])
            b_list.reverse()
            if gogo != gogo_check:
                out.write(str(b_list) + ",")
            else:
                out.write(str(b_list) + ']},"Event":{"__type":"System.Int32","value":0},"Theme":{"__type":"System.Int32","value":3},"Size":{"__type":"System.Int32","value":' + sizeId + '},"Name":{"__type":"System.String","value":"' + conf["mapName"] + '"},"Author":{"__type":"System.String","value":"' + conf["mapName"] + '"},"ID":{"__type":"System.String","value":"' + file_thing + '"}}')
            b_list = []
        else:
            somec += 1
        line = f.readline()
        cnt += 1
print(gogo, "lines processed")
out.close()
save.close()






