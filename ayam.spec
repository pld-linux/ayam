Summary:	Ayam - a free 3D modelling environment for the RenderMan interface
Summary(pl.UTF-8):	Ayam - darmowe środowisko do modelowania 3D dla interfejsu RenderMan
Name:		ayam
Version:	1.8.2
Release:	0.1
Epoch:		0
License:	BSD
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/ayam/%{name}%{version}.src.tar.gz
# Source0-md5:	98984c09e4582e2347e485df962aa499
Patch0:		%{name}-Makefile.shared.patch
URL:		http://ayam.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ayam is a free (as in free speech, BSD-licensed) 3D modelling
environment for the RenderMan interface. Free means that neither the
author nor any contributors make money out of this software. We need
your (yes your!) feedback to keep this project alive. If you use Ayam,
please submit your pictures, bug reports, or feature requests.

Ayam features at a glance:

- RIB (RenderMan Interface Bytestream) export and import.
- Support for NURBS curves and (trimmed) NURBS surfaces, Boxes,
  Quadrics (Sphere, Disk, Cylinder, Cone, Hyperboloid, Paraboloid, and
  Torus), CSG, MetaBalls, Patch Meshes, Polygonal Meshes, and
  Subdivision Surfaces.
- NURBS modelling includes normal and interpolating curves as well as
  extrude, revolve, sweep, birail, skin and gordon objects with caps,
  holes, and bevels.
- Custom objects that may freely implement their representations
  (using OpenGL and RIB) and even small GUIs to edit their type specific
  parameters may be written by the user and dynamically loaded at
  runtime.
- Scripting interface: Tcl.
- Misc: instancing, arbitrary number of modeling views, object
  clipboard, independent property clipboard, console, n-level undo.

%description -l pl.UTF-8
Ayam to wolnodostępne (na licencji BSD) środowisko do modelowania 3D
dla interfejsu RenderMan. Wolnodostępne oznacza, że autor ani
współtwórcy nie otrzymują pieniędzy za to oprogramowanie; potrzebują
natomiast sprzężenia zwrotnego od użytkowników, aby utrzymać projekt
przy życiu. Używający Ayama proszeni są o wysyłanie obrazów, zgłoszeń
błędów i próśb o nowe możliwości.

Przegląd możliwości Ayama:
- eksport i import RIB (RenderMan Interface Bytestream)
- obsługa krzywych NURBS i (obciętych) powierzchni NURBS,
  prostopadłościanów, kwadryk (sfer, dysków, cylindrów, stożków,
  hiperboloid, paraboloid, torusów), CSG, metakul, siatek łat, siatek
  wielokątnych oraz powierzchni podpodziału
- modelowanie NURBS obejmuje krzywe normalne i interpolowane, a także
  wytłaczanie, obroty, odchylanie, obiekty powłok z czapami, dziurami
  i szwami
- użytkownik może tworzyć i wczytywać dynamicznie w czasie działania
  programu własne obiekty łatwo implementujące swoje reprezentacje
  (przy użyciu OpenGL i RIB), a nawet małe GUI do edycji specyficznych
  dla obiektu parametrów
- interfejs skryptowy: Tcl
- różne: tworzenie instancji, dowolna liczba widoków modelowania,
  schowek dla obiektów, niezależny schowek dla własności, konsola,
  n-poziomowe undo

%prep
%setup -q -n %{name}
%patch -P0 -p1

%build
mv src/affine/src/write.c src/affine/src/write.cpp 
%{__make} -C src -f Makefile.shared clean
# TODO: optflags
%{__make} -C src -f Makefile.shared

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} -C src -f Makefile.shared install \
	PREFIX=$RPM_BUILD_ROOT/usr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%{_datadir}/%{name}
