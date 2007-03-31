#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires Internet connection)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	WWW
%define		pnam	Mechanize-Sleepy
Summary:	WWW::Mechanize::Sleepy - provide pauses to WWW::Mechanize
Summary(pl.UTF-8):	WWW::Mechanize::Sleepy - dodanie przerw do WWW::Mechanize
Name:		perl-WWW-Mechanize-Sleepy
Version:	0.6
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/WWW/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a9354b9996eae9ea7ab519dc6d05374a
URL:		http://search.cpan.org/dist/WWW-Mechanize-Sleepy/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-URI
BuildRequires:	perl-libwww >= 5.76
BuildRequires:	perl(Test::More) >= 0.34
%endif
Requires:	perl-WWW-Mechanize
Requires:	perl-libwww >= 5.76
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WWW::Mechanize::Sleepy subclasses WWW::Mechanize to provide pauses
between your server requests.

%description -l pl.UTF-8
WWW::Mechanize::Sleepy udostępnia podklasę WWW::Mechanize
umożliwiającą wprowadzanie przerw między zapytaniami serwera.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo "y" | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/WWW/Mechanize/*.pm
%{_mandir}/man?/*
