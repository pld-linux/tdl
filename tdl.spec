Summary:	Todo list managment
Summary(pl):	Zarz±dzanie list± spraw do zrobienia
Name:		tdl
Version:	1.0
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.rrbcurnow.freeuk.com/tdl/%{name}-%{version}.tar.gz
URL:		http://www.rrbcurnow.freeuk.com/tdl/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tdl is a lightweight program for managing a todo list of pending
jobs that you have.

%description -l pl
Tdl jest ma³owymagaj±cym programem umo¿liwiaj±cym zarz±dzanie list±
spraw do wykonania.

%prep
%setup  -q

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install prefix=$RPM_BUILD_ROOT%{_prefix} \
    bindir=$RPM_BUILD_ROOT%{_bindir} \
    mandir=$RPM_BUILD_ROOT%{_mandir} \
    man1dir=$RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf README NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
