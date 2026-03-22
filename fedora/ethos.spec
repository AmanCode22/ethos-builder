Name:           ethos
Version:        0.2.0
Release:        1%{?dist}
Summary:        The Ethos programming language compiler.

License:        Apache-2.0
URL:            https://github.com/AmanCode22/ethos-lang

Source0:        https://github.com/AmanCode22/ethos-lang/archive/refs/tags/v0.2.0-alpha.tar.gz#/ethos-lang-v0.2.0-alpha.tar.gz

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  python3-pip
BuildRequires:  patchelf


Requires:       bash
Requires:       forge >= %{version}

%description
Ethos is a modern, lightweight programming language designed for cross-platform development. It features a native compiler powered by Nuitka, enabling fast execution and seamless distribution.

%prep
%setup -q -n ethos-lang-v0.2.0-alpha

%build
python3 -m pip install -r requirements.txt
python3 -m nuitka --assume-yes-for-downloads --onefile main.py --output-filename=ethos

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 ethos %{buildroot}%{_bindir}/ethos

%files
%{_bindir}/ethos

%changelog
* Sat Mar 22 2026 Aman Adlakha <amanady125@gmail.com> - 0.2.0-1
- Intial rpm build, for more see release on github.
