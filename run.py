import asyncio, sys
from vpc import VpcResources

async def main(argv):

    try:
        FILE_NAME = argv[0] # The first of command line arguments is file name
        SERVICE   = argv[1]
    except IndexError:
        print("")
        print("❗ Please make sure that arguments")
        print("")
        print("$ python3 run.py [SERVICE NAME]")
        print("")
        exit(128)
    except Exception as error:
        print(error)
        exit(1)
    
    try:
        describe_functions = {
            "vpc": VpcResources.describe,
        }
        func = describe_functions[SERVICE]
        await func()
        exit(0)
    except KeyError as error:
        if SERVICE == "--list":
            print("")
            print("🍳 Service list")
            print("")
            for service_name, _ in describe_functions.items():
                print(f"   ≡ {service_name}")
            print("")
            exit(0)
        else:
            print("")
            print("❗ Invalid service name, please make sure that services list")
            print("")
            print("$ python3 run.py --list")
            print("")
            exit(128)
    except Exception as error:
        print(error)
        exit(1)


if __name__ == "__main__":
    asyncio.run(main(sys.argv))