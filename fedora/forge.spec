%global debug_package %{nil}

Name:           forge
Version:        0.3.0
Release:        1%{?dist}
Summary:        The Forge Project Manager for Ethos

License:        MIT
URL:            https://github.com/AmanCode22/ethos-builder
Source0:        forge-v%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  gcc
BuildRequires:  patchelf
BuildRequires:  zstd
Requires:       ethos >= %{version}

%description
Forge is the official project manager and build tool for the Ethos programming language.
It handles dependency resolution, project scaffolding, and compilation pipelines.

%prep

%setup -q -n forge-%{version}

%build

python3 -m pip install --user --no-index --find-links=vendor nuitka zstandard


python3 -m nuitka --assume-yes-for-downloads --onefile main.py --output-filename=forge

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 0755 forge %{buildroot}%{_bindir}/forge

%files
%{_bindir}/forge

%changelog
* Mon Mar 23 2026 Aman Adlakha <amanady125@gmail.com> - 0.3.0-1
- Version bump to 0.3.0 and OBS offline build support with -v and --version tag support
