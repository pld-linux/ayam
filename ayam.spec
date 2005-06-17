#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	tests		# build without tests
#
Summary:	Ayam is a free 3D modelling environment for the RenderMan interface
Name:		ayam
Version:	1.8.2
Release:	0.1
Epoch:		0
License:	BSD
Group:		-
######		Unknown group!
Source0:	http://dl.sourceforge.net/ayam/%{name}%{version}.src.tar.gz
# Source0-md5:	98984c09e4582e2347e485df962aa499
Patch0:		%{name}-Makefile.shared.patch
URL:		http://ayam.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRequires:	OpenGL-devel
#PreReq:		-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires(postun):	-
#Requires:	-
#Provides:	-
#Obsoletes:	-
#Conflicts:	-
#BuildArch:	noarch
#ExclusiveArch:  %{ix86}
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

%description -l pl

#%package subpackage #Summary: - #Summary(pl): - #Group: -

#%description subpackage

#%description subpackage -l pl

%prep
%setup -q -n %{name}
%patch0 -p1

%build
cd src
make  -f Makefile.shared

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

#%{__make} install \
#	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*

%attr(755,root,root) %{_bindir}/*

%{_datadir}/%{name}

# initscript and its config
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}

#%files subpackage
#%defattr(644,root,root,755)
#%doc extras/*.gz
#%{_datadir}/%{name}-ext
