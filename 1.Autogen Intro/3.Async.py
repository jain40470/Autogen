import asyncio
import time

async def async_brew_coffee():
    print("Starting the coffee brewing process asynchronously...")
    await asyncio.sleep(2)
    print("Coffee is ready!")

async def async_toast_bread():
    print("Starting to toast the bread asynchronously...")
    await asyncio.sleep(3)
    print("Bread is toasted!")

async def main_async():

    print("Welcome to the asynchronous breakfast maker!")

    start = time.time()

    await asyncio.gather(
        async_brew_coffee(),
        async_toast_bread()
    )

    end = time.time()
    total_time = end - start
    print(f"Total time taken for breakfast preparation: {total_time:.2f} seconds")

    print("Breakfast is ready! Enjoy your meal!")

if __name__ == "__main__":
    asyncio.run(main_async())
