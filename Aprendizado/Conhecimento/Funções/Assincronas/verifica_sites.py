'''
Ação: Crie uma função assíncrona que simule o "ping" em um site usando randint(1, 10) para o tempo de resposta.
Desafio: Use asyncio.wait_for para definir um limite de 4 segundos. Se o site responder a tempo, imprima "Sucesso". Se passar do tempo, capture o TimeoutError e imprima "Site fora do ar".

'''

import asyncio
from random import randint

async def ver_ping(url):
    segundos = randint(1,2)
    await asyncio.sleep(segundos)
    return "Ping.."

async def main():
    limite = 4
    print(f"Iniciando download com limite de {limite}s...")
    try:
        res = await asyncio.wait_for(ver_ping('google.com'),timeout=limite)
        print(res)
    except asyncio.TimeoutError:
        print('Limite de tempo excedido')
    

asyncio.run(main())