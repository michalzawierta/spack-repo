# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install libgdsii
#
# You can edit this file again by typing:
#
#     spack edit libgdsii
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Libgdsii(AutotoolsPackage):
    """libGDSII is a C++ library for working with GDSII binary data files, intended primarily for use with the computational 
    electromagnetism codes scuff-em and meep but sufficiently general-purpose to allow other uses as well."""

    homepage = "https://github.com/HomerReid/libGDSII"
    url      = "https://github.com/HomerReid/libGDSII/releases/download/v0.21/libgdsii-0.21.tar.gz"

    version('0.21', sha256='31c90a4fb699746d051c0c597ef0543889c9f17b2a711fed398756ac4f1b1f4c')

    # FIXME: Add dependencies if required.
    # depends_on('foo')
    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool', type='build')

    def configure_args(self):
        spec = self.spec

        config_args = [
            '--host=x86_64-unknown-linux-gnu',
            '--enable-shared'
        ]
        return config_args

    def check(self):
        spec = self.spec

