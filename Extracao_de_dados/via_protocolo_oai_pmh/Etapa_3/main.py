import time
from pacote_funcoes.main_function import main

if __name__ == "__main__":
    start = time.time()

    main()

    end = time.time()
    
    print('\n\n\tDuração total da execução:',round(end-start,2),'segundos.\n')