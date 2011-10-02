# aws_oakley_repo
class awsyum_repo
{
 include centos_base_repo
 include rightscale_repo
 include aws_oakley_repo
}

class aws_oakley_repo {
    file { "/etc/yum.repos.d/AWS_Oakley.repo":
    owner => "root",
    group => "root",
    mode => "0644",
    content => template("/etc/puppet/manifests/templates/all/etc/yum.repos.d/AWS_Oakley.repo")
   }
}

class centos_base_repo {
    file { "/etc/yum.repos.d/CentOS-Base.repo":
    owner => "root",
    group => "root",
    mode => "0644",
    content => template("/etc/puppet/manifests/templates/all/etc/yum.repos.d/CentOS-Base.repo")
   }
}

class rightscale_repo {
    file { "/etc/yum.repos.d/CentOS-RS.repo":
    owner => "root",
    group => "root",
    mode => "0644",
    content => template("/etc/puppet/manifests/templates/all/etc/yum.repos.d/CentOS-RS.repo")
    }
}

