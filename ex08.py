import shutil

archive = shutil.make_archive("backup", "zip")

shutil.unpack_archive(archive, "archive")