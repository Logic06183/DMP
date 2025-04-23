from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def create_geometry(parent, x=None, y=None, width=None, height=None, relative=None):
    """Helper function to create mxGeometry elements consistently"""
    geom = SubElement(parent, 'mxGeometry')
    if x is not None:
        geom.set('x', str(x))
    if y is not None:
        geom.set('y', str(y))
    if width is not None:
        geom.set('width', str(width))
    if height is not None:
        geom.set('height', str(height))
    if relative is not None:
        geom.set('relative', str(relative))
    geom.set('as', 'geometry')
    return geom

# Create base structure
mxfile = Element('mxfile')
mxfile.set('host', 'app.diagrams.net')
mxfile.set('modified', '2023-04-23T12:00:00.000Z')
mxfile.set('agent', 'Mozilla/5.0')
mxfile.set('etag', 'diagram-etag')
mxfile.set('version', '21.0.10')

diagram = SubElement(mxfile, 'diagram')
diagram.set('id', 'heat_center_data_flow')
diagram.set('name', 'HE²AT Center Cloud-Based Data Flow')

mxGraphModel = SubElement(diagram, 'mxGraphModel')
mxGraphModel.set('dx', '1422')
mxGraphModel.set('dy', '798')
mxGraphModel.set('grid', '1')
mxGraphModel.set('gridSize', '10')
mxGraphModel.set('guides', '1')
mxGraphModel.set('tooltips', '1')
mxGraphModel.set('connect', '1')
mxGraphModel.set('arrows', '1')
mxGraphModel.set('fold', '1')
mxGraphModel.set('page', '1')
mxGraphModel.set('pageScale', '1')
mxGraphModel.set('pageWidth', '1169')
mxGraphModel.set('pageHeight', '827')
mxGraphModel.set('math', '0')
mxGraphModel.set('shadow', '0')

root = SubElement(mxGraphModel, 'root')

# Add base layer
SubElement(root, 'mxCell', id='0')
SubElement(root, 'mxCell', id='1', parent='0')

# Title
title = SubElement(root, 'mxCell')
title.set('id', 'title')
title.set('value', 'HE²AT Center Cloud-Based Data Flow with Long-Term Data Retention (Post-Funding Restructure)')
title.set('style', 'text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=20;fontStyle=1')
title.set('vertex', '1')
title.set('parent', '1')
create_geometry(title, x=100, y=20, width=950, height=40)

# Data Provider Section
provider = SubElement(root, 'mxCell')
provider.set('id', 'provider')
provider.set('value', 'Data Providers')
provider.set('style', 'swimlane;fontStyle=1;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#f5f5f5;strokeColor=#666666;fontColor=#333333;')
provider.set('vertex', '1')
provider.set('parent', '1')
create_geometry(provider, x=40, y=100, width=200, height=100)

# Provider Info
provider_info = SubElement(root, 'mxCell')
provider_info.set('id', 'provider_info')
provider_info.set('value', '- Original Study Data ownership\n- Secure data transfer protocols\n- In-region data storage\n- Data Transfer Agreements')
provider_info.set('style', 'text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;rotatable=0;')
provider_info.set('vertex', '1')
provider_info.set('parent', 'provider')
create_geometry(provider_info, y=30, width=200, height=70)

# Core Data Team
core = SubElement(root, 'mxCell')
core.set('id', 'core')
core.set('value', 'Core Data Team (UCT)')
core.set('style', 'swimlane;fontStyle=1;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#dae8fc;strokeColor=#6c8ebf;')
core.set('vertex', '1')
core.set('parent', '1')
create_geometry(core, x=300, y=100, width=240, height=120)

# Core Info
core_info = SubElement(root, 'mxCell')
core_info.set('id', 'core_info')
core_info.set('value', '- Pre-processing & harmonisation\n- Data validation and transformation\n- De-identification processes\n- Geographic masking techniques\n- Audit logs & transformation records\n- Metadata management')
core_info.set('style', 'text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;rotatable=0;')
core_info.set('vertex', '1')
core_info.set('parent', 'core')
create_geometry(core_info, y=30, width=240, height=90)

# Flow arrow from Provider to Core
flow1 = SubElement(root, 'mxCell')
flow1.set('id', 'flow1')
flow1.set('value', 'Original Study Data (Level 0)')
flow1.set('style', 'endArrow=classic;html=1;rounded=0;')
flow1.set('edge', '1')
flow1.set('parent', '1')
flow1.set('source', 'provider')
flow1.set('target', 'core')
create_geometry(flow1, relative=1)

# Write to file
with open('he2at_cloud_flow.drawio', 'w', encoding='utf-8') as f:
    f.write(prettify(mxfile))

print("Draw.IO XML file has been created: he2at_cloud_flow.drawio") 