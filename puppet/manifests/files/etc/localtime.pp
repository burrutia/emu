# set time to pst
class localtime {
file { "/etc/localtime":
    ensure=> link,
    notify => Service[syslog],
    target => "/usr/share/zoneinfo/America/Los_Angeles",
    }
}
