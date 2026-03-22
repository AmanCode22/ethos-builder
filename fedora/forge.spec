Name:           forge
Version:        0.2.0
Release:        1%{?dist}
Summary:        The project management toolchain for the Ethos language.

License:        GPL-3.0-or-later
URL:            https://github.com/AmanCode22/forge

Source0:        https://github.com/AmanCode22/forge/archive/refs/tags/v0.2.0-alpha.tar.gz#/forge-v0.2.0-alpha.tar.gz

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  python3-pip
BuildRequires:  patchelf


Requires:       bash
Requires:       ethos >= %{version}

%description
Forge is the official project manager for Ethos. It handles project initialization, dependency management, and build workflows.

%prep
%setup -q -n forge-0.2.0-alpha

%build
python3 -m pip install -r requirements.txt
python3 -m nuitka --assume-yes-for-downloads --onefile main.py --output-filename=forge

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 forge %{buildroot}%{_bindir}/forge

%files
%{_bindir}/forge

%changelog
* Sat Mar 21 2026 Aman Adhlakha <amanady125@gmail.com> - 0.2.0-1
- Intial rpm build, for more see release on github.
