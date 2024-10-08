# encoding: utf-8

"""
Test module for ``mtag.sif`` singularity build
or ``mtag`` dockerfile build

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
    pth = os.path.join('apptainer', 'mtag.sif')
    try:
        out = subprocess.run('singularity')
        runtime = 'singularity'
    except FileNotFoundError:
        try:
            out = subprocess.run('apptainer')
            runtime = 'apptainer'
        except FileNotFoundError:
            raise FileNotFoundError
    cwd = os.getcwd()
    MTAG = f'{runtime} run {pth}'
    PREFIX = f'{runtime} exec {pth} python'
    PREFIX_MOUNT = f'{runtime} exec --home={cwd}:/home/ {pth} python'
except FileNotFoundError:
    try:
        out = subprocess.run('docker')
        pwd = os.getcwd()
        MTAG = ('docker run ' +
                  'ghcr.io/comorment/mtag')
        PREFIX = ('docker run ' +
                  '--entrypoint python ' +
                  'ghcr.io/comorment/mtag')
        PREFIX_MOUNT = (
            'docker run ' +
            f'--mount type=bind,source={pwd},target={pwd} ' +
            '--entrypoint python ' +
            'ghcr.io/comorment/mtag')
    except FileNotFoundError as err:
        # neither singularity nor docker found, fall back to plain python
        mssg = 'Neither singularity, apptainer nor docker found; tests fail'
        raise FileNotFoundError(mssg) from err
        


def test_assert():
    """dummy test that should pass"""
    assert True


def test_mtag_python():
    """test that the Python installation works"""
    call = f'{PREFIX} --version'
    out = subprocess.run(call.split(' '))
    assert out.returncode == 0


def test_mtag_python_script():
    '''test that Python can run a script'''
    pwd = os.getcwd() if PREFIX.rfind('docker') >= 0 else '.'
    call = f'''{PREFIX_MOUNT} {pwd}/tests/extras/hello.py'''
    out = subprocess.run(call.split(' '), capture_output=True)
    assert out.returncode == 0


def test_mtag_python_packages():
    '''test that the Python packages are installed'''
    packages = [
        'numpy',
        'scipy',
        'pandas',
        'joblib',
        'bitarray',
    ]
    importstr = 'import ' + ', '.join(packages)
    call = f"{PREFIX} -c '{importstr}'"
    out = subprocess.run(call, shell=True)
    assert out.returncode == 0

def test_mtag():
    '''test that the mtag command is available'''
    call = f'{MTAG} --help'
    out = subprocess.run(call.split(' '))
    assert out.returncode == 0