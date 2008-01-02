%define module  SVN-SVNLook
%define name    perl-%{module}
%define version 0.04
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Perl wrapper to the svnlook command
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/SVN/%{module}-%{version}.tar.bz2
BuildRequires:  perl(Module::Build)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
SVN::SVNLook runs the command line client. This module was created to make
adding hooks script easier to manipulate.

%prep
%setup -q -n %{module}-%{version}
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

