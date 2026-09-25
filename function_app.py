import os
import logging
import azure.functions as func


app = func.FunctionApp()

@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def timer_trigger(myTimer: func.TimerRequest) -> None:
    # 1-pesquisar como capturar variaveis de ambiete com a lib os
    # 2-salvar os valores na variaveis do codigo
    # 3-imprimir no console os valores
    ## criar variaveis do codigo
    try:
        usuario = os.environ["USER"]
        host = os.environ["HOST"]
        database = os.environ["DATABASE"]
        password = os.environ["PASSWORD"]
    except KeyError as e:
        logging.error(f"{e} não foi configurada no Azure!")
        return 
    
    #printar variaveis
    logging.info(f"Senha: {password}")
    logging.info(f"Host: {host}")
    logging.info(f"Database: {database}")
    logging.info(f"Usuário: {usuario}")