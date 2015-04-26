Name:           libcoap
Version:        4.1.1
Release:        0
Group: System Environment/Libraries
License:        BSD
Summary:        Lightweight application-protocol for devices that are constrained their resources such as computing power, RF range, memory, bandwith, or network packet sizes.
Url:            http://sourceforge.net/projects/libcoap/
Source:         %{name}-%{version}.tar.gz
Conflicts:      iotivity

%description
Lightweight application-protocol for devices that are constrained their resources such as computing power, RF range, memory, bandwith, or network packet sizes. 
This protocol, CoAP, is developed in the IETF working group "CoRE"


%prep
%setup -q


%build
%configure
make -d

%install
mkdir -p %{buildroot}%{_libdir}/examples

install -m 755 examples/coap* %{buildroot}%{_libdir}/examples
install -m 755 examples/etsi* %{buildroot}%{_libdir}/examples
install -m 755 examples/rd %{buildroot}%{_libdir}/examples

%files
%{_libdir}/examples/*
