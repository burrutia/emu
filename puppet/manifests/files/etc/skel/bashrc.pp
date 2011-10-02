class gitbashrc {
    file {"/etc/skel/.bashrc":
    owner => 'root',
    group => 'root',
    mode => 0644,
    content =>template("/etc/puppet/manifests/templates/all/etc/skel/gitbashrc")
    }
}
