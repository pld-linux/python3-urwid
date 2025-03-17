#
# Conditional build:
%bcond_without	doc	# docs build
%bcond_with	tests	# test target (fails on builders due to lack of pts)

%define 	module	urwid
Summary:	Urwid - a console user interface library for Python 3
Summary(hu.UTF-8):	Urwid egy konzolos felhasználói felület könyvtár Pythonhoz 3
Summary(pl.UTF-8):	Urwid - biblioteka konsolowego interfejsu użytkownika dla Pythona 3
Name:		python3-%{module}
Version:	2.6.16
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Python
#Source0Download: http://urwid.org/
Source0:	https://pypi.python.org/packages/source/u/urwid/%{module}-%{version}.tar.gz
# Source0-md5:	214f9cea321ccae131cecfaef2a4aa9a
URL:		http://urwid.org/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	python3-devel >= 1:3.7
BuildRequires:	python3-setuptools
BuildRequires:	python3-wcwidth
%if %{with doc}
BuildRequires:	sphinx-pdg-3 >= 2.0.0
BuildRequires:	python3-sphinx_github_changelog
%endif
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Urwid is a console user interface library for Python.

%description -l hu.UTF-8
Urwid egy konzolos felhasználói felület könyvtár Pythonhoz.

%description -l pl.UTF-8
Urwid to biblioteka konsolowego interfejsu użytkownika dla Pythona.

%package apidocs
Summary:	API documentation for urwid module
Summary(pl.UTF-8):	Dokumentacja API modułu urwid
Group:		Documentation

%description apidocs
API documentation for urwid module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu urwid.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build %{?with_tests:test}

%if %{with doc}
PYTHONPATH="$(pwd)/build-3/lib" sphinx-build-3 -b html docs docs/_html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

# tests
%if %{with tests}
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/urwid/tests
# unversioned copy installed if tests are run
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/urwid.egg-info
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst docs/changelog.rst
%dir %{py3_sitescriptdir}/urwid
%{py3_sitescriptdir}/urwid/*.py
%{py3_sitescriptdir}/urwid/__pycache__
%dir %{py3_sitescriptdir}/urwid/display
%{py3_sitescriptdir}/urwid/display/*.py
%{py3_sitescriptdir}/urwid/display/_web.css
%{py3_sitescriptdir}/urwid/display/_web.js
%{py3_sitescriptdir}/urwid/display/__pycache__
%dir %{py3_sitescriptdir}/urwid/event_loop
%{py3_sitescriptdir}/urwid/event_loop/*.py
%{py3_sitescriptdir}/urwid/event_loop/__pycache__
%dir %{py3_sitescriptdir}/urwid/widget
%{py3_sitescriptdir}/urwid/widget/*.py
%{py3_sitescriptdir}/urwid/widget/__pycache__
%{py3_sitescriptdir}/urwid-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_html/{_images,_static,examples,manual,reference,tutorial,*.html,*.js}
%endif
