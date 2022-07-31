# ExportSVG.py

# Copyright (c) 2022 Eric M. Chen

# Change History:
# 2022-07-30/ec:    Initial release.

import cadquery as cq
from cadquery import exporters

# exportSvg:    exports a Workplane object to SVG image file.
# result:   Workplane object to extport.
# filePath: Full path to export the SVG file to.
# For other parameters, see CadQuery official documentation on Export to SVG.
# 'width' is fixed to 500. 'height' is calculated from object size.
def exportSvg(
    result,
    filePath,
    marginLeft = 60.0,
    marginTop = 40.0,
    strokeColor = (0, 0, 0),
    hiddenColor = (0, 0, 255),
    showHidden = True):

    r = cq.Workplane()

    # === determine object size ===
    # need to get a single solid, otherwise findSolids will return compound object
    r = r.union(result)

    # --- rotate to get the size at viewing angle ---
    r = r.rotate((0.0, 0.0, 0.0), (0.0, 0.0, 1.0), -45.0)
    r = r.rotate((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), 45.0)

    # --- ---
    r = r.findSolid()
    r = r.BoundingBox() # returns BoundBox()

    # xmax, xmin, ... values are not in the official document,
    # these values are found in CadQuery source code
    width = r.xmax - r.xmin
    height = r.zmax - r.zmin

    # === calculate height ===
    imageWidth = 500.0
    imageHeight = imageWidth * height / width

    # === ===
    # do not change width, use 500.
    # do not change projectionDir, it works properly with the rotated object for export.
    optSvg = {
        'width': imageWidth,
        'height': imageHeight,
        'marginLeft': marginLeft,
        'marginTop': marginTop,
        'projectionDir': (1.0, 1.0, 1.0),
        'strokeWidth': 0.05,
        'strokeColor': strokeColor,
        'hiddenColor': hiddenColor,
        'showHidden': showHidden}

    # must rotate to get the projection the same as displayed on screen
    r = result.rotate((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), -90.0)
    exporters.export(r, filePath, opt = optSvg)
