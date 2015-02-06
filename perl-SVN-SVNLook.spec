%define upstream_name    SVN-SVNLook
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:    Perl wrapper to the svnlook command
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/SVN/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl(Module::Build)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
SVN::SVNLook runs the command line client. This module was created to make
adding hooks script easier to manipulate.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
for file in `find lib -type f` Changes README; do
    chmod 644 $file
    perl -pi -e 'tr/\r//d' $file
done

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/SVN
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 404428
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.04-4mdv2009.0
+ Revision: 258421
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.04-3mdv2009.0
+ Revision: 246486
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.04-1mdv2008.1
+ Revision: 140717
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2008.0
+ Revision: 69248
- update to new version 0.04


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-4mdv2007.0
- Rebuild

* Tue Jan 03 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.03-3mdk
- Add BuildRequires

* Tue Jan 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-2mdk
- fix files encoding and perms

* Tue Jan 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdk
- New release 0.03

* Wed Dec 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-1mdk
- first mdk release

