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
           "", 
           line
        )

        line = re.sub(
           r"([a-z]#\??#|, )[#.]?([a-z-]{1,})?(didomi|[cC]ooo?k[ic][es]|gdpr|GDPR|advanced_ads|[sS]hare|[sS]ocial|[pP]aywall|follow-us|sticky[fF]ollow|[nN]otifi|[fF]acebook|[pP]ush|[cC]onsent|[oO]ptin|[nN]yhetsbrev|[aA]dd[tT]his|[pP]rivacy|[cC]onsensu|[oO]ne[sS]ignal|nwletter|antiblock|unblock|bilmur|login-?require|snowfall|-snow-|[qQ]uantcast|christmas|[oO]netrust|info-?sticky|add-?to-?any|smooth-?scroll|tinypass|scribe|apsis|messaging|sleeknote|disclaimer|cc-container)([a-zA-Z_.=*^$-]|\[|\]|\"){0,}, ", 
           r"\1", 
           line
        )

        line = re.sub(
           r"([a-z]#\??#|, )[#.]?([a-z-]{1,})?(didomi|[cC]ooo?k[ic][es]|gdpr|GDPR|advanced_ads|[sS]hare|[sS]ocial|[pP]aywall|follow-us|sticky[fF]ollow|[nN]otifi|[fF]acebook|[pP]ush|[cC]onsent|[oO]ptin|[nN]yhetsbrev|[aA]dd[tT]his|[pP]rivacy|[cC]onsensu|[oO]ne[sS]ignal|nwletter|antiblock|unblock|bilmur|login-?require|snowfall|-snow-|[qQ]uantcast|christmas|[oO]netrust|info-?sticky|add-?to-?any|smooth-?scroll|tinypass|scribe|apsis|messaging|sleeknote|disclaimer|cc-container)([a-zA-Z_.=*^$-]|\[|\]|\"){0,}, ", 
           r"\1", 
           line
        )

        line = re.sub(
           r"([a-z]#\??#|, )[#.]?([a-z-]{1,})?(didomi|[cC]ooo?k[ic][es]|gdpr|GDPR|advanced_ads|[sS]hare|[sS]ocial|[pP]aywall|follow-us|sticky[fF]ollow|[nN]otifi|[fF]acebook|[pP]ush|[cC]onsent|[oO]ptin|[nN]yhetsbrev|[aA]dd[tT]his|[pP]rivacy|[cC]onsensu|[oO]ne[sS]ignal|nwletter|antiblock|unblock|bilmur|login-?require|snowfall|-snow-|[qQ]uantcast|christmas|[oO]netrust|info-?sticky|add-?to-?any|smooth-?scroll|tinypass|scribe|apsis|messaging|sleeknote|disclaimer|cc-container)([a-zA-Z_.=*^$-]|\[|\]|\"){0,}, ", 
           r"\1", 
           line
        )

        line = re.sub(
           r", [#.]?([a-z-]{1,})?(didomi|[cC]ooo?k[ic][es]|gdpr|GDPR|advanced_ads|[sS]hare|[sS]ocial|[pP]aywall|follow-us|sticky[fF]ollow|[nN]otifi|[fF]acebook|[pP]ush|[cC]onsent|[oO]ptin|[nN]yhetsbrev|[aA]dd[tT]his|[pP]rivacy|[cC]onsensu|[oO]ne[sS]ignal|nwletter|antiblock|unblock|bilmur|login-?require|snowfall|-snow-|[qQ]uantcast|christmas|[oO]netrust|info-?sticky|add-?to-?any|smooth-?scroll|tinypass|scribe|apsis|messaging|sleeknote|disclaimer|cc-container)([a-zA-Z_.=*^$-]|\[|\]|\"){0,}$", 
           "", 
           line
        )

        line = re.sub(
           r".*##[#.]?([a-z-]{1,})?(didomi|[cC]ooo?k[ic][es]|gdpr|GDPR|advanced_ads|[sS]hare|[sS]ocial|[pP]aywall|follow-us|sticky[fF]ollow|[nN]otifi|[fF]acebook|[pP]ush|[cC]onsent|[oO]ptin|[nN]yhetsbrev|[aA]dd[tT]his|[pP]rivacy|[cC]onsensu|[oO]ne[sS]ignal|nwletter|antiblock|unblock|bilmur|login-?require|snowfall|-snow-|[qQ]uantcast|christmas|[oO]netrust|info-?sticky|add-?to-?any|smooth-?scroll|tinypass|scribe|apsis|messaging|sleeknote|disclaimer|cc-container)([a-zA-Z_.=*^$-]|\[|\]|\"){0,}$", 
           "", 
           line
        )

        line = re.sub(
           r".*[cC]ooo?k[ic][es]?.*", 
           "", 
           line
        )

        line = re.sub(
           r".*[aA]d-?[bB]lock.*", 
           "", 
           line
        )

        line = re.sub(
           r".*[nN]ews-?letter.*", 
           "", 
           line
        )

        line = re.sub(
           r".*gdpr.*", 
           "", 
           line
        )

        line = re.sub(
           r".*GDPR.*", 
           "", 
           line
        )

        line = re.sub(
           r".*#\$#.*advanced_ads.*", 
           "", 
           line
        )

        line = re.sub(
           r"=\"([a-zA-Z_-]{1,40})\"", 
           r"=\1", 
           line
        )

        line = re.sub(
           r"^! .*", 
           "", 
           line
        )

        line = re.sub(
           r"^\[Adblock .*", 
           "", 
           line
        )

        line = re.sub(
           r".*[sS]hare.*", 
           "", 
           line
        )

        line = re.sub(
           r".*[sS]ocial.*", 
           "", 
           line
        )

        line = re.sub(
           r".*[pP]aywall.*", 
           "", 
           line
        )

        line = re.sub(
           r".*follow-us.*", 
           "", 
           line
        )

        line = re.sub(
           r".*stickyFollow.*", 
           "", 
           line
        )

        line = re.sub(
           r".*[nN]otifi.*", 
           "", 
           line
        )

        line = re.sub(
           r".*facebook.*", 
           "", 
           line
        )

        line = re.sub(
           r".*push.*", 
           "", 
           line
        )

        line = re.sub(
           r".*-icon\.\$.*", 
           "", 
           line
        )

        line = re.sub(
           r".*[cC]onsent.*", 
           "", 
           line
        )

        line = re.sub(
           r".*optin.*", 
           "", 
           line
        )

        line = re.sub(
           r".*[/.|]like.*", 
           "", 
           line
        )

        line = re.sub(
           r".*nyhetsbrev.*", 
           "", 
           line
        )

        line = re.sub(
           r".*[aA]dd[tT]his.*", 
           "", 
           line
        )

        line = re.sub(
           r".*privacy.*", 
           "", 
           line
        )

        line = re.sub(
           r".*EUModal.*", 
           "", 
           line
        )

        line = re.sub(
           r".*OneSignal.*", 
           "", 
           line
        )

        line = re.sub(
           r".*smartbanner.*", 
           "", 
           line
        )

        line = re.sub(
           r".*consensu.*", 
           "", 
           line
        )

        line = re.sub(
           r".*nwletter.*", 
           "", 
           line
        )

        line = re.sub(
           r".*antiblock.*", 
           "", 
           line
        )

        line = re.sub(
           r".*unblock.*", 
           "", 
           line
        )

        line = re.sub(
           r".*/deblock.*", 
           "", 
           line
        )

        line = re.sub(
           r".*bilmur.*", 
           "", 
           line
        )

        line = re.sub(
           r".*login-required.*", 
           "", 
           line
        )

        line = re.sub(
           r".*snowfall.*", 
           "", 
           line
        )

        line = re.sub(
           r".*-snow-.*", 
           "", 
           line
        )

        line = re.sub(
           r".*quantcast.*", 
           "", 
           line
        )

        line = re.sub(
           r".*christmas.*", 
           "", 
           line
        )

        line = re.sub(
           r".*onetrust.*", 
           "", 
           line
        )

        line = re.sub(
           r".*info-?sticky.*", 
           "", 
           line
        )

        line = re.sub(
           r".*-deblocker.*", 
           "", 
           line
        )

        line = re.sub(
           r".*mail.*", 
           "", 
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
           "", 
           line
        )

        line = re.sub(
           r"^[a-z0-9].*:-abp-has.*,.*", 
           "", 
           line
        )

        line = re.sub(
           r"^/snow.*", 
           "", 
           line
        )

        line = re.sub(
           r".*add-?to-?any.*", 
           "", 
           line
        )

        line = re.sub(
           r".*-copy-.*", 
           "", 
           line
        )

        line = re.sub(
           r".*tinypass.*", 
           "", 
           line
        )

        line = re.sub(
           r".*scribe.*", 
           "", 
           line
        )

        line = re.sub(
           r".*apsis.*", 
           "", 
           line
        )

        line = re.sub(
           r".*messaging.*", 
           "", 
           line
        )

        line = re.sub(
           r".*sleeknote.*", 
           "", 
           line
        )

        line = re.sub(
           r"\$([a-z]{1,15})\$", 
           r"$\1,", 
           line
        )

        line = re.sub(
           r"([a-z])###(.*:-abp-)", 
           r"\1#?##\2", 
           line
        )

        line = re.sub(
           r"^/[a-z]{1,8}\$[a-ce-z]{1,}$", 
           "", 
           line
        )

        line = re.sub(
           r".*\.app\^\$third-party$", 
           "", 
           line
        )

        line = re.sub(
           r"^\|\|.*fonts.*", 
           "", 
           line
        )

        line = re.sub(
           r".*disclaimer.*", 
           "", 
           line
        )

        line = re.sub(
           r".*reco\.se\^.*", 
           "", 
           line
        )

        line = re.sub(
           r".*\.cc-.*", 
           "", 
           line
        )

        line = re.sub(
           r".*message[_-]?contain.*", 
           "", 
           line
        )

        line = re.sub(
           r".*all-in-one-seo.*", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])1p", 
           r"\1~third-party", 
           line
        )

        line = re.sub(
           r".*:remove-attr.*", 
           "", 
           line
        )

        line = re.sub(
           r"([a-z])##(.*:has(-text)?\()", 
           r"\1#?#\2", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(1\)", 
           r"\1#?#\2\3*:has(> \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(2\)", 
           r"\1#?#\2\3*:has(> * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(3\)", 
           r"\1#?#\2\3*:has(> * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(4\)", 
           r"\1#?#\2\3*:has(> * > * >  * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(5\)", 
           r"\1#?#\2\3*:has(> * > * > * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(6\)", 
           r"\1#?#\2\3*:has(> * > * > * > * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(7\)", 
           r"\1#?#\2\3*:has(> * > * > * > * > * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(8\)", 
           r"\1#?#\2\3*:has(> * > * > * > * > * > * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(9\)", 
           r"\1#?#\2\3*:has(> * > * > * > * > * > * > * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(10\)", 
           r"\1#?#\2\3*:has(> * > * > * > * > * > * > * > * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(1\)", 
           r"\1#?#*:has(> \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(2\)", 
           r"\1#?#*:has(> * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(3\)", 
           r"\1#?#*:has(> * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(4\)", 
           r"\1#?#*:has(> * > * >  * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(5\)", 
           r"\1#?#*:has(> * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(6\)", 
           r"\1#?#*:has(> * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(7\)", 
           r"\1#?#*:has(> * > * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(8\)", 
           r"\1#?#*:has(> * > * > * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(9\)", 
           r"\1#?#*:has(> * > * > * > * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(10\)", 
           r"\1#?#*:has(> * > * > * > * > * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r".*:upward\([a-zA-Z0-9.#].*", 
           "", 
           line
        )

        line = re.sub(
           r":remove\(\)?", 
           "", 
           line
        )

        line = re.sub(
           r".*[,$]removeparam.*", 
           "", 
           line
        )

        line = re.sub(
           r".*#\^.*", 
           "", 
           line
        )

        line = re.sub(
           r".*matches-css.*", 
           "", 
           line
        )

        line = re.sub(
           r"(:has\(>.*,)([a-z.# ]|\[)", 
           r"\1>\2", 
           line
        )

        line = re.sub(
           r"(:has\(>.*,)([a-z.# ]|\[)", 
           r"\1>\2", 
           line
        )

        line = re.sub(
           r"(:has\(>.*,)([a-z.# ]|\[)", 
           r"\1>\2", 
           line
        )

        line = re.sub(
           r"(:has\(>.*,)([a-z.# ]|\[)", 
           r"\1>\2", 
           line
        )

        line = re.sub(
           r"(:has\(>.*,)([a-z.# ]|\[)", 
           r"\1>\2", 
           line
        )

        line = re.sub(
           r"(:has\(>.*,)([a-z.# ]|\[)", 
           r"\1>\2", 
           line
        )

        line = re.sub(
           r"(:has\(>.*,)([a-z.# ]|\[)", 
           r"\1>\2", 
           line
        )

        line = re.sub(
           r"(:has\(>.*,)([a-z.# ]|\[)", 
           r"\1>\2", 
           line
        )

        line = re.sub(
           r"[,$]empty$", 
           "", 
           line
        )

        line = re.sub(
           r"^/plugins?/[bce-z0-9][b-z0-9-]{1,}[a-su-z0-9]/?\*?$", 
           "", 
           line
        )

        line = re.sub(
           r".*\.se/scripts/track$", 
           "", 
           line
        )

        line = re.sub(
           r"^([a-z0-9*,.-]{0,})#\?#((([a-zA-Z0-9.#_*=_+>~/\^ -]|\[|\]|:\"|\"){0,}):has\(([_=.+#a-zA-Z0-9~>%&/$',;?^!*一-龯ぁ-んァ-ン・ーㄱ-힣æøåÆØÅäöÄÖ() -]|\[|\]|\"){1,}\))$", 
           r"\1##\2", 
           line
        )

        line = re.sub(
           r":has(\(.*:has-text)", 
           r":-abp-has\1", 
           line
        )

        line = re.sub(
           r".*:remove-class\(.*", 
           "", 
           line
        )

        line = re.sub(
           r".*pji\.nu\^.*", 
           "", 
           line
        )

        line = re.sub(
           r".*prisjakt-a\..*", 
           "", 
           line
        )

        line = re.sub(
           r".*\.kxcdn\.com\^", 
           "", 
           line
        )

        line = re.sub(
           r"^(\||:|/).*ify\..*", 
           "", 
           line
        )

        line = re.sub(
           r"^[|:/a-z0-9].*cdn\..*", 
           "", 
           line
        )

        line = re.sub(
           r".*amazonaws.*", 
           "", 
           line
        )

        line = re.sub(
           r"^.*(download|install).*app.*$", 
           "", 
           line
        )

        line = re.sub(
           r"^.*app-banner.*$", 
           "", 
           line
        )

        line = re.sub(
           r"^.*mooth.*(croll|wheel).*$", 
           "", 
           line
        )

        line = re.sub(
           r"^.*nicescroll.*$", 
           "", 
           line
        )

        line = re.sub(
           r"^.*/[lL]og.*$", 
           "", 
           line
        )

        line = re.sub(
           r"^\..*track.*$", 
           "", 
           line
        )

        line = re.sub(
           r"^\|\|addrevenue\.io\^\$third-party$", 
           "", 
           line
        )

        line = re.sub(
           r"^(\||/|:|-).*(tra?c?k(ing|er)?([.$/_-]|$)|analy|metric).*$", 
           "", 
           line
        )

        line = re.sub(
           r"^(.*)\$all(,reason=([A-Za-z0-9ÅÄÖåäöÉé🇸🇪🇬🇧.:/?= -]|(🇦|🇧|🇨|🇩|🇪|🇫|🇬|🇭|🇮|🇯|🇰|🇱|🇲|🇳|🇴|🇵|🇶|🇷|🇸|🇹|🇺|🇻|🇼|🇽|🇾|🇿)){1,})?$", 
           r"\1\n\1$popup", 
           line
        )

        line = re.sub(
           r"^(.*)\$all(,reason=([A-Za-z0-9ÅÄÖåäöÉé🇸🇪🇬🇧.:/?= -]|(🇦|🇧|🇨|🇩|🇪|🇫|🇬|🇭|🇮|🇯|🇰|🇱|🇲|🇳|🇴|🇵|🇶|🇷|🇸|🇹|🇺|🇻|🇼|🇽|🇾|🇿)){1,})?,domain=([a-z0-9.|-]{1,})$", 
           r"\1$domain=\5\n\1$popup,domain=\5", 
           line
        )

        line = re.sub(
           r"^.*[$,]denyallow.*$", 
           "", 
           line
        )

        line = re.sub(
           r":has-text",
           r":-abp-contains",
           line
        )

        line = re.sub(
           r"^(.*) {2}(.*)$",
           r"\1 \2",
           line
        )

        if is_supported_abp(line) and not line == '':
            text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    abp_filter = prepare_abp(lines)

    with open(OUTPUT, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(text)

    with open(OUTPUT_ABP, 'w', encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(abp_filter)

    print('The regular-file-to-ABP conversion has been generated.')