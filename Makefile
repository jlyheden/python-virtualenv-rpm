clean: ; rm -rf my-virtualenv*

build-virtualenv: clean ; virtualenv --no-site-packages my-virtualenv && my-virtualenv/bin/python setup.py install && virtualenv --relocatable my-virtualenv && tar zcf my-virtualenv.tgz -C my-virtualenv .

build-rpm: ; cp my-virtualenv.tgz rpm/SOURCES && rpmbuild --define '_topdir '`pwd`/rpm --define 'VERSION '$VERSION -ba `pwd`/rpm/SPECS/my-virtualenv.spec
