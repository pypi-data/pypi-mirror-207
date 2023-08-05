import sys
import random
import pexpect

class VPNException(Exception):
    '''exception class for VPN wrapper'''
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code
        super().__init__(f"[{status_code}] - {message}")


class VPN():
    '''
    Wrapper for the linux protonvpn-cli
    '''

    def __init__(self, user, pw, verbose=False, retries=3, timeout=5, location='U'):
        self.user = user
        self.pw = pw
        self.logged_in = False
        self.active = False
        self.verbose = verbose
        self.retries = retries
        self.timeout = timeout
        if location in ['J', 'N', 'U']:
            self.location = location
        else:
            raise VPNException(f'invalid location {location}', 400)

    def login(self):
        '''logs the user into proton vpn'''
        command = f'protonvpn-cli login {self.user}'
        try:
            child = pexpect.spawn(command)
            index = child.expect(['Enter your Proton VPN password:', 'You are already logged in.'], timeout=5)
            if index == 0:
                child.waitnoecho()
                child.sendline(self.pw)
                index = child.expect(['Successful login', ' \r\n', 'Incorrect login credentials', 'error occured'], timeout=self.timeout)
                if index == 0 or index == 1:
                    child.expect(pexpect.EOF)
                    if self.verbose:
                        sys.stdout.write('successfully logged in\n')
                    self.logged_in = True
                    return
                elif index == 2:
                    raise VPNException("invalid credentials", 401)
                else:
                    raise VPNException("error logging in", 401)
            elif index == 1:
                try:
                    raise VPNException("already logged in", 409)
                except VPNException as e:
                    if self.verbose:
                        sys.stderr.write('already logged in skipping step...\n')
                    self.logged_in = True
                    return

        except pexpect.ExceptionPexpect as e:
            raise VPNException(str(e), 500)

    def logout(self):
        '''logs the user out of proton vpn'''
        try:
            child = pexpect.spawn('protonvpn-cli logout')
            index = child.expect(['successfully logged out', 'login first', 'Logging out will disconnect the active VPN'], timeout=5)
            if index == 0:
                child.expect(pexpect.EOF)
                if self.verbose:
                    sys.stdout.write('successfully logged out\n')
                self.logged_in = False
            elif index == 1:
                raise VPNException("not logged in", 409)
            elif index == 2:
                child.sendline('y')
                index_c = child.expect(['successfully logged out'], timeout=10)
                if index_c == 0:
                    child.expect(pexpect.EOF)
                    if self.verbose:
                        sys.stdout.write('successfully logged out\n')
                    self.logged_in = False
                    return
                else:
                    raise VPNException("error logging out", 500)
            else:
                raise VPNException("error logging out", 500)

        except pexpect.ExceptionPexpect as e:
            raise VPNException(str(e), 500)
        
    def connect(self):
        '''
        connects to a random US Proton VPN
        '''
        for retry in range(self.retries):
            try:
                child = pexpect.spawn('protonvpn-cli c')
                child.waitnoecho(timeout=self.timeout//3)
                child.sendline(self.location)  # select location

                child.waitnoecho(timeout=self.timeout//3)
                # randomly select VPN connection
                for _ in range(random.randint(0, 30)):
                    child.send('+')
                child.sendline('+')  # + 1 and enter VPN selection

                child.waitnoecho(timeout=self.timeout//3)
                child.sendline('u')  # select updb - better speed

                index = child.expect(['Successfully connected'], timeout=5)
                if index == 0:
                    output = child.before.decode().strip().splitlines()[-1]
                    child.expect(pexpect.EOF)
                    if self.verbose:
                        sys.stdout.write(output)
                        sys.stdout.write('\nsuccessfully connected\n')
                    self.active = True
                    return
                else:
                    self.logout()
                    raise VPNException('error connecting to vpn', 500)

            except pexpect.ExceptionPexpect as e:
                if retry == self.retries - 1:
                    sys.stderr.write(f'maximum retries reached while connecting to VPN; stopping connection attempt... ({retry + 1}/{self.retries})\n')
                    return
                else:
                    if self.verbose:
                        sys.stderr.write(f'error while connecting to VPN; retrying connection... ({retry + 1}/{self.retries})\n')
                    continue

    def disconnect(self):
        '''disconnects from VPN connection'''
        try:
            child = pexpect.spawn('protonvpn-cli d')
            index = child.expect(['Successfully disconnected', 'No Proton VPN connection was found'], timeout=5)
            if index == 0:
                child.expect(pexpect.EOF)
                if self.verbose:
                    sys.stdout.write('successfully disconnected\n')
                self.active = False
            elif index == 1:
                child.expect(pexpect.EOF)
                if self.verbose:
                    sys.stdout.write('already disconnected\n')
            else:
                raise VPNException('error disconnecting', 500)

        except pexpect.ExceptionPexpect as e:
            raise VPNException(str(e), 500)

    def shuffle(self):
        '''shuffle vpn connection'''
        if self.active:
            if self.verbose:
                sys.stdout.write('shuffling connection...\n')
            self.disconnect()
            self.connect()
        else:
            raise VPNException('error shuffling connection VPN not active', 500)

    ### Context Manager ###

    def __enter__(self):
        '''login and connect to vpn'''
        self.login()
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        '''disconnect and log out of vpn'''
        self.disconnect()
        self.logout()
