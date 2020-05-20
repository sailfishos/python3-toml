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
%py3_build

%install
rm -rf %{buildroot}
%py3_install


%files
%license LICENSE
%doc README.rst examples
# This is a pure python module so only sitelib files
%{python3_sitelib}/toml
%{python3_sitelib}/toml-*.egg-info

