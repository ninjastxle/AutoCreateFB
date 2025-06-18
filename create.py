#--> Author's Info
Author    = 'Dapunta Khurayra X'
Facebook  = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/Dapunta.Ratya'
Whatsapp  = '082245780524'
YouTube   = 'Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA'

#--> Warna (Colores)
P = "\x1b[38;5;231m" # Putih (Blanco)
M = "\x1b[38;5;196m" # Merah (Rojo)
H = "\x1b[38;5;46m"  # Hijau (Verde)
A = '\x1b[38;5;248m' # Abu-Abu (Gris)

#--> Importar Módulos
try:
    import os, sys, time, re, datetime, random
    from datetime import datetime
except Exception as e:
    print(e)
    exit('\n¡Error al importar módulos básicos!')

try:
    import requests
except:
    os.system('pip install requests')
    import requests

try:
    import bs4
    from bs4 import BeautifulSoup as bs
except:
    os.system('pip install bs4')
    import bs4
    from bs4 import BeautifulSoup as bs

#--> Variables Globales
auth1 = 'Dapunta Khurayra X'
auth2 = 'Suci Maharani Putri'
reco = 'No necesitas decodificar esto, solo úsalo'
rede = 'Te dije que no lo decodifiques'
key = len(auth1)*len(auth2)-len(auth1)
bulan = {'1':'Enero','2':'Febrero','3':'Marzo','4':'Abril','5':'Mayo','6':'Junio',
         '7':'Julio','8':'Agosto','9':'Septiembre','10':'Octubre','11':'Noviembre','12':'Diciembre'}
ok = 0
cp = 0

# Nombres aleatorios
boys_name = ['Axel','Anzel','Basheer','Bernardus','Carel','Cyrus','Damian','Dominic',
             'Ephraim','El Fatih','Fawwaz','Faheem','Gianluca','Haddad','Istafa',
             'Kenneth','Nathanael','Vaskylo','Xaferius','Yesaya']

girls_name = ['Atika','Alya','Adzkiya','Adiva','Aqeela','Bilqis','Chayra','Caliana',
              'Chaerunnisa','Dhawiyah','Dilara','Farah','Ghariyah','Hamna','Hanin',
              'Izza','Kayla','Mahreen','Rasahana','Shakayla']

#--> Limpiar Terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#--> Obtener Fecha
def waktu():
    bulan_ = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio",
              "Agosto","Septiembre","Octubre","Noviembre","Diciembre"][datetime.now().month - 1]
    return f"{datetime.now().day}_{bulan_}_{datetime.now().year}"

#--> Espera
def jeda(t):
    for x in range(t+1):
        print(f'\rEspera {t} segundos...', end='')
        t -= 1
        if t == 0: break
        time.sleep(1)

#--> User Agents
def random_ua_vivo():
    a = random.randint(112,115)
    b = random.randint(1000,9999)
    c = random.randint(10,99)
    os_ver = random.randint(10,13)
    dv_typ = random.choice(['vivo 1951','vivo 1918','V2011A','V2047','V2145','V2227A','V2160'])
    bl_typ = random.choice(['RP1A','PKQ1','QP1A','TP1A'])
    return f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{a}.0.{b}.{c} Mobile Safari/537.36'

def random_ua_samsung():
    a = random.randint(112,115)
    b = random.randint(1000,9999)
    c = random.randint(10,99)
    os_ver = random.randint(10,13)
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    bl_typ = random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A'])
    return f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{a}.0.{b}.{c} Mobile Safari/537.36'

#--> Logo
def logo():
    clear()
    print(f'''{P}_________                      __        {M}________________ {P}
{P}\_   ___ \_______ ____ _____ _/  |_  ____{M}\_   ____|___   \\{P}
{P}/    \  \/\_  __ \ __ \\\\__  \\\\   __\/ __ \{M}|    __)   |  _/{P}
{P}\ {M}0.1 {P}\____|  | \/ ___/ / __ \|  | \  ___/{M}|   \  |   |   \\{P}
{P} \________/|__|  \_____>______/__|  \____>{M}|___/  |_______/{P}
{P}\n      ─────────────── {M}• {P}AutoCreateFB {M}• {P}───────────────\n{P}''')

#--> Clase Principal
class menu:
    def __init__(self):
        logo()
        self.main_menu()
    
    def main_menu(self):
        print(f'{M}[{P}1{M}] {P}Crear Cuenta')
        print(f'{M}[{P}2{M}] {P}Ver Resultados')
        print(f'{M}[{P}3{M}] {P}Configuración')
        print(f'{M}[{P}4{M}] {P}Bot')
        x = input(f' {M}└─ {P}Seleccione {M}: {P}').lower()
        print('')
        if x in ['1','01','a']: 
            menu_create()
        elif x in ['2','02','b']: 
            menu_check()
        else: 
            exit(f'{M}¡Selección incorrecta!{P}')

#--> Clase para Crear Cuenta
class menu_create:
    def __init__(self):
        try:
            os.makedirs('Cuentas_Nuevas', exist_ok=True)
        except Exception as e:
            pass
            
        print(f'\n      {H}◉ {P}Recomendado   {M}◉ {P}No recomendado   ◉ Neutral')
        
        self.genero = input(f'{M}[{P}•{M}] {P}Cuenta Masculino/Femenino/Random [{H}l{P}/{H}p{P}/{M}r{P}]: ').lower()
        self.nombre_tipo = input(f'{M}[{P}•{M}] {P}Nombre Aleatorio/Manual [{M}r{P}/{H}m{P}]: ').lower()
        
        if self.nombre_tipo in ['m','manual']:
            self.nombre = input(f' {M}└─ {P}Nombre : {M}').split(',')
        else:
            self.nombre = None
            
        print(f'{M}[{P}•{M}] {P}Email CryptoGmail/SecMail/MinuteMail')
        self.email_tipo = input(f' {M}└─ {P}[c/s/m] [saltar=MinuteMail]: ').lower()
        
        self.mostrar_cp = input(f'{M}[{P}•{M}] {P}Mostrar cuentas CP [{M}y{P}/{H}t{P}]: ').lower()
        
        print(f'{M}[{P}•{M}] {P}User Agent Vivo/Samsung/Realme/Manual')
        self.ua_tipo = input(f' {M}└─ {P}[v/s/r/m] [saltar=estático]: ').lower()
        
        if self.ua_tipo in ['m','manual']:
            self.ua_personalizado = input(f' {M}└─ {P}User Agent : {M}')
            if not self.ua_personalizado.strip():
                exit(f'{M}¡Debes ingresar un User Agent válido!{P}')
        
        self.password_tipo = input(f'{M}[{P}•{M}] {P}Contraseña Aleatoria/Manual [{H}r{P}/{M}m{P}]: ').lower()
        
        if self.password_tipo in ['m','manual']:
            self.password = input(f' {M}└─ {P}Contraseña : {M}')
            if len(self.password) < 6:
                exit(f'{M}¡La contraseña debe tener al menos 6 caracteres!{P}')
        
        self.delay = input(f'{M}[{P}•{M}] {P}Delay (en minutos): ')
        self.delay = int(self.delay)*60 if self.delay.strip() else 60
        
        print('')
        for _ in range(10000):
            if key/len(auth1) == len(reco)/2: 
                crear_fb()
                self.contador(self.delay)
            else: 
                print(rede)

    def contador(self, segundos):
        for x in range(segundos+1):
            print(f'\r[OK:{ok}] [CP:{cp}] Esperando {segundos} segundos...', end='')
            segundos -= 1
            time.sleep(1)

#--> Clase para Crear Facebook
class crear_fb:
    def __init__(self):
        self.archivo = f'Cuentas_Nuevas/{waktu()}.txt'
        self.sesion = requests.Session()
        self.sesion.cookies.clear()
        
        # Configurar User Agent
        if self.ua_tipo == 'v': self.ua = random_ua_vivo()
        elif self.ua_tipo == 's': self.ua = random_ua_samsung()
        elif self.ua_tipo == 'm': self.ua = self.ua_personalizado
        else: self.ua = 'Mozilla/5.0 (Linux; Android 13; RMX3686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'
        
        self.headers = {
            'User-Agent': self.ua,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        
        self.generar_datos()
        self.obtener_tokens()
    
    def generar_datos(self):
        # Generar nombre y género
        if self.genero == 'l': genero = 'male'
        elif self.genero == 'p': genero = 'female'
        else: genero = random.choice(['male','female'])
        
        if self.nombre:
            self.nombre_completo = random.choice(self.nombre)
        else:
            if genero == 'male':
                self.nombre_completo = f"{random.choice(boys_name)} {random.choice(boys_name)}"
            else:
                self.nombre_completo = f"{random.choice(girls_name)} {random.choice(girls_name)}"
        
        # Generar contraseña
        if self.password_tipo == 'm':
            self.password = self.password
        else:
            caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
            self.password = ''.join(random.choice(caracteres) for _ in range(12))
        
        # Generar email
        nombre_email = self.nombre_completo.lower().replace(' ','')
        if self.email_tipo == 'c':
            dominios = ['fexbox.org','chitthi.in','fextemp.com','merepost.com']
            self.email = f"{nombre_email}{random.randint(100,999)}@{random.choice(dominios)}"
        elif self.email_tipo == 's':
            dominios = ['1secmail.com','1secmail.org','1secmail.net']
            self.email = f"{nombre_email}{random.randint(100,999)}@{random.choice(dominios)}"
        else:
            dominios = ['10minutemail.com','tempmail.com']
            self.email = f"{nombre_email}{random.randint(100,999)}@{random.choice(dominios)}"
        
        # Generar fecha de nacimiento
        self.nacimiento = {
            'dia': str(random.randint(1,28)),
            'mes': str(random.randint(1,12)),
            'ano': str(random.randint(1980,2000))
        }
    
    def obtener_tokens(self):
        try:
            # Obtener página de registro
            respuesta = self.sesion.get('https://m.facebook.com/reg/', headers=self.headers)
            sopa = bs(respuesta.text, 'html.parser')
            
            # Buscar formulario
            formulario = sopa.find('form', {'method': 'post'})
            if not formulario:
                raise Exception("No se encontró el formulario de registro")
            
            # Extraer tokens necesarios
            self.lsd = formulario.find('input', {'name': 'lsd'}).get('value', '')
            self.jazoest = formulario.find('input', {'name': 'jazoest'}).get('value', '')
            self.fb_dtsg = re.search('"token":"(.*?)"', respuesta.text).group(1)
            
            if not all([self.lsd, self.jazoest, self.fb_dtsg]):
                raise Exception("No se pudieron obtener todos los tokens necesarios")
            
            self.enviar_registro()
            
        except Exception as e:
            print(f"\r{M}Error al obtener tokens: {str(e)}{P}")
            self.mostrar_resultado('CP')
    
    def enviar_registro(self):
        try:
            datos = {
                'lsd': self.lsd,
                'jazoest': self.jazoest,
                'fb_dtsg': self.fb_dtsg,
                'firstname': self.nombre_completo.split()[0],
                'lastname': ' '.join(self.nombre_completo.split()[1:]),
                'reg_email__': self.email,
                'reg_passwd__': self.password,
                'birthday_day': self.nacimiento['dia'],
                'birthday_month': self.nacimiento['mes'],
                'birthday_year': self.nacimiento['ano'],
                'sex': '1' if 'female' in self.genero else '2',
                'submit': 'Registrarse'
            }
            
            respuesta = self.sesion.post('https://m.facebook.com/reg/', data=datos, headers=self.headers)
            
            if 'confirmemail' in respuesta.url:
                self.mostrar_resultado('OK')
            else:
                self.mostrar_resultado('CP')
                
        except Exception as e:
            print(f"\r{M}Error al enviar registro: {str(e)}{P}")
            self.mostrar_resultado('CP')
    
    def mostrar_resultado(self, estado):
        global ok, cp
        
        if estado == 'OK':
            print(f'\r{P}Estado : {H}Éxito{P}')
            print(f'Nombre : {self.nombre_completo}')
            print(f'Email  : {self.email}')
            print(f'Contraseña : {self.password}\n')
            
            with open(self.archivo, 'a') as f:
                f.write(f"{self.nombre_completo}|{self.email}|{self.password}\n")
            ok += 1
        else:
            if self.mostrar_cp != 't':
                print(f'\r{P}Estado : {M}Checkpoint{P}')
                print(f'Nombre : {self.nombre_completo}')
                print(f'Email  : {self.email}')
                print(f'Contraseña : {self.password}\n')
            cp += 1

#--> Iniciar Script
if __name__ == '__main__':
    try:
        menu()
    except KeyboardInterrupt:
        exit(f'\n{M}Script detenido por el usuario.{P}')
    except Exception as e:
        exit(f'\n{M}Error inesperado: {str(e)}{P}')
