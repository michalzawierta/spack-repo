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
#     spack install libctl
#
# You can edit this file again by typing:
#
#     spack edit libctl
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Libctl(AutotoolsPackage):
    """This is libctl, a Guile-based library for supporting flexible control files in scientific simulations."""

    homepage = "https://github.com/NanoComp/libctl"
    url      = "https://github.com/NanoComp/libctl/releases/download/v4.5.1/libctl-4.5.1.tar.gz"

    version('4.5.1', sha256='fcfeb2f13dda05b560f0ec6872757d9318fdfe8f4bc587eb2053a29ba328ae25')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool', type='build')
    depends_on('guile');
 
    def configure_args(self):
        spec = self.spec

        config_args = [
            '--host=x86_64-unknown-linux-gnu',
            '--enable-shared'
        ]
        return config_args

    def check(self):
        spec = self.spec

