Simple example of how to package a self contained RPM out of python software installed in a virtualenv.

## Build requires

Install these rpms: *rpm-build rpmdevtools rpmlint chrpath*

## Building

Should be quite easy to hook into whatever CI system, the example uses Make to drive the different build phases and respects the env var *VERSION* for setting the module version and RPM version. The env var *PYTHON* is used when setting up the virtualenv and forms the python dependency in the spec file.

```
export VERSION=3.0.0
export PYTHON=/usr/bin/python2.6
make build-sdist
make build-rpm
```

I've added lxml as a dependency just to illustrate how to handle python modules that are linked to dynamic libraries. Rpm-build will automatically scan for .so libraries in the build root and add the necessary install dependencies. Nifty :)
