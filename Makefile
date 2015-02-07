clean: ; rm -rf dist

clean-rpm: ; rm -rf rpm/SOURCES* && rm -rf rpm/BUILD*

build-sdist: ; "${PYTHON}" setup.py sdist

build-rpm: clean-rpm ; test -d rpm/SOURCES || mkdir -p rpm/SOURCES && cp dist/*.tar.gz rpm/SOURCES && rpmbuild --define '_topdir '`pwd`/rpm --define 'VERSION '"${VERSION}" --define 'PYTHON_DEPENDENCY '"${PYTHON}" -ba `pwd`/rpm/SPECS/mymodule.spec
