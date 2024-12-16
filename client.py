import click
import requests

@click.group()
def cli():
  pass

@cli.command('store')
@click.argument('filename')
def store_file(filename):
  """Stores a file on the server."""
 try:
    response = requests.post(f'http://localhost:5000/store', headers = {'User-Agent': 'Mozilla/5.0'}
    print(response.json())
  except requests.exceptions.RequestException as e:
    print(f"Error: {e}") 
# ... your store_file implementation ...

@cli.command('list')
def list_files():
  """Lists all files on the server."""
 try:
    response = requests.get(f'http://localhost:5000/list/{filename}')
    print(response.json())
  except requests.exceptions.RequestException as e:
    print(f"Error: {e}") 
# ... your list_files implementation ...

@cli.command('remove')
@click.argument('filename')
def remove_file(filename):
  """Removes a file from the server."""
  try:
    response = requests.delete(f'http://localhost:5000/remove/{filename}')
    print(response.json())
  except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

if __name__ == '_main_':
  cli()
