from django.test import TestCase
from pywizlight import *
import asyncio
from asgiref.sync import sync_to_async
# Create your tests here.


async def test():
    a = await wizlight("192.168.178.122").get_power()
    print(a)


@sync_to_async
def main():
    test()


if __name__ == '__main__':
    main()