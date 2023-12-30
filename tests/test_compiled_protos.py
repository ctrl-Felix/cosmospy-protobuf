import importlib
import os
import osmosis_protobuf.cosmos.staking.module.v1.module_pb2
package_dir = "src/osmosis_protobuf"

def _generate_all_paths(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".py") and not filename == "__init__.py":
                yield os.path.join(root, filename)


def test_imports():
    paths = _generate_all_paths(directory=package_dir)
    for path in paths:

        path_as_package_name = ".".join(path.replace(".py", "").split("/")[1:])
        if "google" in path_as_package_name:
            continue

        try:
            m = importlib.import_module(path_as_package_name)
        except ModuleNotFoundError as e:
            raise ModuleNotFoundError(f"{path_as_package_name} => {e}")
    assert True
