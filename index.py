"""
list(mydict.keys())[list(mydict.values()).index("value here")]

GETS KEY FROM VALUE
"""
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
    sp_r = "2"
)

out = open(file_thing + ".es3", "w+")
save = open("saves.es3", "w+")
save.write('{"saves":{"__type":"System.Collections.Generic.List`1[[MapSave, Assembly-CSharp, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null]],mscorlib","value":[{"id":"' + file_thing + '","mapName":"' + file_thing + '","mapAuthor":"Anonymous","mapEvent":"Custom"}]}}')
#  fp = input("enter file name here: ")
gogo = 0
cnt = 1
bro = 0
indexc = 0
somec = 0



out.write('{"IDs":{"__type":"System.Int32[,],mscorlib","value":[')




while bro < 693:
    f = open("sample.txt", "r+")
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
            b_list.append(bl["cactus"])
        elif line.strip()[indexc] == "C":
            b_list.append(bl["barrel"])
        elif line.strip()[indexc] == "1":
            b_list.append(bl["sp_b"])
        elif line.strip()[indexc] == "2":
            b_list.append(bl["sp_r"])
        elif line.strip()[indexc] == "B":
            b_list.append(bl["bone"])
        elif line.strip()[indexc] == ".":
            b_list.append(bl["no"])
        else:
            b_list.append(bl["no"])
        bro += 1
        if somec == 32:
            indexc += 1
            somec = 0
            gogo += 1
            print(b_list)
            if gogo != 21:
                out.write(str(b_list) + ",")
            else:
                out.write(str(b_list) + ']},"Event":{"__type":"System.Int32","value":0},"Theme":{"__type":"System.Int32","value":3},"Size":{"__type":"System.Int32","value":0},"Name":{"__type":"System.String","value":"' + file_thing + '"},"Author":{"__type":"System.String","value":"Anonymous"},"ID":{"__type":"System.String","value":"' + file_thing + '"}}')
            b_list = []
        else:
            somec += 1
        line = f.readline()
        cnt += 1
print(gogo, "lines processed")
out.close()
save.close()

















