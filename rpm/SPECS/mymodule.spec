Name:           mymodule
Version:        %{?VERSION}
Release:        1%{?dist}
Summary:        Python package for mymodule
License:        BSD
BuildRequires:  chrpath prelink python-virtualenv libxml2-devel libxslt-devel
Source0:        %{name}-%{version}.tar.gz
Requires:       %{?PYTHON_DEPENDENCY}

%define install_path /opt/%{name}

%description
Python package for mymodule

%prep
%setup -q -n %{name}-%{version}

%build
virtualenv --no-site-packages -p %{PYTHON_DEPENDENCY} $RPM_BUILD_DIR/virtualenv
$RPM_BUILD_DIR/virtualenv/bin/pip install $RPM_BUILD_DIR/%{name}-%{version}
virtualenv --relocatable $RPM_BUILD_DIR/virtualenv

%install
mkdir -p $RPM_BUILD_ROOT%{install_path}
cp -rp $RPM_BUILD_DIR/virtualenv/* $RPM_BUILD_ROOT%{install_path}
find $RPM_BUILD_ROOT%{install_path} -type f -perm /u+x,g+x -exec /usr/sbin/prelink -u {} \;
find $RPM_BUILD_ROOT%{install_path} -type f -name "*.pyc" -delete
#chrpath -d $RPM_BUILD_ROOT/opt/pyenv/%{ENVNAME}/bin/uwsgi
rm $RPM_BUILD_ROOT%{install_path}/lib64
ln -sf %{install_path}/lib $RPM_BUILD_ROOT%{install_path}/lib64
sed -i -e 's|^VIRTUAL_ENV=".*"|VIRTUAL_ENV="%{install_path}"|' $RPM_BUILD_ROOT%{install_path}/bin/activate

%clean

%files
%defattr(-,root,root,-)
%doc
%{install_path}


%changelog

