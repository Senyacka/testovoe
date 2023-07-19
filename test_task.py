import requests
import concurrent.futures


def simple_digits(n: int) -> list:
    '''
    Задание 1: Написать функцию, возвращающую все простые числа до N
    '''
    ls = []
    a = [0] * 2 + [1] * n
    for i in range(int(n**0.5) + 1):
        if a[i]:
            for j in range(i * i, n, i):
                a[j] = 0
    for i in range(n):
        if a[i]:
            ls.append(i)
    return ls


def download_site(url: str, count: int, timeout=10):
    '''
    Задание 2: Написать функцию, которая получает из Сети код страниц из списка
    и сохраняет его (код) на диск.
    '''
    page = requests.get(url=url, timeout=timeout)
    html = page.text
    f = open(f'test{count}.html', 'w')
    f.write(html)
    f.close()


urls = ['http://google.com/' for _ in range(10)]

with concurrent.futures.ThreadPoolExecutor() as executor:
    count = 1
    for url in urls:
        executor.submit(download_site(url=url, count=count))
        count += 1


print(simple_digits(111))
