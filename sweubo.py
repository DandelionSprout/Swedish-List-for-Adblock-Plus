import requests
import re

SOURCES = ['https://raw.githubusercontent.com/lassekongo83/Frellwits-filter-lists/master/Swedish/swe-ubo-filters.txt']

UNSUPPORTED_ABP = ['$important', ',important', '$redirect=', ',redirect=',
    ':style', '##+js', '.*#' , '!#if', '!#endif', '!+ ', '##^', '!#i', '$app', ':not(:-abp-', '$csp=upgrade-insecure-requests', '$badfilter', 'removeparam', 'queryprune']

OUTPUT = 'xyzzyx.txt'
OUTPUT_ABP = 'SwedishList-uBO.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# ——— Adblock Plus version ———

def is_supported_abp(line) -> bool:
    for token in UNSUPPORTED_ABP:
        if token in line:
            return False

    return True

# function that prepares the filter list for ABP
def prepare_abp(lines) -> str:
    text = ''

    # remove or modifiy entries with unsupported modifiers
    for line in lines:

        # remove $document modifier from the rule
        line = re.sub(
           r"\$doc.*", 
           "", 
           line
        )

        # remove $important modifier from the rule
        line = re.sub(
           r"\$important,", 
           "$", 
           line
        )

        line = re.sub(
           r"([$,])important", 
           "", 
           line
        )

        line = re.sub(
           r"^no##.*", 
           "", 
           line
        )

        line = re.sub(
           r"! Redirect:.*", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])xhr", 
           r"\1xmlhttprequest", 
           line
        )

        line = re.sub(
           r"([$,~])3p", 
           r"\1third-party", 
           line
        )

        line = re.sub(
           r"([$,])1p", 
           r"\1~third-party", 
           line
        )

        line = re.sub(
           ":matches-css-before\(", 
           ":-abp-properties(", 
           line
        )

        line = re.sub(
           ":matches-css\(", 
           ":-abp-properties(", 
           line
        )

        line = re.sub(
           ":matches-css-after\(", 
           ":-abp-properties(", 
           line
        )

        line = re.sub(
           r"\.\*\^", 
           r".", 
           line
        )

        line = re.sub(
           "^,", 
           "^$", 
           line
        )

        line = re.sub(
           r"! Version: (.*)January(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>01\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)February(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>02\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)March(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>03\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)April(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>04\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)May(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>05\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)June(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>06\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)July(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>07\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)August(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>08\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)September(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>09\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)October(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>10\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)November(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>11\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)December(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>12\2\3", 
           line
        )

        line = re.sub(
           "redirect=noopjs", 
           "rewrite=abp-resource:blank-js", 
           line
        )

        line = re.sub(
           r"redirect=noopmp[34]-[0]?[.]?1s", 
           r"rewrite=abp-resource:blank-mp3", 
           line
        )

        line = re.sub(
           r"(#\$#.*),", 
           r"\1", 
           line
        )

        line = re.sub(
           r"^[a-z0-9].*:has.*:upward.*", 
           r"", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(1\)", 
           r"\1#?#\2\3*:-abp-has(> \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(2\)", 
           r"\1#?#\2\3*:-abp-has(> * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(3\)", 
           r"\1#?#\2\3*:-abp-has(> * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(4\)", 
           r"\1#?#\2\3*:-abp-has(> * > * >  * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(5\)", 
           r"\1#?#\2\3*:-abp-has(> * > * > * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(6\)", 
           r"\1#?#\2\3*:-abp-has(> * > * > * > * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(7\)", 
           r"\1#?#\2\3*:-abp-has(> * > * > * > * > * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(8\)", 
           r"\1#?#\2\3*:-abp-has(> * > * > * > * > * > * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(9\)", 
           r"\1#?#\2\3*:-abp-has(> * > * > * > * > * > * > * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(10\)", 
           r"\1#?#\2\3*:-abp-has(> * > * > * > * > * > * > * > * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(1\)", 
           r"\1#?#*:-abp-has(> \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(2\)", 
           r"\1#?#*:-abp-has(> * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(3\)", 
           r"\1#?#*:-abp-has(> * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(4\)", 
           r"\1#?#*:-abp-has(> * > * >  * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(5\)", 
           r"\1#?#*:-abp-has(> * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(6\)", 
           r"\1#?#*:-abp-has(> * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(7\)", 
           r"\1#?#*:-abp-has(> * > * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(8\)", 
           r"\1#?#*:-abp-has(> * > * > * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(9\)", 
           r"\1#?#*:-abp-has(> * > * > * > * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(10\)", 
           r"\1#?#*:-abp-has(> * > * > * > * > * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([.?]),script", 
           r"\1$script", 
           line
        )

        line = re.sub(
           r"xmlhttprequest\$", 
           r"xmlhttprequest,", 
           line
        )

        line = re.sub(
           r":remove()", 
           r"", 
           line
        )

        line = re.sub(
           r"##:xpath\((.*)\)$", 
           r"#$#hide-if-matches-xpath \1", 
           line
        )

        line = re.sub(
           r".*\$\$script.*", 
           r"", 
           line
        )

        line = re.sub(
           r"\$~doc$", 
           r"", 
           line
        )

        line = re.sub(
           r".*\$.*,app=.*", 
           r"", 
           line
        )

        line = re.sub(
           r":before", 
           r"::before", 
           line
        )

        line = re.sub(
           r":after", 
           r"::after", 
           line
        )

        line = re.sub(
           r"([$,])frame(,|$)", 
           r"\1subdocument\2", 
           line
        )

        line = re.sub(
           r"^!$", 
           r"", 
           line
        )

        line = re.sub(
           r"(.*)\$all$", 
           r"\1\n\1$popup", 
           line
        )

        line = re.sub(
           r"([a-z])##(.*):has-text", 
           r"\1#?#\2:-abp-contains", 
           line
        )

        line = re.sub(
           r"([a-z])#\??#(.*):has", 
           r"\1#?#\2:-abp-has", 
           line
        )

        line = re.sub(
           r"([a-z])#\??#(.*):has", 
           r"\1#?#\2:-abp-has", 
           line
        )

        line = re.sub(
           r".*[cC]ooo?k[ic][es]?.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*[aA]d-?[bB]lock.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*[nN]ewsletter.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*gdpr.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*GDPR.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*#\$#.*advanced_ads.*", 
           r"", 
           line
        )

        line = re.sub(
           r"=\"([a-zA-Z_-]{1,40})\"", 
           r"=\1", 
           line
        )

        line = re.sub(
           r":-abp-has-text", 
           r":-abp-contains", 
           line
        )

        line = re.sub(
           r".*[sS]hare.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*[sS]ocial.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*[pP]aywall.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*follow-us.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*stickyFollow.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*[nN]otifi.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*facebook.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*push.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*-icon\.\$.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*[cC]onsent.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*optin.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*[/.|]like.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*nyhetsbrev.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*[aA]dd[tT]his.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*privacy.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*(\* > [a-z0-9äöå ]{1,})/i.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*consensu.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^[a-z0-9_]{1,6}$", 
           r"", 
           line
        )

        line = re.sub(
           r".*[$,]queryprune.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*:upward\([a-z.].*", 
           r"", 
           line
        )

        line = re.sub(
           r".*OneSignal.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*nwletter.*", 
           r"", 
           line
        )

        line = re.sub(
           r"\(\)$", 
           r"", 
           line
        )

        line = re.sub(
           r"\$media,mp4", 
           r"$media", 
           line
        )

        line = re.sub(
           r".*antiblock.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*unblock.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*/deblock.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*bilmur.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*login-required.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*snowfall.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*-snow-.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*quantcast.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*christmas.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*onetrust.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*info-?sticky.*", 
           r"", 
           line
        )

        line = re.sub(
           r"\$all,", 
           r"$", 
           line
        )

        line = re.sub(
           r"\$empty,", 
           r"$", 
           line
        )

        line = re.sub(
           r".*addtoany.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*smoothscroll.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*:-abp-contains\([a-z:]{1,} \* .*", 
           r"", 
           line
        )

        line = re.sub(
           r".*-deblocker.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*mail.*", 
           r"", 
           line
        )

        line = re.sub(
           r"([a-z])##(\.?[a-z].*:-abp-)", 
           r"\1#?#\2", 
           line
        )

        line = re.sub(
           r"(\$[a-z]{1,})\$", 
           r"\1,", 
           line
        )

        line = re.sub(
           r".*\.cli-.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^[a-z0-9].*:-abp-has.*,.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*#\?#\*:-abp-has\(> a\[href\^=\"https://kampanj\.\"]\)$", 
           r"", 
           line
        )

        line = re.sub(
           r"^/snow.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*add-?to-?any.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*-copy-.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*tinypass.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*scribe.*", 
           r"", 
           line
        )

        if is_supported_abp(line) and not line == '':
            text += line + '\r\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    abp_filter = prepare_abp(lines)

    with open(OUTPUT, "w") as text_file:
        text_file.write(text)

    with open(OUTPUT_ABP, "w") as text_file:
        text_file.write(abp_filter)

    print('The uBO-file-to-ABP conversion has been generated.')

#/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\
#•X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X•
#\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/lassekongo83/Frellwits-filter-lists/master/Frellwits-Swedish-Filter.txt']

UNSUPPORTED_ABP = ['$important', ',important', '$redirect=', ',redirect=',
    ':style', '##+js', '.*#' , '!#if', '!#endif', '!+ ', '##^', '!#i', '$app', ':not(:-abp-', '$csp=upgrade-insecure-requests', '$badfilter']

OUTPUT = 'xyzzyxregular.txt'
OUTPUT_ABP = 'SwedishList-Regular.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# ——— Adblock Plus version ———

def is_supported_abp(line) -> bool:
    for token in UNSUPPORTED_ABP:
        if token in line:
            return False

    return True

# function that prepares the filter list for ABP
def prepare_abp(lines) -> str:
    text = ''

    # remove or modifiy entries with unsupported modifiers
    for line in lines:

        line = re.sub(
           r"(#\$#.*),", 
           r"\1", 
           line
        )

        line = re.sub(
           r":before", 
           r"::before", 
           line
        )

        line = re.sub(
           r":after", 
           r"::after", 
           line
        )

        line = re.sub(
           r"([$,])frame(,|$)", 
           r"\1subdocument\2", 
           line
        )

        line = re.sub(
           r"^!$", 
           r"", 
           line
        )

        line = re.sub(
           r".*[cC]ooo?k[ic][es]?.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*[aA]d-?[bB]lock.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*[nN]ews-?letter.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*gdpr.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*GDPR.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*#\$#.*advanced_ads.*", 
           r"", 
           line
        )

        line = re.sub(
           r"=\"([a-zA-Z_-]{1,40})\"", 
           r"=\1", 
           line
        )

        line = re.sub(
           r"^! .*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\[Adblock .*", 
           r"", 
           line
        )

        line = re.sub(
           r".*[sS]hare.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*[sS]ocial.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*[pP]aywall.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*follow-us.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*stickyFollow.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*[nN]otifi.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*facebook.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*push.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*-icon\.\$.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*[cC]onsent.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*optin.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*[/.|]like.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*nyhetsbrev.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*[aA]dd[tT]his.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*privacy.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*EUModal.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*OneSignal.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*smartbanner.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*consensu.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*nwletter.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*antiblock.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*unblock.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*/deblock.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*bilmur.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*login-required.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*snowfall.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*-snow-.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*quantcast.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*christmas.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*onetrust.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*info-?sticky.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*-deblocker.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*mail.*", 
           r"", 
           line
        )

        line = re.sub(
           r"([a-z])##(\.?[a-z].*:-abp-)", 
           r"\1#?#\2", 
           line
        )

        line = re.sub(
           r"(\$[a-z]{1,})\$", 
           r"\1,", 
           line
        )

        line = re.sub(
           r".*\.cli-.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^[a-z0-9].*:-abp-has.*,.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^/snow.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*add-?to-?any.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*-copy-.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*tinypass.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*scribe.*", 
           r"", 
           line
        )

        if is_supported_abp(line) and not line == '':
            text += line + '\r\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    abp_filter = prepare_abp(lines)

    with open(OUTPUT, "w") as text_file:
        text_file.write(text)

    with open(OUTPUT_ABP, "w") as text_file:
        text_file.write(abp_filter)

    print('The regular-file-to-ABP conversion has been generated.')