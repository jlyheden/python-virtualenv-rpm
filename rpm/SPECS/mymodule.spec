Name:     mymodule
Version:  %{?VERSION}
Release:  1%{?dist}
Summary:  Python package for mymodule
License:  BSD
Source0:  $RPM_SOURCE_DIR/my-virtualenv.tgz
BuildRequires:  chrpath prelink
Requires: /usr/bin/python2.7

%description
Python package for mymodule

%prep
%setup -q -n %{name}

%build

%install
mkdir -p $RPM_BUILD_ROOT/opt/%{name}
cp -rp $RPM_BUILD_DIR/* $RPM_BUILD_ROOT/opt/%{name}
find $RPM_BUILD_ROOT/opt/%{name} -type f -perm /u+x,g+x -exec /usr/sbin/prelink -u {} \;
#chrpath -d $RPM_BUILD_ROOT/opt/pyenv/%{ENVNAME}/bin/uwsgi
rm $RPM_BUILD_ROOT/opt/%{name}/lib64
ln -sf /opt/%{name}/lib $RPM_BUILD_ROOT/opt/%{name}/lib64
sed -i -e 's|^VIRTUAL_ENV=".*"|VIRTUAL_ENV="/opt/%{name}"|' $RPM_BUILD_ROOT/opt/%{name}/bin/activate

%clean

%files
%defattr(-,root,root,-)
%doc
/opt/%{name}/


%changelog

