import os, json
import boto3

async def describe_vpcs() -> list:
    try:
        client = boto3.client('ec2')
        response = client.describe_vpcs(
            Filters=[
                {
                    'Name': 'is-default',
                    'Values': [ "false" ]
                },
            ]
        )
        return [
            {
                "VpcId": vpc["VpcId"],
                "CidrBlock": vpc["CidrBlock"],
                "Tags": vpc["Tags"]
            }
            for vpc in response["Vpcs"]
        ]
    except Exception as error:
        print(error)
        exit(1)

async def describe_subnets(vpcs: list) -> list:
    try:
        client = boto3.client('ec2')
        response = client.describe_subnets(
            Filters=[
                {
                    'Name': 'vpc-id',
                    'Values': [ vpc['VpcId'] for vpc in vpcs ]
                },
            ],
        )
        return [
            {
                "VpcId": subnet["VpcId"],
                "SubnetId": subnet["SubnetId"],
                "AvailabilityZone": subnet["AvailabilityZone"],
                "CidrBlock": subnet["CidrBlock"],
                "Tags": subnet["Tags"]
            }
            for subnet in response["Subnets"]
        ]
    except Exception as error:
        print(error)
        exit(1)

async def describe_nat_gateways(vpcs: list) -> list:
    try:
        client = boto3.client("ec2")
        response = client.describe_nat_gateways(
            Filters=[
                {
                    'Name': 'vpc-id',
                    'Values': [ vpc["VpcId"] for vpc in vpcs ]
                },
            ],
        )
        return [
            {
                "NatGatewayId": nat_gateway["NatGatewayId"],
                "VpcId": nat_gateway["VpcId"],
                "SubnetId": nat_gateway["SubnetId"],
                "Tags": nat_gateway["Tags"]
            }
            for nat_gateway in response["NatGateways"]
        ]
    except Exception as error:
        print(error)
        exit(1)

async def describe_route_table(vpcs: list) -> list:
    try:
        client = boto3.client("ec2")
        response = client.describe_route_tables(
            Filters=[
                {
                    'Name': 'vpc-id',
                    'Values': [ vpc["VpcId"] for vpc in vpcs ]
                },
            ]
        )
        return [
            {
                "VpcId": route_table["VpcId"],
                "RouteTableId": route_table["RouteTableId"],
                "Associations": route_table["Associations"],
                "Routes": route_table["Routes"],
                "Tags": route_table["Tags"]
            }
            for route_table in response["RouteTables"]
        ]
    except Exception as error:
        print(error)
        exit(1)


class VpcResources:
    
    @classmethod
    async def describe(cls):
        vpcs         = await describe_vpcs()
        subnets      = describe_subnets(vpcs)
        nat_gateways = describe_nat_gateways(vpcs)
        route_tables = describe_route_table(vpcs)

        output_directory = "outputs"
        output_file = "vpc.json"
        output_path = f"{output_directory}/{output_file}"

        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        with open(output_path, "w") as file:
            json.dump({
                "Vpcs": vpcs,
                "Subnets": await subnets,
                "NatGateways": await nat_gateways,
                "RouteTables": await route_tables
            }, file)
