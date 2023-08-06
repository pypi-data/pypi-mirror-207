from machine import UART
import time


def func_timeout_ms(timeout: int = 1000):
    """
    调用函数，超时返回
    :param timeout: 超时时间
    :return: 函数返回值
    """

    def A(func):
        def B(*args, **kwargs):
            start_time = time.ticks_ms()
            while True:
                if time.ticks_ms() - start_time > timeout:
                    return None
                result = func(*args, **kwargs)
                if result is not None:
                    return result

        return B

    return A


class AT:

    def __init__(self, mode: str = '', param: list = None):
        if param is None:
            param = []
        self.mode = mode
        self.param = param

    def __str__(self):
        return f'AT+{self.mode}=' + ','.join(self.param)


class HC04:

    def __init__(self, uart: UART):
        self.uart = uart

    """
    通用指令
    """

    def test(self):
        """
        测试通讯
        :return: bool
        """
        self.uart.write(b'AT')
        return self.uart.read(2) == b'OK'

    def change_baudrate(self, baudrate: int = 9600, parity: str = 'N'):
        """
        改蓝牙串口通讯波特率和校验位
        :param baudrate: 波特率
        :param parity: 校验位 N/E/O 无/偶/奇
        """
        self.uart.write(b'AT+BAUD=' + str(baudrate).encode('utf-8') + b',' + parity.encode('utf-8'))
        result = self.uart.read(2) == b'OK'
        self.uart.read()
        return result

    def get_version(self):
        """
        获取版本号
        :return: 版本号
        """
        self.uart.write(b'AT+VERSION')
        return self.uart.read().decode('utf-8')

    def set_led(self, state: bool):
        """
        设置LED灯
        :param state: 状态 True/False
        """
        self.uart.write(b'AT+LED=' + str(int(state)).encode('utf-8'))
        return self.uart.read(2) == b'OK'

    def get_led(self):
        """
        获取LED灯状态
        :return: 状态 True/False
        """
        self.uart.write(b'AT+LED?')
        return bool(self.uart.read().decode('utf-8')[-1])

    def reset(self):
        """
        参数恢复默认值指令
        :return: bool
        """
        self.uart.write(b'AT+DEFAULT')
        return self.uart.read(2) == b'OK'

    def reboot(self):
        """
        重启模块
        :return: bool
        """
        self.uart.write(b'AT+RESET')
        return self.uart.read(2) == b'OK'

    def set_silent(self, state: bool):
        """
        设置静默模式
        :param state: 状态 True/False
        """
        self.uart.write(b'AT+BTMODE=' + str(int(state)).encode('utf-8'))
        return bool(self.uart.read().decode('utf-8')[-1])

    def set_role(self, role: str = 'BM'):
        """
        设置模块角色
        :param role: 角色 BM/M/S
        """
        self.uart.write(b'AT+ROLE=' + role.encode('utf-8'))
        return self.uart.read()[:2] == b'OK'

    def get_role(self):
        """
        获取模块角色
        :return: Master/Slave
        """
        self.uart.write(b'AT+ROLE?')
        return self.uart.read().decode('utf-8')

    def clear(self):
        """
        主机清除已记录的从机地址指令（仅主机有效）
        :return: bool
        """
        self.uart.write(b'AT+CLEAR')
        return self.uart.read(2) == b'OK'

    """
    SPP 部分指令
    """

    def spp_set_name(self, name: str):
        """
        设置蓝牙名称
        :param name: 名称
        """
        self.uart.write(b'AT+NAME=' + name.encode('utf-8'))
        return self.uart.read()[:2] == b'OK'

    def spp_set_password(self, password: str):
        """
        设置蓝牙密码
        :param password: 密码
        """
        self.uart.write(b'AT+PIN=' + password.encode('utf-8'))
        return self.uart.read()[:2] == b'OK'

    def spp_get_password(self):
        """
        获取蓝牙密码
        :return: 密码
        """
        self.uart.write(b'AT+PIN=?')
        return self.uart.read().decode('utf-8').split('=')[1]

    def spp_set_address(self, address: str):
        """
        设置蓝牙地址, 地址为 12 位的 0~F 大写字符，即 16 进制字符。只能修改后 10 位的地址，前面 2 位固定为 04
        :param address: 地址
        """
        if len(address) != 10:
            return False
        self.uart.write(b'AT+ADDR=' + address.encode('utf-8'))
        return self.uart.read()[:2] == b'OK'

    def spp_get_address(self):
        """
        获取蓝牙地址
        :return: 地址
        """
        self.uart.write(b'AT+ADDR=?')
        return self.uart.read().decode('utf-8').split('=')[1]

    def spp_set_code(self, code: str):
        """
        设置蓝牙编码,修改模块的 COD，默认值是 001F00。支持 6~8 位的 COD，少于 6 位，前面补 0。
        如果有输入除 0~F 之外的字符，COD 将设置为 000000
        :param code: 编码
        """
        self.uart.write(b'AT+CODE=' + code.encode('utf-8'))
        return self.uart.read()[:2] == b'OK'

    def spp_get_code(self):
        """
        获取蓝牙编码
        :return: 编码
        """
        self.uart.write(b'AT+CODE=?')
        return self.uart.read().decode('utf-8').split('=')[1]

    """
    BLE 部分指令
    """

    def ble_set_broadcast(self, state: bool):
        """
        设置广播开关
        :param state: 状态 True/False
        """
        self.uart.write(b'AT+BLE=' + str(int(state)).encode('utf-8'))
        return self.uart.read()[:2] == b'OK'

    def ble_get_broadcast(self):
        """
        获取广播开关
        :return: 状态 True/False
        """
        self.uart.write(b'AT+BLE=?')
        return self.uart.read().decode('utf-8').split('=')[1] == '1'

    def ble_set_name(self, name: str):
        """
        设置蓝牙名称
        :param name: 名称
        """
        self.uart.write(b'AT+BNAME=' + name.encode('utf-8'))
        return self.uart.read()[:2] == b'OK'

    def ble_get_name(self):
        """
        获取蓝牙名称
        :return: 名称
        """
        self.uart.write(b'AT+BNAME=?')
        return self.uart.read().decode('utf-8').split('=')[1]

    def ble_set_address(self, address: str):
        """
        设置蓝牙地址, 地址为 12 位的 0~F 大写字符，即 16 进制字符。只能修改后 10 位的地址，前面 2 位固定为 C4
        :param address: 地址
        """
        if len(address) != 10:
            return False
        self.uart.write(b'AT+BADDR=' + address.encode('utf-8'))
        return self.uart.read()[:2] == b'OK'

    def ble_set_broadcast_interval(self, interval: int):
        """
        设置广播间隔,xx 的单位是 625us（即，若 xx=1，广播间隔就是 625us*1=625us），范围32~16000（相当于 20ms~10s）
        默认值是 100 (62.5ms)
        :param interval: 间隔
        """
        self.uart.write(b'AT+AINT=' + str(interval).encode('utf-8'))
        return self.uart.read()[:2] == b'OK'

    def ble_get_broadcast_interval(self):
        """
        获取广播间隔
        :return: 间隔
        """
        self.uart.write(b'AT+AINT=?')
        return int(self.uart.read().decode('utf-8').split('=')[1])

    def ble_set_connect_interval(self, interval_min: int, interval_max: int):
        """
        设置连接间隔
        单位 1.25ms，设置范围 6~3199（7.5ms~4s）。
        1、此值直接影响实际连接间隔：xx≤实际连接间隔≤yy
        2、必须符合条件 xx≤yy
        3、可以单独输入一个参数 xx，yy 将直接等于 xx。
        4、默认值：8,11
        :param interval_min: 最小间隔
        :param interval_max: 最大间隔
        """
        self.uart.write(b'AT+INT=' + str(interval_min).encode('utf-8') + b',' + str(interval_max).encode('utf-8'))
        return self.uart.read()[:2] == b'OK'

    def ble_get_connect_interval(self):
        """
        获取连接间隔
        :return: 间隔
        """
        self.uart.write(b'AT+INT=?')
        return self.uart.read().decode('utf-8').split('=')[1].split(',')

    def ble_set_connect_timeout(self, timeout: int):
        """
        设置连接超时
        单位 10ms，设置范围 100~3200（1s~32s）
        :param timeout: 超时
        """
        self.uart.write(b'AT+CTOUT=' + str(timeout).encode('utf-8'))
        return self.uart.read()[:2] == b'OK'

    def ble_get_connect_timeout(self):
        """
        获取连接超时
        :return: 超时
        """
        self.uart.write(b'AT+CTOUT=?')
        return int(self.uart.read().decode('utf-8').split('=')[1])

    def ble_set_slave_latency(self, latency: int):
        """
        设置从机延迟
        单位 10ms，设置范围 0~499（0~5s）
        :param latency: 延迟
        """
        self.uart.write(b'AT+LATENCY=' + str(latency).encode('utf-8'))
        return self.uart.read()[:2] == b'OK'

    def ble_get_slave_latency(self):
        """
        获取从机延迟
        :return: 延迟
        """
        self.uart.write(b'AT+LATENCY=?')
        return int(self.uart.read().decode('utf-8').split('=')[1])

    def ble_set_search_uuid(self, uuid: str):
        """
        设置搜索 UUID
        由于蓝牙设备繁多，所以一般蓝牙主机（因为没有显示屏，很难人工选择）
        都设置了搜索 UUID 过滤。这样的话， 只有 UUID 相同的从机才能被搜索到。
        默认 FFF0（意为 0xFFF0）；参数必须要在 0~F 范围内，且长度为 4 位。
        :param uuid: UUID
        """
        self.uart.write(b'AT+LUUID=' + uuid.encode('utf-8'))
        return self.uart.read()[:2] == b'OK'

    def ble_get_search_uuid(self):
        """
        获取搜索 UUID
        :return: UUID
        """
        self.uart.write(b'AT+LUUID=?')
        return self.uart.read().decode('utf-8').split('=')[1]

    def ble_set_service_uuid(self, uuid: str):
        """
        设置服务 UUID
        此服务 UUID 是主机找到服务的依据，找到服务才能找到具体的特征值。
        默认 FFE0（意为 0xFFE0）；参数必须要在 0~F 范围内，且长度为 4 位。
        :param uuid: UUID
        """
        self.uart.write(b'AT+UUID=' + uuid.encode('utf-8'))
        return self.uart.read()[:2] == b'OK'

    def ble_get_service_uuid(self):
        """
        获取服务 UUID
        :return: UUID
        """
        self.uart.write(b'AT+UUID=?')
        return self.uart.read().decode('utf-8').split('=')[1]

    def ble_set_transmit_uuid(self, uuid: str):
        """
        设置透传 UUID
        此透传 UUID 必须正确才能正常透传，收发数据。
        默认 FFE1（意为 0xFFE1）；参数必须要在 0~F 范围内
        :param uuid: UUID
        """
        self.uart.write(b'AT+TUUID=' + uuid.encode('utf-8'))
        return self.uart.read()[:2] == b'OK'

    def ble_get_transmit_uuid(self):
        """
        获取透传 UUID
        :return: UUID
        """
        self.uart.write(b'AT+TUUID=?')
        return self.uart.read().decode('utf-8').split('=')[1]

    """
    综合指令
    """

    def info(self):
        """
        获取设备信息
        :return: 信息
        """
        self.uart.write(b'AT+RX')
        return {x.split('=')[0].split('+')[1]: x.split('=')[1] for x in self.uart.read().decode('utf-8').split('\n')}

    """
    基础指令
    """

    def send_byte(self, data: bytes):
        """
        发送数据
        :param data: 数据
        """
        self.uart.write(data)

    def read_byte(self):
        """
        读取数据
        :return: 数据
        """
        return self.uart.read()

    def send_str(self, data: str):
        """
        发送字符串
        :param data: 字符串
        """
        self.uart.write(data.encode('utf-8'))

    def read_str(self):
        """
        读取字符串
        :return: 字符串
        """
        return self.uart.read().decode('utf-8')

    def send(self, data):
        if type(data) == str:
            self.send_str(data)
        elif type(data) == bytes:
            self.send_byte(data)

    def read(self):
        return self.read_str()


class HC25:

    def __init__(self, uart: UART):
        self.uart = uart

    def send(self, data):
        if type(data) == str:
            self.uart.write(data.encode())
        elif type(data) == bytes:
            self.uart.write(data)

    @func_timeout_ms(500)
    def read(self, n=-1):
        try:
            result = self.uart.read(n).decode()
            return result or None
        except Exception:
            return None

    def into_control_mode(self):
        self.uart.write(b'+++')
        return self.read(28)

    def exit_control_mode(self):
        self.uart.write(b'AT+ENTM')
        return self.read()

    def reset(self):
        self.uart.write(b'AT+RESET')
        return self.read()

    def mac(self):
        self.uart.write(b'AT+MAC')
        return self.read()

    def wscan(self):
        self.uart.write(b'AT+WSCAN')
        return self.read()

    def wmode(self, mode):
        self.uart.write(b'AT+WMODE=' + mode.encode())
        return self.read()