%global debug_package %{nil}

Name:           ethos
Version:        0.3.0
Release:        1%{?dist}
Summary:        The Ethos Programming Language Compiler

License:        MIT
URL:            https://github.com/AmanCode22/ethos-builder
Source0:        ethos-lang-v%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  gcc
BuildRequires:  patchelf
BuildRequires:  zstd
Recommends:     forge

%description
Ethos is a modern, lightweight compiled programming language.
It features a native Nuitka-based compiler designed for speed and simplicity.

%prep

%setup -q -n ethos-lang-%{version}

%build

python3 -m pip install --user --no-index --find-links=vendor nuitka zstandard


python3 -m nuitka --assume-yes-for-downloads --onefile main.py --output-filename=ethos

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 0755 ethos %{buildroot}%{_bindir}/ethos

%files
%{_bindir}/ethos

%changelog
* Mon Mar 23 2026 Aman Adlakha <amanady125@gmail.com> - 0.3.0-1
- Version bump to 0.3.0 and OBS offline build support with -v and --version tag support
