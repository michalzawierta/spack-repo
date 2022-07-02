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
#     spack install meep
#
# You can edit this file again by typing:
#
#     spack edit meep
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Meep(AutotoolsPackage):
    """Meep (or MEEP) is a free finite-difference time-domain (FDTD) simulation
    software package developed at MIT to model electromagnetic systems."""

    homepage = "https://github.com/NanoComp/meep/"
    url      = "https://github.com/NanoComp/meep/releases/download/v1.23.0/meep-1.23.0.tar.gz"

    version('1.23.0', sha256='acf5433614bfe86ef88735ebb6a5782ef4903081f898efba52b314d8d86de739')
    version('1.22.0', sha256='251d5cdf4b3b518b62828bb923b1b7a97d4bd620462457487e2b0cf3b8a51202')
    version('1.21.0', sha256='b9ec0646049d69f7335ebd15edf7b710e00dc4e7715989101debd75b49035401')
    version('1.20.0', sha256='0086aa93a02469aa4155618b9344eb6494b32b55423ab99360a8c1781e40f778')
    version('1.19.0', sha256='89221bfd2516ea3b8c204f9f7a0dd7ade137f953c8719763c45a347eece7c873')
    version('1.18.0', sha256='ff0918b92068a5a70f85a44c80f7061033d7c86b8609b667be492ef17170c859')
    version('1.17.1', sha256='cea11aafe8be1d7ab762324d2dc7d9f4a9b713cee87f9722ced2c5cc30f53a99')
    version('1.17',   sha256='a8ad1f414ae6869929e23b719f4a01d04fd9b41acbef0ffa3097d30e5f0ffa72')
    version('1.16.1', sha256='b0dc3c0090a6562eb67ad1dd986a3347dc188c0816dce3c5ec1e8870428d41d3')
    version('1.16.0', sha256='03b8bccad3760cf08f342860d6a31bfe2cac6ebc5df8f324cc2bc87b9c374132')

    variant('blas',     default=True,  description='Enable BLAS support')
    variant('lapack',   default=True,  description='Enable LAPACK support')
    variant('harminv',  default=True,  description='Enable Harminv support')
    variant('guile',    default=True,  description='Enable Guilde support')
    variant('libctl',   default=True,  description='Enable libctl support')
    variant('libgdsii', default=True,  description='Enable libgdsii support')
    variant('mpi',      default=True,  description='Enable MPI support')
    variant('mpb',      default=True,  description='Enable MPB support')
    variant('hdf5',     default=True,  description='Enable HDF5 support')
    variant('gsl',      default=True,  description='Enable GSL support')
    variant('python',   default=True,  description='Enable Python support')
    variant('single',   default=False, description='Enable Single Precision')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool', type='build')

    depends_on('blas',        when='+blas')
    depends_on('lapack',      when='+lapack')
    depends_on('harminv',     when='+harminv')
    depends_on('guile',       when='+guile')
    depends_on('libctl',      when='+libctl')
    depends_on('libgdsii',    when='+libgdsii')
    depends_on('mpi',         when='+mpi')
    depends_on('mpb',         when='+mpb')
    depends_on('hdf5~mpi',    when='+hdf5~mpi')
    depends_on('hdf5+mpi',    when='+hdf5+mpi')
    depends_on('gsl',         when='+gsl')
    with when('+python'):
        depends_on('python')
        depends_on('py-numpy')
        depends_on('swig')
        depends_on('py-mpi4py', when='+mpi')

    def configure_args(self):
        spec = self.spec

        config_args = [
            '--enable-shared'
        ]

        if '+blas' in spec:
            config_args.append('--with-blas={0}'.format(
                spec['blas'].prefix.lib))
        else:
            config_args.append('--without-blas')

        if '+lapack' in spec:
            config_args.append('--with-lapack={0}'.format(
                spec['lapack'].prefix.lib))
        else:
            config_args.append('--without-lapack')

        if '+libctl' in spec:
            config_args.append('--with-libctl={0}'.format(
                join_path(spec['libctl'].prefix.share, 'libctl')))
        else:
            config_args.append('--without-libctl')

        if '+mpi' in spec:
            config_args.append('--with-mpi')
        else:
            config_args.append('--without-mpi')

        if '+hdf5' in spec:
            config_args.append('--with-hdf5')
        else:
            config_args.append('--without-hdf5')

        if '+python' in spec:
            config_args.append('--with-python')
        else:
            config_args.append('--without-python')
            config_args.append('--without-scheme')

        if '+single' in spec:
            config_args.append('--enable-single')

        #if spec.satisfies('@1.21.0:'):
        #    config_args.append('--enable-maintainer-mode')

        return config_args

    def check(self):
        spec = self.spec

        # aniso_disp test fails unless installed with harminv
        # near2far test fails unless installed with gsl
        if '+harminv' in spec and '+gsl' in spec:
            # Most tests fail when run in parallel
            # 2D_convergence tests still fails to converge for unknown reasons
            make('check', parallel=False)

    # test of fixing path
    def setup_run_environment(self, env):
        env.prepend_path('PYTHONPATH', join_path(self.prefix, 'lib', 'python3.9', 'site-packages'))

