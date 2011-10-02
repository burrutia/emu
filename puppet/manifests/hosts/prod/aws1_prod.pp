node aws1_prd {
 include default_packages
 include debug_tools
}

node "aws1prdweb1.burrutiaprd.internal", "aws1prdweb2.burrutiaprd.internal" inherits aws1_prd {
   $aws_secgroup = extlookup("AWS1_PRD_WEB")
   $channel_master = extlookup("AWS1_WEB_ADM")
   include gmond
}
