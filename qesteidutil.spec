%define version 0.3.0
%define rel 1
%define release %mkrel %rel

Name:		qesteidutil
Version:	%{version}
Release:	%{release}
Summary:	Estonian ID card utility

Group:		Office
License:	LGPLv2+
URL:		http://code.google.com/p/esteid
Source0:	http://esteid.googlecode.com/files/%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-langfix.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	cmake
BuildRequires:	libp11-devel
BuildRequires:	openssl-devel
BuildRequires:	qt4-devel
BuildRequires:	smartcardpp-devel
Requires:	opensc

%description
QEsteidUtil is a user-friendly application for managing Estonian ID Cards.
It can be used to to change and unlock PIN codes, examine the personal 
information stored on the card, extract and view the certificates, set 
up mobile ID and configure a personal @eesti.ee e-mail address.


%prep
%setup -q
%patch0 -p1 -b langfix


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ../..
popd

%make -C %{_target_platform}/build


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C %{_target_platform}/build


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README
%{_bindir}/qesteidutil
%{_datadir}/applications/qesteidutil.desktop
%{_datadir}/icons/hicolor/*/apps/qesteidutil.png


