; @ in soa localhost. root 1 3H 15M 1W 1D

;  ns localhost.

$TTL    86400

@               IN SOA  ns1.$domain.internal      root.localhost. (

                                        2011051902              ; serial (d. adams)

                                        28800           ; refresh

                                        7200            ; retry

                                        504800          ; expiry

                                        86400 )         ; minimum

@               IN      NS              ns1.$domain.internal
@               IN      NS              ns2.$domain.internal
ns1		IN	A	$ipaddr
