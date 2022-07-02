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
#     spack install h5utils
#
# You can edit this file again by typing:
#
#     spack edit h5utils
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class H5utils(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/NanoComp/h5utils"
    url      = "https://github.com/NanoComp/h5utils/releases/download/1.13.1/h5utils-1.13.1.tar.gz"

    version('1.13.1', sha256='c5a76f064d6daa3e65583dce2b61202510e67cf6590f076af9a8aa72511d7d65')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool', type='build')
    depends_on('hdf5')
    depends_on('libmatheval')

    def configure_args(self):
        spec = self.spec

        config_args = [
            '--host=x86_64-unknown-linux-gnu',
            '--enable-shared'
        ]
        return config_args

    def check(self):
        spec = self.spec

