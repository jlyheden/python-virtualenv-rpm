clean: ; rm -rf my-virtualenv*

clean-rpm: ; rm -rf rpm/SOURCES* && rm -rf rpm/BUILD*

build-virtualenv: clean ; virtualenv --no-site-packages -p "${PYTHON}" my-virtualenv && my-virtualenv/bin/python setup.py install && virtualenv --relocatable my-virtualenv

build-rpm: clean-rpm ; test -d rpm/BUILD || mkdir rpm/BUILD && cp -rp my-virtualenv/* rpm/BUILD && rpmbuild --define '_topdir '`pwd`/rpm --define 'VERSION '"${VERSION}" --define 'PYTHON_DEPENDENCY '"${PYTHON}" -ba `pwd`/rpm/SPECS/mymodule.spec
