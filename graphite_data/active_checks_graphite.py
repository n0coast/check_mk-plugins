group = "activechecks"

register_rule(group,
    "active_checks:graphite",
    Tuple(
        title = _("Check graphite data"),
        help = _("Alert on data, based on number from Graphite."),
        elements = [
            TextUnicode(
                title = _("Name"),
                help = _("Will be used in the service description. If the name starts with"
                         "a caret (^) the service description will not be prefixed with Graphite." ),
                allow_empty = False),
            Alternative(
                title = _("Mode of the Check"),
                help = _("""Check values from a single graph, Holt-Winters graph or diff the latest values between two.\n
                         Wildcards are allowed.\n
                         Single or diff URL like: http://graphite.example.com/render/?target=your.metric.here\n
                         Holt-Winters like: http://graphite.example.com/render/?target=holtWintersConfidenceBands(your.metric.here)&target=your.metric.here"""),
                elements = [
                    Dictionary(
                        title = _("Single Graph"),
                        elements = [
                            ( "url",
                              TextAscii(
                                title = _("Graphite graph URL"),
                                allow_empty = False
                              )
                            ),
                            ( "trad_thresh",
                              Tuple(
                                title = _("Warning and critical thresholds"),
                                elements = [
                                  Float(
                                    title = _("Warning threshold"),
                                    allow_empty = False
                                  ),
                                  Float(
                                    title = _("Critical threshold"),
                                    allow_empty = False
                                  ),
                                ]
                              ),
                            ),
                            ( "reverse",
                              FixedValue(
                                value = False,
                                totext = _("Thresholds reversed"),
                                title = _("Reverse - Alert when the value is UNDER warn/crit instead of OVER.")
                              )
                            ),
                        ],
                        required_keys = [ "url", "trad_thresh" ],
                    ),
                    Dictionary(
                        title = _("Single Graph - Holt-Winters"),
                        elements = [
                            ( "hw_url",
                              TextAscii(
                                title = _("Graphite graph URL"),
                                allow_empty = False
                              )
                            ),
                            ( "hw_upper",
                              FixedValue(
                                title = _("Upper breach causes critical."),
                                value = True,
                              )
                            ),
                            ( "hw_lower",
                              FixedValue(
                                title = _("Lower breach causes critical."),
                                value = True,
                              )
                            ),
                        ],
                        required_keys = [ "hw_url" ],
                    ),
                    Dictionary(
                        title = _("Two Graphs"),
                        elements = [
                            ( "diffgraph",
                              Tuple(
                                title = _("Diff the latest values between two graphs"),
                                elements = [
                                  TextAscii(
                                    title = _("Graphite URL"),
                                    allow_empty = False
                                  ),
                                  TextAscii(
                                    title = _("Graphite URL"),
                                    allow_empty = False
                                  ),
                                ]
                              )
                            ),
                            ( "trad_thresh",
                              Tuple(
                                title = _("Warning and critical thresholds"),
                                elements = [
                                  Float(
                                    title = _("Warning threshold"),
                                    allow_empty = False
                                  ),
                                  Float(
                                    title = _("Critical threshold"),
                                    allow_empty = False
                                  ),
                                ]
                              ),
                            ),
                            ( "reverse",
                              FixedValue(
                                value = False,
                                totext = _("Thresholds reversed"),
                                title = _("Reverse - Alert when the value is UNDER warn/crit instead of OVER.")
                              )
                            ),
                        ],
                        required_keys = [ "diffgraph" ],
                    )
                ]
            ),
            Dictionary(
                title = _("Optional parameters"),
                elements = [
                    ( "perf",
                      FixedValue(
                        value = True,
                        title = _("Include performance data in check output."),
                        help = _("Performance data will be included output, "
                                 "graphs will be created by nagios."),
                      ),
                    ),
                    ( "average",
                      Integer(
                        title = _("Average over the last N seconds of data"),
                        default_value = 60,
                      ),
                    ),
                ]
            ),
        ]
    ),
    match = 'all'
)

