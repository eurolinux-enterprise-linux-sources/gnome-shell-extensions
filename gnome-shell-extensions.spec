%global major_version %%(cut -d "." -f 1-2 <<<%{version})
# Minimum GNOME Shell version supported
%global min_gs_version %%(cut -d "." -f 1-3 <<<%{version})

%global pkg_prefix gnome-shell-extension

Name:           gnome-shell-extensions
Version:        3.22.2
Release:        10%{?dist}
Summary:        Modify and extend GNOME Shell functionality and behavior

Group:          User Interface/Desktops
# The entire source code is GPLv2+ except lib/convenience.js which is BSD
License:        GPLv2+ and BSD
URL:            http://wiki.gnome.org/Projects/GnomeShell/Extensions
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{major_version}/%{name}-%{version}.tar.xz
# BuildRequires:  gnome-common
BuildRequires:  autoconf automake
BuildRequires:  gettext >= 0.19.6
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(libgtop-2.0)
Requires:       gnome-shell >= %{min_gs_version}
BuildArch:      noarch

Patch1: 0001-classic-shade-panel-in-overview.patch
Patch2: 0001-apps-menu-add-logo-icon-to-Applications-menu.patch
Patch3: add-extra-extensions.patch
Patch4: 0001-apps-menu-Explicitly-set-label_actor.patch
Patch5: 0001-window-list-Hide-workspace-indicator-when-there-s-1-.patch
Patch6: apps-menu-desktop-dnd.patch
Patch7: resurrect-system-monitor.patch
Patch8: 0001-loginDialog-make-info-messages-themed.patch

%description
GNOME Shell Extensions is a collection of extensions providing additional and
optional functionality to GNOME Shell.

Enabled extensions:
  * alternate-tab
  * apps-menu
  * auto-move-windows
  * drive-menu
  * launch-new-instance
  * native-window-placement
  * places-menu
  * screenshot-window-sizer
  * systemMonitor
  * updates-dialog
  * user-theme
  * window-list
  * windowsNavigator
  * workspace-indicator


%package -n %{pkg_prefix}-common
Summary:        Files common to GNOME Shell Extensions
Group:          User Interface/Desktops
License:        GPLv2+
Requires:       gnome-shell >= %{min_gs_version}
# Dock extension no longer provided by GNOME Shell extensions >= 3.7.1
Obsoletes:      %{pkg_prefix}-dock < 3.7.1
# Alternative-status-menu extension no longer provided by GNOME Shell extensions >= 3.9.5
Obsoletes:      %{pkg_prefix}-alternative-status-menu < 3.9.5
# Xrandr-indicator extension no longer provided by GNOME Shell extensions >= 3.9.5
Obsoletes:      %{pkg_prefix}-xrandr-indicator < 3.9.90
# Obsolete extensions dropped in favor of schema overrides by upstream
Obsoletes:       %{pkg_prefix}-default-min-max < 3.9.3-1
Obsoletes:       %{pkg_prefix}-static-workspaces < 3.9.3-1

%description -n %{pkg_prefix}-common
GNOME Shell Extensions is a collection of extensions providing additional and
optional functionality to GNOME Shell.

This package provides common data files shared by various extensions.


%package -n gnome-classic-session
Summary:        GNOME "classic" mode session
Group:          User Interface/Desktops
License:        GPLv2+
Requires:       %{pkg_prefix}-alternate-tab = %{version}-%{release}
Requires:       %{pkg_prefix}-apps-menu = %{version}-%{release}
Requires:       %{pkg_prefix}-launch-new-instance = %{version}-%{release}
Requires:       %{pkg_prefix}-places-menu = %{version}-%{release}
Requires:       %{pkg_prefix}-window-list = %{version}-%{release}
Requires:       nautilus
# Obsolete fallback mode components
Obsoletes:      gnome-applets < 1:3.5.92-5
%global gnome_applet_sensors_obsolete_ver 3.0.0-6
Obsoletes:      gnome-applet-sensors < %{gnome_applet_sensors_obsolete_ver}
Obsoletes:      gnome-applet-sensors-devel < %{gnome_applet_sensors_obsolete_ver}
%global gnome_panel_obsolete_ver 3.6.2-7
Obsoletes:      gnome-panel < %{gnome_panel_obsolete_ver}
Obsoletes:      gnome-panel-devel < %{gnome_panel_obsolete_ver}
Obsoletes:      gnome-panel-libs < %{gnome_panel_obsolete_ver}

%description -n gnome-classic-session
This package contains the required components for the GNOME Shell "classic"
mode, which aims to provide a GNOME 2-like user interface.


%package -n %{pkg_prefix}-alternate-tab
Summary:        Classic Alt+Tab behavior for GNOME Shell
Group:          User Interface/Desktops
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-alternate-tab
This GNOME Shell extension changes Alt+Tab to be window-based instead of
app-based.


%package -n %{pkg_prefix}-apps-menu
Summary:        Application menu for GNOME Shell
Group:          User Interface/Desktops
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}
Requires:       gnome-menus

%description  -n %{pkg_prefix}-apps-menu
This GNOME Shell extension adds a GNOME 2.x style menu for applications.


%package -n %{pkg_prefix}-auto-move-windows
Summary:        Assign specific workspaces to applications in GNOME Shell
Group:          User Interface/Desktops
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-auto-move-windows
This GNOME Shell extension enables easy workspace management. A specific
workspace can be assigned to each application as soon as it creates a window, in
a manner configurable with a GSettings key.


%package -n %{pkg_prefix}-dash-to-dock
Summary:        Show the dash outside the activities overview
Group:          User Interface/Desktops
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-dash-to-dock
This GNOME Shell extension makes the dash available outside the activities overview.


%package -n %{pkg_prefix}-drive-menu
Summary:        Drive status menu for GNOME Shell
Group:          User Interface/Desktops
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-drive-menu
This GNOME Shell extension provides a panel status menu for accessing and
unmounting removable devices.


%package -n %{pkg_prefix}-launch-new-instance
Summary:        Always launch a new application instance for GNOME Shell
Group:          User Interface/Desktops
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description  -n %{pkg_prefix}-launch-new-instance
This GNOME Shell extension modifies the behavior of clicking in the dash and app
launcher to always launch a new application instance.


%package -n %{pkg_prefix}-native-window-placement
Summary:        Native window placement for GNOME Shell
Group:          User Interface/Desktops
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description  -n %{pkg_prefix}-native-window-placement
This GNOME Shell extension provides additional configurability for the window
layout in the overview, including a mechanism similar to KDE4.


%package -n %{pkg_prefix}-panel-favorites
Summary:        Favorite launchers in GNOME Shell's top bar
Group:          User Interface/Desktops
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-panel-favorites
This GNOME Shell extension adds favorite launchers to the top bar.


%package -n %{pkg_prefix}-places-menu
Summary:        Places status menu for GNOME Shell
Group:          User Interface/Desktops
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-places-menu
This GNOME Shell extension add a system status menu for quickly navigating
places in the system.


%package -n %{pkg_prefix}-screenshot-window-sizer
Summary:        Screenshot window sizer for GNOME Shell
Group:          User Interface/Desktops
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-screenshot-window-sizer
This GNOME Shell extension allows to easily resize windows for GNOME Software
screenshots.


%package -n %{pkg_prefix}-systemMonitor
Summary:        System Monitor for GNOME Shell
Group:          User Interface/Desktops
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}
# Should be pulled in by control-center, but in case someone tries for a
# minimalist gnome-shell installation
Requires:       libgtop2

%description -n %{pkg_prefix}-systemMonitor
This GNOME Shell extension is a message tray indicator for CPU and memory usage



%package -n %{pkg_prefix}-top-icons
Summary:        Show legacy icons on top
Group:          User Interface/Desktops
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-top-icons
This GNOME Shell extension moves legacy tray icons into the top bar.

%package -n %{pkg_prefix}-updates-dialog
Summary:        Show a modal dialog when there are software updates
Group:          User Interface/Desktops
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-updates-dialog
This GNOME Shell extension shows a modal dialog when there are software updates

%package -n %{pkg_prefix}-user-theme
Summary:        Support for custom themes in GNOME Shell
Group:          User Interface/Desktops
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-user-theme
This GNOME Shell extension enables loading a GNOME Shell theme from
~/.themes/<name>/gnome-shell/.


%package -n %{pkg_prefix}-window-list
Summary:        Display a window list at the bottom of the screen in GNOME Shell
Group:          User Interface/Desktops
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-window-list
This GNOME Shell extension displays a window list at the bottom of the screen.


%package -n %{pkg_prefix}-windowsNavigator
Summary:        Support for keyboard selection of windows and workspaces in GNOME Shell
Group:          User Interface/Desktops
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-windowsNavigator
This GNOME Shell extension enables keyboard selection of windows and workspaces
in overlay mode, by pressing the Alt and Ctrl key respectively.


%package -n %{pkg_prefix}-workspace-indicator
Summary:        Workspace indicator for GNOME Shell
Group:          User Interface/Desktops
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-workspace-indicator
This GNOME Shell extension add a system status menu for quickly changing
workspaces.


%prep
%setup -q

%patch1 -p1 -b .shade-panel-in-overview
%patch2 -p1 -b .brand-applications-menu
%patch3 -p1 -b .add-extra-extensions
%patch4 -p1 -b .fix-menu-category-accessibility
%patch5 -p1 -b .hide-indicator-in-single-workspace-case
%patch6 -p1 -b .apps-menu-desktop-dnd
%patch7 -p1 -b .apps-menu-desktop-dnd
%patch8 -p1 -b .fix-pam-info-messages


%build
autoreconf -f
# In case we build from a Git checkout
[ -x autogen.sh ] && NOCONFIGURE=1 ./autogen.sh 
%configure  --enable-extensions="all"
make %{?_smp_mflags}


%install
%make_install

# Drop useless example extension
rm -r $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/example*/
rm $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.example.gschema.xml

%find_lang %{name}


%files -n %{pkg_prefix}-common -f %{name}.lang
%doc COPYING NEWS README


%files -n gnome-classic-session
%{_datadir}/gnome-session/sessions/gnome-classic.session
%{_datadir}/gnome-shell/modes/classic.json
%{_datadir}/gnome-shell/theme/*.svg
%{_datadir}/gnome-shell/theme/gnome-classic-high-contrast.css
%{_datadir}/gnome-shell/theme/gnome-classic.css
%{_datadir}/xsessions/gnome-classic.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.classic-overrides.gschema.xml

%files -n %{pkg_prefix}-alternate-tab
%{_datadir}/gnome-shell/extensions/alternate-tab*/


%files -n %{pkg_prefix}-apps-menu
%{_datadir}/gnome-shell/extensions/apps-menu*/


%files -n %{pkg_prefix}-auto-move-windows
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.auto-move-windows.gschema.xml
%{_datadir}/gnome-shell/extensions/auto-move-windows*/

%files -n %{pkg_prefix}-dash-to-dock
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.dash-to-dock.gschema.xml
%{_datadir}/gnome-shell/extensions/dash-to-dock*/

%files -n %{pkg_prefix}-drive-menu
%{_datadir}/gnome-shell/extensions/drive-menu*/


%files -n %{pkg_prefix}-launch-new-instance
%{_datadir}/gnome-shell/extensions/launch-new-instance*/


%files -n %{pkg_prefix}-native-window-placement
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.native-window-placement.gschema.xml
%{_datadir}/gnome-shell/extensions/native-window-placement*/

%files -n %{pkg_prefix}-panel-favorites
%{_datadir}/gnome-shell/extensions/panel-favorites*/

%files -n %{pkg_prefix}-places-menu
%{_datadir}/gnome-shell/extensions/places-menu*/


%files -n %{pkg_prefix}-screenshot-window-sizer
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.screenshot-window-sizer.gschema.xml
%{_datadir}/gnome-shell/extensions/screenshot-window-sizer*/


%files -n %{pkg_prefix}-systemMonitor
%{_datadir}/gnome-shell/extensions/systemMonitor*/


%files -n %{pkg_prefix}-top-icons
%{_datadir}/gnome-shell/extensions/top-icons*/


%files -n %{pkg_prefix}-updates-dialog
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.updates-dialog.gschema.xml
%{_datadir}/gnome-shell/extensions/updates-dialog*/


%files -n %{pkg_prefix}-user-theme
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.user-theme.gschema.xml
%{_datadir}/gnome-shell/extensions/user-theme*/


%files -n %{pkg_prefix}-window-list
%{_datadir}/gnome-shell/extensions/window-list*/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.window-list.gschema.xml


%files -n %{pkg_prefix}-windowsNavigator
%{_datadir}/gnome-shell/extensions/windowsNavigator*/


%files -n %{pkg_prefix}-workspace-indicator
%{_datadir}/gnome-shell/extensions/workspace-indicator*/


%postun -n gnome-classic-session
if [ $1 -eq 0 ]; then
  /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :
fi

%posttrans -n gnome-classic-session
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :


%postun -n %{pkg_prefix}-auto-move-windows
if [ $1 -eq 0 ]; then
  /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :
fi

%posttrans -n %{pkg_prefix}-auto-move-windows
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :


%postun -n %{pkg_prefix}-dash-to-dock
if [ $1 -eq 0 ]; then
  /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :
fi

%posttrans -n %{pkg_prefix}-dash-to-dock
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :


%postun -n %{pkg_prefix}-native-window-placement
if [ $1 -eq 0 ]; then
  /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :
fi

%posttrans -n %{pkg_prefix}-native-window-placement
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :


%postun -n %{pkg_prefix}-screenshot-window-sizer
if [ $1 -eq 0 ]; then
  /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :
fi

%posttrans -n %{pkg_prefix}-screenshot-window-sizer
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :


%postun -n %{pkg_prefix}-updates-dialog
if [ $1 -eq 0 ]; then
  /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :
fi

%posttrans -n %{pkg_prefix}-updates-dialog
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :


%postun -n %{pkg_prefix}-user-theme
if [ $1 -eq 0 ]; then
  /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :
fi

%posttrans -n %{pkg_prefix}-user-theme
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :


%postun -n %{pkg_prefix}-window-list
if [ $1 -eq 0 ]; then
  /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :
fi

%posttrans -n %{pkg_prefix}-window-list
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :


%changelog
* Mon Jun 26 2017 Ray Strode <rstrode@redhat.com> - 3.22.2-10
- Fix pam info messages at the unlock screen
  Related: #1449359

* Sat Jun 24 2017 Florian Müllner <fmuellner@redhat.com> - 3.22.3-9
- Update dash-to-dock to latest upstream
- Resolves: #1464614

* Wed May 17 2017 Florian Müllner <fmuellner@redhat.com> - 3.22.3-8
- Resurrect system monitor extension
- Resolves: #1452319

* Fri Apr 28 2017 Florian Müllner <fmuellner@redhat.com> - 3.22.3-7
- Include DND improvements from upstream
- Resolves: #1236601

* Wed Apr 05 2017 Florian Müllner <fmuellner@redhat.com> - 3.22.2-6
- Update last patch to not rely on newer JS API
- Resolves: #1236601

* Tue Mar 21 2017 Florian Müllner <fmuellner@redhat.com> - 3.22.2-5
- Allow creating desktop launchers via DND from apps menu
- Resolves: #1236601

* Tue Mar 14 2017 Florian Müllner <fmuellner@redhat.com> - 3.22.2-4
- Fix downstream branding
- Resolves: #1386960

* Tue Mar 14 2017 Florian Müllner <fmuellner@redhat.com> - 3.22.2-3
- Hide workspace indicator in window list if there's just 1 workspace
- Resolves: #1414817

* Tue Mar 14 2017 Florian Müllner <fmuellner@redhat.com> - 3.22.2-2
- Re-add downstream patches
- Resolves: #1386960

* Wed Nov 16 2016 Kalev Lember <klember@redhat.com> - 3.22.2-1
- Update to 3.22.2
- Resolves: #1386960

* Wed Sep 07 2016 Florian Müllner <fmuellner@redhat.com> - 3.14.4-21
- Improve menu category accessibility further
  Related: rhbz#1263128

* Fri Jul 08 2016 Florian Müllner <fmuellner@redhat.com> - 3.14.4-20
- Fix handling of menu entries from non-standard locations
  Resolves: #1353249

* Tue Jun 28 2016 Florian Müllner <fmuellner@redhat.com> - 3.14.4-19
- Update translations
  Resolves: #1304265

* Fri Jun 10 2016 Florian Müllner <fmuellner@redhat.com> - 3.14.4-18
- Adjust to changes from backported gnome-shell patches
  Resolves: #1343953

* Thu May 12 2016 Florian Müllner <fmuellner@redhat.com> - 3.14.4-17
- Fix updates-dialog schema errors
  Related: rhbz#1302864

* Thu Mar 17 2016 Florian Müllner <fmuellner@redhat.com> - 3.14.4-16
- Fix menu category accessibility
  Related: rhbz#1263128

* Fri Mar 04 2016 Florian Müllner <fmuellner@redhat.com> - 3.14.4-15
- Add updates-dialog extension
  Related: rhbz#1302864

* Tue Sep 22 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-14
- Fix rebase error in last patch series
  Related: rhbz#1263368

* Fri Sep 18 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-13
- Add option to display window-list on all monitors
  Resolves: rhbz#1263368

* Fri Sep 04 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-12
- Fix window list scaling in classic mode
  Resolves: rhbz#1229324

* Fri Sep 04 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-11
- Fix apps-menu taking over panel shortcut
  Resolves: rhbz#1255702

* Thu Sep 03 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-10
- Add back nautilus dependency to classic-session
  Resolves: rhbz#1256722

* Fri Jul 31 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-9
- Number workspaces consistently
  Resolves: rhbz#1249018

* Thu Jul 30 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-8
- Fix window list sorting
  Resolves: rhbz#1025370

* Fri Jul 24 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-7
- Support headless mode
  Related: rhbz#1243856

* Thu Jun 25 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-6
- Scale window list with text
  Resolves: rhbz#1229324

* Wed Jun 17 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-5
- Fix failure of apps-menu to open applications
  Resolves: rhbz#1229676

* Wed May 20 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-4
- Include additional (popular) extensions
  Resolves: rhbz#1208513

* Thu May 14 2015 Matthias Clasen <mclasen@redhat.com> - 3.14.4-3
- Make the apps-menu package depend on gnome-menus
- Resolves: #1221531

* Tue May 12 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-2
- Backport menu arrow fix from 3.16
- Related: #1174574

* Mon Mar 23 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-1
- Update to 3.14.4
- Resolves: #1174574

* Tue Oct 07 2014 David King <dking@redhat.com> 3.8.4-12
- Rebuild for libgtop2 soversion change (#1082123)

* Wed May 28 2014 Lubos Kocman <lkocman@redhat.com> - 3.8.4-11
- Resolves: #1100332 (bump release against 0day)

* Tue Feb 19 2014 Florian Müllner <fmuellner@redhat.com> - 3.8.4-10
- Fix odd menu behavior in window list
  Resolves: #1025374

* Thu Feb 13 2014 Florian Müllner <fmuellner@redhat.com> - 3.8.4-9
- Fix context menu backport
  Resolves: #1025374

* Mon Feb 10 2014 Debarshi Ray <rishi@fedoraproject.org> - 3.8.4-8
- Add Requires: nautilus
  Resolves: #1053753

* Tue Jan 21 2014 Ray Strode <rstrode@redhat.com> - 3.8.4-7
- Add logo to apps menu
  Resolves: #1052990

* Wed Jan 15 2014 Debarshi Ray <rishi@fedoraproject.org> - 3.8.4-6
- Shade the overview panel
  Resolves: #1053069

* Tue Jan 07 2014 Ray Strode <rstrode@redhat.com> - 3.8.4-5
- Use environment variable for session mode
  Related: #1031188

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.8.4-4
- Mass rebuild 2013-12-27

* Thu Dec 12 2013 Matthias Clasen <mclasen@redhat.com> - 3.8.4-3
- Update translations
  Resolves: #1030349

* Thu Oct 24 2013 Florian Müllner <fmuellner@redhat.com> - 3.8.4-2
- Backport some classic-mode improvements from 3.10 cycle:
  - context menu in window list (close, minimize, maximize)
  - use same order for favorites in applications menu as in dash

* Thu Sep 12 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.8.4-1
- Update to 3.8.4

* Sun Aug 04 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.8.3.1-1
- Update to 3.8.3.1
- Drop places-volume.patch patch, merged upstream

* Mon Jun 17 2013 Matthias Clasen <mclasen@redhat.com> - 3.8.3-2
- Fix a problem notices in updates-testing with the places extension

* Sun Jun 09 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.8.3-1
- Update to 3.8.3
- Drop mini-extensions default-min-max and static-workspaces, no longer
  available (see https://bugzilla.gnome.org/show_bug.cgi?id=701717)

* Tue May 14 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.8.2-1
- Update to 3.8.2
- Drop useless dependency on libgtop for static-workspaces subpackage

* Fri May 10 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-3
- Obsolete gnome-applet-sensors

* Wed May 01 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-2
- Obsolete a few more fallback mode packages
- Remove gnome-panel provides

* Tue Apr 16 2013 Matthias Clasen <mclasen@redhat.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.8.0-1
- Update to 3.8.0

* Tue Mar 19 2013 Ray Strode <rstrode@redhat.com> 3.7.92-1
- Update to 3.7.92

* Tue Mar 05 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.7.91-1
- Update to 3.7.91

* Sat Mar 02 2013 Adel Gadllah <adel.gadllah@gmail.com> - 3.7.90-2
- Obsolete gnome-panel

* Fri Feb 22 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.90-1
- Update to 3.7.90

* Thu Feb 07 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.5.1-2
- Depend on gnome-shell 3.7.5, there's no 3.7.5.1

* Thu Feb 07 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.7.5.1-1
- Update to 3.7.5
- Enable new launch-new-instance and window-list extensions, and add them in the
  classic-mode extension set
- Re-add places-menu in the classic-mode extension set

* Wed Jan 16 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.7.4-1
- Update to 3.7.4
- places-menu extension no longer part of the classic-mode extension set

* Tue Jan 01 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.7.3-1
- Update to 3.7.3
- Enable new default-min-max and static-workspaces extensions
- Provide new subpackage gnome-classic-session
- Revamp summaries and descriptions

* Tue Oct 30 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.7.1-1
- Update to 3.7.1
- Drop dock and gajim extensions, no longer provided

* Tue Oct 30 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.6.1-1
- Update to 3.6.1

* Tue Oct 02 2012 Mohamed El Morabity <melmorabity@fedorapeople.org> - 3.6.0-1
- Update to 3.6.0

* Thu Sep 06 2012 Mohamed El Morabity <melmorabity@fedorapeople.org> - 3.5.91-1
- Update to 3.5.91

* Wed Aug 29 2012 Mohamed El Morabity <melmorabity@fedorapeople.org> - 3.5.90-1
- Update to 3.5.90

* Sat Aug 11 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.5.5-1
- Update to 3.5.5

* Sun Jul 22 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.5.4-1
- Update to 3.5.4

* Wed Jul 18 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.5.2-1
- Update to 3.5.2
- Drop useless Provides/Obsoletes

* Sat Mar 24 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0
- Minor spec fixes

* Sat Mar 24 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.3.92-1
- Update to 3.3.92

* Tue Feb 28 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.3.90-1
- Update to 3.3.90

* Thu Feb 16 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.3.5-1
- Update to 3.3.5
- Spec cleanup

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 30 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.3.2-1
- Update to 3.3.2

* Wed Nov 30 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.2.1-1
- Update to 3.2.1
- Fix alternative-status-menu extension crash when login

* Wed Nov 09 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.2.0-2
- Fix dock and alternate-tab extensions
- Fix GNOME Shell version to work with GS 3.2.1

* Mon Oct 03 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0

* Mon Sep 26 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.1.91-3.20111001gite102c0c6
- Update to a newer git snapshot
- Fix GNOME Shell version to work with GS 3.2.0
- Add Requires on GS 3.2.0 or above to gnome-shell-common

* Wed Sep 14 2011 Mohamed El Morabity <melmorabity@fedorapeople.org> - 3.1.91-2
- Enable xrandr-indicator and workspace-indicator extensions

* Mon Sep 12 2011 Michel Salim <salimma@fedoraproject.org> - 3.1.91-1
- Update to 3.1.91
- add more documentation

* Thu Sep  1 2011 Michel Salim <salimma@fedoraproject.org> - 3.1.4-3.20110830git6b5e3a3e
- Update to git snapshot, for gnome-shell 3.1.90

* Sun Aug 21 2011 Michel Salim <salimma@fedoraproject.org> - 3.1.4-2
- Enable apps-menu extension
- Spec cleanup

* Sun Aug 21 2011 Michel Salim <salimma@fedoraproject.org> - 3.1.4-1
- Update to 3.1.4
- Enable systemMonitor extension
- Prepare xrandr-indicator, commenting out since it does not seem to work yet
- Rename subpackages in line with new guidelines (# 715367)
- Sort subpackages in alphabetical order

* Sat May 28 2011 Timur Kristóf <venemo@fedoraproject.org> - 3.0.2-1.g63dd27cgit
- Update to a newer git snapshot
- Fix RHBZ bug #708230
- Enabled systemMonitor extension, but commented out since the requirements are not available

* Fri May 13 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.0.1-3.03660fgit
- Update to a newer git snapshot
- Enable native-window-placement extension

* Fri May 06 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 3.0.1-2b20cbagit
- Fix description 

* Thu May 5 2011 Elad Alfassa <elad@fedoraproject.org> - 3.0.1-1.b20cbagit
- Update to a newer git snapshot
- Enabled the places-menu extension

* Tue Apr 26 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.0.1-1.f016b9git
- Update to a newer git snapshot (post-3.0.1 release)
- Enable drive-menu extension

* Mon Apr 11 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.0.0-5.6d56cfgit
- Enable auto-move-windows extension

* Sun Apr 10 2011 Rahul Sundaram <sundaram@fedoraproject.org>  - 3.0.0-4.6d56cfgit
- Add glib2-devel as build requires

* Sun Apr 10 2011 Rahul Sundaram <sundaram@fedoraproject.org>  - 3.0.0-3.6d56cfgit
- Tweak description
- Fix typo in configure

* Sun Apr 10 2011 Rahul Sundaram <sundaram@fedoraproject.org>  - 3.0.0-2.6d56cfgit
- Added the user-theme extension
- Patch from Timur Kristóf <venemo@msn.com>

* Fri Apr 08 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 3.0.0-1.6d56cfgit
- Make sure configure doesn't get called twice

* Fri Apr 08 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 3.0.0-0.6d56cfgit
- Initial build
