%define	name	slune
%define	oname	Slune
%define	version	1.0.15
%define	rel	4
%define	release	%mkrel %{rel}
%define	Summary	A multiplayer 3D racing and car-crashing game in Python

Name:		%{name}
Summary:	%{Summary}
Version:	%{version}
Release:	%{release}
Source0:	%{oname}-%{version}.tar.bz2
License:	GPL
Group:		Games/Arcade
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python >= %{pyver} tkinter soya >= 0.14
Requires:	pyopenal >= 0.1.5 py2play >= 0.1.7 pyvorbis
BuildRequires:	python-devel
Url:		http://home.gna.org/oomadness/en/slune/index.html

%description
A 3D racing and car-crashing game in Python, with multiplayer mode.
In this game, Gnu and Tux must provide AIDS medicine for Africa.
Includes a multiplayer mode.

%prep
%setup -q -n %{oname}-%{version}

#(eandry) pt .mo file is not provided in 1.0.15 because of empty .po (check if still valid with new versions)
rm -rf locale/pt

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install	--root=%{buildroot} \
			--install-purelib %{_gamesdatadir} \
			--install-scripts %{_gamesbindir} \
			--install-data %{_gamesdatadir} \
			--no-lang

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Slune
Comment=%{Summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
StartupNotify=true
EOF

install -m644 ./images/slune.16.png -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 ./images/slune.32.png -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 ./images/slune.48.png -D %{buildroot}%{_liconsdir}/%{name}.png

# install translations
for f in ./locale/*
	do install -m644 ./$f/LC_MESSAGES/%{name}.mo -D %{buildroot}%{_datadir}/$f/LC_MESSAGES/%{name}.mo
done

%find_lang %{name}

# remove %lang(en) from slune.lang to ensure english text being installed, as it's required
perl -pi -e "s#\%lang\(en\) ##g" slune.lang

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README README.fr AUTHORS CHANGES manual.fr.pdf
%{_gamesdatadir}/%{name}
%{_gamesdatadir}/*.egg-info
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%defattr(755,root,root,755)
%{_gamesbindir}/%{name}



