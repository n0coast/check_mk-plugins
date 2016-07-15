* graphite_data-1.0.mkp: check_mk plugin, includes active_checks_graphite.py
check_graphite_data and check_mk_active-graphite.php, still need to manually
install libexec/check_graphite_data

* active_checks_graphite.py: wato plugin to allow configuring check from GUI,
if not using .mkp install into ~/local/share/check_mk/web/plugins/wato/

* check_graphite_data: defines check parameters/fields to check_mk,
if not using .mkp install into ~/local/share/check_mk/checks/
Based on etsy `chec_graphite_data` with minor tweaks to make it work
in the cmk environment a little better.

* check_mk_active-graphite.php: defines graph format for pnp4nagios,
if not using .mkp install into ~/local/share/check_mk/pnp-templates/

* libexec/check_graphite_data: nagios plugin, not included in .mkp plugin,
install into ~/local/lib/nagios/plugins
