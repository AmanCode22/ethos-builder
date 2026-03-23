%global debug_package %{nil}

Name:           forge
Version:        0.3.0
Release:        1%{?dist}
Summary:        The Ethos Package Manager

License:        GPL-3.0
URL:            https://github.com/AmanCode22/ethos-builder
Source0:        forge-v%{version}.tar.gz


BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-packaging
BuildRequires:  gcc
BuildRequires:  patchelf


BuildRequires:  python3-zstandard

Requires:       ethos-lang

%description
Forge is the official package manager for the Ethos programming language.

%prep
%setup -q -n forge-%{version}

%build

%global pip_flags --user --no-build-isolation --no-deps --no-index --find-links=vendor


%if 0%{?suse_version} == 1500
python3 -m pip install %{pip_flags} nuitka
%else

python3 -m pip install %{pip_flags} --break-system-packages nuitka
%endif


python3 -m nuitka --assume-yes-for-downloads --low-memory --jobs=1 --lto=no --onefile main.py --output-filename=forge

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 0755 forge %{buildroot}%{_bindir}/forge

%files
%{_bindir}/forge

%changelog
* Mon Mar 23 2026 Aman Adhlakha <amanady125@gmail.com> - 0.3.0-1
- Initial release for OBS offline build support
- Implemented Hybrid Vendoring (OS Zstandard + Local Nuitka)
