#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	YAML
Summary:	YAML - YAML Ain't Markup Language (tm)
Summary(pl):	YAML - YAML nie jest jêzykiem znaczników
Name:		perl-YAML
Version:	0.35
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/I/IN/INGY/%{pdir}-%{version}.tar.gz
URL:		http://www.yaml.org/spec/
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The YAML.pm module implements a YAML Loader and Dumper based on the
YAML 1.0 specification.

YAML is a generic data serialization language that is optimized for
human readability. It can be used to express the data structures of
most modern programming languages.  (Including Perl!!!)

%description -l pl
Modu³ YAML.pm jest implementacj± klas YAML Loader i Dumper bazuj±cych
na specyfikacji YAML 1.0. YAML to jêzyk do serializacji ogólnych
danych, zoptymalizowany pod wzglêdem czytelno¶ci dla cz³owieka. Mo¿e
byæ u¿ywany do wyra¿ania struktur danych wiêkszo¶ci wspó³czesnych
jêzyków programowania (w³±cznie z Perlem).

%prep
%setup -q -n %{pdir}-%{version}

%build
yes | perl Makefile.PL \
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
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/%{pdir}
%{_mandir}/man[13]/*
