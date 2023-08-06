#!/usr/bin/env python3
# coding=utf-8
# Copyright (c) 2015-2022, UT-BATTELLE, LLC
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""Move tests from a non-regression testing framework to a directory structure for LIVV.
"""
import argparse
import time
from pathlib import Path
import shutil

def parse_args(args=None):
    """
    Handles the parsing of options for LIVVkit's command line interface

    Args:
        args: The list of arguments, typically sys.argv[1:]
    """
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        fromfile_prefix_chars="@",
    )

    parser.add_argument(
        "-o",
        "--out-dir",
        default=Path("./", f"cism_{time.strftime('%Y-%m-%d')}").absolute(),
        help="Root test output directory.",
    )

    parser.add_argument(
        "-i",
        "--in-dir",
        default=None,
        help="Input testing directory."
    )

    parser.add_argument(
        "-m",
        "--model",
        default="CISM_glissade",
        help="Name of model used, will be used to select LIVVkit bundle for processing"
    )

    parser.add_argument(
        "-p",
        "--platform",
        default="cheyenne-intel",
        help="Platform on which CISM tests were run (machine-compiler pair)"
    )
    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        default=False,
        help="Debug mode on, don't move files just do a lot of printing."
    )
    return parser.parse_args()


def main():
    """Read CL arguments and process files."""
    args = parse_args()
    assert args.in_dir is not None, "Input test directory must be specified."

    # Create output directory structure
    # |-- args.out_dir
    #     |-- PLATFORM-COMPILER
    #         |-- ICE-MODEL
    #             |-- TEST FAMILY [e.g. dome, EISMINT, ismip-hom]
    #                 |-- TEST CASE
    #                     |-- DOF (degrees of freedom)
    #                         |-- PROCESSORS
    #                             |-- [OPTIONAL TEST SPECIFIC DIRS]
    #                                 |-- files.ext

    out_root = Path(args.out_dir, args.platform, args.model)
    if not out_root.exists() and not args.debug:
        out_root.mkdir(parents=True)
    elif not out_root.exists() and args.debug:
        print(f"#### CREATE {out_root}")

    # Find all tests in root test directory
    # Use netCDF extension .nc to find which tests actually have output
    test_in = Path(args.in_dir)
    nc_files = sorted(test_in.rglob("*out.nc"))
    for _file in nc_files:
        _parts = _file.parts
        # Find where "tests" directory starts, use that to find test family, case, etc.
        _fam, _, *_name = _parts[_parts.index("tests") + 1:]
        if len(_name) == 1:
            file_name = _name[0]
            _dof = "s0"
            extra = []
            _case = file_name.split(".")[0]
        elif len(_name) == 2:
            file_name = _name[-1]
            _dof = _name[0]
            extra = []
            _case = file_name.split(".")[0]
        elif "mismip" in _name[-1].lower() and not "+" in _name[-1]:
            file_name = _name[-1]
            _dof = _name[1]
            extra = ["_".join(_name[2:-1])]
            _case = _name[0]
        else:
            breakpoint()

        try:
            _pcount = int(file_name.split(".")[2][1:])
        except ValueError:
            _pcount = 1
        _outdir = Path(out_root, _fam, _case, _dof, f"p{_pcount:d}", *extra)

        if not _outdir.exists() and not args.debug:
            _outdir.mkdir(parents=True)
        elif not _outdir.exists() and args.debug:
            print(f"#### CREATE {_outdir}")

        outfile_match = f"{'.'.join(_file.stem.split('.')[:-1])}*"
        test_output_files = sorted(Path(*_file.parts[:-1]).glob(outfile_match))

        for test_outfile in test_output_files:
            new_outfile = Path(_outdir, test_outfile.name)
            if args.debug:
                print(f"\tcp {test_outfile}\n\t    {new_outfile}\n")
            else:
                if new_outfile.exists():
                    print(f"OUTFILE: {new_outfile} EXISTS")
                else:
                    shutil.copy2(test_outfile, new_outfile)

    # Determine where each case ought to go

    # Put them there


if __name__ == "__main__":
    main()
