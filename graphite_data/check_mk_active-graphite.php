<?php
# Create graphs for graphite data, redundant but pretty.
#
# Graph title pulled from service description
$opt[1] = "-X 0 --title \"$NAGIOS_AUTH_SERVICEDESC\" ";
$def[1]  = "DEF:graphite_data=$RRDFILE[1]:$DS[1]:AVERAGE " ;
# Here is the graphite data itself, this should get printed
# no matter what.
$def[1] .= "LINE1.5:graphite_data#c80032:\"current value\" ";
$def[1] .= "GPRINT:graphite_data:LAST:\"%.2lf\\n\" " ;
# If lower and upper band are set then we will print those out
if (isset($DS[2], $DS[3])) {
  $def[1] .= "DEF:upper_band=$RRDFILE[3]:$DS[3]:AVERAGE " ;
  $def[1] .= "LINE:upper_band#00c800:\"upper band   \" ";
  $def[1] .= "GPRINT:upper_band:LAST:\"%.2lf\\n\" " ;
  $def[1] .= "DEF:lower_band=$RRDFILE[2]:$DS[2]:AVERAGE " ;
  $def[1] .= "LINE:lower_band#6464ff:\"lower band   \" ";
  $def[1] .= "GPRINT:lower_band:LAST:\"%.2lf\\n\" " ;
  # Calculate value between upper and lower bands,
  # use the value to color the area between bands.
  $def[1] .= "CDEF:diff=upper_band,lower_band,- " ;
  $def[1] .= "AREA:diff#ff7f0060::STACK " ;
}
# If we are not graphing Holt-Winters bands then warning 
# and critical values might exist, and we should show those
# as well
if (!empty($WARN[1]) && !empty($CRIT[1])) {
  $warn = $WARN[1];
  $crit = $CRIT[1];
  $def[1] .= "HRULE:$warn#ffff00:\"warning at $warn\\n\" ";
  $def[1] .= "HRULE:$crit#ff0000:\"critical at $crit\" ";
}
