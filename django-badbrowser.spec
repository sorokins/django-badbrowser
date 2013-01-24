%global with_doc 0

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif


Name:             django-badbrowser
Version:          1.0.10
Release:          1
Summary:          Django Badbrowser
License:          MIT
Vendor:           PlayNice.ly
URL:              playnice.ly
Group:            Development/Languages/Python

Source0:          %{name}-%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-build
BuildArch:        noarch
# for Python 2.6.6
Requires:         python-httpagentparser

%description


%prep
%setup -q -n %{name}-%{version}


%build
%{__python} setup.py build


%install
%__rm -rf %{buildroot}

%{__python} setup.py install -O1


%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README*
%{_usr}/bin
%{python_sitelib}/*

%changelog