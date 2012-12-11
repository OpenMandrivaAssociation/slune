%define	oname	Slune

Name:		slune
Summary:	Summary	A multiplayer 3D racing and car-crashing game in Python
Version:	1.0.15
Release:	6
Source0:	%{oname}-%{version}.tar.bz2
License:	GPL
Group:		Games/Arcade
BuildArch:	noarch
Requires:	python >= %{py_ver} tkinter soya >= 0.14
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

%clean

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





%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.15-5mdv2011.0
+ Revision: 614900
- the mass rebuild of 2010.1 packages

* Sat Apr 10 2010 Samuel Verschelde <stormi@mandriva.org> 1.0.15-4mdv2010.1
+ Revision: 533552
- fix desktop file

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 1.0.15-3mdv2010.0
+ Revision: 445133
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 1.0.15-2mdv2009.1
+ Revision: 350110
- 2009.1 rebuild

* Sat Sep 06 2008 Emmanuel Andry <eandry@mandriva.org> 1.0.15-1mdv2009.0
+ Revision: 281899
- New version

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 1.0.13-1mdv2009.0
+ Revision: 218429
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Oct 06 2007 Emmanuel Andry <eandry@mandriva.org> 1.0.13-1mdv2008.1
+ Revision: 95660
- New version (fixes bug #29980)

* Sun Sep 16 2007 Emmanuel Andry <eandry@mandriva.org> 1.0.12-4mdv2008.0
+ Revision: 87901
- drop old menu
- package egg-info file
- Import slune



* Mon Sep 25 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.0.12-3mdv2007.0
- drop python-psyco from enhances..

* Sun Aug 27 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.0.12-2mdv2007.0
- fix use of summary macro in menu
- fix xdg menu permissions
- add mandriva category to xdg menu
- add enhances tag on python-psyco
- cosmetics

* Sun Aug 27 2006 Emmanuel Andry <eandry@mandriva.org> 1.0.12-1mdv2007.0
- 1.0.12
- various fixes for xdg menu

* Tue Jul 11 2006 Lenny Cartier <lenny@mandriva.com> 1.0.11-2mdv2007.0
- xdg menu

* Fri May 12 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.0.11-1mdk
- 1.0.11
- update url

* Wed Oct 26 2005 Lenny Cartier <lenny@mandriva.com> 1.0.9-3mdk
- rebuild for allegro

* Mon Oct 10 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.9-2mdk
- Fix BuildRequires

* Wed Aug 31 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.0.9-1mdk
- 1.0.9

* Thu Jun 16 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.0.7-2mdk
- don't require psyco (package is noarch and %%if is done at build time..)
- update url
- %%mkrel

* Wed Mar 02 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.7-1mdk
- 1.0.7
- require python-psyco on %%ix86 to for performance gain
- es translation now exist, don't remove it

* Thu Jan 20 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.6-2mdk
- fix buildrequires

* Mon Jan 10 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.6-1mdk
- 1.0.6

* Mon Oct 25 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.0.4-1mdk
- 1.0.4

* Fri Oct 22 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.3-1mdk
- 1.0.3

* Mon Aug 16 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.7b-2mdk
- fix dependency suckage (fixes #10352)
- update url

* Thu Jul 08 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.7b-1mdk
- 0.7b
- update versions requirements on dependencies
- fix doc permissions

* Tue Dec 23 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.6.1-2mdk
- add pyvorbis to requires
- fix my formatting again *grmpf!*
- cleanups

* Mon Dec 22 2003 Pierre Hugues Husson <phh@sidenux.ath.cx> 0.6.1-1mdk
- 0.6.1

* Thu Jul 24 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.5-1mdk
- 0.5

* Sat Apr 26 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.4-1mdk
- spec file fixes
- from Jean-Baptiste Lamy <jiba@tuxfamily.org>
  - new version
  - icons and nb translation have been integrated to Slune
  - better description
  - removed soundwrapper (Slune is not binary => don't work; and OpenAL is normally
    able to figure out the sound system to use (ESD, ARTS, OSS,...))
  - move stuff from %%{_datadir}/%%{name} to %%{_gamesdatadir}/%%{name}
  
* Mon Apr 07 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.3.1-2mdk
- corrected group
- added nb translation

* Mon Apr 07 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.3.1-1mdk
- initial mdk release
