from sys import argv, stdout
import yaml
import json
import csv

routesFile = argv[1]


def readRoutes(file):
    with open(file) as routes:
        return yaml.safe_load(routes)


ALL_COLUMNS = [
    SERVICE, ROOT_PATH, GATEWAY_PATH, INTERNAL_PATH, MATCHER, AUTH, METHODS
] = [
    'service', 'root', 'gateway-path', 'internal-path', 'matcher', 'disable-auth', 'methods'
]
COLUMNS = [
    SERVICE, GATEWAY_PATH, MATCHER, METHODS, INTERNAL_PATH, AUTH,
]

data = readRoutes(routesFile)
services = data['routeTables']
routes = [
    { 
        SERVICE: service['name'],
        GATEWAY_PATH: route['path'],
        INTERNAL_PATH: options.get('prefixRewrite','*'),
        MATCHER: route.get('matcher'),
        AUTH: route.get('disableAuth', False),
        METHODS: ','.join(options.get('methods', ['*']))

    }
    for service in services
    for route in service.get('routes')
    for options in [route.get('options') or {}]
]


out = csv.writer(stdout)
out.writerow(COLUMNS)
for r in routes:
    out.writerow([r[c] for c in COLUMNS])
