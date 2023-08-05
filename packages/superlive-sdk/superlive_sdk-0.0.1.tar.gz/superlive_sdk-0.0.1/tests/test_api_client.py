import json
from src.superlive import Host

# Configuration
API_ENDPOINT = "{xxxxxxxxxxxxxxxxxxxx}"
API_KEY     = "{xxxxxxxxxxxxxxxxxxxx}"

def main():

    # Create default HTTP client with its configuration
    initHost = Host({
        "api_endpoint": API_ENDPOINT,
        "api_key": API_KEY
    })

    ## CREATE
    # response    = initHost.createHost({"username": "demo1", "password": "123456", "name": "Demo1", "description": "Testing"})

    # GET HOSTS
    response = initHost.getHosts({"limit": 10})

    ## UPDATE
    # response = initHost.updateHost('6450b5bc0dffad61135f9cae', {"username": "demo1", "password": "123456", "name": "Demo2", "description": "Update description"})

    ## DELETE
    # response = initHost.deleteHostById('6450b5bc0dffad61135f9cae')

    ## COUNT
    # response = initHost.countHost()

    print('============================== HttpResponse ==============================')
    print(json.dumps(response, indent=4))
    print('============================== END ==============================')

if __name__ == "__main__":
    main()