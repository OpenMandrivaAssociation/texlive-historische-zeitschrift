%global tl_name historische-zeitschrift
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	BibLaTeX style for the journal Historische Zeitschrift
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/historische-zeitschrift
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/historische-zeitschrift.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/historische-zeitschrift.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides citations according with the house style of the
'Historische Zeitschrift', a German historical journal. The scheme is a
fullcite for the first citation and 'Author, Shorttitle (as note N, P)'
for later citations (P being the page number). For further details, see
the description of the house style at the journal's site. The package
depends on BibLaTeX (version 3.3 or higher) as well as etoolbox (version
1.5 or higher).

