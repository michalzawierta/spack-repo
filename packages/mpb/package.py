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
#     spack install mpb
#
# You can edit this file again by typing:
#
#     spack edit mpb
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Mpb(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/NanoComp/mpb/releases/download/v1.11.1/mpb-1.11.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('1.11.1', sha256='dc55b081c56079727dac92d309f8e4ea84ca6eea9122ec24b7955f8c258608e1')

    variant('libctl',   default=True,  description='Enable libctl support')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool', type='build')
    depends_on('guile')
    depends_on('gsl')
    depends_on('hdf5')
    depends_on('harminv')
    depends_on('libctl', when='+libctl')
    depends_on('zlib')
    depends_on('fftw')

    def configure_args(self):
        spec = self.spec

        config_args = [
            '--with-hdf5',
            '--enable-shared', 
            '--with-hermitian-eps'
        ]

        if '+libctl' in spec:
            config_args.append('--with-libctl={0}'.format(
                join_path(spec['libctl'].prefix.share, 'libctl')))
        else:
            config_args.append('--without-libctl')

        return config_args

    def check(self):
        spec = self.spec

