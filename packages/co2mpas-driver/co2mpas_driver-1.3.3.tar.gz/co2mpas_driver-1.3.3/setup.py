#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright 2015-2019 European Commission (JRC);
# Licensed under the EUPL (the 'Licence');
# You may not use this work except in compliance with the Licence.
# You may obtain a copy of the Licence at: http://ec.europa.eu/idabc/eupl
"""
new_MFC setup.

"""

import os
import shutil
from os import path as osp

my_dir = osp.dirname(osp.abspath(__file__))
os.chdir(my_dir)

name = "co2mpas_driver"


if __name__ == "__main__":
    from setuptools import setup, find_packages

    def read_file(fpath):
        with open(fpath) as fd:
            return fd.read()

    dir_list = ["build", "dist", "{}.egg-info".format(name)]

    for d in dir_list:
        try:
            shutil.rmtree(d)
        except:
            pass

    test_deps = ["pytest"]

    url = "https://code.europa.eu/jrc-ldv/%s" % name

    setup(
        name=name,
        version="1.3.3",
        packages=find_packages(
            exclude=[
                "test",
                "test.*",
            ]
        ),
        license="European Union Public Licence 1.1 or later (EUPL 1.1+)",
        description="A lightweight microsimulation free-flow acceleration model"
        "(MFC) or co2mpas_driver is a model that is able to "
        "capture the vehicle acceleration dynamics accurately and "
        "consistently",
        long_description=read_file("README.rst"),
        project_urls={"Sources": url},
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research",
            "Intended Audience :: Manufacturing",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: Implementation :: CPython",
            "Natural Language :: English",
            "Environment :: Console",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: POSIX",
            "Operating System :: Unix",
        ],
        install_requires=[
            "PyYAML",
            "schedula[all]>=0.3.2",
            "tqdm",
            "scikit-learn",
            "regex",
            "lmfit>=0.9.7",
            "numpy",
            "schema",
            "scipy",
            "wltp",
            "xgboost",
            "pandas",
            "networkx",
        ],
        tests_require=test_deps,
        package_data={"co2mpas_driver": ["template/*.xlsx", "db/*.csv", "*"]},
        entry_points="""[console_scripts]
        run_simulation=co2mpas_driver.sample_simulation:run_simulation""",
        include_package_data=True,
        zip_safe=True,
        options={"bdist_wheel": {"universal": True}},
        platforms=["any"],
    )
