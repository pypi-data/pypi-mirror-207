import sys, os

import argparse

import subprocess
from setuptools_cuda_cpp import find_cuda_home_path

import logging

if __name__ == "__main__":

    logger = logging.getLogger("pyUAMMD")

    parser = argparse.ArgumentParser(description="Get UAMMD information")

    group = parser.add_mutually_exclusive_group()

    group.add_argument("--includers", action="store_true",help="Print the includers of the \
                                                                UAMMD and UAMMD-structured library")

    group.add_argument("--flags", action="store_true",help="Print the flags used to compile \
                                                            the UAMMD and UAMMD-structured library")

    group.add_argument("--arch", action="store_true",help="Print the architecture used to compile \
                                                           the UAMMD and UAMMD-structured library")

    group.add_argument("--libraries", action="store_true",help="Print the libraries used to link \
                                                                the UAMMD and UAMMD-structured library")

    group.add_argument("--cuda", action="store_true",help="Print the CUDA path")

    args = parser.parse_args()

    if args.includers:

        # Try to import read environment variables UAMMD_PATH and UAMMD_STRUCTURED_PATH
        try:

            UAMMD_PATH = os.environ['UAMMD_PATH']

        except:

            logger.error("Environment variables UAMMD_STRUCTURED_PATH")
            raise RuntimeError("Environment variables not found")

        try:

            UAMMD_STRUCTURED_PATH = os.environ['UAMMD_STRUCTURED_PATH']

        except:

            logger.error("Environment variables UAMMD_PATH")
            raise RuntimeError("Environment variables not found")

        try:

            CUDA_PATH = find_cuda_home_path()

        except:
            raise RuntimeError('Can not find CUDA_HOME path')

        if CUDA_PATH is None:
            raise RuntimeError('Can not find CUDA_HOME path')

        INCLUDES = ['-I'+str(CUDA_PATH)+'/include/',
                    '-I'+UAMMD_PATH+'/src/',
                    '-I'+UAMMD_PATH+'/src/third_party/',
                    '-I'+UAMMD_STRUCTURED_PATH+'/']

        print(' '.join(INCLUDES))

    elif args.flags:

        FLAGS = ['--expt-relaxed-constexpr',
                 '--expt-extended-lambda',
                 '-std=c++14',
                 '-O3',
                 '-DUAMMD_EXTENSIONS',
                 '-DMAXLOGLEVEL=5',
                 '-Xcompiler=\"-O3 -march=native -fPIC\"',
                 '-ccbin=g++']

        print(' '.join(FLAGS))

    elif args.arch:
        try:

            NVCC_PATH = os.path.join(find_cuda_home_path(), 'bin', 'nvcc')

            gencode = []

            # Get the current list gpu capturing nvcc output
            p = subprocess.Popen([NVCC_PATH, '--list-gpu-code'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()

            archs = out.decode('utf-8').split('\n')[0:-1]
            archs = [arch.split("_")[-1] for arch in archs]

            for arch in archs:
                gencode += ['-gencode',f'arch=compute_{arch},code=sm_{arch}']

        except:
            raise RuntimeError('Could not run nvcc')

        print(' '.join(gencode))

    elif args.libraries:

        LIBS = ['-lcufft',
                '-llapacke',
                '-lcublas',
                '-lblas',
                '-lcurand',
                '-lcusolver',
                '-lstdc++fs']

        print(' '.join(LIBS))

    elif args.cuda:

        try:

            CUDA_PATH = find_cuda_home_path()

        except:
            raise RuntimeError('Can not find CUDA_HOME path')

        print(os.path.join(CUDA_PATH, 'bin', 'nvcc'))

    else:
        parser.print_help()
        sys.exit(0)




