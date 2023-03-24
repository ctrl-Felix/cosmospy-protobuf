import argparse
import os
import re
import subprocess
import sys
import logging

parser = argparse.ArgumentParser(description='Aggregate all protobuf files')
parser.add_argument('-p', '--package_name', type=str, default="cosmospy_protobuf", help="Name for the package to build. This will aggregate all files in the src/{package_name} folder")
args = parser.parse_args()


package_name = 'src/' + args.package_name
logging.basicConfig(format='%(asctime)s - %(levelname)s:%(message)s', level=logging.DEBUG)
absolute_path = os.path.abspath(package_name)

def run_protoc(filepath):
    if os.path.basename(filepath) == "query.proto" or os.path.basename(filepath) == "service.proto":
        cmd = [sys.executable, '-m', 'grpc_tools.protoc',
               '--proto_path', absolute_path,
               '--python_out', package_name,
               '--pyi_out', package_name,
               '--grpc_python_out', package_name,
               filepath]
        logging.info(f"Compiling proto and grpc file: {filepath}")
    else:
        cmd = [sys.executable, '-m', 'grpc_tools.protoc',
               f'--proto_path={absolute_path}',
               f'--python_out={package_name}',
               f'--pyi_out={package_name}',
               filepath]
        logging.info(f"Compiling proto file: {filepath}")

    subprocess.run(cmd)


def fix_proto_imports(filepath):
    logging.info(f"Fixing file at: {filepath}")
    cmd = [sys.executable, '-m', 'protoletariat',
           '--create-package', '--in-place',
           '--python-out', package_name,
           'protoc', f'--proto-path={absolute_path}',
           filepath]
    subprocess.run(cmd)


def walk_through_project_and_compile_proto(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.proto'):
                run_protoc(os.path.abspath(os.path.join(root, filename)))


def walk_through_project_and_fix_imports(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.proto'):
                fix_proto_imports(os.path.abspath(os.path.join(root, filename)))
                logging.info(f"Fixed imports for {filename}")


def remove_all_compiled_python_files(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.py') or filename.endswith('.pyi'):
                logging.info(f"Deleting {os.path.join(root, filename)}")
                os.remove(os.path.join(root, filename))

def rename_any_proto_imports(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            with open(os.path.join(root, filename), 'r') as file:
                lines = file.readlines()

            if 'import "google/protobuf/any.proto";\n' in lines:
                with open(os.path.join(root, filename), 'w') as file:
                    for line in lines:
                        file.write(re.sub(r'^import "google/protobuf/any.proto";\n', 'import "google/protobuf/cosmos_any.proto";\n', line))





#rename_any_proto_imports(package_name)
remove_all_compiled_python_files(package_name)
walk_through_project_and_compile_proto(package_name)
walk_through_project_and_fix_imports(package_name)
