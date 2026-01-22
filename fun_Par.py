# %%
def is_par(numero:int)->str:
    
    """Essa função faz uma verificação se o número é par ou ímpar

    Args:
        numero (int): O número que será verificado se é par ou ímpar
    """
    
    if numero % 2 == 0:
        print("esse número é Par")
    else:
        print("esse número é Ímpar")
# %%
is_par(2)
is_par(3)
# %%
is_par()