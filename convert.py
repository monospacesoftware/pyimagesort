import atexit
import json
from pathlib import Path

import exiftool
from PIL import Image
from pillow_heif import register_heif_opener
import piexif


exif_tool = exiftool.ExifTool()
exif_tool.start()
atexit.register(lambda: exif_tool.terminate())

register_heif_opener()

heic_path = Path("temp.heic")
#heic_data = piexif.load(heic_path.as_posix())
#heic = Image.open(Path("temp.heic"))
heic_exif = exif_tool.get_metadata(heic_path.as_posix())
print(json.dumps(heic_exif, indent=2))
exif_bytes = piexif.dump({"Exif": heic_exif})

#
# jpg_path = Path("temp.jpg")
# with open(jpg_path.as_posix(), "wb") as jpg:
#     heic.save(jpg, format="jpeg")
#
# exif_bytes = piexif.dump(heic_exif)
#
# piexif.insert(exif_bytes, jpg_path.as_posix())
#
# #jpg_exif = piexif.load(jpg_path.as_posix())
# print(jpg_exif)
