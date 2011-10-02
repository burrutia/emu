# The aws1%{env}ns1 server
PUPPET_SERVER=aws1${ENV}${class}1.$BIZ.internal
PUPPET_PORT=8140
PUPPET_LOG=/var/log/puppet/puppet.log
PUPPET_EXTRA_OPTS=--waitforcert=500
