""" This is a conversion dictionary built for Early Modern Texts from the VEP Pipeline repository
(see appended license below)
author of comment: sarah konrad data+ 2023

BSD 2-Clause License

Copyright (c) 2017, Authors who have agreed to assign their rights to The University of Wisconsin All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR

IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

def getBrevigraphList():
    brevs = ['CON','bus','con', 'er','is','PER','per','pre','pri','PRI','PRO','pro','qu','quam','que','QUE','qui','QUOD','quod','ris','rum','RUM','sed','ser','ur','us','US','es','etc','ou','precipi','subli','ignifi']
    shorthand = ['THAT','that','half','ducat','quarter','hundred','aqua fortis','aqua regis','air','alembic','alum','antimony','aqua regis','arsenic','ashes','quicklime','potash','query','vitriol','abl.','vinegar','sulfur','fire','earth','glass','tartar','talc']
    brevs.extend(shorthand)
    return brevs

def getConversionDict():
    conversion_dict = dict()
    # conversion_dict is a hand-curated dictionary of ascii equivalents for common unicode characters in the TCP

    conversion_dict['Œ'] = 'OE'
    conversion_dict['œ'] = 'oe'
    conversion_dict['À'] = 'A'
    conversion_dict['Á'] = 'A'
    conversion_dict['Â'] = 'A'
    conversion_dict['Ã'] = 'A'
    conversion_dict['Ä'] = 'A'
    conversion_dict['Å'] = 'A'
    conversion_dict['Æ'] = 'AE'
    conversion_dict['Ç'] = 'C'
    conversion_dict['È'] = 'E'
    conversion_dict['É'] = 'E'
    conversion_dict['Ê'] = 'E'
    conversion_dict['Ë'] = 'E'
    conversion_dict['Ì'] = 'I'
    conversion_dict['Í'] = 'I'
    conversion_dict['Î'] = 'I'
    conversion_dict['Ï'] = 'I'
    conversion_dict['Ð'] = 'TH'
    conversion_dict['Ñ'] = 'N'
    conversion_dict['Ò'] = 'O'
    conversion_dict['Ó'] = 'O'
    conversion_dict['Ô'] = 'O'
    conversion_dict['Õ'] = 'O'
    conversion_dict['Ö'] = 'O'
    conversion_dict['Ø'] = 'O'
    conversion_dict['Ù'] = 'U'
    conversion_dict['Ú'] = 'U'
    conversion_dict['Û'] = 'U'
    conversion_dict['Ü'] = 'U'
    conversion_dict['Ý'] = 'Y'
    conversion_dict['Þ'] = 'TH'
    conversion_dict['ß'] = 'S'
    conversion_dict['à'] = 'a'
    conversion_dict['á'] = 'a'
    conversion_dict['â'] = 'a'
    conversion_dict['ã'] = 'a'
    conversion_dict['ä'] = 'a'
    conversion_dict['å'] = 'a'
    conversion_dict['æ'] = 'ae'
    conversion_dict['ç'] = 'c'
    conversion_dict['è'] = 'e'
    conversion_dict['é'] = 'e'
    conversion_dict['ê'] = 'e'
    conversion_dict['ë'] = 'e'
    conversion_dict['ē'] = 'e'
    conversion_dict['ì'] = 'i'
    conversion_dict['í'] = 'i'
    conversion_dict['î'] = 'i'
    conversion_dict['ï'] = 'i'
    conversion_dict['ð'] = 'th'
    conversion_dict['ñ'] = 'n'
    conversion_dict['ò'] = 'o'
    conversion_dict['ó'] = 'o'
    conversion_dict['ô'] = 'o'
    conversion_dict['õ'] = 'o'
    conversion_dict['ô'] = 'o'
    conversion_dict['ö'] = 'o'
    conversion_dict['ø'] = 'o'
    conversion_dict['ù'] = 'u'
    conversion_dict['ú'] = 'u'
    conversion_dict['û'] = 'u'
    conversion_dict['ü'] = 'u'
    conversion_dict['ý'] = 'y'
    conversion_dict['þ'] = 'th'
    conversion_dict['ÿ'] = 'y'
    conversion_dict['÷'] = '/'
    conversion_dict['×'] = 'x'
    conversion_dict['¢'] = 'c'
    conversion_dict['£'] = 'L'
    conversion_dict['±'] = '+/-'
    conversion_dict['Ÿ'] = 'Y'
    conversion_dict['š'] = 's'
    conversion_dict['ž'] = 'z'
    ## Latin
    conversion_dict['Ʋ'] = 'V'
    conversion_dict['ʋ'] = 'v'
    ## Greek letters
    conversion_dict['α'] = 'a'
    conversion_dict['β'] = 'b'
    conversion_dict['Γ'] = 'G'
    conversion_dict['γ'] = 'g'
    conversion_dict['Δ'] = 'D'
    conversion_dict['δ'] = 'd'
    conversion_dict['ε'] = 'e'
    conversion_dict['ζ'] = 'z'
    conversion_dict['η'] = 'e'
    conversion_dict['Θ'] = 'TH'
    conversion_dict['θ'] = 'th'
    conversion_dict['η'] = 'e'
    conversion_dict['ι'] = 'i'
    conversion_dict['κ'] = 'k'
    conversion_dict['Λ'] = 'L'
    conversion_dict['λ'] = 'l'
    conversion_dict['μ'] = 'm'
    conversion_dict['ν'] = 'n'
    conversion_dict['Ξ'] = 'X'
    conversion_dict['ξ'] = 'x'
    conversion_dict['Π'] = 'P'
    conversion_dict['π'] = 'p'
    conversion_dict['Λ'] = 'L'
    conversion_dict['ρ'] = 'r'
    conversion_dict['Σ'] = 'S'
    conversion_dict['σ'] = 's'
    conversion_dict['τ'] = 't'
    conversion_dict['υ'] = 'u'
    conversion_dict['Φ'] = 'PH'
    conversion_dict['φ'] = 'ph'
    conversion_dict['χ'] = 'ch'
    conversion_dict['Ψ'] = 'PS'
    conversion_dict['ψ'] = 'ps'
    conversion_dict['Ω'] = 'O'
    conversion_dict['ω'] = 'o'

    # macrons
    conversion_dict['Ā'] = 'A^'
    conversion_dict['Ē'] = 'E^'
    conversion_dict['Ī'] = 'I^'
    conversion_dict['Ō'] = 'O^'
    conversion_dict['Ū'] = 'U^'
    conversion_dict['Ȳ'] = 'Y^'
    conversion_dict['ā'] = 'a^'
    conversion_dict['ē'] = 'e^'
    conversion_dict['ī'] = 'i^'
    conversion_dict['ō'] = 'o^'
    conversion_dict['ū'] = 'u^'
    conversion_dict['ȳ'] = 'y^'

    # line breaker
    # http://www.kreativekorp.com/charset/whatis.php
    conversion_dict['∣'] = '|' # unicode 2223 DIVIDES // Deidre: TCP end-of-line straddling soft hyphen
    conversion_dict['▪'] = '*' # unicode 25AA BLACK SMALL SQUARE // Deidre: TCP ambiguious punctuation mark, changed character insertion from | to *
    conversion_dict['¦'] = '|' # unicode 00A6 BROKEN BAR // Deidre: TCP editor inserted end-of-line straddling soft hyphen
    conversion_dict['|'] = '|' # unicode 007C VERTICAL LINE, *EQUAL* to the ascii one
    conversion_dict['❘'] = '|' # unicode 2758 LIGHT VERTICAL BAR
    conversion_dict['ǀ'] = '|' # unicode 01C0 LATIN LETTER DENTAL CLICK
    conversion_dict['∥'] = '|' # unicode 2225 PARALLEL TO

    # special punctuation
    conversion_dict['—'] = '--'
    # no matched
    conversion_dict['¶'] = '|' # Deidre: changed character from * to | so it can be stripped out of text


    #char cleaner expansion


    #punctuation fixes
    conversion_dict['’'] = "'"  #apostrophe fix
    conversion_dict['‐'] = '-'
    conversion_dict['\u2026'] = '...'
    conversion_dict['.'] = '.'
    conversion_dict[' '] = ' '
    conversion_dict['●'] = '^'
    conversion_dict['\xb7'] = '^'
    conversion_dict['\u25CF'] = '^'
    conversion_dict['¯'] = '@'
    conversion_dict['\u2020'] = '@' #dagger
    conversion_dict['\u2021'] = '@' #double dagger
    conversion_dict[u"'"] = '\''
    conversion_dict['\u3009'] = ')'
    conversion_dict['\u3008'] = '('
    conversion_dict['\u25ca'] = '@'
    conversion_dict['\u2011'] = '-'
    conversion_dict['\u201e'] = '"'
    conversion_dict['\xa0'] = ' ' #non-breaking space
    conversion_dict['\u201c'] = '"'
    conversion_dict['\u2022'] = '^'
    conversion_dict['\u2018'] = '\''
    conversion_dict['﻿'] = '@'
    conversion_dict['⁂'] = '*'


    conversion_dict['\u0163'] = 't'
    conversion_dict['\u014d'] = 'o'
    conversion_dict['\u016b'] = 'u'
    conversion_dict['\u0107'] = 'c'
    conversion_dict['\u01f5'] = 'g'
    conversion_dict['\u017f']= 's'
    conversion_dict['\u0101'] = 'a'
    conversion_dict['\u0391'] = 'A'
    conversion_dict['\u0395'] = 'E'
    conversion_dict['\u0399'] = 'I'
    conversion_dict['\u039d'] = 'N'
    conversion_dict['ă'] = 'a'
    conversion_dict['Ă'] = 'A'
    conversion_dict['Ο'] = 'O'
    conversion_dict['ο'] = 'o'
    conversion_dict['Ρ'] = 'P'
    conversion_dict['Τ'] = 'T'
    conversion_dict['ŭ'] = 'u'
    conversion_dict['ŏ'] = 'o'
    conversion_dict['\u03a5'] = 'Y'
    conversion_dict['é'] = 'e'
    conversion_dict['Å'] = 'A'
    conversion_dict['т'] = 'T'
    conversion_dict['⁽'] = '('
    conversion_dict['╌'] = '--'
    conversion_dict['ŵ'] = 'w'
    conversion_dict['ḍ'] = 'd'
    conversion_dict['−'] = '-'
    conversion_dict['ʐ'] = 'z'
    conversion_dict['Κ'] = 'K'
    conversion_dict['Ụ'] = 'U'
    conversion_dict['Ἥ'] = 'H'
    conversion_dict['❴'] = '{'
    conversion_dict['Т'] = 'T'
    conversion_dict['Š'] = 'S'
    conversion_dict['Ή'] = 'H'
    conversion_dict['Е'] = 'E'
    conversion_dict['Ϝ'] = 'F'
    conversion_dict['В'] = 'B'
    conversion_dict['М'] = 'M'
    conversion_dict['А'] = 'A'
    conversion_dict['¡'] = 'i'
    conversion_dict['Έ'] = 'E'
    conversion_dict['Ὴ'] = 'H'
    conversion_dict['ʗ'] = 'C'
    conversion_dict['Ŷ'] = 'Y'
    conversion_dict['ĥ'] = 'h'
    conversion_dict['Ὰ'] = 'A'
    conversion_dict['Ń'] = 'N'
    conversion_dict['У'] = 'y'


    return conversion_dict
