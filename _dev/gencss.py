import json

# copy the appropriate string from here:
# https://flatuicolors.com/static/js/app.0b36eb8.js
palette = """
[{name:"Jigglypuff",hex:"#ff9ff3"},{name:"Casandora Yellow",hex:"#feca57"},{name:"Pastel Red",hex:"#ff6b6b"},{name:"Megaman",hex:"#48dbfb"},{name:"Wild Caribbean Green",hex:"#1dd1a1"},{name:"Lián Hóng Lotus Pink",hex:"#f368e0"},{name:"Double Dragon Skin",hex:"#ff9f43"},{name:"Amour",hex:"#ee5253"},{name:"Cyanite",hex:"#0abde3"},{name:"Dark Mountain Meadow",hex:"#10ac84"},{name:"Jade Dust",hex:"#00d2d3"},{name:"Joust Blue",hex:"#54a0ff"},{name:"Nasu Purple",hex:"#5f27cd"},{name:"Light Blue Ballerina",hex:"#c8d6e5"},{name:"Fuel Town",hex:"#576574"},{name:"Aqua Velvet",hex:"#01a3a4"},{name:"Bleu De France",hex:"#2e86de"},{name:"Bluebell",hex:"#341f97"},{name:"Storm Petrel",hex:"#8395a7"},{name:"Imperial Primer",hex:"#222f3e"}]
"""
colornames = {
    "#5f27cd": "primary",
    "#48dbfb": "secondary",

    "#1dd1a1": "success",
    "#ff6b6b": "danger",
    "#feca57": "warning",
    "#54a0ff": "info",

    "#ff9ff3": "purple",
    "#00d2d3": "brand",

    "#c8d6e5": "light",
    "#576574": "dark",
}


palette = json.loads(palette.replace("name",'"name"').replace("hex",'"hex"'))



# parse in pairs:
str0 = []
pa1,pa2 = palette[0:5] + palette[10:15], palette[5:10] + palette[15:20]
for col1,col2 in zip(pa1,pa2):
    name1 = colornames.get(col1["hex"])
    name2 = colornames.get(col2["hex"])

    if name1 is None and name2 is not None:
        name1 = name2
    elif name2 is None and name1 is not None:
        name2 = name1
    elif name2 is None and name1 is None:
        name1 = name2 = col1["name"].lower().replace(" ", "-")

    str0.append(f".text-{name2} {{ color: {col2['hex']} !important; }}.bg-{name1} {{ background-color: {col1['hex']} !important; }}\n")

print("".join(str0))
