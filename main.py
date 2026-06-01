from bot.cli import parse_arguments
from bot.orders import execute_order


def main():

    try:

        order_data = parse_arguments()

        response = execute_order(**order_data)

        print("\n========== ORDER RESPONSE ==========\n")

        if response.get("status"):

            print(f"Order ID      : {response.get('orderId')}")
            print(f"Status        : {response.get('status')}")
            print(f"Executed Qty  : {response.get('executedQty')}")
            print(f"Symbol        : {response.get('symbol')}")
            print(f"Side          : {response.get('side')}")

            if response.get("avgPrice"):
                print(f"Average Price : {response.get('avgPrice')}")

            print(f"\nOrder placed successfully! Status: {response.get('status')}")

        else:

            print("Order Failed")
            print(response)

    except Exception as e:

        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()