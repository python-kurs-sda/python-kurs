"""
    Napisz funkcje laczaca ze soba dwa napisy w sposob:
    najpierw pierwsza litera pierwszego napisu, potem pierwsza litera
    drugiego, druga litera drugiego napisu, itd...
    Funkcja powinna zwrocic nowy napis bedacy polaczeniem tych podanych
    jako parametry. Uwaga: wejsciowe napisy nie musza byc tej samej
    dlugosci!
    Przyklad:
    >> merge_strings("pies", "buda")
    pbiuedsa
    >> merge_strings("stop", "supermarket)
    sstuoopermarket
    W przypadku kiedy jakis napis jest dluzszy, nalezy go po prostu
    przepisac, podobnie jak to zostalo pokazane na drugim przykladzie.
"""


def merge_strings(string1, string2):
    """Laczy naprzemiennie napisy string1 oraz string2.

    :param string1: pierwszy napis do polaczenia.
    :param string2: drugi napis do polaczenia.
    :return: napis zlozony z podanych jako argumenty.

    """
    if len(string1) > len(string2):
        end = len(string2)
        slice_word = string1[end:]
    else:
        end = len(string1)
        slice_word = string2[end:]
    new_word = ''
    for i in range(end):
        new_word += string1[i]
        new_word += string2[i]
    return new_word + slice_word


