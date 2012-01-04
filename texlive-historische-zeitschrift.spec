# revision 20170
# category Package
# catalog-ctan /macros/latex/exptl/biblatex-contrib/historische-zeitschrift
# catalog-date 2010-10-19 15:53:57 +0200
# catalog-license lppl
# catalog-version 0.9a
Name:		texlive-historische-zeitschrift
Version:	0.9a
Release:	2
Summary:	Biblatex style for the journal 'Historische Zeitschrift'
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/exptl/biblatex-contrib/historische-zeitschrift
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/historische-zeitschrift.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/historische-zeitschrift.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides citations according with the house style
of the 'Historische Zeitschrift', a German historical journal.
The scheme is a fullcite for the first citation and 'Author,
Shorttitle (as note N, P)' for later citations (P being the
page number). For further details, see the description of the
house style at the journal's site. The package depends on
biblatex (version 0.8 or higher) as well as etoolbox (version
1.5 or higher).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/historische-zeitschrift/bbx/historische-zeitschrift.bbx
%{_texmfdistdir}/tex/latex/historische-zeitschrift/cbx/historische-zeitschrift.cbx
%{_texmfdistdir}/tex/latex/historische-zeitschrift/lbx/historische-zeitschrift.lbx
%doc %{_texmfdistdir}/doc/latex/historische-zeitschrift/CHANGES
%doc %{_texmfdistdir}/doc/latex/historische-zeitschrift/LIESMICH
%doc %{_texmfdistdir}/doc/latex/historische-zeitschrift/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
