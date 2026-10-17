

Name:           miryu-niri-config
Version:        45.0.0
Release:        1%{?dist}
Summary:        NyxNiri desktop configuration for the niri compositor and the Noctalia shell

License:        MIT
URL:            https://github.com/evernightvista/miryu-niri-config
Source0:        https://github.com/evernightvista/miryu-niri-config/archive/refs/heads/main.zip

BuildArch:      noarch

# The configuration targets this exact compositor + shell pair.
Requires:       niri
Requires:       noctalia

%description
NyxNiri provides the default desktop configuration for the niri Wayland
compositor together with the Noctalia desktop shell.

The package installs the configuration tree under /etc/skel so that every newly
created user account starts with a complete niri session out of the box:
includes, keybindings, layout, animations, window/layer rules, startup scripts,
the eyecare toggle and the NyxNiri Material 3 wallpaper picker, plus the seeded
Noctalia shell state and theme.

The mouse pointer is set to the Bibata-Material-Lilac cursor theme for the
whole session: niri's cursor block selects it for the compositor, and
XCURSOR_THEME / XCURSOR_SIZE are exported so niri-spawned clients (including
Noctalia and XWayland / GTK applications) inherit the same pointer.

%prep
%autosetup -n %{name}-main

%build
# Configuration only - nothing to compile.

%install
install -d %{buildroot}%{_sysconfdir}/skel/.config/niri
install -d %{buildroot}%{_sysconfdir}/skel/.local/state/noctalia

# Map the upstream module directories onto the per-user layout:
#   niri/     -> ~/.config/niri/
#   noctalia/ -> ~/.local/state/noctalia/
cp -a niri/.     %{buildroot}%{_sysconfdir}/skel/.config/niri/
cp -a noctalia/. %{buildroot}%{_sysconfdir}/skel/.local/state/noctalia/

# The entire NyxNiri payload must ship with mode 0777 (files and directories).
chmod -R 0777 %{buildroot}%{_sysconfdir}/skel/.config/niri \
              %{buildroot}%{_sysconfdir}/skel/.local/state/noctalia

%files
%defattr(0777, root, root, 0777)
%{_sysconfdir}/skel/.config/niri
%{_sysconfdir}/skel/.local/state/noctalia

%changelog
* Sat Oct 17 2026 KairikiFedora <13278297951@sina.cn> - 45.0.0-1
- Initial package: /etc/skel configuration for niri + Noctalia.
- Pin the pointer to the bibata-material-lilac cursor theme (niri cursor block
  plus XCURSOR_THEME / XCURSOR_SIZE).
- Ship the payload with mode 0777 for every file and directory.
