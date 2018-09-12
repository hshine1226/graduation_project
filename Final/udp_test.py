#! /usr/bin/env python

# Client and server for udp (datagram) echo.
#
# Usage: udpecho -s [port]            (to start a server)
# or:    udpecho -c host [port] <file (client)

import sys
from socket import *

# ECHO_PORT 기본 포트
ECHO_PORT = 50000 + 7

# 버퍼 사이즈
BUFSIZE = 1024

# 메인 함수 
def main():
    # 매개변수가 2개보다 적다면
    if len(sys.argv) < 2:
        # 사용 방법 표시
        usage()

    # 첫 매개변수가 '-s' 라면 
    if sys.argv[1] == '-s':
        #서버 함수 호출 
        server()

    # 첫 매개변수가 '-c' 라면
    elif sys.argv[1] == '-c':
        #클라이언트 함수 호출
        client()

    # '-s' 또는 '-c' 가 아니라면 
    else:
        # 사용 방법 표시
        usage()

# 사용하는 방법 화면에 표시하는 함수
def usage():
    sys.stdout = sys.stderr
    print 'Usage: udpecho -s [port]            (server)'
    print 'or:    udpecho -c host [port] <file (client)'
    # 종료
    sys.exit(2)

# 서버 함수
def server():
    # 매개 변수가 2개 초과라면 
    # ex>$ python udp_echo.py -s 8001
    if len(sys.argv) > 2:
        # 두번째 매개변수를 포트로 지정
        port = eval(sys.argv[2])

    # 매개 변수가 2개 라면 
    # ex>$ python udp_echo.py -s
    else:
        # 기본 포트로 설정        
        port = ECHO_PORT

    # 소켓 생성 (UDP = SOCK_DGRAM, TCP = SOCK_STREAM)
    s = socket(AF_INET, SOCK_DGRAM)
    
    # 포트 설정
    s.bind(('', port))
    
    # 준비 완료 화면에 표시
    print 'udp echo server ready'

    # 무한 루프 돌림
    while 1:
        # 클라이언트로 메시지가 도착하면 다음 줄로 넘어가고
        # 그렇지 않다면 대기(Blocking)
        data, addr = s.recvfrom(BUFSIZE)

        # 받은 메시지와 클라이언트 주소 화면에 출력
        print 'server received %r from %r' % (data, addr)
    
        # 받은 메시지를 클라이언트로 다시 전송
        s.sendto(data, addr)
        # 다시 처음 루프로 돌아감


# 클라이언트 함수
def client():
    # 매개변수가 3개 미만 이라면
    if len(sys.argv) < 3:
        # 사용 방법 화면에 출력
        # usage함수에서 프로그램 종료
        usage()

    # 두번째 매개변수를 서버 IP로 설정
    host = sys.argv[2]

    # 매개변수가 3개를 초과하였다면(4개라면)
    # ex>$ python udp_echo.py -c 127.0.0.1 8001
    if len(sys.argv) > 3:
        # 3번째 매개변수를 포트로 설정
        port = eval(sys.argv[3])

    # 초과하지 않았다면(즉, 3개라면) 
    # ex>$ python udp_echo.py -c 127.0.0.1
    else:
        # 기본 포트로 설정
        port = ECHO_PORT

    # IP 주소 변수에 서버 주소와 포트 설정 
    addr = host, port

    # 소켓 생성
    s = socket(AF_INET, SOCK_DGRAM)
   
    # 클라이언트 포트 설정 : 자동
    s.bind(('', 0))

    # 준비 완료 화면에 출력
    print 'udp echo client ready, reading stdin'

    # 무한 루프
    while 1:
        #터미널 차(입력창)에서 타이핑을하고 ENTER키를 누를때 까지  
        line = sys.stdin.readline()
        #변수에 값이 없다면
        if not line:
            break

        # 입력받은 텍스트를 서버로 발송
        s.sendto(line, addr)

        # 리턴 대기
        data, fromaddr = s.recvfrom(BUFSIZE)
        # 서버로부터 받은 메시지 출력
        print 'client received %r from %r' % (data, fromaddr)

main()
