# Using zip-code to visualize where most of the customers are from!
# ----------------------------------------------------------------------------------------------------------------
# Libraries
import csv
from BeautifulSoup import BeautifulSoup
from collections import defaultdict


# Create a dictionary for FIPS list in the csv file
participents = defaultdict(int)
FIPSlist =[]

reader = csv.reader(open('2013Data.csv'), delimiter=",")
for row in reader:
    try:
        FIPSlist.append(row[9])
    except:
        pass

# Count occurances of FIPS in the file
for fips in FIPSlist:
    participents[fips] += 1

# Convert the participents from default dict to normal dict
participents = dict(participents)

# Take out the empty count
map(participents.pop, [''])

# Open empty USA counties map
svg = open('USA_counties.svg', 'r').read()

# Use Beautiful Soup to load in data
soup = BeautifulSoup(svg, selfClosingTags=['defs','sodipodi:namedview'])

# Find all the counties
paths = soup.findAll('path')

# Map colors
#colors = ["#F1EEF6", "#D4B9DA", "#C994C7", "#DF65B0", "#DD1C77", "#980043"]
#colors = ["#D73027", "#FC8D59", "#FEE090", "#E0F3F8", "#91BFDB", "#4575B4"]
colors = ["EFF3FF", "#C6DBEF", "#9ECAE1", "#6BAED6", "#3182BD", "#08519C"]

# Set county style
path_style = 'font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:'

# Place the color by the occurances of zip-code
for p in paths:

    if p['id'] not in ["State_Lines", "separator"]:
        try:
            count = participents[p['id']]
        except:
            continue

        if count > 5:
            color_class = 5
        elif count > 4:
            color_class = 4
        elif count > 3:
            color_class = 3
        elif count > 2:
            color_class = 2
        elif count > 1:
            color_class = 1
        else:
            color_class = 0


        color = colors[color_class]
        p['style'] = path_style + color

# Wite the soup into svg format and close
svgD = open("2013Graph.svg", 'w')
svgD.write(soup.prettify())
svgD.close()

# Graph is updated and can be see through any browser!
