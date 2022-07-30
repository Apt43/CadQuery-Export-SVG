# ExportSVG.py

# Copyright (c) 2022 Eric M. Chen

# Change History:
# 2022-07-30/ec:    Initial release.

import cadquery as cq
from cadquery import exporters

# result:   Workplane object to extport.
# filePath: Full path to export the svg file to.
# for other parameters, see CadQuery official documentation on export to SVG.
def exportSvg(
    result,
    filePath,
    marginLeft = 60.0,
    marginTop = 40.0,
    strokeColor = (0, 0, 0),
    hiddenColor = (0, 0, 255),
    showHidden = True):

    s = cq.Workplane()
    # need to get a single solid, otherwise findSolids will return compound
    s = s.union(result)

    # === determine object size ===
    # --- rotate to get the size at view angle ---
    s = s.rotate((0, 0, 0), (0, 0, 1), -45)
    s = s.rotate((0, 0, 0), (0, 1, 1), 45)

    # --- ---
    s = s.findSolid()
    s = s.BoundingBox() # returns BoundBox()

    # xmax, xmin, ... values are not in the official document,
    # found in CadQuery source code
    width = s.xmax - s.xmin
    height = s.zmax - s.zmin

    # === ===
    printWidth = 500.0
    printHeight = printWidth * height / width

    # do not change width, use 500.
    # do not change projectionDir, work properly with the rotated object for export
    # color can be changed freely.
    optSvg = {
        'width': printWidth,
        'height': printHeight,
        'marginLeft': marginLeft,
        'marginTop': marginTop,
        'projectionDir': (1, 1, 1),
        'strokeWidth': 0.05,
        'strokeColor': strokeColor,
        'hiddenColor': hiddenColor,
        'showHidden': showHidden}

    # must rotate to get the projection align with displayed on screen
    r = result.rotate((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), -90)
    exporters.export(r, filePath, opt = optSvg)

# === test ===
if __name__ == 'temp':
    r = cq.Workplane()
    r = r.box(8.0, 8.0, 1.0)
    r = r.faces('>Z')
    r = r.workplane()
    r = r.moveTo(1.0, 1.0)
    r = r.polygon(5, 3.0)
    r = r.extrude(2.0)

    show_object(r)

    filePath = 'D:\\Temp\\ExportSVG1.svg'
    exportSvg(r, filePath)
