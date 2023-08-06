import uvicorn
from https.server import get_app
import argparse

parser = argparse.ArgumentParser(description='Start a RESTful server.')
parser.add_argument('--num_worker', type=int, default=1)
parser.add_argument('--port', type=int, default=8000)
parser.add_argument('--host', type=str, default='0.0.0.0')
args = parser.parse_args()


app = get_app()

if __name__ == "__main__":

    uvicorn.run('wsgi:app', host="0.0.0.0", port=args.port, workers=args.num_worker)