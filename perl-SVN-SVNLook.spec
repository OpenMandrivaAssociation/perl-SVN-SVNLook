%define upstream_name    SVN-SVNLook
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

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
