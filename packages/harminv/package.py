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
#     spack install harminv
#
# You can edit this file again by typing:
#
#     spack edit harminv
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Harminv(AutotoolsPackage):
    """Harmonic Inversion of Time Signals by the Filter Diagonalization Method (FDM), implemented by Steven G. Johnson, Massachusetts Institute of Technology."""

    homepage = "https://github.com/NanoComp/harminv/"
    url      = "https://github.com/NanoComp/harminv/releases/download/v1.4.1/harminv-1.4.1.tar.gz"

    version('1.4.1', sha256='e1b923c508a565f230aac04e3feea23b888b47d8e19b08816a97ee4444233670')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool', type='build')
    depends_on('blas')
    depends_on('lapack')

    def configure_args(self):
        spec = self.spec

        config_args = [
            '--host=x86_64-unknown-linux-gnu',
            '--enable-shared'
        ]
        return config_args

    def check(self):
        spec = self.spec


