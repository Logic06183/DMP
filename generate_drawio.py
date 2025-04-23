from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

def prettify(elem):
    return minidom.parseString(tostring(elem)).toprettyxml(indent="  ")

# Create XML structure for draw.io import
mxfile = Element('mxfile', host="app.diagrams.net", modified="2025-04-23T00:00:00.000Z")
diagram = SubElement(mxfile, 'diagram', name="HE2AT Cloud Data Flow")

# Diagram metadata - GraphModel
mxGraphModel = SubElement(diagram, 'mxGraphModel')
root = SubElement(mxGraphModel, 'root')

# Add base layer
SubElement(root, 'mxCell', id="0")
SubElement(root, 'mxCell', id="1", parent="0")

# Nodes definition with colors and styles
nodes = {
    "provider": ("Data Providers", 320, 20, "fillColor=#f0f0f0;strokeColor=#666666"),
    "core": ("Core Data Team (UCT)", 320, 100, "fillColor=#dae8fc;strokeColor=#6c8ebf"),
    "cloud": ("Azure Cloud Platform", 320, 180, "fillColor=#d5e8d4;strokeColor=#82b366"),
    "whc": ("WHC (Level 1)", 520, 110, "fillColor=#ffe6cc;strokeColor=#d79b00"),
    "cesshar": ("CeSHHAR (Level 1)", 520, 180, "fillColor=#fff2cc;strokeColor=#d6b656"),
    "ibm": ("IBM Africa (Level 1)", 520, 250, "fillColor=#e1d5e7;strokeColor=#9673a6"),
    "upgc": ("UPGC (Level 1)", 520, 320, "fillColor=#d5e8d4;strokeColor=#82b366"),
    "external": ("External Researchers (Level 2)", 520, 390, "fillColor=#f8cecc;strokeColor=#b85450")
}

for i, (key, (label, x, y, style)) in enumerate(nodes.items(), start=2):
    node = SubElement(root, 'mxCell', id=str(i), value=label, 
                     style=f"rounded=1;whiteSpace=wrap;html=1;{style}", 
                     vertex="1", parent="1")
    geometry = SubElement(node, 'mxGeometry', x=str(x), y=str(y), width="180", height="40", as_="geometry")

# Edges definition with labels and styles
edges = [
    ("2", "3", "Original Study Data (Level 0)", "endArrow=block;html=1;fontSize=12;"),
    ("3", "4", "Harmonised + De-identified Data by Region", "endArrow=block;html=1;fontSize=12;"),
    ("4", "5", "", "endArrow=block;html=1;"),
    ("4", "6", "", "endArrow=block;html=1;"),
    ("4", "7", "", "endArrow=block;html=1;"),
    ("4", "8", "", "endArrow=block;html=1;"),
    ("4", "9", "DAC-approved access to fully de-identified data", "dashed=1;endArrow=block;html=1;fontSize=12;")
]

edge_id = 10
for source, target, label, style in edges:
    edge = SubElement(root, 'mxCell', id=str(edge_id), value=label, 
                     style=style, edge="1", parent="1", 
                     source=source, target=target)
    SubElement(edge, 'mxGeometry', relative="1", as_="geometry")
    edge_id += 1

# Write to file
with open('he2at_cloud_flow.drawio', 'w') as f:
    f.write(prettify(mxfile))

print("Draw.IO XML file has been created: he2at_cloud_flow.drawio") 