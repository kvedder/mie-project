#!/usr/bin/env bash

# install the ISC DCHPD package (no longer maintained by ISC)
apt install -y isc-dhcp-server

# backup the original default config file
cp /etc/dhcp/dhcpd.conf /etc/dhcp/dhcpd.conf.DIST

# backup the original interface config file
cp /etc/default/isc-dhcp-server /etc/default/isc-dhcp-server.DIST

# specify what interfaces the DHCP server will listen on
cat > /etc/default/isc-dhcp-server << EOF
INTERFACESv4="ens18"
INTERFACESv6=""
EOF

# declare some global DCHP params, and setup a subnet with DNS, Next Hop Routers and a declared available IP range
cat > /etc/dhcp/dhcpd.conf << EOF
option domain-name "kvedder.com";
option domain-name-servers 8.8.8.8, 1.1.1.1;
authoritative;

default-lease-time 600;
max-lease-time 7200;

subnet 192.168.240.0 netmask 255.255.255.0 {
  range 192.168.240.100 192.168.240.254;
  option routers 192.168.240.1;
  option subnet-mask 255.255.255.0;
}

EOF

service isc-dhcp-server start






