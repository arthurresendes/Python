import asyncio

async def monitor_sistema():
    while True:
        print("\n[MONITOR]: Sistema OK...")
        await asyncio.sleep(2)

async def obter_input():
    """Roda o input() bloqueante sem travar o loop assíncrono."""
    loop = asyncio.get_running_loop()
    # Executa o input em uma thread separada
    nome = await loop.run_in_executor(None, input, "Digite seu nome a qualquer momento: ")
    return nome

async def main():
    print("Iniciando o programa...")
    
    # 1. Cria a tarefa do monitor e a dispara (não espera o await aqui)
    tarefa_monitor = asyncio.create_task(monitor_sistema())
    
    # 2. Espera pelo input do usuário de forma não bloqueante
    nome_usuario = await obter_input()
    
    print(f"\nShow, {nome_usuario}! Agora vamos encerrar o monitor.")
    
    # 3. Cancela a tarefa de background antes de sair
    tarefa_monitor.cancel()
    try:
        await tarefa_monitor
    except asyncio.CancelledError:
        print("Monitor encerrado com sucesso.")

if __name__ == "__main__":
    asyncio.run(main())
