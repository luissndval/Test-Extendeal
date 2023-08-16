import argparse
import os
import subprocess

if __name__ == '__main__':
    p = argparse.ArgumentParser()

    # --testdir command line argument added

    p.add_argument('--testdir', required=False, help="File path")

    a = p.parse_args()

    # testdir = f"C:\\proyectos\\Turnera\\turnera-backend-administracion\\TestAutomation\\features\\{t03}"  # PUEDES INDICAR EL SCRIPT A EJECUTAR

    ruta_actual = os.path.abspath(__file__)
    ruta_padre = os.path.dirname(os.path.dirname(ruta_actual))
    ruta_txt = os.path.join(ruta_padre, 'features')


    testdir =  os.path.join(ruta_txt)# PUEDES INDICAR EL SCRIPT A EJECUTAR

    # complete command

    c = f'behave --no-capture {testdir}'

    s = subprocess.run(c, shell=True, check=True)
