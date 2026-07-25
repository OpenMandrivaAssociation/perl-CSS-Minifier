%define upstream_name    CSS-Minifier
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	5

Summary:	Remove unnecessary whitespace from CSS files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/CSS-Minifier
Source0:	https://cpan.metacpan.org/authors/id/P/PM/PMICHAUX/CSS-Minifier-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildArch:	noarch

%description
This module removes unnecessary whitespace from CSS. The primary
requirement developing this module is to not break working stylesheets: if
working CSS is in input then working CSS is output. The Mac/Internet
Explorer comment hack will be minimized but not stripped and so will
continue to function.

This module understands space, horizontal tab, new line, carriage return,
and form feed characters to be whitespace. Any other characters that may be
considered whitespace are not minimized. These other characters include
paragraph separator and vertical tab.

For static CSS files, it is recommended that you minify during the build
stage of web deployment. If you minify on-the-fly then it might be a good
idea to cache the minified file. Minifying static files on-the-fly
repeatedly is wasteful.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Fri Sep 09 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 699162
- import perl-CSS-Minifier

