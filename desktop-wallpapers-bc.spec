Summary:	Desktop Background Images
Summary(pl.UTF-8):   Miodne obrazki na tło pulpitu
Name:		desktop-wallpapers-bc
Version:	1.0
Release:	2
License:	LGPL
Group:		X11/Applications/Multimedia
Source0:	http://irc.linux.pl/~spider/source/v1-%{version}.tar.gz
# Source0-md5:	50348d0dbae88184a6e6c547076afc10
Source1:	http://irc.linux.pl/~spider/source/v2-%{version}.tar.gz
# Source1-md5:	90bc16c20c5f18105708faa94e3e6770
Source2:        http://irc.linux.pl/~spider/source/v3-%{version}.tar.gz
# Source2-md5:	6b2ff0d064c477f7ed779f242d16285b
#Obsoletes:	desktop-backgrounds ?
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Desktop Background Images designed by Marcin Biernat.

%description -l pl.UTF-8
Miodne obrazki na tło pulpitu zaprojektowane przez Marcina Biernata.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/wallpapers

cd $RPM_BUILD_ROOT%{_datadir}/wallpapers
tar xzf %{SOURCE0}
tar xzf %{SOURCE1}
tar xzf %{SOURCE2}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/wallpapers/v1
%{_datadir}/wallpapers/v2
%{_datadir}/wallpapers/v3
