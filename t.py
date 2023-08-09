import os
import shutil
from os.path import dirname, abspath

d = dirname(abspath(__file__))
root_abs_path = os.path.join(d, "src/osmosis_protobuf")


def recursively_check_filenames():
    for root, dirs, files in os.walk(root_abs_path):
        for dir in dirs:
            if "-" in dir:
                old_path = os.path.abspath(os.path.join(root, dir))
                new_path = os.path.abspath(os.path.join(root, dir.replace("-", "_")))
                shutil.move(src=old_path, dst=new_path)
                print(f"Renamed {old_path} to {new_path}")
                for root, dirs, files in os.walk(root_abs_path):
                    for file in files:
                        with open(os.path.abspath(os.path.join(root, file)), "r") as f:
                            content = f.read()

                        if dir in content:
                            updated_content = content.replace(dir, dir.replace("-", "_"))
                            print(f"Updating {dir} in {os.path.join(root, file)}")

                            with open(os.path.abspath(os.path.join(root, file)), "w") as f:
                                f.write(updated_content)

                return recursively_check_filenames()


recursively_check_filenames()
