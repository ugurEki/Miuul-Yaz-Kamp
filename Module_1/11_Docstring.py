### Docstring :
# Docstring, bir programlama dilinde bir işlev, 
# sınıf veya modülün açıklamasını sağlayan bir dökümantasyon stringidir. 
# Genellikle fonksiyonun veya diğer kod bloğunun başında yer alır ve açıklama yapısı,
# kullanım talimatları, parametrelerin ve dönen değerin
# açıklamaları gibi bilgileri içerebilir.

def summer(arg1, arg2):
    """
    Sum of two numbers

    Args:
        arg1 : int, float
        arg2 : int, float

    Returns:
        int, float

    """
    print(arg1 + arg2)

print(summer(5, 8))

print(help(summer))

    