#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Date
%define	pnam	ICal
Summary:	Perl extension for ICalendar date objects
Summary(pl):	Modu³ perla Date::ICal
Name:		perl-Date-ICal
Version:	1.72
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	69e10541f5da09fc0f53474073da6744
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-Date-Leapyear >= 1.03
BuildRequires:	perl-Storable
BuildRequires:	perl-Test-Simple >= 0.19
BuildRequires:	perl-Time-HiRes
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl extension for ICalendar date objects.

%description -l pl
Rozszerzenie perla do obiektów danych ICalendar.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorlib}/Date/ICal.pm
%{perl_vendorlib}/Date/ICal
%{_mandir}/man3/*
