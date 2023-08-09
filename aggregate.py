import json
import os
import shutil
import time
from os.path import dirname, abspath, isfile, isdir
import fnmatch
import argparse

from git import Repo

parser = argparse.ArgumentParser(description='Aggregate all protobuf files')
parser.add_argument('coin', type=str, help="Coin to parse from the .json file in the config folder")
parser.add_argument('-p', '--package_name', type=str, default="osmosis_protobuf",
                    help="Name for the package to build. This will aggregate all files in the src/{package_name} folder")
args = parser.parse_args()


# https://stackoverflow.com/questions/52071642/python-copying-the-files-with-include-pattern
def include_patterns(*patterns):
    def _ignore_patterns(path, names):
        keep = set(name for pattern in patterns
                   for name in fnmatch.filter(names, pattern))
        ignore = set(name for name in names
                     if name not in keep and not isdir(os.path.join(path, name)))
        return ignore

    return _ignore_patterns


# Get current directory
d = dirname(abspath(__file__))

# Check if requested coin has a config
coin = args.coin
try:
    config_path = os.path.join(d, f'configs/{coin.lower()}.json')
    f = open(config_path, "r")
    coin_config = json.load(f)
    f.close()
except Exception:
    print("Coin couldn't be found")
    exit()

tmp_dir = os.path.join(d, "tmp")
if not os.path.isdir(tmp_dir):
    os.mkdir(tmp_dir)

project_dir = os.path.join(tmp_dir, str(time.time()))
os.mkdir(project_dir)

# Delete all existing protobuf files
root_dir = "src/" + args.package_name
root_abs_path = os.path.join(d, root_dir)
os.makedirs(root_abs_path, exist_ok=True)  # Create folder for package

for filename in os.listdir(root_abs_path):
    if filename == ".gitignore":
        continue

    file_path = os.path.join(root_abs_path, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

# Load config
i = 1
for repo_url, repo_config in coin_config.items():
    print(f"Cloning {repo_url} | {repo_config['branch']}")
    repo_dir = project_dir + "/" + str(i)
    Repo.clone_from(
        repo_url,
        project_dir + "/" + str(i),
        branch=repo_config['branch']
    )

    # Copy proto files to root_dir
    for proto_folder in repo_config['paths']:
        proto_dir = os.path.join(repo_dir, proto_folder)
        proto_path_list = proto_folder.split('/')
        target = repo_config["target"] + "/" if "target" in repo_config else ""
        proto_path_in_repo = root_abs_path + "/" + (target if target else proto_path_list[-1]).replace("-", "_")
        formatted_proto_path_in_package = proto_path_in_repo
        try:
            shutil.copytree(proto_dir, formatted_proto_path_in_package,
                            dirs_exist_ok=True, ignore=include_patterns("*.proto"))
            print(f"Copied {formatted_proto_path_in_package}")
        except OSError as exc:
            try:
                # Remove file from path ending to be compatible with the folder creation and copy path
                proto_path_in_repo_for_file = target if target else "/".join(proto_path_in_repo.split('/')[:-1])
                os.makedirs(os.path.dirname(proto_path_in_repo_for_file), exist_ok=True)  # Create folder for file
                shutil.copy(proto_dir, proto_path_in_repo_for_file)
                print(f"File {proto_dir} copied successfully")
            except:
                raise

    i += 1


# Rename all folders that contain dashes to folder names with underscores
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
