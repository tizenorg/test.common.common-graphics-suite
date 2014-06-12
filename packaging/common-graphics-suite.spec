Name:            common-graphics-suite
Summary:         Graphics suite for Tizen Common
Version:         1.0.0
Release:         1
License:         GPL-2.0
Group:           Development/Testing
Source:          %{name}-%{version}.tar.gz
Source1001:      %{name}.manifest
BuildRoot:       %{_tmppath}/%{name}-%{version}-build
Requires:        common-suite-launcher
Requires:        testkit-lite
Requires:        wayland-fits-master
BuildArch:       noarch


%description
The common-graphics-suite validates graphical features of the Tizen Common image : wayland, wayland-efl integration - software and accelerated modes


%prep
%setup -q
cp %{SOURCE1001} .


%build


%install
install -d %{buildroot}/%{_datadir}/tests/%{name}
install -m 0755 common/runtest.sh %{buildroot}/%{_datadir}/tests/%{name}
install -m 0644 common/*.xml %{buildroot}/%{_datadir}/tests/%{name}
install -m 0644 LICENSE %{buildroot}/%{_datadir}/tests/%{name}
cp -r common/TESTDIR %{buildroot}/%{_datadir}/tests/%{name}


%files
%manifest %{name}.manifest
%defattr(-,root,root)
%{_datadir}/tests/%{name}
