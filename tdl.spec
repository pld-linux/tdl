Summary:	Todo list managment
Summary(pl.UTF-8):	Zarządzanie listą spraw do zrobienia
Name:		tdl
Version:	1.4.1
Release:	3
License:	GPL
Group:		Applications
Source0:	http://www.rpcurnow.force9.co.uk/tdl/%{name}-%{version}.tar.gz
# Source0-md5:	298b5ac103e6d3cadfdbcd046a6745a9
Patch0:		%{name}-install.patch
URL:		http://www.rc0.org.uk/tdl/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tdl is a lightweight program for managing a todo list of pending
jobs that you have.

%description -l pl.UTF-8
Tdl jest mało wymagającym programem umożliwiającym zarządzanie listą
spraw do wykonania.

%prep
%setup  -q
%patch0 -p1

%build
# not GNU configure
./configure \
	--prefix=%{_prefix} \
	--mandir=%{_mandir} \
	--infodir=%{_infodir}
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	man1dir=$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
