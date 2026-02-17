import asyncio

async def despertar(nome,segundos):
    print(f"Acordando {nome}...")
    await asyncio.sleep(segundos)
    print(f"{nome} acordado")

async def main():
    await despertar('Arthur',2)
    await despertar('Maria',3)
    await despertar('Josias',5)
asyncio.run(main())