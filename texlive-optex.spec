Name:		texlive-optex
Version:	64050
Release:	2
Summary:	LuaTeX format based on Plain TeX and OPmac
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/optex
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/optex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/optex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
OpTeX is a LuaTeX format based on Plain TeX macros with power
from OPmac (fonts selection system, colors, external graphics,
references, hyperlinks, ...) with unicode fonts.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/tex/optex
%doc %{_texmfdistdir}/texmf-dist/doc/optex
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/optex.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/optex.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
