#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	25.08.0
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kde-dev-scripts
Summary:	Kde dev scripts
Name:		ka6-%{kaname}
Version:	25.08.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	c68d8b64e21f62ad319e4b0b9059568f
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%global		debug_package	%{nil}

%description
Scripts and setting files useful during development of KDE software.

%description -l pl.UTF-8
Skrypty i pliki ustawień użyteczne przy programowaniu KDE.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQT_MAJOR_VERSION=6
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

find $RPM_BUILD_ROOT%{_bindir} -type f -exec sed -i -e 's#/usr/bin/env perl#/usr/bin/perl#' '{}' +
find $RPM_BUILD_ROOT%{_bindir} -type f -exec sed -i -e 's#/usr/bin/env python3#/usr/bin/python3#' '{}' +
find $RPM_BUILD_ROOT%{_bindir} -type f -exec sed -i -e 's#/usr/bin/env python#/usr/bin/python3#' '{}' +
find $RPM_BUILD_ROOT%{_bindir} -type f -exec sed -i -e 's#/usr/bin/env bash#/bin/bash#' '{}' +

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/adddebug
%attr(755,root,root) %{_bindir}/addmocincludes
%attr(755,root,root) %{_bindir}/build-progress.sh
%attr(755,root,root) %{_bindir}/c++-copy-class-and-file
%attr(755,root,root) %{_bindir}/c++-rename-class-and-file
%attr(755,root,root) %{_bindir}/cheatmake
%attr(755,root,root) %{_bindir}/clean-forward-declaration.sh
%attr(755,root,root) %{_bindir}/clean-includes.sh
%attr(755,root,root) %{_bindir}/colorsvn
%attr(755,root,root) %{_bindir}/create_cvsignore
%attr(755,root,root) %{_bindir}/create_makefile
%attr(755,root,root) %{_bindir}/create_makefiles
%attr(755,root,root) %{_bindir}/create_svnignore
%attr(755,root,root) %{_bindir}/cvs-clean
%attr(755,root,root) %{_bindir}/cvsaddcurrentdir
%attr(755,root,root) %{_bindir}/cvsbackport
%attr(755,root,root) %{_bindir}/cvsblame
%attr(755,root,root) %{_bindir}/cvscheck
%attr(755,root,root) %{_bindir}/cvsforwardport
%attr(755,root,root) %{_bindir}/cvslastchange
%attr(755,root,root) %{_bindir}/cvslastlog
%attr(755,root,root) %{_bindir}/cvsrevertlast
%attr(755,root,root) %{_bindir}/cvsversion
%attr(755,root,root) %{_bindir}/cxxmetric
%attr(755,root,root) %{_bindir}/draw_lib_dependencies
%attr(755,root,root) %{_bindir}/extend_dmalloc
%attr(755,root,root) %{_bindir}/extractattr
%attr(755,root,root) %{_bindir}/extractrc
%attr(755,root,root) %{_bindir}/findmissingcrystal
%attr(755,root,root) %{_bindir}/fix-include.sh
%attr(755,root,root) %{_bindir}/fixkdeincludes
%attr(755,root,root) %{_bindir}/fixuifiles
%attr(755,root,root) %{_bindir}/grantlee_strings_extractor.py
%attr(755,root,root) %{_bindir}/includemocs
%attr(755,root,root) %{_bindir}/kde-systemsettings-tree.py
%attr(755,root,root) %{_bindir}/kde_generate_export_header
%attr(755,root,root) %{_bindir}/kdedoc
%attr(755,root,root) %{_bindir}/kdekillall
%attr(755,root,root) %{_bindir}/kdelnk2desktop.py
%attr(755,root,root) %{_bindir}/kdemangen.pl
%attr(755,root,root) %{_bindir}/krazy-licensecheck
%attr(755,root,root) %{_bindir}/makeobj
%attr(755,root,root) %{_bindir}/noncvslist
%attr(755,root,root) %{_bindir}/nonsvnlist
%attr(755,root,root) %{_bindir}/optimizegraphics
%attr(755,root,root) %{_bindir}/package_crystalsvg
%attr(755,root,root) %{_bindir}/png2mng.pl
%attr(755,root,root) %{_bindir}/port_new_gitlab_ci_template.sh
%attr(755,root,root) %{_bindir}/pruneemptydirs
%attr(755,root,root) %{_bindir}/reviewboard-am
%attr(755,root,root) %{_bindir}/svn-clean
%attr(755,root,root) %{_bindir}/svnbackport
%attr(755,root,root) %{_bindir}/svnchangesince
%attr(755,root,root) %{_bindir}/svnforwardport
%attr(755,root,root) %{_bindir}/svngettags
%attr(755,root,root) %{_bindir}/svnintegrate
%attr(755,root,root) %{_bindir}/svnlastchange
%attr(755,root,root) %{_bindir}/svnlastlog
%attr(755,root,root) %{_bindir}/svnrevertlast
%attr(755,root,root) %{_bindir}/svnversions
%attr(755,root,root) %{_bindir}/uncrustify-kf5
%attr(755,root,root) %{_bindir}/wcgrep
%attr(755,root,root) %{_bindir}/zonetab2pot.py
%lang(ca) %{_mandir}/ca/man1/adddebug.1*
%lang(ca) %{_mandir}/ca/man1/cheatmake.1*
%lang(ca) %{_mandir}/ca/man1/create_cvsignore.1*
%lang(ca) %{_mandir}/ca/man1/create_makefile.1*
%lang(ca) %{_mandir}/ca/man1/create_makefiles.1*
%lang(ca) %{_mandir}/ca/man1/cvscheck.1*
%lang(ca) %{_mandir}/ca/man1/cvslastchange.1*
%lang(ca) %{_mandir}/ca/man1/cvslastlog.1*
%lang(ca) %{_mandir}/ca/man1/cvsrevertlast.1*
%lang(ca) %{_mandir}/ca/man1/cxxmetric.1*
%lang(ca) %{_mandir}/ca/man1/extend_dmalloc.1*
%lang(ca) %{_mandir}/ca/man1/extractrc.1*
%lang(ca) %{_mandir}/ca/man1/fixincludes.1*
%lang(ca) %{_mandir}/ca/man1/pruneemptydirs.1*
%lang(ca) %{_mandir}/ca/man1/zonetab2pot.py.1*
%lang(da) %{_mandir}/da/man1/adddebug.1*
%lang(da) %{_mandir}/da/man1/cheatmake.1*
%lang(da) %{_mandir}/da/man1/create_cvsignore.1*
%lang(da) %{_mandir}/da/man1/create_makefiles.1*
%lang(da) %{_mandir}/da/man1/cvscheck.1*
%lang(da) %{_mandir}/da/man1/cvslastchange.1*
%lang(da) %{_mandir}/da/man1/cvslastlog.1*
%lang(da) %{_mandir}/da/man1/cvsrevertlast.1*
%lang(da) %{_mandir}/da/man1/cxxmetric.1*
%lang(da) %{_mandir}/da/man1/extend_dmalloc.1*
%lang(da) %{_mandir}/da/man1/extractrc.1*
%lang(da) %{_mandir}/da/man1/fixincludes.1*
%lang(da) %{_mandir}/da/man1/pruneemptydirs.1*
%lang(da) %{_mandir}/da/man1/zonetab2pot.py.1*
%lang(de) %{_mandir}/de/man1/adddebug.1*
%lang(de) %{_mandir}/de/man1/cheatmake.1*
%lang(de) %{_mandir}/de/man1/create_cvsignore.1*
%lang(de) %{_mandir}/de/man1/create_makefile.1*
%lang(de) %{_mandir}/de/man1/create_makefiles.1*
%lang(de) %{_mandir}/de/man1/cvscheck.1*
%lang(de) %{_mandir}/de/man1/cvslastchange.1*
%lang(de) %{_mandir}/de/man1/cvslastlog.1*
%lang(de) %{_mandir}/de/man1/cvsrevertlast.1*
%lang(de) %{_mandir}/de/man1/cxxmetric.1*
%lang(de) %{_mandir}/de/man1/extend_dmalloc.1*
%lang(de) %{_mandir}/de/man1/extractrc.1*
%lang(de) %{_mandir}/de/man1/fixincludes.1*
%lang(de) %{_mandir}/de/man1/pruneemptydirs.1*
%lang(de) %{_mandir}/de/man1/zonetab2pot.py.1*
%lang(es) %{_mandir}/es/man1/adddebug.1*
%lang(es) %{_mandir}/es/man1/cheatmake.1*
%lang(es) %{_mandir}/es/man1/create_cvsignore.1*
%lang(es) %{_mandir}/es/man1/create_makefile.1*
%lang(es) %{_mandir}/es/man1/create_makefiles.1*
%lang(es) %{_mandir}/es/man1/cvscheck.1*
%lang(es) %{_mandir}/es/man1/cvslastchange.1*
%lang(es) %{_mandir}/es/man1/cvslastlog.1*
%lang(es) %{_mandir}/es/man1/cvsrevertlast.1*
%lang(es) %{_mandir}/es/man1/cxxmetric.1*
%lang(es) %{_mandir}/es/man1/extend_dmalloc.1*
%lang(es) %{_mandir}/es/man1/extractrc.1*
%lang(es) %{_mandir}/es/man1/fixincludes.1*
%lang(es) %{_mandir}/es/man1/pruneemptydirs.1*
%lang(es) %{_mandir}/es/man1/zonetab2pot.py.1*
%lang(fr) %{_mandir}/fr/man1/adddebug.1*
%lang(fr) %{_mandir}/fr/man1/cheatmake.1*
%lang(fr) %{_mandir}/fr/man1/create_cvsignore.1*
%lang(fr) %{_mandir}/fr/man1/create_makefile.1*
%lang(fr) %{_mandir}/fr/man1/create_makefiles.1*
%lang(fr) %{_mandir}/fr/man1/cvscheck.1*
%lang(fr) %{_mandir}/fr/man1/cvslastchange.1*
%lang(fr) %{_mandir}/fr/man1/cvslastlog.1*
%lang(fr) %{_mandir}/fr/man1/cvsrevertlast.1*
%lang(fr) %{_mandir}/fr/man1/cxxmetric.1*
%lang(fr) %{_mandir}/fr/man1/extend_dmalloc.1*
%lang(fr) %{_mandir}/fr/man1/extractrc.1*
%lang(fr) %{_mandir}/fr/man1/fixincludes.1*
%lang(fr) %{_mandir}/fr/man1/pruneemptydirs.1*
%lang(fr) %{_mandir}/fr/man1/zonetab2pot.py.1*
%lang(gl) %{_mandir}/gl/man1/adddebug.1*
%lang(gl) %{_mandir}/gl/man1/cheatmake.1*
%lang(gl) %{_mandir}/gl/man1/create_cvsignore.1*
%lang(gl) %{_mandir}/gl/man1/create_makefiles.1*
%lang(gl) %{_mandir}/gl/man1/cvscheck.1*
%lang(gl) %{_mandir}/gl/man1/cvslastchange.1*
%lang(gl) %{_mandir}/gl/man1/cvslastlog.1*
%lang(gl) %{_mandir}/gl/man1/cvsrevertlast.1*
%lang(gl) %{_mandir}/gl/man1/cxxmetric.1*
%lang(gl) %{_mandir}/gl/man1/extend_dmalloc.1*
%lang(gl) %{_mandir}/gl/man1/extractrc.1*
%lang(gl) %{_mandir}/gl/man1/fixincludes.1*
%lang(gl) %{_mandir}/gl/man1/pruneemptydirs.1*
%lang(gl) %{_mandir}/gl/man1/zonetab2pot.py.1*
%lang(it) %{_mandir}/it/man1/adddebug.1*
%lang(it) %{_mandir}/it/man1/cheatmake.1*
%lang(it) %{_mandir}/it/man1/create_cvsignore.1*
%lang(it) %{_mandir}/it/man1/create_makefile.1*
%lang(it) %{_mandir}/it/man1/create_makefiles.1*
%lang(it) %{_mandir}/it/man1/cvscheck.1*
%lang(it) %{_mandir}/it/man1/cvslastchange.1*
%lang(it) %{_mandir}/it/man1/cvslastlog.1*
%lang(it) %{_mandir}/it/man1/cvsrevertlast.1*
%lang(it) %{_mandir}/it/man1/cxxmetric.1*
%lang(it) %{_mandir}/it/man1/extend_dmalloc.1*
%lang(it) %{_mandir}/it/man1/extractrc.1*
%lang(it) %{_mandir}/it/man1/fixincludes.1*
%lang(it) %{_mandir}/it/man1/pruneemptydirs.1*
%lang(it) %{_mandir}/it/man1/zonetab2pot.py.1*
%lang(C) %{_mandir}/man1/adddebug.1*
%lang(C) %{_mandir}/man1/cheatmake.1*
%lang(C) %{_mandir}/man1/create_cvsignore.1*
%lang(C) %{_mandir}/man1/create_makefile.1*
%lang(C) %{_mandir}/man1/create_makefiles.1*
%lang(C) %{_mandir}/man1/cvscheck.1*
%lang(C) %{_mandir}/man1/cvslastchange.1*
%lang(C) %{_mandir}/man1/cvslastlog.1*
%lang(C) %{_mandir}/man1/cvsrevertlast.1*
%lang(C) %{_mandir}/man1/cxxmetric.1*
%lang(C) %{_mandir}/man1/extend_dmalloc.1*
%lang(C) %{_mandir}/man1/extractrc.1*
%lang(C) %{_mandir}/man1/fixincludes.1*
%lang(C) %{_mandir}/man1/pruneemptydirs.1*
%lang(C) %{_mandir}/man1/zonetab2pot.py.1*
%lang(nl) %{_mandir}/nl/man1/adddebug.1*
%lang(nl) %{_mandir}/nl/man1/cheatmake.1*
%lang(nl) %{_mandir}/nl/man1/create_cvsignore.1*
%lang(nl) %{_mandir}/nl/man1/create_makefile.1*
%lang(nl) %{_mandir}/nl/man1/create_makefiles.1*
%lang(nl) %{_mandir}/nl/man1/cvscheck.1*
%lang(nl) %{_mandir}/nl/man1/cvslastchange.1*
%lang(nl) %{_mandir}/nl/man1/cvslastlog.1*
%lang(nl) %{_mandir}/nl/man1/cvsrevertlast.1*
%lang(nl) %{_mandir}/nl/man1/cxxmetric.1*
%lang(nl) %{_mandir}/nl/man1/extend_dmalloc.1*
%lang(nl) %{_mandir}/nl/man1/extractrc.1*
%lang(nl) %{_mandir}/nl/man1/fixincludes.1*
%lang(nl) %{_mandir}/nl/man1/pruneemptydirs.1*
%lang(nl) %{_mandir}/nl/man1/zonetab2pot.py.1*
%lang(pt) %{_mandir}/pt/man1/adddebug.1*
%lang(pt) %{_mandir}/pt/man1/cheatmake.1*
%lang(pt) %{_mandir}/pt/man1/create_cvsignore.1*
%lang(pt) %{_mandir}/pt/man1/create_makefile.1*
%lang(pt) %{_mandir}/pt/man1/create_makefiles.1*
%lang(pt) %{_mandir}/pt/man1/cvscheck.1*
%lang(pt) %{_mandir}/pt/man1/cvslastchange.1*
%lang(pt) %{_mandir}/pt/man1/cvslastlog.1*
%lang(pt) %{_mandir}/pt/man1/cvsrevertlast.1*
%lang(pt) %{_mandir}/pt/man1/cxxmetric.1*
%lang(pt) %{_mandir}/pt/man1/extend_dmalloc.1*
%lang(pt) %{_mandir}/pt/man1/extractrc.1*
%lang(pt) %{_mandir}/pt/man1/fixincludes.1*
%lang(pt) %{_mandir}/pt/man1/pruneemptydirs.1*
%lang(pt) %{_mandir}/pt/man1/zonetab2pot.py.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/adddebug.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/cheatmake.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/create_cvsignore.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/create_makefile.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/create_makefiles.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/cvscheck.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/cvslastchange.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/cvslastlog.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/cvsrevertlast.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/cxxmetric.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/extend_dmalloc.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/extractrc.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/fixincludes.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/pruneemptydirs.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/zonetab2pot.py.1*
%lang(ru) %{_mandir}/ru/man1/adddebug.1*
%lang(ru) %{_mandir}/ru/man1/cheatmake.1*
%lang(ru) %{_mandir}/ru/man1/create_cvsignore.1*
%lang(ru) %{_mandir}/ru/man1/create_makefile.1*
%lang(ru) %{_mandir}/ru/man1/create_makefiles.1*
%lang(ru) %{_mandir}/ru/man1/cvscheck.1*
%lang(ru) %{_mandir}/ru/man1/cvslastchange.1*
%lang(ru) %{_mandir}/ru/man1/cvslastlog.1*
%lang(ru) %{_mandir}/ru/man1/cvsrevertlast.1*
%lang(ru) %{_mandir}/ru/man1/cxxmetric.1*
%lang(ru) %{_mandir}/ru/man1/extend_dmalloc.1*
%lang(ru) %{_mandir}/ru/man1/extractrc.1*
%lang(ru) %{_mandir}/ru/man1/fixincludes.1*
%lang(ru) %{_mandir}/ru/man1/pruneemptydirs.1*
%lang(ru) %{_mandir}/ru/man1/zonetab2pot.py.1*
%lang(sl) %{_mandir}/sl/man1/adddebug.1*
%lang(sl) %{_mandir}/sl/man1/cheatmake.1*
%lang(sl) %{_mandir}/sl/man1/create_cvsignore.1*
%lang(sl) %{_mandir}/sl/man1/create_makefile.1*
%lang(sl) %{_mandir}/sl/man1/create_makefiles.1*
%lang(sl) %{_mandir}/sl/man1/cvscheck.1*
%lang(sl) %{_mandir}/sl/man1/cvslastchange.1*
%lang(sl) %{_mandir}/sl/man1/cvslastlog.1*
%lang(sl) %{_mandir}/sl/man1/cvsrevertlast.1*
%lang(sl) %{_mandir}/sl/man1/cxxmetric.1*
%lang(sl) %{_mandir}/sl/man1/extend_dmalloc.1*
%lang(sl) %{_mandir}/sl/man1/extractrc.1*
%lang(sl) %{_mandir}/sl/man1/fixincludes.1*
%lang(sl) %{_mandir}/sl/man1/pruneemptydirs.1*
%lang(sl) %{_mandir}/sl/man1/zonetab2pot.py.1*
%lang(sv) %{_mandir}/sv/man1/adddebug.1*
%lang(sv) %{_mandir}/sv/man1/cheatmake.1*
%lang(sv) %{_mandir}/sv/man1/create_cvsignore.1*
%lang(sv) %{_mandir}/sv/man1/create_makefile.1*
%lang(sv) %{_mandir}/sv/man1/create_makefiles.1*
%lang(sv) %{_mandir}/sv/man1/cvscheck.1*
%lang(sv) %{_mandir}/sv/man1/cvslastchange.1*
%lang(sv) %{_mandir}/sv/man1/cvslastlog.1*
%lang(sv) %{_mandir}/sv/man1/cvsrevertlast.1*
%lang(sv) %{_mandir}/sv/man1/cxxmetric.1*
%lang(sv) %{_mandir}/sv/man1/extend_dmalloc.1*
%lang(sv) %{_mandir}/sv/man1/extractrc.1*
%lang(sv) %{_mandir}/sv/man1/fixincludes.1*
%lang(sv) %{_mandir}/sv/man1/pruneemptydirs.1*
%lang(sv) %{_mandir}/sv/man1/zonetab2pot.py.1*
%lang(uk) %{_mandir}/uk/man1/adddebug.1*
%lang(uk) %{_mandir}/uk/man1/cheatmake.1*
%lang(uk) %{_mandir}/uk/man1/create_cvsignore.1*
%lang(uk) %{_mandir}/uk/man1/create_makefile.1*
%lang(uk) %{_mandir}/uk/man1/create_makefiles.1*
%lang(uk) %{_mandir}/uk/man1/cvscheck.1*
%lang(uk) %{_mandir}/uk/man1/cvslastchange.1*
%lang(uk) %{_mandir}/uk/man1/cvslastlog.1*
%lang(uk) %{_mandir}/uk/man1/cvsrevertlast.1*
%lang(uk) %{_mandir}/uk/man1/cxxmetric.1*
%lang(uk) %{_mandir}/uk/man1/extend_dmalloc.1*
%lang(uk) %{_mandir}/uk/man1/extractrc.1*
%lang(uk) %{_mandir}/uk/man1/fixincludes.1*
%lang(uk) %{_mandir}/uk/man1/pruneemptydirs.1*
%lang(uk) %{_mandir}/uk/man1/zonetab2pot.py.1*
%{_datadir}/uncrustify
