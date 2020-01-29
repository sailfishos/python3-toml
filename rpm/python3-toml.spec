# fixme: should be defined in base system side
%define python3_sitearch %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")

Name:       python3-toml
Summary:    TOML library (ini-like config parser) for Python 3
Version:    0.10.0
Release:    1
License:    MIT
URL:        https://github.com/uiri/toml.git
Source0:    %{name}-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  python3-devel

%description
Python Library for Tom's Obvious, Minimal Language
TOML is a configuration file format that somewhat resembles that of
.INI files. It is intended to be easy to read and write due to
obvious semantics which aim to be "minimal", and is designed to map
unambiguously to a dictionary.
https://en.wikipedia.org/wiki/TOML

%prep
%autosetup -n %{name}-%{version}/upstream

%build
%{__python3} setup.py build

%install
rm -rf %{buildroot}
%{__python3} setup.py install --skip-build --root %{buildroot}
find %{buildroot}

%files
%license LICENSE
%doc README.rst examples
%{python3_sitearch}/*

