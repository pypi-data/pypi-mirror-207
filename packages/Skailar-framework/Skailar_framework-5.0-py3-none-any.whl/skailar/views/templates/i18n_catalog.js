{% autoescape off %}
'use strict';
{
  const globals = this;
  const skailar = globals.skailar || (globals.skailar = {});

  {% if plural %}
  skailar.pluralidx = function(n) {
    const v = {{ plural }};
    if (typeof v === 'boolean') {
      return v ? 1 : 0;
    } else {
      return v;
    }
  };
  {% else %}
  skailar.pluralidx = function(count) { return (count == 1) ? 0 : 1; };
  {% endif %}

  /* gettext library */

  skailar.catalog = skailar.catalog || {};
  {% if catalog_str %}
  const newcatalog = {{ catalog_str }};
  for (const key in newcatalog) {
    skailar.catalog[key] = newcatalog[key];
  }
  {% endif %}

  if (!skailar.jsi18n_initialized) {
    skailar.gettext = function(msgid) {
      const value = skailar.catalog[msgid];
      if (typeof value === 'undefined') {
        return msgid;
      } else {
        return (typeof value === 'string') ? value : value[0];
      }
    };

    skailar.ngettext = function(singular, plural, count) {
      const value = skailar.catalog[singular];
      if (typeof value === 'undefined') {
        return (count == 1) ? singular : plural;
      } else {
        return value.constructor === Array ? value[skailar.pluralidx(count)] : value;
      }
    };

    skailar.gettext_noop = function(msgid) { return msgid; };

    skailar.pgettext = function(context, msgid) {
      let value = skailar.gettext(context + '\x04' + msgid);
      if (value.includes('\x04')) {
        value = msgid;
      }
      return value;
    };

    skailar.npgettext = function(context, singular, plural, count) {
      let value = skailar.ngettext(context + '\x04' + singular, context + '\x04' + plural, count);
      if (value.includes('\x04')) {
        value = skailar.ngettext(singular, plural, count);
      }
      return value;
    };

    skailar.interpolate = function(fmt, obj, named) {
      if (named) {
        return fmt.replace(/%\(\w+\)s/g, function(match){return String(obj[match.slice(2,-2)])});
      } else {
        return fmt.replace(/%s/g, function(match){return String(obj.shift())});
      }
    };


    /* formatting library */

    skailar.formats = {{ formats_str }};

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

    skailar.jsi18n_initialized = true;
  }
};
{% endautoescape %}
