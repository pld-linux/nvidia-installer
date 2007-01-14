Summary:	A tool for installing NVIDIA software packages on Unix and Linux systems
Summary(pl):	Narzêdzie do instalowania oprogramowania NVIDIA na systemach Unix i Linux
Name:		nvidia-installer
Version:	1.0.7
Release:	1
License:	GPL v2
Group:		X11
Source0:	ftp://download.nvidia.com/XFree86/nvidia-settings/%{name}-%{version}.tar.gz
# Source0-md5:	40822f911597be9477ebc8054116ea1a
URL:		ftp://download.nvidia.com/XFree86/nvidia-settings/
Patch0:		%{name}-pcilib.patch
BuildRequires:	XFree86-devel
BuildRequires:	ncurses-devel
BuildRequires:	pciutils-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tool for installing NVIDIA software packages on Unix and Linux
systems.

%description -l pl
Narzêdzie do instalowania oprogramowania NVIDIA na systemach Unix
i Linux.

%prep
%setup -q
%patch0 -p1
# x86 static lib
rm -f libpci.a

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=$RPM_BUILD_ROOT%{_prefix} \

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog DRIVER_VERSION README
%attr(755,root,root) %{_bindir}/mkprecompiled
%attr(755,root,root) %{_bindir}/nvidia-installer
%{_mandir}/man1/nvidia-installer.1*
