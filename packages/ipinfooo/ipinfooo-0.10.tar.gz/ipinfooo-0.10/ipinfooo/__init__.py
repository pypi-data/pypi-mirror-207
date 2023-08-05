#  For the sake of humanity here's a python script retrieving
#  ip information of the network interfaces.
#
#  Pay some tribute to my soul cause I lost a few years on this one
#
#  based on code from jaraco and many other attempts
#  on internet.
#  Fixed by <@gpotter2> from scapy's implementation to
#  add IPv6 support + fix structures
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.\
#

import itertools
from ctypes import Structure
from socket import AF_INET6

from six import u
import ctypes
import ipaddress
import ctypes.wintypes
from ctypes.wintypes import DWORD, BYTE
from socket import AF_INET

def get_win_ifaddrs():
    """
    A method for retrieving info of the network
    interfaces. Returns a nested dictionary of
    interfaces in Windows.
    """


    # from iptypes.h
    MAX_ADAPTER_ADDRESS_LENGTH = 8
    MAX_DHCPV6_DUID_LENGTH = 130

    GAA_FLAG_INCLUDE_PREFIX = ctypes.c_ulong(0x0010)

    class in_addr(Structure):
        _fields_ = [("byte", ctypes.c_ubyte * 4)]

    class in6_addr(ctypes.Structure):
        _fields_ = [("byte", ctypes.c_ubyte * 16)]

    class sockaddr_in(ctypes.Structure):
        _fields_ = [("sin_family", ctypes.c_short),
                    ("sin_port", ctypes.c_ushort),
                    ("sin_addr", in_addr),
                    ("sin_zero", 8 * ctypes.c_char)]

    class sockaddr_in6(ctypes.Structure):
        _fields_ = [("sin6_family", ctypes.c_short),
                    ("sin6_port", ctypes.c_ushort),
                    ("sin6_flowinfo", ctypes.c_ulong),
                    ("sin6_addr", in6_addr),
                    ("sin6_scope_id", ctypes.c_ulong)]

    class SOCKADDR_INET(ctypes.Union):
        _fields_ = [("Ipv4", sockaddr_in),
                    ("Ipv6", sockaddr_in6),
                    ("si_family", ctypes.c_short)]

    LPSOCKADDR_INET = ctypes.POINTER(SOCKADDR_INET)

    class SOCKET_ADDRESS(ctypes.Structure):
        _fields_ = [
            ('address', LPSOCKADDR_INET),
            ('length', ctypes.c_int),
        ]

    class _IP_ADAPTER_ADDRESSES_METRIC(ctypes.Structure):
        _fields_ = [
            ('length', ctypes.c_ulong),
            ('interface_index', DWORD),
        ]

    class _IP_ADAPTER_ADDRESSES_U1(ctypes.Union):
        _fields_ = [
            ('alignment', ctypes.c_ulonglong),
            ('metric', _IP_ADAPTER_ADDRESSES_METRIC),
        ]

    class IP_ADAPTER_UNICAST_ADDRESS(ctypes.Structure):
        pass

    PIP_ADAPTER_UNICAST_ADDRESS = ctypes.POINTER(IP_ADAPTER_UNICAST_ADDRESS)
    IP_ADAPTER_UNICAST_ADDRESS._fields_ = [
        ("length", ctypes.c_ulong),
        ("flags", DWORD),
        ("next", PIP_ADAPTER_UNICAST_ADDRESS),
        ("address", SOCKET_ADDRESS),
        ("prefix_origin", ctypes.c_int),
        ("suffix_origin", ctypes.c_int),
        ("dad_state", ctypes.c_int),
        ("valid_lifetime", ctypes.c_ulong),
        ("preferred_lifetime", ctypes.c_ulong),
        ("lease_lifetime", ctypes.c_ulong),
        ("on_link_prefix_length", ctypes.c_ubyte)
    ]

    class IP_ADAPTER_PREFIX(ctypes.Structure):
        pass

    PIP_ADAPTER_PREFIX = ctypes.POINTER(IP_ADAPTER_PREFIX)
    IP_ADAPTER_PREFIX._fields_ = [
        ("alignment", ctypes.c_ulonglong),
        ("next", PIP_ADAPTER_PREFIX),
        ("address", SOCKET_ADDRESS),
        ("prefix_length", ctypes.c_ulong)
    ]

    class IP_ADAPTER_ADDRESSES(ctypes.Structure):
        pass

    LP_IP_ADAPTER_ADDRESSES = ctypes.POINTER(IP_ADAPTER_ADDRESSES)

    # for now, just use void * for pointers to unused structures
    PIP_ADAPTER_ANYCAST_ADDRESS = ctypes.c_void_p
    PIP_ADAPTER_MULTICAST_ADDRESS = ctypes.c_void_p
    PIP_ADAPTER_DNS_SERVER_ADDRESS = ctypes.c_void_p
    # PIP_ADAPTER_PREFIX = ctypes.c_void_p
    PIP_ADAPTER_WINS_SERVER_ADDRESS_LH = ctypes.c_void_p
    PIP_ADAPTER_GATEWAY_ADDRESS_LH = ctypes.c_void_p
    PIP_ADAPTER_DNS_SUFFIX = ctypes.c_void_p

    IF_OPER_STATUS = ctypes.c_uint  # this is an enum, consider http://code.activestate.com/recipes/576415/
    IF_LUID = ctypes.c_uint64

    NET_IF_COMPARTMENT_ID = ctypes.c_uint32
    GUID = ctypes.c_byte * 16
    NET_IF_NETWORK_GUID = GUID
    NET_IF_CONNECTION_TYPE = ctypes.c_uint  # enum
    TUNNEL_TYPE = ctypes.c_uint  # enum

    IP_ADAPTER_ADDRESSES._fields_ = [
        ('length', ctypes.c_ulong),
        ('interface_index', DWORD),
        ('next', LP_IP_ADAPTER_ADDRESSES),
        ('adapter_name', ctypes.c_char_p),
        ('first_unicast_address', PIP_ADAPTER_UNICAST_ADDRESS),
        ('first_anycast_address', PIP_ADAPTER_ANYCAST_ADDRESS),
        ('first_multicast_address', PIP_ADAPTER_MULTICAST_ADDRESS),
        ('first_dns_server_address', PIP_ADAPTER_DNS_SERVER_ADDRESS),
        ('dns_suffix', ctypes.c_wchar_p),
        ('description', ctypes.c_wchar_p),
        ('friendly_name', ctypes.c_wchar_p),
        ('byte', BYTE * MAX_ADAPTER_ADDRESS_LENGTH),
        ('physical_address_length', DWORD),
        ('flags', DWORD),
        ('mtu', DWORD),
        ('interface_type', DWORD),
        ('oper_status', IF_OPER_STATUS),
        ('ipv6_interface_index', DWORD),
        ('zone_indices', DWORD * 16),
        ('first_prefix', PIP_ADAPTER_PREFIX),
        ('transmit_link_speed', ctypes.c_uint64),
        ('receive_link_speed', ctypes.c_uint64),
        ('first_wins_server_address', PIP_ADAPTER_WINS_SERVER_ADDRESS_LH),
        ('first_gateway_address', PIP_ADAPTER_GATEWAY_ADDRESS_LH),
        ('ipv4_metric', ctypes.c_ulong),
        ('ipv6_metric', ctypes.c_ulong),
        ('luid', IF_LUID),
        ('dhcpv4_server', SOCKET_ADDRESS),
        ('compartment_id', NET_IF_COMPARTMENT_ID),
        ('network_guid', NET_IF_NETWORK_GUID),
        ('connection_type', NET_IF_CONNECTION_TYPE),
        ('tunnel_type', TUNNEL_TYPE),
        ('dhcpv6_server', SOCKET_ADDRESS),
        ('dhcpv6_client_duid', ctypes.c_byte * MAX_DHCPV6_DUID_LENGTH),
        ('dhcpv6_client_duid_length', ctypes.c_ulong),
        ('dhcpv6_iaid', ctypes.c_ulong),
        ('first_dns_suffix', PIP_ADAPTER_DNS_SUFFIX),
    ]

    def GetAdaptersAddresses(af=0):
        """
        Returns an iteratable list of adapters.
        param:
         - af: the address family to read on
        """
        size = ctypes.c_ulong()
        AF_UNSPEC = 0
        flags = GAA_FLAG_INCLUDE_PREFIX
        GetAdaptersAddresses = ctypes.windll.iphlpapi.GetAdaptersAddresses
        GetAdaptersAddresses.argtypes = [
            ctypes.c_ulong,
            ctypes.c_ulong,
            ctypes.c_void_p,
            ctypes.POINTER(IP_ADAPTER_ADDRESSES),
            ctypes.POINTER(ctypes.c_ulong),
        ]
        GetAdaptersAddresses.restype = ctypes.c_ulong
        res = GetAdaptersAddresses(af, flags, None, None, size)
        if res != 0x6f:  # BUFFER OVERFLOW -> populate size
            raise RuntimeError("Error getting structure length (%d)" % res)
        pointer_type = ctypes.POINTER(IP_ADAPTER_ADDRESSES)
        buffer = ctypes.create_string_buffer(size.value)
        struct_p = ctypes.cast(buffer, pointer_type)
        res = GetAdaptersAddresses(af, flags, None, struct_p, size)
        if res != 0x0:  # NO_ERROR
            raise RuntimeError("Error retrieving table (%d)" % res)
        while struct_p:
            yield struct_p.contents
            struct_p = struct_p.contents.next

    result = []
    # In theory, we could use AF_UNSPEC = 0, but it doesn't work in practice
    for i in itertools.chain(GetAdaptersAddresses(AF_INET), GetAdaptersAddresses(AF_INET6)):
        # print("--------------------------------------")
        # print("IF: {0}".format(i.description))
        # print("\tdns_suffix: {0}".format(i.dns_suffix))
        # print("\tinterface type: {0}".format(i.interface_type))
        fu = i.first_unicast_address.contents
        ad = fu.address.address.contents
        # print("\tfamily: {0}".format(ad.family))
        if ad.si_family == AF_INET:
            ip_bytes = bytes(bytearray(ad.Ipv4.sin_addr))
            ip = ipaddress.IPv4Address(ip_bytes)
            ip_if = ipaddress.IPv4Interface(u("{0}/{1}".format(ip, fu.on_link_prefix_length)))
        elif ad.si_family == AF_INET6:
            ip_bytes = bytes(bytearray(ad.Ipv6.sin6_addr))
            ip = ipaddress.IPv6Address(ip_bytes)
            ip_if = ipaddress.IPv6Interface(u("{0}/{1}".format(ip, fu.on_link_prefix_length)))
        # print("\tipaddress: {0}".format(ip))
        # print("\tnetmask: {0}".format(ip_if.netmask))
        # print("\tnetwork: {0}".format(ip_if.network.network_address))
        # print("\tbroadcast: {0}".format(ip_if.network.broadcast_address))
        # print("\tmask length: {0}".format(fu.on_link_prefix_length))
        data = {}
        data['addr'] = "{0}".format(ip)
        data['netmask'] = "{0}".format(ip_if.netmask)
        data['broadcast'] = "{0}".format(ip_if.network.broadcast_address)
        data['network'] = "{0}".format(ip_if.network.network_address)

        name = i.description
        # result[i.description] = { ad.family : d}
        iface = {}
        for interface in result:
            if name in interface.keys():
                iface = interface
                break
        if iface:
            iface[name][ad.si_family] = data
        else:
            iface[name] = {ad.si_family: data}
            result.append(iface)

    return result


if __name__ == "__main__":
    get_win_ifaddrs()
