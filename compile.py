import os
import subprocess
import sys
import logging

package_name = 'cosmospy_protobuf'
logging.basicConfig(format='%(asctime)s - %(levelname)s:%(message)s', level=logging.DEBUG)
absolute_path = os.path.abspath(package_name)


def run_protoc(filepath):
    if os.path.basename(filepath) == "query.proto" or os.path.basename(filepath) == "service.proto":
        cmd = [sys.executable, '-m', 'grpc_tools.protoc',
               '--proto_path', absolute_path,
               '--python_out', 'cosmospy_protobuf',
               '--grpc_python_out', 'cosmospy_protobuf',
               filepath]
        logging.info(f"Compiling proto and grpc file: {filepath}")
    else:
        cmd = [sys.executable, '-m', 'grpc_tools.protoc',
               f'--proto_path={absolute_path}',
               '--python_out=cosmospy_protobuf',
               filepath]
        logging.info(f"Compiling proto file: {filepath}")

    subprocess.run(cmd)


def fix_proto_imports(filepath):
    logging.info(f"Fixing file at: {filepath}")
    cmd = [sys.executable, '-m', 'protoletariat',
           '--create-package', '--in-place',
           '--python-out', 'cosmospy_protobuf',
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


remove_all_compiled_python_files(package_name)
walk_through_project_and_compile_proto(package_name)
walk_through_project_and_fix_imports(package_name)
