%global tl_name optex
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.20
Release:	%{tl_revision}.1
Summary:	LuaTeX format based on Plain TeX and OPmac
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/optex
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/optex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/optex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(amsfonts)
Requires:	texlive(cm)
Requires:	texlive(ec)
Requires:	texlive(hyphen-base)
Requires:	texlive(librarian)
Requires:	texlive(lm)
Requires:	texlive(luaotfload)
Requires:	texlive(luatex)
Requires:	texlive(optex.bin)
Requires:	texlive(rsfs)
Requires:	texlive(unicode-data)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
OpTeX is a LuaTeX format based on Plain TeX macros with power from OPmac
(fonts selection system, colors, external graphics, references,
hyperlinks, ...) with unicode fonts.

