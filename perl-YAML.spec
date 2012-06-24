#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	YAML
Summary:	YAML - YAML Ain't Markup Language (tm)
Summary(pl):	YAML - YAML nie jest j�zykiem znacznik�w
Name:		perl-YAML
Version:	0.38
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/I/IN/INGY/%{pdir}-%{version}.tar.gz
# Source0-md5:	13820faf3a87324f46b22908b9f0a755
URL:		http://www.yaml.org/spec/
BuildRequires:	perl-devel >= 1:5.8.0
%{?with_tests:BuildRequires:	perl-perldoc}
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
Modu� YAML.pm jest implementacj� klas YAML Loader i Dumper bazuj�cych
na specyfikacji YAML 1.0. YAML to j�zyk do serializacji og�lnych
danych, zoptymalizowany pod wzgl�dem czytelno�ci dla cz�owieka. Mo�e
by� u�ywany do wyra�ania struktur danych wi�kszo�ci wsp�czesnych
j�zyk�w programowania (w��cznie z Perlem).

%prep
%setup -q -n %{pdir}-%{version}

%build
yes | perl Makefile.PL \
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
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/%{pdir}
%{_mandir}/man[13]/*
