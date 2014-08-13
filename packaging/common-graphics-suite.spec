Name:            common-graphics-suite
Summary:         Graphics suite for Tizen Common
Version:         1.1
Release:         0
License:         GPL-2.0
Group:           Development/Testing
Source:          %{name}-%{version}.tar.gz
Source1001:      %{name}.manifest
Requires:        common-suite-launcher
Requires:        testkit-lite
Requires:        wayland-fits-master
BuildArch:       noarch


%description
The common-graphics-suite validates graphical features of the
Tizen Common image : wayland, wayland-efl integration in software
and accelerated modes


%prep
%setup -q
cp %{SOURCE1001} .


%build


%install
install -d %{buildroot}/%{_datadir}/tests/%{profile}/%{name}
install -m 0755 runtest %{buildroot}/%{_datadir}/tests/%{profile}/%{name}
install -m 0644 *.xml %{buildroot}/%{_datadir}/tests/%{profile}/%{name}
install -m 0644 LICENSE %{buildroot}/%{_datadir}/tests/%{profile}/%{name}
cp -r TESTDIR %{buildroot}/%{_datadir}/tests/%{profile}/%{name}


%files
%manifest %{name}.manifest
%defattr(-,root,root)
%{_datadir}/tests/%{profile}/%{name}
