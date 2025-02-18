# 아두이노 보드가 우분투의 어떤 포트에 연결되어있는지 찾기 위한 코드
# 우분투에서 모듈 설치 후 사용
# $ sudo apt install python3-serial

import serial.tools.list_ports as serial_port_list

ports = serial_port_list.comports()

for port in ports:
  print(port)
