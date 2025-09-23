#!/usr/bin/env python3
import socket 
import requests
import sys
from rich.panel import Panel
from rich.console import Console
from rich.align import Align
from rich.style import Style
from rich import print
from colorama import init, Fore

init(autoreset=False)


console = Console()

banner = """\
  █████▒▓█████  ██▀███   ██▀███   ▄▄▄       ███▄ ▄███▓▓█████  ███▄    █ ▄▄▄█████▓ ▄▄▄       ██▓    ▓█████  ▒█████  
▓██   ▒ ▓█   ▀ ▓██ ▒ ██▒▓██ ▒ ██▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒▒████▄    ▓██▒    ▓█   ▀ ▒██▒  ██▒
▒████ ░ ▒███   ▓██ ░▄█ ▒▓██ ░▄█ ▒▒██  ▀█▄  ▓██    ▓██░▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░▒██  ▀█▄  ▒██░    ▒███   ▒██░  ██▒
░▓█▒  ░ ▒▓█  ▄ ▒██▀▀█▄  ▒██▀▀█▄  ░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ ░██▄▄▄▄██ ▒██░    ▒▓█  ▄ ▒██   ██░
░▒█░    ░▒████▒░██▓ ▒██▒░██▓ ▒██▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒▒██░   ▓██░  ▒██▒ ░  ▓█   ▓██▒░██████▒░▒████▒░ ████▓▒░
 ▒ ░    ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░    ▒▒   ▓▒█░░ ▒░▓  ░░░ ▒░ ░░ ▒░▒░▒░ 
 ░       ░ ░  ░  ░▒ ░ ▒░  ░▒ ░ ▒░  ▒   ▒▒ ░░  ░      ░ ░ ░  ░░ ░░   ░ ▒░    ░      ▒   ▒▒ ░░ ░ ▒  ░ ░ ░  ░  ░ ▒ ▒░ 
 ░ ░       ░     ░░   ░   ░░   ░   ░   ▒   ░      ░      ░      ░   ░ ░   ░        ░   ▒     ░ ░      ░   ░ ░ ░ ▒  
           ░  ░   ░        ░           ░  ░       ░      ░  ░         ░                ░  ░    ░  ░   ░  ░    ░ ░                                                                                         
           [underline yellow2]@AUTHOR LEONARDO ☻ [/underline yellow2]
        ┌─────                                                                                                  
        │                                              
        └(1:DNS_Recon e port scan)
            │
            └(3:Ataque DDos escreva esse comando:)
                                                                                                
                                                                                                [reverse underline dark_goldenrod] Edição Premium™[/reverse underline dark_goldenrod]                                
 """                    
console.print(Panel(banner, title="[yellow2]FERRAMENTA LEO™[/yellow2]",subtitle="[reverse yellow2]Leonardo Scripts™[/reverse yellow2]", style="blue_violet"))

ports = [443,21,68,80,400,20,23,110,67,143,161,465,993,995,22,53,1080,1443,1521,1723,2049,2082,2083,2181,24800,3306,3389,3690,4444,5000,5432,5900,6000,6379,6667,8000,8080,8443,8888,9000,9200,10000]

estilo_scan = Style(color="dark_red",italic=True,encircle=True,blink2=True,bold=True)
dominio = sys.argv[1]
def dns_recon():
        try:
          console.print("Escaneando porta. Apos terminar o scanner aperte 'CRTL C' para ir para a proxima etapa",style=estilo_scan)
          for port in ports:
                cliente = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                cliente.settimeout(0.5)
                resu = cliente.connect_ex((dominio,port))
                if resu == 0:
                        console.print("[underline gold3][☺ + ☺][/underline gold3][underline gray100] Portas Abertas → {}::({})".format(port,socket.getservbyport(port)))
        except:
               pass                         
          #---------------------- dnsRecon
        with open('dns.txt',"r")as dnsFile:
                subdomains = dnsFile.read().splitlines()
                contador = dnsFile.readlines()
                contador = 0
        for subs in subdomains:
                subdominios = ""+subs+"."+dominio+"" 
                try:
                        contador += 1 #nao modifique o contador sempre deixe nessa posicao pois nao pode detectar o admin
                        ip = socket.gethostbyname(subdominios)
                        if contador == 23:
                              console.print("[reverse green]INFO: ADMIN ENCONTRADO {}".format(subdominios))
                        console.print("[underline gold3][☺ + ☺][/underline gold3][underline blue_violet]Novo subdominio encontrado│→  {} ({})".format(subdominios,ip,port))
                        with open('dadosDn.txt','a')as dadosDn:
                               dadosDn.write(subdominios,ip)
                except:        
                        pass  

          
                  

#funcao principal
def main():
        
        arg = sys.argv[1]
        #comandos1
        if arg == '-hlp':
               console.print("Como usar a ferramenta leo:Escreva o dominio para capturar outros subdominios e portas. Como nesse ex:exampleSite.com")
               
        elif arg == '-git':
                 GithubCode = "[italic orange_red1]GITHUB → https://github.com/Pistolinha089[/ italic orange_red1]"
                 centralizar_texto = Align.center(GithubCode)
                 console.print(Panel(centralizar_texto,style="gold3"))
        elif arg == '-vpremium':
                console.print(Panel("[bold]Ia em manutencao.....[/bold]"))      
        else:
               dns_recon()        
              
if __name__ == "__main__":
        main()
