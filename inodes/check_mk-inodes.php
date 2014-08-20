<?php
setlocale(LC_ALL, "POSIX");

# RRDtool Options
#$servicedesc=$NAGIOS_SERVICEDESC

$fsname = str_replace("_", "/", substr($servicedesc, 7));
$fstitle = $fsname;

$usedperc = $DS[1];
$warn = $WARN[1];
$crit = $CRIT[1];

$opt[1] = "--vertical-label % -M -l 0 --title '$hostname: $fstitle' ";

$def[1] = "DEF:usedperc=$RRDFILE[1]:$DS[1]:MAX ";
$def[1] .= "AREA:usedperc#00ffc6:\"used inodes % on $fsname\\n\" ";
$def[1] .= "LINE1:usedperc#003300 ";
$def[1] .= "HRULE:$warn#ffff00:\"Warning at $warn% \" ";
$def[1] .= "HRULE:$crit#ff0000:\"Critical at $crit%\\n\" ";
$def[1] .= "GPRINT:usedperc:LAST:\"current\: %6.0lf%% \" ";
$def[1] .= "GPRINT:usedperc:MAX:\"max\: %6.0lf%% \" ";
$def[1] .= "GPRINT:usedperc:AVERAGE:\"avg\: %6.0lf%% \\n\" ";
?>
