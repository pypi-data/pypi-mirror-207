# -*- coding: utf-8 -*-
# @Time   : 2023/3/31 14:40
# @Author : zhangzhongtian
# @File   : _ig902_contents_locators.py
"""
_ig902_contents_locators

"""
from playwright.sync_api import Locator, Page


class IGContentsLocators:

    def __init__(self, page: Page, language='en', model='IG902'):
        self.page = page
        self.language = language
        self.model = model.upper()
        if language == 'en':
            self.__locale: dict = {'network': 'Network', 'network_interface': 'Network Interface',
                                   'network_interface_cellular': 'Cellular', 'network_interface_ethernet': 'Ethernet',
                                   'network_interface_bridge': 'Bridge', 'network_interface_loopback': 'Loopback',
                                   'network_service': 'Network Services', 'network_service_dhcp': 'DHCP',
                                   'network_service_dns': 'DNS', "gps_configure": "GPS Configure",
                                   "gps_ip_forwarding": "GPS IP Forwarding",
                                   "gps_serial_forwarding": "GPS Serial Forwarding",
                                   'network_service_host': 'Host List', 'network_routing': 'Routing',
                                   'network_routing_status': 'Routing Status',
                                   'network_routing_static': 'Static Routing', 'network_firewall': 'Firewall',
                                   'network_firewall_acl': 'ACL', 'network_firewall_nat': 'NAT',
                                   'l2tp_status': 'Status', 'l2tp_client': 'L2TP Client',
                                   'l2tp_service': 'L2TP Service',
                                   'edge': 'Edge Computing', 'python_edge': 'Python Edge Computing',
                                   'docker_manager': 'Docker Manager', 'cloud_edge_computing': 'Cloud Edge Computing',
                                   'device_supervisor': 'Device Supervisor', 'measure_monitor': 'Measure Monitor',
                                   'monitoring_list': 'Monitoring List', 'group': 'Group',
                                   'alarm': 'Alarm', 'realtime_alarms': 'Realtime Alarms', 'alarm_rules': 'Alarm Rules',
                                   'history_alarms': 'History Alarms', 'alarm_label': 'Alarm Label',
                                   'cloud': 'Cloud', 'mqtt_cloud_service': 'MQTT Cloud Service',
                                   'whitehawk_energy_manager': 'Whitehawk Energy Manager', 'protocol': 'Protocol',
                                   'parameter_settings': 'Parameter Settings',
                                   'custom_quickfunctions': 'Custom QuickFunctions',
                                   'system': 'System', 'system_time': 'System Time', 'system_log': 'Log',
                                   'system_config': 'Configuration Management', 'system_cloud': 'InHand Cloud',
                                   'system_firmware': 'Firmware Upgrade', 'system_tools': 'Access Tools',
                                   'system_user_management': 'User Management', 'system_reboot': 'Reboot',
                                   'system_network_tools': 'Network Tools', 'logout': 'Logout',
                                   'system_3rd_party': '3rd Party Notification', 'logout_submit': 'Confirm',
                                   'configuration': ' Configuration', 'trigger_condition': 'Trigger Condition',
                                   'gigabitethernet': 'Gigabitethernet',
                                   }
        else:
            self.__locale: dict = {'network': '网络', 'network_interface': '网络接口',
                                   'network_interface_cellular': '蜂窝网', 'network_interface_ethernet': '以太网',
                                   'network_interface_bridge': '桥接口', 'network_interface_loopback': '环回接口',
                                   'network_service': '网络服务', 'network_service_dhcp': 'DHCP服务',
                                   'network_service_dns': 'DNS服务', "gps_configure": "GPS 配置",
                                   "gps_ip_forwarding": "GPS IP转发",
                                   "gps_serial_forwarding": "GPS 串口转发", 'network_service_host': '主机列表',
                                   'network_routing': '路由', 'network_routing_status': '路由状态',
                                   'network_routing_static': '静态路由', 'network_firewall': '防火墙',
                                   'network_firewall_acl': '访问控制列表', 'network_firewall_nat': '网络地址转换',
                                   'l2tp_status': '状态', 'l2tp_client': 'L2TP客户端', 'l2tp_service': 'L2TP服务器',
                                   'edge': '边缘计算', 'python_edge': 'Python边缘计算', 'docker_manager': 'Docker 管理',
                                   'cloud_edge_computing': '公有云边缘计算', 'device_supervisor': '设备监控',
                                   'measure_monitor': '测点监控', 'monitoring_list': '监控列表', 'group': '分组',
                                   'alarm': '告警', 'realtime_alarms': '实时告警', 'alarm_rules': '告警规则',
                                   'history_alarms': '历史告警', 'alarm_label': '告警标签',
                                   'cloud': '云服务', 'mqtt_cloud_service': 'MQTT云服务',
                                   'whitehawk_energy_manager': '白鹰能源管家', 'protocol': '协议转换',
                                   'parameter_settings': '参数设置', 'custom_quickfunctions': '自定义快函数',
                                   'system': '系统管理', 'system_time': '系统时间', 'system_log': '系统日志',
                                   'system_config': '配置管理', 'system_cloud': '设备云平台',
                                   'system_firmware': '固件升级', 'system_tools': '管理工具',
                                   'system_user_management': '用户管理', 'system_reboot': '重启',
                                   'system_network_tools': '工具', 'system_3rd_party': '第三方软件声明',
                                   'logout': '退出登录', 'logout_submit': '确 认', 'configuration': '配置',
                                   'trigger_condition': '触发条件', 'gigabitethernet': '千兆以太网口',
                                   }

    def content_span_text(self, menu) -> Locator:
        one_menu = {"en": {"overview": "Performance And Storage", "cellular": "Enable Cellular",
                           "ethernet": "Gigabitethernet 0/1", "bridge": "Bridge Member",
                           "wlan": "Wireless Connection Status", "loopback": "127.0.0.1",
                           "dhcp": "DHCP Server", "dns": "DNS Server", "gps": "GPS Configure",
                           "host_list": "MAC Address", "routing_status": "Distance/Metric",
                           "static_routing": "Track ID", "acl": "Access Control Strategy",
                           "nat": "Network Address Translation(NAT) Rules",
                           "l2tp_status": "Local Session ID", "l2tp_client": "L2TPv3 Session",
                           "l2tp_service": "Enable L2TP Server", "python_edge_computing": "Python Engine",
                           "docker_manager": "Enable Docker Manager", "cloud_edge_computing": "Azure IoT Edge",
                           "azure_iot_edge": "Enable Security Daemon",
                           "aws_iot_greengrass": "Enable AWS IoT Greengrass",
                           "measure_monitor": "Controller List", "alarm": "Realtime Alarms",
                           "cloud": "MQTT Cloud Service", "mqtt_cloud_service": "Enable Cloud",
                           "whitehawk_energy_manager": "Enable Whitehawk Energy Manager",
                           "protocol": "Modbus TCP Slave",
                           "parameter_settings": "Serial Port Settings", "custom_quickfunctions": "QuickFunction List",
                           "system_time": "Enable SNTP Clients", "log": "View Recent",
                           "log_configure": "Send to the remote log server",
                           "configuration_management": "Configuration Files Operations",
                           "inhand_cloud": "InHand Connect Service", "firmware_upgrade": "Select Firmware",
                           "access_tools": "Enable HTTPS", "user_management": "User Permissions",
                           "reboot": "Immediately Reboot", "network_tools": "Traceroute",
                           "3rd_party_notification": "Third Party Software Notifications and Licenses"
                           },
                    'cn': {"overview": "性能与存储", "cellular": "启用蜂窝网", "ethernet": "千兆以太网口 0/1",
                           "bridge": "网桥成员", "wlan": "无线连接状态", "loopback": "127.0.0.1",
                           "dhcp": "DHCP 服务器", "dns": "域名服务器", "gps": "GPS 配置", "host_list": "MAC地址",
                           "routing_status": "距离/度量", "static_routing": "Track标识", "acl": "访问控制策略",
                           "nat": "网络地址转换(NAT)规则", "l2tp": "L2TP客户端", "l2tp_status": "本地隧道会话ID",
                           "l2tp_client": "L2TPv3会话", "l2tp_service": "启用L2TP服务器",
                           "python_edge_computing": "Python边缘计算引擎", "docker_manager": "启用Docker管理器",
                           "cloud_edge_computing": "Azure IoT Edge", "azure_iot_edge": "启用安全守护程序",
                           "aws_iot_greengrass": "启用AWS IoT Greengrass", "measure_monitor": "控制器列表",
                           "alarm": "实时告警", "cloud": "MQTT云服务", "mqtt_cloud_service": "启用云服务",
                           "whitehawk_energy_manager": "启用白鹰能源管家", "protocol": "Modbus TCP Slave",
                           "parameter_settings": "串口设置", "custom_quickfunctions": "快函数列表",
                           "system_time": "启用SNTP客户端", "log": "查看最新的",
                           "log_configure": "发送到远程日志服务器", "configuration_management": "配置文件操作",
                           "inhand_cloud": "InHand Connect Service", "firmware_upgrade": "选择固件",
                           "access_tools": "启用HTTPS", "user_management": "用户权限",
                           "reboot": "立即重启", "network_tools": "路由探测",
                           "3rd_party_notification": "Third Party Software Notifications and Licenses"

                           }}
        if self.language == 'en':
            span_text = one_menu.get('en').get(menu)
        else:
            span_text = one_menu.get('cn').get(menu)
        return self.page.locator(f'text={span_text}')

    @property
    def overview_menu(self) -> Locator:
        return self.page.locator('//*[@id="root"]/div/section/section/header/div/div/div[1]/div[2]/div/ul/li[2]/a')

    @property
    def network_menu(self) -> Locator:
        return self.page.locator('//*[@id="root"]/div/section/section/header/div/div/div[1]/div[2]/div/ul/li[4]/a')

    @property
    def edge_menu(self) -> Locator:
        return self.page.locator('//*[@id="root"]/div/section/section/header/div/div/div[1]/div[2]/div/ul/li[6]/a')

    @property
    def system_menu(self) -> Locator:
        return self.page.locator('//*[@id="root"]/div/section/section/header/div/div/div[1]/div[2]/div/ul/li[8]/a')

    @property
    def network_interface_menu(self) -> Locator:
        return self.page.locator(f'div:text-is("{self.__locale.get("network_interface")}")')

    @property
    def network_interface_cellular_menu(self) -> Locator:
        return self.page.locator(f'a:has-text("{self.__locale.get("network_interface_cellular")}")')

    @property
    def network_interface_ethernet_menu(self) -> Locator:
        return self.page.locator(f'a:has-text("{self.__locale.get("network_interface_ethernet")}")')

    @property
    def network_interface_bridge_menu(self) -> Locator:
        return self.page.locator(f'a:has-text("{self.__locale.get("network_interface_bridge")}")')

    @property
    def network_interface_wlan_menu(self) -> Locator:
        return self.page.locator('a:has-text("WLAN")')

    @property
    def network_interface_loopback_menu(self) -> Locator:
        return self.page.locator(f'a:has-text("{self.__locale.get("network_interface_loopback")}")')

    @property
    def network_interface_502_wan_menu(self) -> Locator:
        return self.page.locator('a:has-text("WAN")')

    @property
    def network_interface_502_lan_menu(self) -> Locator:
        return self.page.locator('a:has-text("LAN")')

    @property
    def network_service_menu(self) -> Locator:
        return self.page.locator(f'div:text-is("{self.__locale.get("network_service")}")')

    @property
    def network_service_dhcp_menu(self) -> Locator:
        return self.page.locator(f'a:has-text("{self.__locale.get("network_service_dhcp")}")')

    @property
    def network_service_dns_menu(self) -> Locator:
        return self.page.locator(f'a:has-text("{self.__locale.get("network_service_dns")}")')

    @property
    def network_service_gps_menu(self) -> Locator:
        return self.page.locator('a:has-text("GPS")')

    @property
    def network_service_host_menu(self) -> Locator:
        return self.page.locator(f'a:has-text("{self.__locale.get("network_service_host")}")')

    @property
    def network_routing_menu(self) -> Locator:
        return self.page.locator(f'div:text-is("{self.__locale.get("network_routing")}")')

    @property
    def network_routing_status_menu(self) -> Locator:
        return self.page.locator(f'a:has-text("{self.__locale.get("network_routing_status")}")')

    @property
    def network_routing_static_menu(self) -> Locator:
        return self.page.locator(f'a:has-text("{self.__locale.get("network_routing_static")}")')

    @property
    def network_firewall_menu(self) -> Locator:
        return self.page.locator(f'div:text-is("{self.__locale.get("network_firewall")}")')

    @property
    def network_firewall_acl_menu(self) -> Locator:
        return self.page.locator(f'a:has-text("{self.__locale.get("network_firewall_acl")}")')

    @property
    def network_firewall_nat_menu(self) -> Locator:
        return self.page.locator(f'a:has-text("{self.__locale.get("network_firewall_nat")}")')

    @property
    def network_vpn_menu(self) -> Locator:
        return self.page.locator('div:text-is("VPN")')

    @property
    def network_vpn_l2tp_menu(self) -> Locator:
        return self.page.locator('a:has-text("L2TP")')

    @property
    def python_edge_menu(self) -> Locator:
        return self.page.locator(f'a:has-text("{self.__locale.get("python_edge")}")')

    @property
    def docker_manager_menu(self) -> Locator:
        return self.page.locator(f'a:has-text("{self.__locale.get("docker_manager")}")')

    @property
    def cloud_edge_computing_menu(self) -> Locator:
        return self.page.locator(f'a:has-text("{self.__locale.get("cloud_edge_computing")}")')

    @property
    def cloud_edge_computing_azure_iot_edge_menu(self) -> Locator:
        return self.page.locator('div:text-is("Azure IoT Edge")')

    @property
    def cloud_edge_computing_aws_iot_greengrass_menu(self) -> Locator:
        return self.page.locator('div:text-is("AWS IoT Greengrass")')

    @property
    def device_supervisor_menu(self) -> Locator:
        return self.page.locator(f'div:text-is("{self.__locale.get("device_supervisor")}")')

    @property
    def measure_monitor_menu(self) -> Locator:
        return self.page.locator(
            f'.ant-menu.ant-menu-sub.ant-menu-inline >> a:has-text("{self.__locale.get("measure_monitor")}")')

    @property
    def alarm_menu(self) -> Locator:
        return self.page.locator(
            f'.ant-menu.ant-menu-sub.ant-menu-inline >> a:has-text("{self.__locale.get("alarm")}")')

    @property
    def cloud_menu(self) -> Locator:
        return self.page.locator(
            f'.ant-menu.ant-menu-sub.ant-menu-inline >> a:has-text("{self.__locale.get("cloud")}")')

    @property
    def protocol_menu(self) -> Locator:
        return self.page.locator(
            f'.ant-menu.ant-menu-sub.ant-menu-inline >> a:has-text("{self.__locale.get("protocol")}")')

    @property
    def parameter_settings_menu(self) -> Locator:
        return self.page.locator(
            f'.ant-menu.ant-menu-sub.ant-menu-inline >> a:has-text("{self.__locale.get("parameter_settings")}")')

    @property
    def custom_quickfunctions_menu(self) -> Locator:
        return self.page.locator(
            f'.ant-menu.ant-menu-sub.ant-menu-inline >> a:has-text("{self.__locale.get("custom_quickfunctions")}")')

    @property
    def system_time_menu(self) -> Locator:
        return self.page.locator(f'a:has-text("{self.__locale.get("system_time")}")')

    @property
    def system_log_menu(self) -> Locator:
        return self.page.locator(f'a:has-text("{self.__locale.get("system_log")}")')

    @property
    def system_config_menu(self) -> Locator:
        return self.page.locator(f'a:has-text("{self.__locale.get("system_config")}")')

    @property
    def system_cloud_menu(self) -> Locator:
        return self.page.locator(f'a:has-text("{self.__locale.get("system_cloud")}")')

    @property
    def system_firmware_menu(self) -> Locator:
        return self.page.locator(f'a:has-text("{self.__locale.get("system_firmware")}")')

    @property
    def system_tools_menu(self) -> Locator:
        return self.page.locator(f'a:has-text("{self.__locale.get("system_tools")}")')

    @property
    def system_user_management_menu(self) -> Locator:
        return self.page.locator(f'a:has-text("{self.__locale.get("system_user_management")}")')

    @property
    def system_reboot_menu(self) -> Locator:
        return self.page.locator(f'a:has-text("{self.__locale.get("system_reboot")}")')

    @property
    def system_network_tools_menu(self) -> Locator:
        return self.page.locator(f'a:has-text("{self.__locale.get("system_network_tools")}")')

    @property
    def system_3rd_party_menu(self) -> Locator:
        return self.page.locator(f'a:has-text("{self.__locale.get("system_3rd_party")}")')

    @property
    def tags_menu(self) -> dict:
        return {
            'overview': {
                'menu': self.overview_menu,
                'visible_locator': [self.content_span_text('overview')],
            },
            'network': {
                'default': 'network_interface',
                'menu': self.network_menu,
                'visible_locator': [self.network_interface_menu],
                'wait_locator': [self.network_interface_menu],
                # Network Interface
                'network_interface': {
                    'menu': self.network_interface_menu,
                    'visible_locator': [self.network_interface_cellular_menu],
                    'wait_locator': [self.network_interface_cellular_menu],
                    'cellular': {
                        'menu': self.network_interface_cellular_menu,
                        'visible_locator': [self.content_span_text('cellular')],
                        'wait_locator': [self.content_span_text('cellular')]},
                    'ethernet': {
                        'default': 'gigabitethernet_01',
                        'menu': self.network_interface_ethernet_menu,
                        'visible_locator': [self.content_span_text('ethernet')],
                        'wait_locator': [self.content_span_text('ethernet')],
                        'gigabitethernet_01': {
                            'menu': self.page.locator(f'div:text-is("{self.__locale.get("gigabitethernet")} 0/1")'),
                        },
                        'gigabitethernet_02': {
                            'menu': self.page.locator(f'div:text-is("{self.__locale.get("gigabitethernet")} 0/2")'),
                        }
                    },
                    'bridge': {
                        'menu': self.network_interface_bridge_menu,
                        'visible_locator': [self.content_span_text('bridge')],
                        'wait_locator': [self.content_span_text('bridge')]},
                    'wlan': {
                        'menu': self.network_interface_wlan_menu,
                        'visible_locator': [self.content_span_text('"wlan')],
                        'wait_locator': [self.content_span_text('"wlan')]},
                    'loopback': {
                        'menu': self.network_interface_loopback_menu,
                        'visible_locator': [self.content_span_text('loopback')],
                        'wait_locator': [self.content_span_text('loopback')]}},
                # Network Services
                'network_services': {
                    'menu': self.network_service_menu,
                    'visible_locator': [self.network_service_dhcp_menu],
                    'wait_locator': [self.network_service_dhcp_menu],
                    'dhcp': {
                        'menu': self.network_service_dhcp_menu,
                        'visible_locator': [self.content_span_text('dhcp')],
                        'wait_locator': [self.content_span_text('dhcp')]},
                    'dns': {
                        'menu': self.network_service_dns_menu,
                        'visible_locator': [self.content_span_text('dns')],
                        'wait_locator': [self.content_span_text('dns')]},
                    'gps': {
                        'default': 'gps_configure',
                        'menu': self.network_service_gps_menu,
                        'visible_locator': [self.content_span_text('gps')],
                        'wait_locator': [self.content_span_text('gps')],
                        'gps_configure': {
                            'menu': self.page.locator(f'div:text-is("{self.__locale.get("gps_configure")}")'),
                            'visible_locator': [self.page.locator('.ant-form-item-no-colon')],
                            'wait_locator': [self.page.locator('.ant-form-item-no-colon')],
                        },
                        'gps_ip_forwarding': {
                            'menu': self.page.locator(f'div:text-is("{self.__locale.get("gps_ip_forwarding")}")'),
                            'visible_locator': [self.page.locator('#enable')],
                            'wait_locator': [self.page.locator('#enable')],
                        },
                        'gps_serial_forwarding': {
                            'menu': self.page.locator(f'div:text-is("{self.__locale.get("gps_serial_forwarding")}")'),
                            'visible_locator': [self.page.locator('#enable')],
                            'wait_locator': [self.page.locator('#enable')],
                        },
                    },
                    'host_list': {
                        'menu': self.network_service_host_menu,
                        'visible_locator': [self.content_span_text('host_list')],
                        'wait_locator': [self.content_span_text('host_list')]}},
                # Routing
                'routing': {
                    'menu': self.network_routing_menu,
                    'visible_locator': [self.network_routing_status_menu],
                    'wait_locator': [self.network_routing_status_menu],
                    'routing_status': {
                        'menu': self.network_routing_status_menu,
                        'visible_locator': [self.content_span_text('routing_status')],
                        'wait_locator': [self.content_span_text('routing_status')]},
                    'static_routing': {
                        'menu': self.network_routing_static_menu,
                        'visible_locator': [self.content_span_text('static_routing')],
                        'wait_locator': [self.content_span_text('static_routing')]}},
                # Firewall
                'firewall': {
                    'menu': self.network_firewall_menu,
                    'visible_locator': [self.network_firewall_acl_menu],
                    'wait_locator': [self.network_firewall_acl_menu],
                    'acl': {
                        'menu': self.network_firewall_acl_menu,
                        'visible_locator': [self.content_span_text('acl')],
                        'wait_locator': [self.content_span_text('acl')]},
                    'nat': {
                        'menu': self.network_firewall_nat_menu,
                        'visible_locator': [self.content_span_text('nat')],
                        'wait_locator': [self.content_span_text('nat')]}},
                # VPN
                'vpn': {
                    'menu': self.network_vpn_menu,
                    'visible_locator': [self.network_vpn_l2tp_menu],
                    'wait_locator': [self.network_vpn_l2tp_menu],
                    'l2tp': {
                        'default': 'status',
                        'menu': self.network_vpn_l2tp_menu,
                        'status': {
                            'menu': self.page.locator(f'div:text-is("{self.__locale.get("l2tp_status")}")'),
                            'visible_locator': [self.content_span_text('l2tp_status')],
                            'wait_locator': [self.content_span_text('l2tp_status')]
                        },
                        'l2tp_client': {
                            'menu': self.page.locator(f'div:text-is("{self.__locale.get("l2tp_client")}")'),
                            'visible_locator': [self.content_span_text('l2tp_client')],
                            'wait_locator': [self.content_span_text('l2tp_client')]
                        },
                        'l2tp_service': {
                            'menu': self.page.locator(f'div:text-is("{self.__locale.get("l2tp_service")}")'),
                            'visible_locator': [self.content_span_text('l2tp_service')],
                            'wait_locator': [self.content_span_text('l2tp_service')]}
                    }
                }
            },
            'edge_computing': {
                'default': 'python_edge_computing',
                'menu': self.edge_menu,
                'visible_locator': [self.device_supervisor_menu],
                'wait_locator': [self.device_supervisor_menu],
                'python_edge_computing': {
                    'menu': self.python_edge_menu,
                    'visible_locator': [self.content_span_text('python_edge_computing')],
                    'wait_locator': [self.content_span_text('python_edge_computing')]
                },
                'docker_manager': {
                    'menu': self.docker_manager_menu,
                    'visible_locator': [self.content_span_text('docker_manager')],
                    'wait_locator': [self.content_span_text('docker_manager')]
                },
                'cloud_edge_computing': {
                    'default': 'azure_iot_edge',
                    'menu': self.cloud_edge_computing_menu,
                    'visible_locator': [self.content_span_text('cloud_edge_computing')],
                    'wait_locator': [self.content_span_text('cloud_edge_computing')],
                    'azure_iot_edge': {
                        'menu': self.cloud_edge_computing_azure_iot_edge_menu,
                        'visible_locator': [self.content_span_text('azure_iot_edge')],
                        'wait_locator': [self.content_span_text('azure_iot_edge')],
                    },
                    'aws_iot_greengrass': {
                        'menu': self.cloud_edge_computing_aws_iot_greengrass_menu,
                        'visible_locator': [self.content_span_text('aws_iot_greengrass')],
                        'wait_locator': [self.content_span_text('aws_iot_greengrass')],
                    }
                },
                # Device Supervisor
                'device_supervisor': {
                    'menu': self.device_supervisor_menu,
                    'visible_locator': [self.measure_monitor_menu],
                    'wait_locator': [self.measure_monitor_menu],
                    'measure_monitor': {
                        'default': 'monitoring_list',
                        'menu': self.measure_monitor_menu,
                        'monitoring_list': {
                            'menu': self.page.locator(f'div:text-is("{self.__locale.get("monitoring_list")}")')
                        },
                        'group': {
                            'menu': self.page.locator(f'div:text-is("{self.__locale.get("group")}")')
                        },
                    },
                    'alarm': {
                        'default': 'realtime_alarms',
                        'menu': self.alarm_menu,
                        'visible_locator': [self.content_span_text('alarm')],
                        'wait_locator': [self.content_span_text('alarm')],
                        'realtime_alarms': {
                            'menu': self.page.locator(f'div:text-is("{self.__locale.get("realtime_alarms")}")'),
                            'visible_locator': [self.page.locator('.ant-table-header.ant-table-hide-scrollbar')],
                            'wait_locator': [self.page.locator('.ant-table-header.ant-table-hide-scrollbar')]
                        },
                        'alarm_rules': {
                            'menu': self.page.locator(f'div:text-is("{self.__locale.get("alarm_rules")}")'),
                            'visible_locator': [
                                self.page.locator(f'span:text-is("{self.__locale.get("trigger_condition")}")')],
                            'wait_locator': [
                                self.page.locator(f'span:text-is("{self.__locale.get("trigger_condition")}")')]
                        },
                        'history_alarms': {
                            'menu': self.page.locator(f'div:text-is("{self.__locale.get("history_alarms")}")'),
                            'visible_locator': [self.page.locator('span:text-is("~")')],
                            'wait_locator': [self.page.locator('span:text-is("~")')]
                        },
                        'alarm_label': {
                            'menu': self.page.locator(f'div:text-is("{self.__locale.get("alarm_label")}")'),
                            'visible_locator': [self.page.locator('.ant-table-selection-column >> nth=0')],
                            'wait_locator': [self.page.locator('.ant-table-selection-column >> nth=0')]
                        },
                    },
                    'cloud': {
                        'default': 'mqtt_cloud_service',
                        'menu': self.cloud_menu,
                        'visible_locator': [self.content_span_text('cloud')],
                        'wait_locator': [self.content_span_text('cloud')],
                        'mqtt_cloud_service': {
                            'menu': self.page.locator(f'div:text-is("{self.__locale.get("mqtt_cloud_service")}")'),
                            'visible_locator': [self.content_span_text('mqtt_cloud_service')],
                            'wait_locator': [self.content_span_text('mqtt_cloud_service')]
                        },
                        'whitehawk_energy_manager': {
                            'menu': self.page.locator(
                                f'div:text-is("{self.__locale.get("whitehawk_energy_manager")}")'),
                            'visible_locator': [self.content_span_text('whitehawk_energy_manager')],
                            'wait_locator': [self.content_span_text('whitehawk_energy_manager')]
                        }
                    },
                    'protocol': {
                        'default': 'modbus_tcp_slave',
                        'menu': self.protocol_menu,
                        'modbus_tcp_slave': {
                            'menu': self.page.locator(f'div:text-is("Modbus TCP Slave")'),
                            'visible_locator': [
                                self.page.locator(f'text=Modbus TCP Slave{self.__locale.get("configuration")}')],
                            'wait_locator': [
                                self.page.locator(f'text=Modbus TCP Slave{self.__locale.get("configuration")}')],
                        },
                        'iec_104_server': {
                            'menu': self.page.locator(f'div:text-is("IEC 104 Server")'),
                            'visible_locator': [
                                self.page.locator(f'text=IEC 104 Server{self.__locale.get("configuration")}')],
                            'wait_locator': [
                                self.page.locator(f'text=IEC 104 Server{self.__locale.get("configuration")}')],
                        },
                        'opcua_server': {
                            'menu': self.page.locator(f'div:text-is("OPCUA Server")'),
                            'visible_locator': [
                                self.page.locator(f'text=OPCUA Server{self.__locale.get("configuration")}')],
                            'wait_locator': [
                                self.page.locator(f'text=OPCUA Server{self.__locale.get("configuration")}')],
                        },
                        'modbus_rtu_slave': {
                            'menu': self.page.locator(f'div:text-is("Modbus RTU Slave")'),
                            'visible_locator': [
                                self.page.locator(f'text=Modbus RTU Slave{self.__locale.get("configuration")}')],
                            'wait_locator': [
                                self.page.locator(f'text=Modbus RTU Slave{self.__locale.get("configuration")}')],
                        },
                    },
                    'parameter_settings': {
                        'menu': self.parameter_settings_menu,
                        'visible_locator': [self.content_span_text('parameter_settings')],
                        'wait_locator': [self.content_span_text('parameter_settings')]
                    },
                    'custom_quickfunctions': {
                        'menu': self.custom_quickfunctions_menu,
                        'visible_locator': [self.content_span_text('custom_quickfunctions')],
                        'wait_locator': [self.content_span_text('custom_quickfunctions')]}
                }
            },
            'system': {
                'default': 'system_time',
                'menu': self.system_menu,
                'system_time': {
                    'menu': self.system_time_menu,
                    'visible_locator': [self.content_span_text('system_time')],
                    'wait_locator': [self.content_span_text('system_time')],
                },
                'log': {
                    'default': 'log',
                    'menu': self.system_log_menu,
                    'log': {
                        'menu': self.page.locator('.ant-tabs-tab >> nth=0'),
                        'visible_locator': [self.content_span_text('log')],
                        'wait_locator': [self.content_span_text('log')],
                    },
                    'configure': {
                        'menu': self.page.locator('.ant-tabs-tab >> nth=1'),
                        'visible_locator': [self.content_span_text('log_configure')],
                        'wait_locator': [self.content_span_text('log_configure')],
                    }
                },
                'configuration_management': {
                    'menu': self.system_config_menu,
                    'visible_locator': [self.content_span_text('configuration_management')],
                    'wait_locator': [self.content_span_text('configuration_management')],
                },
                'inhand_cloud': {
                    'default': 'inhand_connect_service',
                    'menu': self.system_cloud_menu,
                    'visible_locator': [self.content_span_text('inhand_cloud')],
                    'wait_locator': [self.content_span_text('inhand_cloud')],
                    'inhand_connect_service': {
                        'menu': self.page.locator(f'div:text-is("InHand Connect Service")'),
                    },
                    'inhand_device_manager': {
                        'menu': self.page.locator(f'div:text-is("InHand Device Manager")'),
                    },
                    'inhand_iscada_cloud': {
                        'menu': self.page.locator(f'div:text-is("InHand iSCADA Cloud")'),
                    }
                },
                'firmware_upgrade': {
                    'menu': self.system_firmware_menu,
                    'visible_locator': [self.content_span_text('firmware_upgrade')],
                    'wait_locator': [self.content_span_text('firmware_upgrade')],
                },
                'access_tools': {
                    'menu': self.system_tools_menu,
                    'visible_locator': [self.content_span_text('access_tools')],
                    'wait_locator': [self.content_span_text('access_tools')],
                },
                'user_management': {
                    'menu': self.system_user_management_menu,
                    'visible_locator': [self.content_span_text('user_management')],
                    'wait_locator': [self.content_span_text('user_management')],
                },
                'reboot': {
                    'menu': self.system_reboot_menu,
                    'visible_locator': [self.content_span_text('reboot')],
                    'wait_locator': [self.content_span_text('reboot')],
                },
                'network_tools': {
                    'menu': self.system_network_tools_menu,
                    'visible_locator': [self.content_span_text('network_tools')],
                    'wait_locator': [self.content_span_text('network_tools')],
                },
                '3rd_party_notification': {
                    'menu': self.system_3rd_party_menu,
                    'visible_locator': [self.content_span_text('3rd_party_notification')],
                    'wait_locator': [self.content_span_text('3rd_party_notification')],
                }
            },
        }
