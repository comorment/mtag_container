# encoding: utf-8

"""
Test module for ``mtag_container.sif`` singularity build
or ``mtag_container`` dockerfile build

In case ``singularity`` is unavailable, the test function(s) should fall
back to ``docker``.
"""

import os
import socket
import subprocess


# port used by tests
sock = socket.socket()
sock.bind(('', 0))
port = sock.getsockname()[1]

# Check that (1) singularity exist, and (2) if not, check for docker.
# If neither are found, tests will fall back to plain python.
try:
    pth = os.path.join('containers', 'mtag_container.sif')
    out = subprocess.run('singularity')
    cwd = os.getcwd()
    PREFIX = f'singularity run {pth} python'
    PREFIX_MOUNT = f'singularity run --home={cwd}:/home/ {pth} python'
except FileNotFoundError:
    try:
        out = subprocess.run('docker')
        pwd = os.getcwd()
        PREFIX = (f'docker run -p {port}:{port} ' +
                  'ghcr.io/comorment/mtag_container python')
        PREFIX_MOUNT = (
            f'docker run -p {port}:{port} ' +
            f'--mount type=bind,source={pwd},target={pwd} ' +
            'ghcr.io/comorment/mtag_container python')
    except FileNotFoundError:
        # neither singularity nor docker found, fall back to plain python
        PREFIX = 'python'
        PREFIX_MOUNT = 'python'


def test_assert():
    """dummy test that should pass"""
    assert True


def test_mtag_container_python():
    """test that the Python installation works"""
    call = f'{PREFIX} --version'
    out = subprocess.run(call.split(' '))
    assert out.returncode == 0


def test_mtag_container_python_script():
    '''test that Python can run a script'''
    pwd = os.getcwd() if PREFIX.rfind('docker') >= 0 else '.'
    call = f'''{PREFIX_MOUNT} {pwd}/tests/extras/hello.py'''
    out = subprocess.run(call.split(' '), capture_output=True)
    assert out.returncode == 0


def test_mtag_container_python_packages():
    '''test that the Python packages are installed'''
    packages = [
        'numpy',
        'scipy',
        'pandas',
        'matplotlib',
        'seaborn',
        'sklearn',
        'pytest',
        'jupyterlab',
    ]
    importstr = 'import ' + ', '.join(packages)
    call = f"{PREFIX} -c '{importstr}'"
    out = subprocess.run(call, shell=True)
    assert out.returncode == 0
