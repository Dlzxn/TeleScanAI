import asyncio
from src.services.telegram_bot import run_telegram_bot


async def main():
    await run_telegram_bot()


if __name__ == '__main__':
    asyncio.run(main())