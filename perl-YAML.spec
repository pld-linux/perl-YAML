#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	YAML
Summary:	YAML - YAML Ain't Markup Language (tm)
#Summary(pl):	
Name:		perl-YAML
Version:	0.35
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/I/IN/INGY/%{pdir}-%{version}.tar.gz
URL:		http://www.yaml.org/spec/
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The YAML.pm module implements a YAML Loader and Dumper based on the YAML
1.0 specification.

YAML is a generic data serialization language that is optimized for human
readability. It can be used to express the data structures of most modern
programming languages.  (Including Perl!!!)

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{version}

%build
yes | perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/*.pm
%{perl_sitelib}/%{pdir}
%{_bindir}/*
%{_mandir}/man[13]/*
