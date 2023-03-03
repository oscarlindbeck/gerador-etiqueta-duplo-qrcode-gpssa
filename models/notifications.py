from winotify import Notification


class Notifications:
    def __init__(self, path, duration):
        self.path = path
        self.duration = duration

    def start(self):
        notification = Notification(app_id='Gerador de qrcode',
                                    title='Geração de qrcodes iniciada',
                                    msg='Aguarde a conclusão da geração dos qrcodes. Isto poderá demorar.\n\n'
                                        'Verifique a documentação abaixo.',
                                    icon=f'{self.path}\\src\\icon\\iconPython.png',
                                    duration=f'{self.duration}')
        notification.add_actions(label='GitHub', launch='https://github.com/oscarlindbeck?tab=repositories')
        notification.show()

    def finish(self):
        notification = Notification(app_id='Gerador de qrcode',
                                    title='Geração de qrcodes finalizada',
                                    msg='A geração de qrcodes foi finalizada. Verifique a consistência do arquivo \n'
                                        'gerado.',
                                    icon=f'{self.path}\\src\\icon\\iconPython.png',
                                    duration=f'{self.duration}')
        notification.add_actions(label='GitHub', launch='https://github.com/oscarlindbeck?tab=repositories')
        notification.show()
