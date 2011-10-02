class users::dba {

    @group { dba:
        gid    => 867,
        ensure => present,
    }

}
