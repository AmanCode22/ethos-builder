# Disable debuginfo and debugsource packages for Nuitka onefile builds
%global debug_package %{nil}

Name:           ethos-lang
Version:        0.3.0
Release:        1%{?dist}
Summary:        The Ethos programming language compiler.

License:        Apache-2.0
URL:            https://github.com/AmanCode22/ethos-lang

Source0:        https://github.com/AmanCode22/ethos-lang/archive/refs/tags/v0.3.0-alpha.tar.gz#/ethos-lang-v0.3.0-alpha.tar.gz

BuildRequires:  python3-devel >= 3.7
BuildRequires:  gcc
BuildRequires:  python3-pip
BuildRequires:  patchelf

Requires:       bash
Recommends:    forge


%description
Ethos is a modern, lightweight programming language designed for cross-platform development.
It features a native compiler powered by Nuitka, enabling fast execution and seamless distribution.

%prep
%setup -q -n ethos-lang-0.3.0-alpha

%build

python3 -m pip install --user -r requirements.txt
python3 -m nuitka --assume-yes-for-downloads --onefile main.py --output-filename=ethos

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 ethos %{buildroot}%{_bindir}/ethos

%files
%{_bindir}/ethos

%changelog
* Mon Mar 23 2026 Aman Adhlakha <amanady125@gmail.com> - 0.3.0-1
- Add -v and --version.
