class users::dev {

    @group { web_user:
        gid    => 2000,
        ensure => present,
    }

}
