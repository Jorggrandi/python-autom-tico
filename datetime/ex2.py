from datetime import datetime


def mensagem():
    agora = datetime.now()
    meses_faltantes = 12 - agora.month
    print(
        agora.strftime(
            f"Estamos no mês %B, faltam {meses_faltantes} mêses para o ano acabar!"
        )
    )
    return


mensagem()
