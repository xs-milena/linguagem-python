import psutil, datetime, time, csv # importando as bibliotecas 

# cabeçalho

with open("./captura-python/captura-dados/captura.csv", mode='w') as csvfile:
    csv.writer(csvfile, delimiter=',').writerow(["CAPTURA A CADA 10 SEGUNDOS"])
    csv.writer(csvfile, delimiter=',').writerow(["ID","CAPTURA (DATA/HORA)", "CPU (%)", "MEMÓRIA RAM (%)", "ESPAÇO EM DISCO (%)"])

# repetir a captura de dados 10 vezes a cada 10 segundos

contador = 1

while contador <= 10:

    # captura: DATA/HORA, CPU, MEMÓRIA RAM, ESPAÇO EM DISCO

    time_now = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    cpu = psutil.cpu_percent(interval=1)
    ram_memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    # salva no .CSV
    # mode='a' add linhas

    with open("./captura-python/captura-dados/captura.csv", mode='a') as csvfile:
        csv.writer(csvfile, delimiter=',').writerow([contador, time_now, cpu, ram_memory, disk])

    contador+=1
    time.sleep(10) # intervalo de 10s

    # ler csvfile no python
    with open("./captura-python/captura-dados/captura.csv") as csvfile:
        for x in csv.reader(csvfile):
            print(x)
        