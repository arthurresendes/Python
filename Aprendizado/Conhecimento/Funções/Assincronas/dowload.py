import asyncio
from random import randint 

async def download():
    tempo_execucao = randint(1, 10)
    print(f"O download levará {tempo_execucao} segundos...")
    await asyncio.sleep(tempo_execucao)
    return "Download concluído com sucesso!"

async def main():
    limite = 7
    print(f"Iniciando download com limite de {limite}s...")
    
    try:
        result = await asyncio.wait_for(download(), timeout=limite)
        print(result)
    except asyncio.TimeoutError:
        print("Erro: O download demorou demais e foi cancelado!")

asyncio.run(main())
