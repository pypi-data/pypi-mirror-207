'use strict';
{
    const globals = this;
    const skailar = globals.skailar;

    skailar.pluralidx = function(count) { return (count === 1) ? 0 : 1; };

    /* gettext identity library */

    skailar.gettext = function(msgid) { return msgid; };
    skailar.ngettext = function(singular, plural, count) {
        return (count === 1) ? singular : plural;
    };
    skailar.gettext_noop = function(msgid) { return msgid; };
    skailar.pgettext = function(context, msgid) { return msgid; };
    skailar.npgettext = function(context, singular, plural, count) {
        return (count === 1) ? singular : plural;
    };

    skailar.interpolate = function(fmt, obj, named) {
        if (named) {
            return fmt.replace(/%\(\w+\)s/g, function(match) {
                return String(obj[match.slice(2, -2)]);
            });
        } else {
            return fmt.replace(/%s/g, function(match) {
                return String(obj.shift());
            });
        }
    };

    /* formatting library */

    skailar.formats = {
        "DATETIME_FORMAT": "N j, Y, P",
        "DATETIME_INPUT_FORMATS": [
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d %H:%M:%S.%f",
            "%Y-%m-%d %H:%M",
            "%Y-%m-%d",
            "%m/%d/%Y %H:%M:%S",
            "%m/%d/%Y %H:%M:%S.%f",
            "%m/%d/%Y %H:%M",
            "%m/%d/%Y",
            "%m/%d/%y %H:%M:%S",
            "%m/%d/%y %H:%M:%S.%f",
            "%m/%d/%y %H:%M",
            "%m/%d/%y"
        ],
        "DATE_FORMAT": "N j, Y",
        "DATE_INPUT_FORMATS": [
            "%Y-%m-%d",
            "%m/%d/%Y",
            "%m/%d/%y"
        ],
        "DECIMAL_SEPARATOR": ".",
        "FIRST_DAY_OF_WEEK": 0,
        "MONTH_DAY_FORMAT": "F j",
        "NUMBER_GROUPING": 3,
        "SHORT_DATETIME_FORMAT": "m/d/Y P",
        "SHORT_DATE_FORMAT": "m/d/Y",
        "THOUSAND_SEPARATOR": ",",
        "TIME_FORMAT": "P",
        "TIME_INPUT_FORMATS": [
            "%H:%M:%S",
            "%H:%M:%S.%f",
            "%H:%M"
        ],
        "YEAR_MONTH_FORMAT": "F Y"
    };

    skailar.get_format = function(format_type) {
        const value = skailar.formats[format_type];
        if (typeof value === 'undefined') {
            return format_type;
        } else {
            return value;
        }
    };

    /* add to global namespace */
    globals.pluralidx = skailar.pluralidx;
    globals.gettext = skailar.gettext;
    globals.ngettext = skailar.ngettext;
    globals.gettext_noop = skailar.gettext_noop;
    globals.pgettext = skailar.pgettext;
    globals.npgettext = skailar.npgettext;
    globals.interpolate = skailar.interpolate;
    globals.get_format = skailar.get_format;
};
