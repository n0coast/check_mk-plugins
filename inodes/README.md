* inodes-1.0.mkp: check_mk plugin, includes inodes agent plugin and 
check_mk-inodes.php pnp4nagios template.

* plugins/inodes: check_mk agent plugin, this needs to be distributed to each
node and placed in local plugin directory, then it will be executed each
time the check_mk agent is run and results returned

* checks/inodes: check_mk check handler, interprets data returned by plugin
if not using .mkp install into ~/local/share/check_mk/checks/inodes

* check_mk_inodes.php: defines graph format for pnp4nagios,
if not using .mkp install into ~/local/share/check_mk/pnp-templates/
