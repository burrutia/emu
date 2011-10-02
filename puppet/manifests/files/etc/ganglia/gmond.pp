class ec2_gmond {
  include ganglia_gmond
  include ec2_gmond_conf
}

class ec2_gmond_conf {
    file{"/etc/ganglia/gmond.conf":
        owner =>'root',
        group =>'root',
        mode => 0644,
        notify => Service[gmond],
        content => template("/etc/puppet/manifests/templates/all/etc/ganglia/ec2_gmond.conf")
    }
}
