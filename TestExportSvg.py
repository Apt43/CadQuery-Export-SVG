# TestExportSvg.py

# Copyright (c) 2022 Eric M. Chen

# Change History:
# 2022-07-31/ec:    Initial release.

import ExportSvg

r = cq.Workplane()
r = r.box(8.0, 8.0, 1.0)
r = r.faces('>Z')
r = r.workplane()
r = r.moveTo(1.0, 1.0)
r = r.polygon(5, 3.0)
r = r.extrude(2.0)

filePath = 'D:\\Temp\\TestExportSVG-1.svg'
ExportSvg.exportSvg(r, filePath)

r = r.box(1.0, 1.0, 14.0)
filePath = 'D:\\Temp\\TestExportSVG-2.svg'
ExportSvg.exportSvg(r, filePath)

show_object(r)
