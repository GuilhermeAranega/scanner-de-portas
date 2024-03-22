import socket, sys, multiprocessing as mp
from print_color import print
from portas import ports

def escanearPortas(ip, porta):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    if s.connect_ex((ip, porta)):
        print(f'A porta {porta} está ', end='')
        print('fechada', color='red', format='bold')
    else:
        print(f'A porta {porta} está ', end='')
        print('aberta', color='green', format='bold')

def multiProcessamento(ip, porta, escanearPortas):
    p = mp.Process(target=escanearPortas, args=(ip, porta))
    p.start()
    return p

def main():
    while True:
        ip = input('Digite um endereço ip (nada para parar): ')
        if ip == '':
            sys.exit(0)
        try:
            socket.gethostbyname(ip)
        except socket.gaierror: 
            print('\nIP não disponível', color='red', format='bold', end='')
            sys.exit(1)

        processos = []
        for port in ports:
            p = multiProcessamento(ip, port, escanearPortas)
            processos.append(p)

        for p in processos:
            p.join()

if __name__ == '__main__':
    main()