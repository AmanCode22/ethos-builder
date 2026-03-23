%global debug_package %{nil}

Name:           ethos-lang
Version:        0.3.0
Release:        1%{?dist}
Summary:        The Ethos Programming Language Compiler

License:        Apache-2.0
URL:            https://github.com/AmanCode22/ethos-builder
Source0:        ethos-lang-v%{version}.tar.gz


BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-packaging
BuildRequires:  gcc
BuildRequires:  patchelf


BuildRequires:  python3-zstandard

Recommends:     forge

%description
Ethos is a modern, lightweight compiled programming language.
It features a native Nuitka-based compiler designed for speed and simplicity.

%prep
%setup -q -n ethos-lang-%{version}

%build

%global pip_flags --user --no-build-isolation --no-deps --no-index --find-links=vendor


%if 0%{?suse_version} == 1500
python3 -m pip install %{pip_flags} nuitka
%else

python3 -m pip install %{pip_flags} --break-system-packages nuitka
%endif


python3 -m nuitka --assume-yes-for-downloads --jobs=1 --low-memory --lto=no --onefile main.py --output-filename=ethos

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 0755 ethos %{buildroot}%{_bindir}/ethos

%files
%{_bindir}/ethos

%changelog
* Mon Mar 23 2026 Aman Adlakha <amanady125@gmail.com> - 0.3.0-1
- Version bump to 0.3.0 and OBS offline build support
- Implemented Hybrid Vendoring (OS Zstandard + Local Nuitka)
- Added conditional PIP flags for Leap 15.6 compatibility
- Throttled Nuitka build (--jobs=1 --lto=no) to prevent ARM OOM crashes
