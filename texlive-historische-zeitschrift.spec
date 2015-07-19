# revision 27124
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/historische-zeitschrift
# catalog-date 2012-07-15 23:35:06 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-historische-zeitschrift
Version:	1.0
Release:	9
Summary:	Biblatex style for the journal 'Historische Zeitschrift'
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/historische-zeitschrift
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


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 812289
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.9a-2
+ Revision: 752581
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.9a-1
+ Revision: 718620
- texlive-historische-zeitschrift
- texlive-historische-zeitschrift
- texlive-historische-zeitschrift
- texlive-historische-zeitschrift

